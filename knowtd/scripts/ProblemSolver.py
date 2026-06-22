import networkx as nx
import sympy
from matplotlib import pyplot as plt
from itertools import chain

from linkml_runtime.utils.schemaview import SchemaView

class ProblemSolver():

    def __init__(self, symbols, equations, find):
        
        self.symbols = {instance.id: sympy.symbols(instance.id) for instance in symbols}
        self.assignments = {instance.id: self.symbols[instance.id] - sympy.sympify(instance.value, locals=self.symbols) for instance in symbols if isinstance(instance.value,float)}
        self.equations = self._init_equations(equations)
        self.find = find

    
    def solve(self):
        self._init_reasoning_graph()
        self._reasoning_traversal()
        self._simplify()

        # return the solution
        solution = {n: self.G_optimized.nodes[n].get('value') for n in self.G_optimized if self.G_optimized.nodes[n]["type"] == "symbol"}
        return solution

    def _init_equations(self, equations):
        eqns = {}
        for eqn in equations:
            eqn_str = '({})'.format(eqn.as_text.replace(' = ',')-('))
            eqns[eqn.id] = sympy.sympify(eqn_str, locals=self.symbols)
        for assignment in self.assignments:
            eqns['Assignment' + assignment] = self.assignments[assignment]
        return eqns

    def _init_reasoning_graph(self):
        self.G_reasoning = nx.DiGraph()

        # add all symbols to the graph
        for s in self.symbols:
            self.G_reasoning.add_node(s, type='symbol')

        # print(self.G_reasoning.nodes())

        # add equation nodes and link to symbols
        for e in self.equations:
            # print('eqn',e)
            self.G_reasoning.add_node(e, type='equation', expression=self.equations[e])

            # link it to all involved symbols
            for s in self.equations[e].free_symbols:
                # create symbol if not known before (created by AdditionalEquation)
                if not s.name in self.symbols:
                    s.name = 'additional_'+s.name
                    self.symbols[s.name] = s
                    self.G_reasoning.add_node(s.name, type='symbol')
                self.G_reasoning.add_edge(s.name,e)

    def _reasoning_traversal(self):
        self.G_traversal = self.G_reasoning.reverse(copy=True) # equations point to symbols
        nx.set_node_attributes(self.G_traversal, values=False, name='reachable')
        nx.set_node_attributes(self.G_traversal, values=None, name='value')

        # start with equations where only one symbol is used in the equation
        self.worklist = [node for node,data in self.G_traversal.nodes(data=True) if data["type"] == "equation" and self.G_traversal.out_degree(node) == 1]
        if self.worklist==[]:
            self.worklist = [node for node,data in self.G_traversal.nodes(data=True) if data["type"] == "equation"]
        while self.worklist:
            node = self.worklist.pop(0)
            if self.G_traversal.nodes[node]["type"] == "equation" and not self.G_traversal.nodes[node].get('reachable'):
                self._check_equation_applicable(node)
        
        # check if target in traversal
        # print('success', self._check_traversal_successful())
    
    def _check_equation_applicable(self, equation_node):
        if self.G_traversal.nodes[equation_node].get('reachable'):
            # already reachable
            return
        # substitute the already known symbols
        neighbors_with_values = {s: self.G_traversal.nodes[s].get('value') for s in self.G_traversal.predecessors(equation_node) if not self.G_traversal.nodes[s].get('value') is None and self.G_traversal.nodes[s].get('reachable')}
        subs_equation = sympy.simplify(self.equations[equation_node]).subs(neighbors_with_values) # simplify increases computation time
        equation_free_symbols = list(subs_equation.free_symbols)
        
        if len(equation_free_symbols) == 0:
            # no information gain
            self.G_traversal.nodes[equation_node]['reachable'] = True
        elif len(equation_free_symbols) == 1:
            try:
                values = sympy.nonlinsolve([subs_equation], equation_free_symbols)
            except:
                values = None
                print('Could not solve using sympy.nonlinsolve.')
            if type(values) == sympy.FiniteSet:
                symbol_node = equation_free_symbols[0].name
                value, = next(iter(values))
                if value.is_number: # sometimes empty set or condition set
                    self.G_traversal.nodes[symbol_node]['value'] = value
                    self.G_traversal.nodes[equation_node]['reachable'] = True
                    self.G_traversal.nodes[symbol_node]['reachable'] = True

                    next_equation_nodes = [n for n in self.G_traversal.predecessors(symbol_node) if not self.G_traversal.nodes[n].get('reachable')]
                    for equation in next_equation_nodes:
                        self.G_traversal.add_edge(symbol_node,equation)
                        if self.G_traversal.has_edge(equation, symbol_node):
                            self.G_traversal.remove_edge(equation, symbol_node)
                        self.worklist.append(equation)
        return

    def _check_traversal_successful(self):
        return all(self.G_traversal.nodes[target].get('reachable') and not self.G_traversal.nodes[target].get('value') is None for target in self.find)

    def _filter_reachable_nodes(self, node):
        return self.G_traversal.nodes[node].get('reachable') and self._filter_useful_nodes(node)
    
    def _filter_useful_nodes(self, node):
        for tgt in self.find:
            if node == tgt:
                return True
            if node in nx.ancestors(self.G_traversal, tgt):
                return True
        return False
        
    def _simplify(self):
        self.G_optimized = nx.subgraph_view(self.G_traversal, filter_node=self._filter_reachable_nodes)

    def draw_nx(self, graph, values={}, save=False, title=''):
        labeldict = {}
        if values:
            for n in graph:
                if n in self.equations:
                    labeldict[n] = f'{n}\n{self.equations[n]}'
                elif n in values and not values[n] is None:
                    labeldict[n] = f'{n}\n{values[n]:.2f}'
                else:
                    labeldict[n] = n

        colormap = {'object': '#66c2a5', 'symbol': '#fc8d62', 'equation': '#cbd5e8', 'given': '#b2df8a', 'find': '#fb9a99', 'constraint': '#8da0cb', 'neutral': '#fdcdac'} 
        colors = []
        for n in graph.nodes():
            if n in self.find:
                colors.append(colormap['find'])
            elif n in self.assignments:
                colors.append(colormap['given'])
            elif n in self.equations:
                colors.append(colormap['equation'])
            else:
                colors.append(colormap['neutral'])
        
        plt.figure(figsize=(20,20))
        plt.title('Graph: ' + title, {'fontsize': 20})
        pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")
        if labeldict:
            nx.draw(graph, pos, labels=labeldict, with_labels=True, node_color=colors, node_size=2500)
        else:
            nx.draw(graph, pos, with_labels=True, node_color=colors, node_size=2500)
        if save:
            plt.savefig(f'Graph{title}.svg', transparent=True)
        plt.show()