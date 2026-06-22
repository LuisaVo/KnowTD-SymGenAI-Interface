# Auto generated from thermodynamics_ontology.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-18T14:55:07
# Schema: thermo_ontology
#
# id: https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml
# description: Ontology to describe classes relating to thermodynamics. It consists of concepts, variables, attributes, equations, rules and problems
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "2.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
THMO_ATTRIBUTES = CurieNamespace('thmo_attributes', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_attributes.yaml/')
THMO_CONCEPTS = CurieNamespace('thmo_concepts', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_concepts.yaml/')
THMO_EQUATIONS = CurieNamespace('thmo_equations', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_equations.yaml/')
THMO_PROBLEMS = CurieNamespace('thmo_problems', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_problems.yaml/')
THMO_RULES = CurieNamespace('thmo_rules', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_rules.yaml/')
THMO_VARIABLES = CurieNamespace('thmo_variables', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_variables.yaml/')
WIKIDATA = CurieNamespace('wikidata', 'https://www.wikidata.org/wiki/')
DEFAULT_ = CurieNamespace('', 'https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/')


# Types

# Class references
class ConceptId(extended_str):
    pass


class SystemId(ConceptId):
    pass


class ClosedSystemId(SystemId):
    pass


class OpenSystemId(SystemId):
    pass


class MaterialId(ConceptId):
    pass


class PureMaterialId(MaterialId):
    pass


class MixtureId(MaterialId):
    pass


class EquationOfStateId(ConceptId):
    pass


class StateId(ConceptId):
    pass


class TransitionId(ConceptId):
    pass


class ChangeOfStateId(ConceptId):
    pass


class EquationId(extended_str):
    pass


class InequalityId(EquationId):
    pass


class SecondLawAdiabaticIrreversibleId(InequalityId):
    pass


class BaseEquationId(EquationId):
    pass


class DefiningEquationId(BaseEquationId):
    pass


class AdditionalEquationId(EquationId):
    pass


class SystemEquationId(EquationId):
    pass


class AmountOfSubstanceEquationId(SystemEquationId):
    pass


class MaterialEquationId(EquationId):
    pass


class MolarHeatCapacityConstantPressureEquationId(MaterialEquationId):
    pass


class MolarHeatCapacityConstantVolumeEquationId(MaterialEquationId):
    pass


class KappaPolytropicExponentEquationId(MaterialEquationId):
    pass


class IdealGasEquationId(MaterialEquationId):
    pass


class CaloricEquationOfStateIdealGasId(IdealGasEquationId):
    pass


class SpecificGasConstantEquationId(IdealGasEquationId):
    pass


class StateEquationId(EquationId):
    pass


class EnthalpyEquationId(StateEquationId):
    pass


class SpecificEnthalpyEquationId(StateEquationId):
    pass


class ThermalDensityEquationId(StateEquationId):
    pass


class SystemInStateEquationId(EquationId):
    pass


class SpecificStateVariableVEquationId(SystemInStateEquationId):
    pass


class SpecificStateVariableUEquationId(SystemInStateEquationId):
    pass


class SpecificStateVariableHEquationId(SystemInStateEquationId):
    pass


class SpecificStateVariableSEquationId(SystemInStateEquationId):
    pass


class MolarStateVariableSEquationId(SystemInStateEquationId):
    pass


class SpecificKineticEnergyCenterMassEquationId(SystemInStateEquationId):
    pass


class SpecificPotentialEnergyCenterMassEquationId(SystemInStateEquationId):
    pass


class SpecificDensityEquationId(SystemInStateEquationId):
    pass


class IdealGasSystemInStateEquationId(SystemInStateEquationId):
    pass


class IdealGasLawId(IdealGasSystemInStateEquationId):
    pass


class SpecificIdealGasLawId(IdealGasSystemInStateEquationId):
    pass


class IdealGasLawAmountOfSubstanceId(IdealGasSystemInStateEquationId):
    pass


class SpecificVolumeDensityEquationId(IdealGasSystemInStateEquationId):
    pass


class PerfectGasSystemInStateEquationId(SystemInStateEquationId):
    pass


class InternalEnergyEquationId(PerfectGasSystemInStateEquationId):
    pass


class ChangeOfStateEquationId(EquationId):
    pass


class ChangeOfStateDifferenceEquationId(ChangeOfStateEquationId):
    pass


class DelTEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelPEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelVEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelvEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelUEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DeluEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelHEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelhEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelSEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelsEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelsmEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelCEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelZEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelEKinEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelEPotEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DeleKinEquationId(ChangeOfStateDifferenceEquationId):
    pass


class DelePotEquationId(ChangeOfStateDifferenceEquationId):
    pass


class PolytropicExponentEquationId(ChangeOfStateEquationId):
    pass


class WorkOnInternalExternalStateEquationId(ChangeOfStateEquationId):
    pass


class SpecificWorkOnInternalExternalStateEquationId(ChangeOfStateEquationId):
    pass


class VolumeStirringElectricalWorkEquationId(ChangeOfStateEquationId):
    pass


class FirstLawId(ChangeOfStateEquationId):
    pass


class FirstLawSpecificId(ChangeOfStateEquationId):
    pass


class TechnicalWorkEquationId(ChangeOfStateEquationId):
    pass


class WorkOnExternalStateEquationId(ChangeOfStateEquationId):
    pass


class RatioVolumeEquationId(ChangeOfStateEquationId):
    pass


class RatioTemperatureEquationId(ChangeOfStateEquationId):
    pass


class RatioPressureEquationId(ChangeOfStateEquationId):
    pass


class SystemInChangeOfStateEquationId(EquationId):
    pass


class SpecificHeatTransferEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificWorkTransferEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificWorkOnInternalStateEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificWorkOnExternalStateEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificVolumeChangeWorkEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificStirringWorkEquationId(SystemInChangeOfStateEquationId):
    pass


class SpecificElectricalWorkEquationId(SystemInChangeOfStateEquationId):
    pass


class PerfectGasChangeOfStateEquationId(SystemInChangeOfStateEquationId):
    pass


class DelHPerfectGasEquationId(PerfectGasChangeOfStateEquationId):
    pass


class DelUPerfectGasEquationId(PerfectGasChangeOfStateEquationId):
    pass


class DelSPerfectGasVolumeEquationId(PerfectGasChangeOfStateEquationId):
    pass


class DelSPerfectGasVolumeEquationIIId(PerfectGasChangeOfStateEquationId):
    pass


class IsochoricEquationId(ChangeOfStateEquationId):
    pass


class IsochoricVolumeEquationId(IsochoricEquationId):
    pass


class IsochoricSpecificVolumeEquationId(IsochoricEquationId):
    pass


class IsochoricSpecificWorkOnInternalStateEquationId(IsochoricEquationId):
    pass


class IsochoricWorkOnInternalStateEquationId(IsochoricEquationId):
    pass


class IsochoricTechnicalWorkEquationId(IsochoricEquationId):
    pass


class IsochoricIdealGasEquationId(SystemInChangeOfStateEquationId):
    pass


class IsochoricIdealGasPressureTemperatureRatioId(IsochoricIdealGasEquationId):
    pass


class IsothermalChangeOfStateEquationId(ChangeOfStateEquationId):
    pass


class IsothermalPropertiesId(IsothermalChangeOfStateEquationId):
    pass


class IsothermalWorkOnInternalStateEquationId(IsothermalChangeOfStateEquationId):
    pass


class IsothermalIdealGasEquationId(SystemInChangeOfStateEquationId):
    pass


class IsothermalIdealGasPressureVolumeRatioId(IsothermalIdealGasEquationId):
    pass


class IsothermalIdealGasWorkEquationId(IsothermalIdealGasEquationId):
    pass


class IsothermalIdealGasWorkEquationIIId(IsothermalIdealGasEquationId):
    pass


class IsothermalIdealGasPolytropicExponentEquationId(IsothermalIdealGasEquationId):
    pass


class IsothermalPerfectGasEquationId(SystemInChangeOfStateEquationId):
    pass


class IsothermalPerfectGasEntropyEquationId(IsothermalPerfectGasEquationId):
    pass


class IsothermalPerfectGasWorkOnInternalStateEquationId(IsothermalPerfectGasEquationId):
    pass


class IsobaricEquationId(ChangeOfStateEquationId):
    pass


class IsobaricPropertiesId(IsobaricEquationId):
    pass


class IsobaricWorkOnInternalStateEquationId(IsobaricEquationId):
    pass


class IsobaricSpecificWorkOnInternalStateEquationId(IsobaricEquationId):
    pass


class IsobaricPolytropicExponentEquationId(IsobaricEquationId):
    pass


class IsobaricPerfectGasEquationId(SystemInChangeOfStateEquationId):
    pass


class IsobaricPerfectGasHeatEquationId(IsobaricPerfectGasEquationId):
    pass


class AdiabaticEquationId(ChangeOfStateEquationId):
    pass


class AdiabaticHeatEquationId(AdiabaticEquationId):
    pass


class AdiabaticSpecificHeatEquationId(AdiabaticEquationId):
    pass


class IsentropicEquationId(ChangeOfStateEquationId):
    pass


class IsentropicHeatEquationId(IsentropicEquationId):
    pass


class IsentropicEntropyEquationId(IsentropicEquationId):
    pass


class IsentropicMolarEntropyEquationId(IsentropicEquationId):
    pass


class IsentropicPerfectGasEquationId(SystemInChangeOfStateEquationId):
    pass


class IsentropicPerfectGasPolytropicExponentEquationId(IsentropicPerfectGasEquationId):
    pass


class IsentropicPerfectGasTechnicalWorkEquationId(IsentropicPerfectGasEquationId):
    pass


class IsentropicPerfectGasWorkEquationId(IsentropicPerfectGasEquationId):
    pass


class IsentropicPerfectGasTemperatureEquationId(IsentropicPerfectGasEquationId):
    pass


class PolytropicEquationId(SystemInChangeOfStateEquationId):
    pass


class PolytropicWorkEquationId(PolytropicEquationId):
    pass


class IdealGasPolytropicChangeOfStateEquationId(SystemInChangeOfStateEquationId):
    pass


class IdealGasPolytropicChangeOfStateEquationIIId(SystemInChangeOfStateEquationId):
    pass


class NotInMotionEquationId(ChangeOfStateEquationId):
    pass


class NotInMotionDelCEquationId(NotInMotionEquationId):
    pass


class NotInMotionDelZEquationId(NotInMotionEquationId):
    pass


class NotInMotionDelEkinEquationId(NotInMotionEquationId):
    pass


class NotInMotionDelekinEquationId(NotInMotionEquationId):
    pass


class NotInMotionDelEpotEquationId(NotInMotionEquationId):
    pass


class NotInMotionDelepotEquationId(NotInMotionEquationId):
    pass


class Element(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["Element"]
    class_class_curie: ClassVar[str] = "thmo_concepts:Element"
    class_name: ClassVar[str] = "Element"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Element")


@dataclass(repr=False)
class Concept(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["Concept"]
    class_class_curie: ClassVar[str] = "thmo_concepts:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Concept")

    id: Union[str, ConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class System(Concept):
    """
    Is the part of the universe, we are studying.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["System"]
    class_class_curie: ClassVar[str] = "thmo_concepts:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/System")

    id: Union[str, SystemId] = None
    material: Optional[Union[str, PureMaterialId]] = None
    m: Optional[Union[dict, "Mass"]] = None
    n: Optional[Union[dict, "AmountOfSubstance"]] = None
    related_changes_and_states: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    related_changes: Optional[Union[Union[str, ChangeOfStateId], List[Union[str, ChangeOfStateId]]]] = empty_list()
    related_states: Optional[Union[Union[str, StateId], List[Union[str, StateId]]]] = empty_list()
    closed: Optional[Union[bool, Bool]] = True
    equilibrium: Optional[Union[bool, Bool]] = True
    motion: Optional[Union[bool, Bool]] = False
    homogeneous: Optional[Union[bool, Bool]] = True
    amount_of_substance_equation: Optional[Union[str, AmountOfSubstanceEquationId]] = None
    isothermal_perfect_gas_work_on_internal_state_equation: Optional[Union[str, IsothermalPerfectGasWorkOnInternalStateEquationId]] = None
    specific_state_variable_v_equation: Optional[Union[str, SpecificStateVariableVEquationId]] = None
    specific_state_variable_u_equation: Optional[Union[str, SpecificStateVariableUEquationId]] = None
    specific_state_variable_h_equation: Optional[Union[str, SpecificStateVariableHEquationId]] = None
    specific_state_variable_s_equation: Optional[Union[str, SpecificStateVariableSEquationId]] = None
    molar_state_variable_s_equation: Optional[Union[str, MolarStateVariableSEquationId]] = None
    specific_kinetic_energy_center_mass_equation: Optional[Union[str, SpecificKineticEnergyCenterMassEquationId]] = None
    specific_potential_energy_center_mass_equation: Optional[Union[str, SpecificPotentialEnergyCenterMassEquationId]] = None
    specific_density_equation: Optional[Union[str, SpecificDensityEquationId]] = None
    ideal_gas_law: Optional[Union[str, IdealGasLawId]] = None
    specific_ideal_gas_law: Optional[Union[str, SpecificIdealGasLawId]] = None
    ideal_gas_law_amount_of_substance: Optional[Union[str, IdealGasLawAmountOfSubstanceId]] = None
    internal_energy_equation: Optional[Union[str, InternalEnergyEquationId]] = None
    specific_volume_density_equation: Optional[Union[str, SpecificVolumeDensityEquationId]] = None
    specific_heat_transfer_equation: Optional[Union[str, SpecificHeatTransferEquationId]] = None
    specific_work_transfer_equation: Optional[Union[str, SpecificWorkTransferEquationId]] = None
    specific_work_on_internal_state_equation: Optional[Union[str, SpecificWorkOnInternalStateEquationId]] = None
    specific_work_on_external_state_equation: Optional[Union[str, SpecificWorkOnExternalStateEquationId]] = None
    specific_volume_change_work_equation: Optional[Union[str, SpecificVolumeChangeWorkEquationId]] = None
    specific_stirring_work_equation: Optional[Union[str, SpecificStirringWorkEquationId]] = None
    specific_electrical_work_equation: Optional[Union[str, SpecificElectricalWorkEquationId]] = None
    ideal_gas_polytropic_change_of_state_equation: Optional[Union[str, IdealGasPolytropicChangeOfStateEquationId]] = None
    ideal_gas_polytropic_change_of_state_equationII: Optional[Union[str, IdealGasPolytropicChangeOfStateEquationIIId]] = None
    polytropic_work_equation: Optional[Union[str, PolytropicWorkEquationId]] = None
    isentropic_perfect_gas_polytropic_exponent_equation: Optional[Union[str, IsentropicPerfectGasPolytropicExponentEquationId]] = None
    isentropic_perfect_gas_work_equation: Optional[Union[str, IsentropicPerfectGasWorkEquationId]] = None
    isobaric_perfect_gas_heat_equation: Optional[Union[str, IsobaricPerfectGasHeatEquationId]] = None
    isothermal_ideal_gas_pressure_volume_ratio: Optional[Union[str, IsothermalIdealGasPressureVolumeRatioId]] = None
    isothermal_ideal_gas_work_equation: Optional[Union[str, IsothermalIdealGasWorkEquationId]] = None
    isothermal_ideal_gas_work_equation_II: Optional[Union[str, IsothermalIdealGasWorkEquationIIId]] = None
    isothermal_ideal_gas_polytropic_exponent_equation: Optional[Union[str, IsothermalIdealGasPolytropicExponentEquationId]] = None
    isothermal_perfect_gas_entropy_equation: Optional[Union[str, IsothermalPerfectGasEntropyEquationId]] = None
    isochoric_ideal_gas_pressure_temperature_ratio: Optional[Union[str, IsochoricIdealGasPressureTemperatureRatioId]] = None
    del_H_perfect_gas_equation: Optional[Union[str, DelHPerfectGasEquationId]] = None
    del_U_perfect_gas_equation: Optional[Union[str, DelUPerfectGasEquationId]] = None
    del_S_perfect_gas_volume_equation: Optional[Union[str, DelSPerfectGasVolumeEquationId]] = None
    del_S_perfect_gas_volume_equation_ii: Optional[Union[str, DelSPerfectGasVolumeEquationIIId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemId):
            self.id = SystemId(self.id)

        if self.material is not None and not isinstance(self.material, PureMaterialId):
            self.material = PureMaterialId(self.material)

        if self.m is not None and not isinstance(self.m, Mass):
            self.m = Mass(**as_dict(self.m))

        if self.n is not None and not isinstance(self.n, AmountOfSubstance):
            self.n = AmountOfSubstance(**as_dict(self.n))

        if not isinstance(self.related_changes_and_states, list):
            self.related_changes_and_states = [self.related_changes_and_states] if self.related_changes_and_states is not None else []
        self.related_changes_and_states = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.related_changes_and_states]

        if not isinstance(self.related_changes, list):
            self.related_changes = [self.related_changes] if self.related_changes is not None else []
        self.related_changes = [v if isinstance(v, ChangeOfStateId) else ChangeOfStateId(v) for v in self.related_changes]

        if not isinstance(self.related_states, list):
            self.related_states = [self.related_states] if self.related_states is not None else []
        self.related_states = [v if isinstance(v, StateId) else StateId(v) for v in self.related_states]

        if self.closed is not None and not isinstance(self.closed, Bool):
            self.closed = Bool(self.closed)

        if self.equilibrium is not None and not isinstance(self.equilibrium, Bool):
            self.equilibrium = Bool(self.equilibrium)

        if self.motion is not None and not isinstance(self.motion, Bool):
            self.motion = Bool(self.motion)

        if self.homogeneous is not None and not isinstance(self.homogeneous, Bool):
            self.homogeneous = Bool(self.homogeneous)

        if self.amount_of_substance_equation is not None and not isinstance(self.amount_of_substance_equation, AmountOfSubstanceEquationId):
            self.amount_of_substance_equation = AmountOfSubstanceEquationId(self.amount_of_substance_equation)

        if self.isothermal_perfect_gas_work_on_internal_state_equation is not None and not isinstance(self.isothermal_perfect_gas_work_on_internal_state_equation, IsothermalPerfectGasWorkOnInternalStateEquationId):
            self.isothermal_perfect_gas_work_on_internal_state_equation = IsothermalPerfectGasWorkOnInternalStateEquationId(self.isothermal_perfect_gas_work_on_internal_state_equation)

        if self.specific_state_variable_v_equation is not None and not isinstance(self.specific_state_variable_v_equation, SpecificStateVariableVEquationId):
            self.specific_state_variable_v_equation = SpecificStateVariableVEquationId(self.specific_state_variable_v_equation)

        if self.specific_state_variable_u_equation is not None and not isinstance(self.specific_state_variable_u_equation, SpecificStateVariableUEquationId):
            self.specific_state_variable_u_equation = SpecificStateVariableUEquationId(self.specific_state_variable_u_equation)

        if self.specific_state_variable_h_equation is not None and not isinstance(self.specific_state_variable_h_equation, SpecificStateVariableHEquationId):
            self.specific_state_variable_h_equation = SpecificStateVariableHEquationId(self.specific_state_variable_h_equation)

        if self.specific_state_variable_s_equation is not None and not isinstance(self.specific_state_variable_s_equation, SpecificStateVariableSEquationId):
            self.specific_state_variable_s_equation = SpecificStateVariableSEquationId(self.specific_state_variable_s_equation)

        if self.molar_state_variable_s_equation is not None and not isinstance(self.molar_state_variable_s_equation, MolarStateVariableSEquationId):
            self.molar_state_variable_s_equation = MolarStateVariableSEquationId(self.molar_state_variable_s_equation)

        if self.specific_kinetic_energy_center_mass_equation is not None and not isinstance(self.specific_kinetic_energy_center_mass_equation, SpecificKineticEnergyCenterMassEquationId):
            self.specific_kinetic_energy_center_mass_equation = SpecificKineticEnergyCenterMassEquationId(self.specific_kinetic_energy_center_mass_equation)

        if self.specific_potential_energy_center_mass_equation is not None and not isinstance(self.specific_potential_energy_center_mass_equation, SpecificPotentialEnergyCenterMassEquationId):
            self.specific_potential_energy_center_mass_equation = SpecificPotentialEnergyCenterMassEquationId(self.specific_potential_energy_center_mass_equation)

        if self.specific_density_equation is not None and not isinstance(self.specific_density_equation, SpecificDensityEquationId):
            self.specific_density_equation = SpecificDensityEquationId(self.specific_density_equation)

        if self.ideal_gas_law is not None and not isinstance(self.ideal_gas_law, IdealGasLawId):
            self.ideal_gas_law = IdealGasLawId(self.ideal_gas_law)

        if self.specific_ideal_gas_law is not None and not isinstance(self.specific_ideal_gas_law, SpecificIdealGasLawId):
            self.specific_ideal_gas_law = SpecificIdealGasLawId(self.specific_ideal_gas_law)

        if self.ideal_gas_law_amount_of_substance is not None and not isinstance(self.ideal_gas_law_amount_of_substance, IdealGasLawAmountOfSubstanceId):
            self.ideal_gas_law_amount_of_substance = IdealGasLawAmountOfSubstanceId(self.ideal_gas_law_amount_of_substance)

        if self.internal_energy_equation is not None and not isinstance(self.internal_energy_equation, InternalEnergyEquationId):
            self.internal_energy_equation = InternalEnergyEquationId(self.internal_energy_equation)

        if self.specific_volume_density_equation is not None and not isinstance(self.specific_volume_density_equation, SpecificVolumeDensityEquationId):
            self.specific_volume_density_equation = SpecificVolumeDensityEquationId(self.specific_volume_density_equation)

        if self.specific_heat_transfer_equation is not None and not isinstance(self.specific_heat_transfer_equation, SpecificHeatTransferEquationId):
            self.specific_heat_transfer_equation = SpecificHeatTransferEquationId(self.specific_heat_transfer_equation)

        if self.specific_work_transfer_equation is not None and not isinstance(self.specific_work_transfer_equation, SpecificWorkTransferEquationId):
            self.specific_work_transfer_equation = SpecificWorkTransferEquationId(self.specific_work_transfer_equation)

        if self.specific_work_on_internal_state_equation is not None and not isinstance(self.specific_work_on_internal_state_equation, SpecificWorkOnInternalStateEquationId):
            self.specific_work_on_internal_state_equation = SpecificWorkOnInternalStateEquationId(self.specific_work_on_internal_state_equation)

        if self.specific_work_on_external_state_equation is not None and not isinstance(self.specific_work_on_external_state_equation, SpecificWorkOnExternalStateEquationId):
            self.specific_work_on_external_state_equation = SpecificWorkOnExternalStateEquationId(self.specific_work_on_external_state_equation)

        if self.specific_volume_change_work_equation is not None and not isinstance(self.specific_volume_change_work_equation, SpecificVolumeChangeWorkEquationId):
            self.specific_volume_change_work_equation = SpecificVolumeChangeWorkEquationId(self.specific_volume_change_work_equation)

        if self.specific_stirring_work_equation is not None and not isinstance(self.specific_stirring_work_equation, SpecificStirringWorkEquationId):
            self.specific_stirring_work_equation = SpecificStirringWorkEquationId(self.specific_stirring_work_equation)

        if self.specific_electrical_work_equation is not None and not isinstance(self.specific_electrical_work_equation, SpecificElectricalWorkEquationId):
            self.specific_electrical_work_equation = SpecificElectricalWorkEquationId(self.specific_electrical_work_equation)

        if self.ideal_gas_polytropic_change_of_state_equation is not None and not isinstance(self.ideal_gas_polytropic_change_of_state_equation, IdealGasPolytropicChangeOfStateEquationId):
            self.ideal_gas_polytropic_change_of_state_equation = IdealGasPolytropicChangeOfStateEquationId(self.ideal_gas_polytropic_change_of_state_equation)

        if self.ideal_gas_polytropic_change_of_state_equationII is not None and not isinstance(self.ideal_gas_polytropic_change_of_state_equationII, IdealGasPolytropicChangeOfStateEquationIIId):
            self.ideal_gas_polytropic_change_of_state_equationII = IdealGasPolytropicChangeOfStateEquationIIId(self.ideal_gas_polytropic_change_of_state_equationII)

        if self.polytropic_work_equation is not None and not isinstance(self.polytropic_work_equation, PolytropicWorkEquationId):
            self.polytropic_work_equation = PolytropicWorkEquationId(self.polytropic_work_equation)

        if self.isentropic_perfect_gas_polytropic_exponent_equation is not None and not isinstance(self.isentropic_perfect_gas_polytropic_exponent_equation, IsentropicPerfectGasPolytropicExponentEquationId):
            self.isentropic_perfect_gas_polytropic_exponent_equation = IsentropicPerfectGasPolytropicExponentEquationId(self.isentropic_perfect_gas_polytropic_exponent_equation)

        if self.isentropic_perfect_gas_work_equation is not None and not isinstance(self.isentropic_perfect_gas_work_equation, IsentropicPerfectGasWorkEquationId):
            self.isentropic_perfect_gas_work_equation = IsentropicPerfectGasWorkEquationId(self.isentropic_perfect_gas_work_equation)

        if self.isobaric_perfect_gas_heat_equation is not None and not isinstance(self.isobaric_perfect_gas_heat_equation, IsobaricPerfectGasHeatEquationId):
            self.isobaric_perfect_gas_heat_equation = IsobaricPerfectGasHeatEquationId(self.isobaric_perfect_gas_heat_equation)

        if self.isothermal_ideal_gas_pressure_volume_ratio is not None and not isinstance(self.isothermal_ideal_gas_pressure_volume_ratio, IsothermalIdealGasPressureVolumeRatioId):
            self.isothermal_ideal_gas_pressure_volume_ratio = IsothermalIdealGasPressureVolumeRatioId(self.isothermal_ideal_gas_pressure_volume_ratio)

        if self.isothermal_ideal_gas_work_equation is not None and not isinstance(self.isothermal_ideal_gas_work_equation, IsothermalIdealGasWorkEquationId):
            self.isothermal_ideal_gas_work_equation = IsothermalIdealGasWorkEquationId(self.isothermal_ideal_gas_work_equation)

        if self.isothermal_ideal_gas_work_equation_II is not None and not isinstance(self.isothermal_ideal_gas_work_equation_II, IsothermalIdealGasWorkEquationIIId):
            self.isothermal_ideal_gas_work_equation_II = IsothermalIdealGasWorkEquationIIId(self.isothermal_ideal_gas_work_equation_II)

        if self.isothermal_ideal_gas_polytropic_exponent_equation is not None and not isinstance(self.isothermal_ideal_gas_polytropic_exponent_equation, IsothermalIdealGasPolytropicExponentEquationId):
            self.isothermal_ideal_gas_polytropic_exponent_equation = IsothermalIdealGasPolytropicExponentEquationId(self.isothermal_ideal_gas_polytropic_exponent_equation)

        if self.isothermal_perfect_gas_entropy_equation is not None and not isinstance(self.isothermal_perfect_gas_entropy_equation, IsothermalPerfectGasEntropyEquationId):
            self.isothermal_perfect_gas_entropy_equation = IsothermalPerfectGasEntropyEquationId(self.isothermal_perfect_gas_entropy_equation)

        if self.isochoric_ideal_gas_pressure_temperature_ratio is not None and not isinstance(self.isochoric_ideal_gas_pressure_temperature_ratio, IsochoricIdealGasPressureTemperatureRatioId):
            self.isochoric_ideal_gas_pressure_temperature_ratio = IsochoricIdealGasPressureTemperatureRatioId(self.isochoric_ideal_gas_pressure_temperature_ratio)

        if self.del_H_perfect_gas_equation is not None and not isinstance(self.del_H_perfect_gas_equation, DelHPerfectGasEquationId):
            self.del_H_perfect_gas_equation = DelHPerfectGasEquationId(self.del_H_perfect_gas_equation)

        if self.del_U_perfect_gas_equation is not None and not isinstance(self.del_U_perfect_gas_equation, DelUPerfectGasEquationId):
            self.del_U_perfect_gas_equation = DelUPerfectGasEquationId(self.del_U_perfect_gas_equation)

        if self.del_S_perfect_gas_volume_equation is not None and not isinstance(self.del_S_perfect_gas_volume_equation, DelSPerfectGasVolumeEquationId):
            self.del_S_perfect_gas_volume_equation = DelSPerfectGasVolumeEquationId(self.del_S_perfect_gas_volume_equation)

        if self.del_S_perfect_gas_volume_equation_ii is not None and not isinstance(self.del_S_perfect_gas_volume_equation_ii, DelSPerfectGasVolumeEquationIIId):
            self.del_S_perfect_gas_volume_equation_ii = DelSPerfectGasVolumeEquationIIId(self.del_S_perfect_gas_volume_equation_ii)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClosedSystem(System):
    """
    A closed thermodynamic system contains a macroscopic amount of matter. There is no mass flow across its boundary,
    the mass of the system is constant. Work and heat can be transferred across the system's boundary. The boundary
    can be a real object (e.g. walls) or we can just imagine it. The system can move freely in space. Everything
    outside the system is called "surroundings".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["ClosedSystem"]
    class_class_curie: ClassVar[str] = "thmo_concepts:ClosedSystem"
    class_name: ClassVar[str] = "ClosedSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ClosedSystem")

    id: Union[str, ClosedSystemId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClosedSystemId):
            self.id = ClosedSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpenSystem(System):
    """
    An open system is a fixed part of the space that we are interested in. Work and heat as well as matter can be
    transferred across its boundary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["OpenSystem"]
    class_class_curie: ClassVar[str] = "thmo_concepts:OpenSystem"
    class_name: ClassVar[str] = "OpenSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/OpenSystem")

    id: Union[str, OpenSystemId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OpenSystemId):
            self.id = OpenSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Material(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["Material"]
    class_class_curie: ClassVar[str] = "thmo_concepts:Material"
    class_name: ClassVar[str] = "Material"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Material")

    id: Union[str, MaterialId] = None
    homogeneous: Optional[Union[bool, Bool]] = True
    pure: Optional[Union[bool, Bool]] = None
    mixed: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialId):
            self.id = MaterialId(self.id)

        if self.homogeneous is not None and not isinstance(self.homogeneous, Bool):
            self.homogeneous = Bool(self.homogeneous)

        if self.pure is not None and not isinstance(self.pure, Bool):
            self.pure = Bool(self.pure)

        if self.mixed is not None and not isinstance(self.mixed, Bool):
            self.mixed = Bool(self.mixed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PureMaterial(Material):
    """
    A pure material contains only a single component.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["PureMaterial"]
    class_class_curie: ClassVar[str] = "thmo_concepts:PureMaterial"
    class_name: ClassVar[str] = "PureMaterial"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PureMaterial")

    id: Union[str, PureMaterialId] = None
    equation_of_state: Optional[Union[dict, "EquationOfState"]] = None
    M: Optional[Union[dict, "MolarMass"]] = None
    R: Optional[Union[dict, "IndividualGasConstant"]] = None
    kappa: Optional[Union[dict, "HeatCapacityRatio"]] = None
    Rbar: Optional[Union[dict, "UniversalGasConstant"]] = None
    c_p: Optional[Union[dict, "SpecificHeatCapacityConstantPressure"]] = None
    c_v: Optional[Union[dict, "SpecificHeatCapacityConstantVolume"]] = None
    c_pm: Optional[Union[dict, "MolarHeatCapacityConstantPressure"]] = None
    c_vm: Optional[Union[dict, "MolarHeatCapacityConstantVolume"]] = None
    specific_gas_constant_equation: Optional[Union[str, SpecificGasConstantEquationId]] = None
    kappa_polytropic_exponent_equation: Optional[Union[str, KappaPolytropicExponentEquationId]] = None
    molar_heat_capacity_constant_pressure_equation: Optional[Union[str, MolarHeatCapacityConstantPressureEquationId]] = None
    molar_heat_capacity_constant_volume_equation: Optional[Union[str, MolarHeatCapacityConstantVolumeEquationId]] = None
    caloric_equation_of_state_ideal_gas: Optional[Union[str, CaloricEquationOfStateIdealGasId]] = None
    homogeneous: Optional[Union[bool, Bool]] = True
    pure: Optional[Union[bool, Bool]] = True

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PureMaterialId):
            self.id = PureMaterialId(self.id)

        if self.equation_of_state is not None and not isinstance(self.equation_of_state, EquationOfState):
            self.equation_of_state = EquationOfState(**as_dict(self.equation_of_state))

        if self.M is not None and not isinstance(self.M, MolarMass):
            self.M = MolarMass(**as_dict(self.M))

        if self.R is not None and not isinstance(self.R, IndividualGasConstant):
            self.R = IndividualGasConstant(**as_dict(self.R))

        if self.kappa is not None and not isinstance(self.kappa, HeatCapacityRatio):
            self.kappa = HeatCapacityRatio(**as_dict(self.kappa))

        if self.Rbar is not None and not isinstance(self.Rbar, UniversalGasConstant):
            self.Rbar = UniversalGasConstant(**as_dict(self.Rbar))

        if self.c_p is not None and not isinstance(self.c_p, SpecificHeatCapacityConstantPressure):
            self.c_p = SpecificHeatCapacityConstantPressure(**as_dict(self.c_p))

        if self.c_v is not None and not isinstance(self.c_v, SpecificHeatCapacityConstantVolume):
            self.c_v = SpecificHeatCapacityConstantVolume(**as_dict(self.c_v))

        if self.c_pm is not None and not isinstance(self.c_pm, MolarHeatCapacityConstantPressure):
            self.c_pm = MolarHeatCapacityConstantPressure(**as_dict(self.c_pm))

        if self.c_vm is not None and not isinstance(self.c_vm, MolarHeatCapacityConstantVolume):
            self.c_vm = MolarHeatCapacityConstantVolume(**as_dict(self.c_vm))

        if self.specific_gas_constant_equation is not None and not isinstance(self.specific_gas_constant_equation, SpecificGasConstantEquationId):
            self.specific_gas_constant_equation = SpecificGasConstantEquationId(self.specific_gas_constant_equation)

        if self.kappa_polytropic_exponent_equation is not None and not isinstance(self.kappa_polytropic_exponent_equation, KappaPolytropicExponentEquationId):
            self.kappa_polytropic_exponent_equation = KappaPolytropicExponentEquationId(self.kappa_polytropic_exponent_equation)

        if self.molar_heat_capacity_constant_pressure_equation is not None and not isinstance(self.molar_heat_capacity_constant_pressure_equation, MolarHeatCapacityConstantPressureEquationId):
            self.molar_heat_capacity_constant_pressure_equation = MolarHeatCapacityConstantPressureEquationId(self.molar_heat_capacity_constant_pressure_equation)

        if self.molar_heat_capacity_constant_volume_equation is not None and not isinstance(self.molar_heat_capacity_constant_volume_equation, MolarHeatCapacityConstantVolumeEquationId):
            self.molar_heat_capacity_constant_volume_equation = MolarHeatCapacityConstantVolumeEquationId(self.molar_heat_capacity_constant_volume_equation)

        if self.caloric_equation_of_state_ideal_gas is not None and not isinstance(self.caloric_equation_of_state_ideal_gas, CaloricEquationOfStateIdealGasId):
            self.caloric_equation_of_state_ideal_gas = CaloricEquationOfStateIdealGasId(self.caloric_equation_of_state_ideal_gas)

        if self.homogeneous is not None and not isinstance(self.homogeneous, Bool):
            self.homogeneous = Bool(self.homogeneous)

        if self.pure is not None and not isinstance(self.pure, Bool):
            self.pure = Bool(self.pure)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mixture(Material):
    """
    A mixture contains at least two components.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["Mixture"]
    class_class_curie: ClassVar[str] = "thmo_concepts:Mixture"
    class_name: ClassVar[str] = "Mixture"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Mixture")

    id: Union[str, MixtureId] = None
    mixed: Optional[Union[bool, Bool]] = True

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixtureId):
            self.id = MixtureId(self.id)

        if self.mixed is not None and not isinstance(self.mixed, Bool):
            self.mixed = Bool(self.mixed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EquationOfState(Concept):
    """
    An EOS relates state variables of a given material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["EquationOfState"]
    class_class_curie: ClassVar[str] = "thmo_concepts:EquationOfState"
    class_name: ClassVar[str] = "EquationOfState"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/EquationOfState")

    id: Union[str, EquationOfStateId] = None
    model: Optional[str] = "perfect gas"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EquationOfStateId):
            self.id = EquationOfStateId(self.id)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class State(Concept):
    """
    The thermodynamic state of a system is characterized by macroscopic, measurable properties (state variables).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["State"]
    class_class_curie: ClassVar[str] = "thmo_concepts:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/State")

    id: Union[str, StateId] = None
    T: Optional[Union[dict, "Temperature"]] = None
    T0: Optional[Union[dict, "StandardTemperature"]] = None
    p: Optional[Union[dict, "Pressure"]] = None
    V: Optional[Union[dict, "Volume"]] = None
    v: Optional[Union[dict, "SpecificVolume"]] = None
    rho: Optional[Union[dict, "SpecificDensity"]] = None
    U: Optional[Union[dict, "InternalEnergy"]] = None
    u: Optional[Union[dict, "SpecificInternalEnergy"]] = None
    H: Optional[Union[dict, "Enthalpy"]] = None
    h: Optional[Union[dict, "SpecificEnthalpy"]] = None
    S: Optional[Union[dict, "Entropy"]] = None
    s: Optional[Union[dict, "SpecificEntropy"]] = None
    sm: Optional[Union[dict, "MolarEntropy"]] = None
    c: Optional[Union[dict, "VelocityCenterMass"]] = None
    z: Optional[Union[dict, "PositionCenterMass"]] = None
    E_kin: Optional[Union[dict, "KineticEnergyCenterMass"]] = None
    e_kin: Optional[Union[dict, "SpecificKineticEnergyCenterMass"]] = None
    E_pot: Optional[Union[dict, "PotentialEnergyCenterMass"]] = None
    e_pot: Optional[Union[dict, "SpecificPotentialEnergyCenterMass"]] = None
    equilibrium: Optional[Union[bool, Bool]] = True
    enthalpy_equation: Optional[Union[str, EnthalpyEquationId]] = None
    specific_enthalpy_equation: Optional[Union[str, SpecificEnthalpyEquationId]] = None
    thermal_density_equation: Optional[Union[str, ThermalDensityEquationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StateId):
            self.id = StateId(self.id)

        if self.T is not None and not isinstance(self.T, Temperature):
            self.T = Temperature(**as_dict(self.T))

        if self.T0 is not None and not isinstance(self.T0, StandardTemperature):
            self.T0 = StandardTemperature(**as_dict(self.T0))

        if self.p is not None and not isinstance(self.p, Pressure):
            self.p = Pressure(**as_dict(self.p))

        if self.V is not None and not isinstance(self.V, Volume):
            self.V = Volume(**as_dict(self.V))

        if self.v is not None and not isinstance(self.v, SpecificVolume):
            self.v = SpecificVolume(**as_dict(self.v))

        if self.rho is not None and not isinstance(self.rho, SpecificDensity):
            self.rho = SpecificDensity(**as_dict(self.rho))

        if self.U is not None and not isinstance(self.U, InternalEnergy):
            self.U = InternalEnergy(**as_dict(self.U))

        if self.u is not None and not isinstance(self.u, SpecificInternalEnergy):
            self.u = SpecificInternalEnergy(**as_dict(self.u))

        if self.H is not None and not isinstance(self.H, Enthalpy):
            self.H = Enthalpy(**as_dict(self.H))

        if self.h is not None and not isinstance(self.h, SpecificEnthalpy):
            self.h = SpecificEnthalpy(**as_dict(self.h))

        if self.S is not None and not isinstance(self.S, Entropy):
            self.S = Entropy(**as_dict(self.S))

        if self.s is not None and not isinstance(self.s, SpecificEntropy):
            self.s = SpecificEntropy(**as_dict(self.s))

        if self.sm is not None and not isinstance(self.sm, MolarEntropy):
            self.sm = MolarEntropy(**as_dict(self.sm))

        if self.c is not None and not isinstance(self.c, VelocityCenterMass):
            self.c = VelocityCenterMass(**as_dict(self.c))

        if self.z is not None and not isinstance(self.z, PositionCenterMass):
            self.z = PositionCenterMass(**as_dict(self.z))

        if self.E_kin is not None and not isinstance(self.E_kin, KineticEnergyCenterMass):
            self.E_kin = KineticEnergyCenterMass(**as_dict(self.E_kin))

        if self.e_kin is not None and not isinstance(self.e_kin, SpecificKineticEnergyCenterMass):
            self.e_kin = SpecificKineticEnergyCenterMass(**as_dict(self.e_kin))

        if self.E_pot is not None and not isinstance(self.E_pot, PotentialEnergyCenterMass):
            self.E_pot = PotentialEnergyCenterMass(**as_dict(self.E_pot))

        if self.e_pot is not None and not isinstance(self.e_pot, SpecificPotentialEnergyCenterMass):
            self.e_pot = SpecificPotentialEnergyCenterMass(**as_dict(self.e_pot))

        if self.equilibrium is not None and not isinstance(self.equilibrium, Bool):
            self.equilibrium = Bool(self.equilibrium)

        if self.enthalpy_equation is not None and not isinstance(self.enthalpy_equation, EnthalpyEquationId):
            self.enthalpy_equation = EnthalpyEquationId(self.enthalpy_equation)

        if self.specific_enthalpy_equation is not None and not isinstance(self.specific_enthalpy_equation, SpecificEnthalpyEquationId):
            self.specific_enthalpy_equation = SpecificEnthalpyEquationId(self.specific_enthalpy_equation)

        if self.thermal_density_equation is not None and not isinstance(self.thermal_density_equation, ThermalDensityEquationId):
            self.thermal_density_equation = ThermalDensityEquationId(self.thermal_density_equation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transition(Concept):
    """
    The transition is related to change of state. The exact path of the transition may be known (transition through
    equilibrium states) or not known (general case, irreversible transition).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["Transition"]
    class_class_curie: ClassVar[str] = "thmo_concepts:Transition"
    class_name: ClassVar[str] = "Transition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Transition")

    id: Union[str, TransitionId] = None
    equilibrium: Optional[Union[bool, Bool]] = None
    motion: Optional[Union[bool, Bool]] = False
    adiabatic: Optional[Union[bool, Bool]] = None
    reversible: Optional[Union[bool, Bool]] = None
    Q: Optional[Union[dict, "Heat"]] = None
    q: Optional[Union[dict, "HeatPerMass"]] = None
    W: Optional[Union[dict, "Work"]] = None
    w: Optional[Union[dict, "WorkPerMass"]] = None
    W_i: Optional[Union[dict, "WorkOnInternalState"]] = None
    W_a: Optional[Union[dict, "WorkOnExternalState"]] = None
    w_i: Optional[Union[dict, "WorkOnInternalStatePerMass"]] = None
    w_a: Optional[Union[dict, "WorkOnExternalStatePerMass"]] = None
    w_t: Optional[Union[dict, "TechnicalWorkPerMass"]] = None
    W_vol: Optional[Union[dict, "VolumeChangeWork"]] = None
    w_vol: Optional[Union[dict, "VolumeChangeWorkPerMass"]] = None
    W_stir: Optional[Union[dict, "StirringWork"]] = None
    w_stir: Optional[Union[dict, "StirringWorkPerMass"]] = None
    W_electrical: Optional[Union[dict, "ElectricalWork"]] = None
    w_electrical: Optional[Union[dict, "ElectricalWorkPerMass"]] = None
    del_T: Optional[Union[dict, "TemperatureDifference"]] = None
    del_p: Optional[Union[dict, "PressureDifference"]] = None
    del_V: Optional[Union[dict, "VolumeDifference"]] = None
    del_v: Optional[Union[dict, "SpecificVolumeDifference"]] = None
    del_U: Optional[Union[dict, "InternalEnergyDifference"]] = None
    del_u: Optional[Union[dict, "SpecificInternalEnergyDifference"]] = None
    del_H: Optional[Union[dict, "EnthalpyDifference"]] = None
    del_h: Optional[Union[dict, "SpecificEnthalpyDifference"]] = None
    del_S: Optional[Union[dict, "EntropyDifference"]] = None
    del_s: Optional[Union[dict, "SpecificEntropyDifference"]] = None
    del_sm: Optional[Union[dict, "MolarEntropyDifference"]] = None
    del_z: Optional[Union[dict, "PositionCenterMassDifference"]] = None
    del_c: Optional[Union[dict, "VelocityCenterMassDifference"]] = None
    del_E_pot: Optional[Union[dict, "PotentialEnergyCenterMassDifference"]] = None
    del_e_pot: Optional[Union[dict, "SpecificPotentialEnergyCenterMassDifference"]] = None
    del_E_kin: Optional[Union[dict, "KineticEnergyCenterMassDifference"]] = None
    del_e_kin: Optional[Union[dict, "SpecificKineticEnergyCenterMassDifference"]] = None
    n_poly: Optional[Union[dict, "PolytropicExponent"]] = None
    ratio_T: Optional[Union[dict, "TemperatureRatio"]] = None
    ratio_p: Optional[Union[dict, "PressureRatio"]] = None
    ratio_v: Optional[Union[dict, "VolumeRatio"]] = None
    is_isothermal: Optional[Union[bool, Bool]] = None
    is_isochoric: Optional[Union[bool, Bool]] = None
    is_polytropic: Optional[Union[bool, Bool]] = None
    is_isobaric: Optional[Union[bool, Bool]] = None
    is_isenthalpic: Optional[Union[bool, Bool]] = None
    is_isentropic: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransitionId):
            self.id = TransitionId(self.id)

        if self.equilibrium is not None and not isinstance(self.equilibrium, Bool):
            self.equilibrium = Bool(self.equilibrium)

        if self.motion is not None and not isinstance(self.motion, Bool):
            self.motion = Bool(self.motion)

        if self.adiabatic is not None and not isinstance(self.adiabatic, Bool):
            self.adiabatic = Bool(self.adiabatic)

        if self.reversible is not None and not isinstance(self.reversible, Bool):
            self.reversible = Bool(self.reversible)

        if self.Q is not None and not isinstance(self.Q, Heat):
            self.Q = Heat(**as_dict(self.Q))

        if self.q is not None and not isinstance(self.q, HeatPerMass):
            self.q = HeatPerMass(**as_dict(self.q))

        if self.W is not None and not isinstance(self.W, Work):
            self.W = Work(**as_dict(self.W))

        if self.w is not None and not isinstance(self.w, WorkPerMass):
            self.w = WorkPerMass(**as_dict(self.w))

        if self.W_i is not None and not isinstance(self.W_i, WorkOnInternalState):
            self.W_i = WorkOnInternalState(**as_dict(self.W_i))

        if self.W_a is not None and not isinstance(self.W_a, WorkOnExternalState):
            self.W_a = WorkOnExternalState(**as_dict(self.W_a))

        if self.w_i is not None and not isinstance(self.w_i, WorkOnInternalStatePerMass):
            self.w_i = WorkOnInternalStatePerMass(**as_dict(self.w_i))

        if self.w_a is not None and not isinstance(self.w_a, WorkOnExternalStatePerMass):
            self.w_a = WorkOnExternalStatePerMass(**as_dict(self.w_a))

        if self.w_t is not None and not isinstance(self.w_t, TechnicalWorkPerMass):
            self.w_t = TechnicalWorkPerMass(**as_dict(self.w_t))

        if self.W_vol is not None and not isinstance(self.W_vol, VolumeChangeWork):
            self.W_vol = VolumeChangeWork(**as_dict(self.W_vol))

        if self.w_vol is not None and not isinstance(self.w_vol, VolumeChangeWorkPerMass):
            self.w_vol = VolumeChangeWorkPerMass(**as_dict(self.w_vol))

        if self.W_stir is not None and not isinstance(self.W_stir, StirringWork):
            self.W_stir = StirringWork(**as_dict(self.W_stir))

        if self.w_stir is not None and not isinstance(self.w_stir, StirringWorkPerMass):
            self.w_stir = StirringWorkPerMass(**as_dict(self.w_stir))

        if self.W_electrical is not None and not isinstance(self.W_electrical, ElectricalWork):
            self.W_electrical = ElectricalWork(**as_dict(self.W_electrical))

        if self.w_electrical is not None and not isinstance(self.w_electrical, ElectricalWorkPerMass):
            self.w_electrical = ElectricalWorkPerMass(**as_dict(self.w_electrical))

        if self.del_T is not None and not isinstance(self.del_T, TemperatureDifference):
            self.del_T = TemperatureDifference(**as_dict(self.del_T))

        if self.del_p is not None and not isinstance(self.del_p, PressureDifference):
            self.del_p = PressureDifference(**as_dict(self.del_p))

        if self.del_V is not None and not isinstance(self.del_V, VolumeDifference):
            self.del_V = VolumeDifference(**as_dict(self.del_V))

        if self.del_v is not None and not isinstance(self.del_v, SpecificVolumeDifference):
            self.del_v = SpecificVolumeDifference(**as_dict(self.del_v))

        if self.del_U is not None and not isinstance(self.del_U, InternalEnergyDifference):
            self.del_U = InternalEnergyDifference(**as_dict(self.del_U))

        if self.del_u is not None and not isinstance(self.del_u, SpecificInternalEnergyDifference):
            self.del_u = SpecificInternalEnergyDifference(**as_dict(self.del_u))

        if self.del_H is not None and not isinstance(self.del_H, EnthalpyDifference):
            self.del_H = EnthalpyDifference(**as_dict(self.del_H))

        if self.del_h is not None and not isinstance(self.del_h, SpecificEnthalpyDifference):
            self.del_h = SpecificEnthalpyDifference(**as_dict(self.del_h))

        if self.del_S is not None and not isinstance(self.del_S, EntropyDifference):
            self.del_S = EntropyDifference(**as_dict(self.del_S))

        if self.del_s is not None and not isinstance(self.del_s, SpecificEntropyDifference):
            self.del_s = SpecificEntropyDifference(**as_dict(self.del_s))

        if self.del_sm is not None and not isinstance(self.del_sm, MolarEntropyDifference):
            self.del_sm = MolarEntropyDifference(**as_dict(self.del_sm))

        if self.del_z is not None and not isinstance(self.del_z, PositionCenterMassDifference):
            self.del_z = PositionCenterMassDifference(**as_dict(self.del_z))

        if self.del_c is not None and not isinstance(self.del_c, VelocityCenterMassDifference):
            self.del_c = VelocityCenterMassDifference(**as_dict(self.del_c))

        if self.del_E_pot is not None and not isinstance(self.del_E_pot, PotentialEnergyCenterMassDifference):
            self.del_E_pot = PotentialEnergyCenterMassDifference(**as_dict(self.del_E_pot))

        if self.del_e_pot is not None and not isinstance(self.del_e_pot, SpecificPotentialEnergyCenterMassDifference):
            self.del_e_pot = SpecificPotentialEnergyCenterMassDifference(**as_dict(self.del_e_pot))

        if self.del_E_kin is not None and not isinstance(self.del_E_kin, KineticEnergyCenterMassDifference):
            self.del_E_kin = KineticEnergyCenterMassDifference(**as_dict(self.del_E_kin))

        if self.del_e_kin is not None and not isinstance(self.del_e_kin, SpecificKineticEnergyCenterMassDifference):
            self.del_e_kin = SpecificKineticEnergyCenterMassDifference(**as_dict(self.del_e_kin))

        if self.n_poly is not None and not isinstance(self.n_poly, PolytropicExponent):
            self.n_poly = PolytropicExponent(**as_dict(self.n_poly))

        if self.ratio_T is not None and not isinstance(self.ratio_T, TemperatureRatio):
            self.ratio_T = TemperatureRatio(**as_dict(self.ratio_T))

        if self.ratio_p is not None and not isinstance(self.ratio_p, PressureRatio):
            self.ratio_p = PressureRatio(**as_dict(self.ratio_p))

        if self.ratio_v is not None and not isinstance(self.ratio_v, VolumeRatio):
            self.ratio_v = VolumeRatio(**as_dict(self.ratio_v))

        if self.is_isothermal is not None and not isinstance(self.is_isothermal, Bool):
            self.is_isothermal = Bool(self.is_isothermal)

        if self.is_isochoric is not None and not isinstance(self.is_isochoric, Bool):
            self.is_isochoric = Bool(self.is_isochoric)

        if self.is_polytropic is not None and not isinstance(self.is_polytropic, Bool):
            self.is_polytropic = Bool(self.is_polytropic)

        if self.is_isobaric is not None and not isinstance(self.is_isobaric, Bool):
            self.is_isobaric = Bool(self.is_isobaric)

        if self.is_isenthalpic is not None and not isinstance(self.is_isenthalpic, Bool):
            self.is_isenthalpic = Bool(self.is_isenthalpic)

        if self.is_isentropic is not None and not isinstance(self.is_isentropic, Bool):
            self.is_isentropic = Bool(self.is_isentropic)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChangeOfState(Concept):
    """
    In a "change of state" a system undergoes a change from one equilibirum state (initial state) to another (final
    state). The transistion between these states may or may not be reversible.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_CONCEPTS["ChangeOfState"]
    class_class_curie: ClassVar[str] = "thmo_concepts:ChangeOfState"
    class_name: ClassVar[str] = "ChangeOfState"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ChangeOfState")

    id: Union[str, ChangeOfStateId] = None
    initial_state: Optional[Union[str, StateId]] = None
    final_state: Optional[Union[str, StateId]] = None
    transition: Optional[Union[dict, Transition]] = None
    polytropic_exponent_equation: Optional[Union[str, PolytropicExponentEquationId]] = None
    work_on_internal_external_state_equation: Optional[Union[str, WorkOnInternalExternalStateEquationId]] = None
    specific_work_on_internal_external_state_equation: Optional[Union[str, SpecificWorkOnInternalExternalStateEquationId]] = None
    volume_stirring_electrical_work_equation: Optional[Union[str, VolumeStirringElectricalWorkEquationId]] = None
    first_law: Optional[Union[str, FirstLawId]] = None
    first_law_specific: Optional[Union[str, FirstLawSpecificId]] = None
    technical_work_equation: Optional[Union[str, TechnicalWorkEquationId]] = None
    work_on_external_state_equation: Optional[Union[str, WorkOnExternalStateEquationId]] = None
    not_in_motion_del_c_equation: Optional[Union[str, NotInMotionDelCEquationId]] = None
    not_in_motion_del_z_equation: Optional[Union[str, NotInMotionDelZEquationId]] = None
    not_in_motion_del_E_kin_equation: Optional[Union[str, NotInMotionDelEkinEquationId]] = None
    not_in_motion_del_e_kin_equation: Optional[Union[str, NotInMotionDelekinEquationId]] = None
    not_in_motion_del_E_pot_equation: Optional[Union[str, NotInMotionDelEpotEquationId]] = None
    not_in_motion_del_e_pot_equation: Optional[Union[str, NotInMotionDelepotEquationId]] = None
    adiabatic_heat_equation: Optional[Union[str, AdiabaticHeatEquationId]] = None
    adiabatic_specific_heat_equation: Optional[Union[str, AdiabaticSpecificHeatEquationId]] = None
    isentropic_heat_equation: Optional[Union[str, IsentropicHeatEquationId]] = None
    isentropic_entropy_equation: Optional[Union[str, IsentropicEntropyEquationId]] = None
    isentropic_molar_entropy_equation: Optional[Union[str, IsentropicMolarEntropyEquationId]] = None
    isobaric_properties: Optional[Union[str, IsobaricPropertiesId]] = None
    isobaric_work_on_internal_state_equation: Optional[Union[str, IsobaricWorkOnInternalStateEquationId]] = None
    isobaric_specific_work_on_internal_state_equation: Optional[Union[str, IsobaricSpecificWorkOnInternalStateEquationId]] = None
    isothermal_properties: Optional[Union[str, IsothermalPropertiesId]] = None
    isothermal_work_on_internal_state_equation: Optional[Union[str, IsothermalWorkOnInternalStateEquationId]] = None
    isochoric_volume_equation: Optional[Union[str, IsochoricVolumeEquationId]] = None
    isochoric_specific_volume_equation: Optional[Union[str, IsochoricSpecificVolumeEquationId]] = None
    isochoric_specific_work_on_internal_state_equation: Optional[Union[str, IsochoricSpecificWorkOnInternalStateEquationId]] = None
    isochoric_work_on_internal_state_equation: Optional[Union[str, IsochoricWorkOnInternalStateEquationId]] = None
    isochoric_technical_work_equation: Optional[Union[str, IsochoricTechnicalWorkEquationId]] = None
    del_T_equation: Optional[Union[str, DelTEquationId]] = None
    del_p_equation: Optional[Union[str, DelPEquationId]] = None
    del_V_equation: Optional[Union[str, DelVEquationId]] = None
    del_v_equation: Optional[Union[str, DelvEquationId]] = None
    del_U_equation: Optional[Union[str, DelUEquationId]] = None
    del_u_equation: Optional[Union[str, DeluEquationId]] = None
    del_H_equation: Optional[Union[str, DelHEquationId]] = None
    del_h_equation: Optional[Union[str, DelhEquationId]] = None
    del_S_equation: Optional[Union[str, DelSEquationId]] = None
    del_s_equation: Optional[Union[str, DelsEquationId]] = None
    del_sm_equation: Optional[Union[str, DelsmEquationId]] = None
    del_c_equation: Optional[Union[str, DelCEquationId]] = None
    del_z_equation: Optional[Union[str, DelZEquationId]] = None
    del_E_Kin_equation: Optional[Union[str, DelEKinEquationId]] = None
    del_E_Pot_equation: Optional[Union[str, DelEPotEquationId]] = None
    del_e_Kin_equation: Optional[Union[str, DeleKinEquationId]] = None
    del_e_Pot_equation: Optional[Union[str, DelePotEquationId]] = None
    ratio_pressure_equation: Optional[Union[str, RatioPressureEquationId]] = None
    ratio_volume_equation: Optional[Union[str, RatioVolumeEquationId]] = None
    ratio_temperature_equation: Optional[Union[str, RatioTemperatureEquationId]] = None
    isobaric_polytropic_exponent_equation: Optional[Union[str, IsobaricPolytropicExponentEquationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChangeOfStateId):
            self.id = ChangeOfStateId(self.id)

        if self.initial_state is not None and not isinstance(self.initial_state, StateId):
            self.initial_state = StateId(self.initial_state)

        if self.final_state is not None and not isinstance(self.final_state, StateId):
            self.final_state = StateId(self.final_state)

        if self.transition is not None and not isinstance(self.transition, Transition):
            self.transition = Transition(**as_dict(self.transition))

        if self.polytropic_exponent_equation is not None and not isinstance(self.polytropic_exponent_equation, PolytropicExponentEquationId):
            self.polytropic_exponent_equation = PolytropicExponentEquationId(self.polytropic_exponent_equation)

        if self.work_on_internal_external_state_equation is not None and not isinstance(self.work_on_internal_external_state_equation, WorkOnInternalExternalStateEquationId):
            self.work_on_internal_external_state_equation = WorkOnInternalExternalStateEquationId(self.work_on_internal_external_state_equation)

        if self.specific_work_on_internal_external_state_equation is not None and not isinstance(self.specific_work_on_internal_external_state_equation, SpecificWorkOnInternalExternalStateEquationId):
            self.specific_work_on_internal_external_state_equation = SpecificWorkOnInternalExternalStateEquationId(self.specific_work_on_internal_external_state_equation)

        if self.volume_stirring_electrical_work_equation is not None and not isinstance(self.volume_stirring_electrical_work_equation, VolumeStirringElectricalWorkEquationId):
            self.volume_stirring_electrical_work_equation = VolumeStirringElectricalWorkEquationId(self.volume_stirring_electrical_work_equation)

        if self.first_law is not None and not isinstance(self.first_law, FirstLawId):
            self.first_law = FirstLawId(self.first_law)

        if self.first_law_specific is not None and not isinstance(self.first_law_specific, FirstLawSpecificId):
            self.first_law_specific = FirstLawSpecificId(self.first_law_specific)

        if self.technical_work_equation is not None and not isinstance(self.technical_work_equation, TechnicalWorkEquationId):
            self.technical_work_equation = TechnicalWorkEquationId(self.technical_work_equation)

        if self.work_on_external_state_equation is not None and not isinstance(self.work_on_external_state_equation, WorkOnExternalStateEquationId):
            self.work_on_external_state_equation = WorkOnExternalStateEquationId(self.work_on_external_state_equation)

        if self.not_in_motion_del_c_equation is not None and not isinstance(self.not_in_motion_del_c_equation, NotInMotionDelCEquationId):
            self.not_in_motion_del_c_equation = NotInMotionDelCEquationId(self.not_in_motion_del_c_equation)

        if self.not_in_motion_del_z_equation is not None and not isinstance(self.not_in_motion_del_z_equation, NotInMotionDelZEquationId):
            self.not_in_motion_del_z_equation = NotInMotionDelZEquationId(self.not_in_motion_del_z_equation)

        if self.not_in_motion_del_E_kin_equation is not None and not isinstance(self.not_in_motion_del_E_kin_equation, NotInMotionDelEkinEquationId):
            self.not_in_motion_del_E_kin_equation = NotInMotionDelEkinEquationId(self.not_in_motion_del_E_kin_equation)

        if self.not_in_motion_del_e_kin_equation is not None and not isinstance(self.not_in_motion_del_e_kin_equation, NotInMotionDelekinEquationId):
            self.not_in_motion_del_e_kin_equation = NotInMotionDelekinEquationId(self.not_in_motion_del_e_kin_equation)

        if self.not_in_motion_del_E_pot_equation is not None and not isinstance(self.not_in_motion_del_E_pot_equation, NotInMotionDelEpotEquationId):
            self.not_in_motion_del_E_pot_equation = NotInMotionDelEpotEquationId(self.not_in_motion_del_E_pot_equation)

        if self.not_in_motion_del_e_pot_equation is not None and not isinstance(self.not_in_motion_del_e_pot_equation, NotInMotionDelepotEquationId):
            self.not_in_motion_del_e_pot_equation = NotInMotionDelepotEquationId(self.not_in_motion_del_e_pot_equation)

        if self.adiabatic_heat_equation is not None and not isinstance(self.adiabatic_heat_equation, AdiabaticHeatEquationId):
            self.adiabatic_heat_equation = AdiabaticHeatEquationId(self.adiabatic_heat_equation)

        if self.adiabatic_specific_heat_equation is not None and not isinstance(self.adiabatic_specific_heat_equation, AdiabaticSpecificHeatEquationId):
            self.adiabatic_specific_heat_equation = AdiabaticSpecificHeatEquationId(self.adiabatic_specific_heat_equation)

        if self.isentropic_heat_equation is not None and not isinstance(self.isentropic_heat_equation, IsentropicHeatEquationId):
            self.isentropic_heat_equation = IsentropicHeatEquationId(self.isentropic_heat_equation)

        if self.isentropic_entropy_equation is not None and not isinstance(self.isentropic_entropy_equation, IsentropicEntropyEquationId):
            self.isentropic_entropy_equation = IsentropicEntropyEquationId(self.isentropic_entropy_equation)

        if self.isentropic_molar_entropy_equation is not None and not isinstance(self.isentropic_molar_entropy_equation, IsentropicMolarEntropyEquationId):
            self.isentropic_molar_entropy_equation = IsentropicMolarEntropyEquationId(self.isentropic_molar_entropy_equation)

        if self.isobaric_properties is not None and not isinstance(self.isobaric_properties, IsobaricPropertiesId):
            self.isobaric_properties = IsobaricPropertiesId(self.isobaric_properties)

        if self.isobaric_work_on_internal_state_equation is not None and not isinstance(self.isobaric_work_on_internal_state_equation, IsobaricWorkOnInternalStateEquationId):
            self.isobaric_work_on_internal_state_equation = IsobaricWorkOnInternalStateEquationId(self.isobaric_work_on_internal_state_equation)

        if self.isobaric_specific_work_on_internal_state_equation is not None and not isinstance(self.isobaric_specific_work_on_internal_state_equation, IsobaricSpecificWorkOnInternalStateEquationId):
            self.isobaric_specific_work_on_internal_state_equation = IsobaricSpecificWorkOnInternalStateEquationId(self.isobaric_specific_work_on_internal_state_equation)

        if self.isothermal_properties is not None and not isinstance(self.isothermal_properties, IsothermalPropertiesId):
            self.isothermal_properties = IsothermalPropertiesId(self.isothermal_properties)

        if self.isothermal_work_on_internal_state_equation is not None and not isinstance(self.isothermal_work_on_internal_state_equation, IsothermalWorkOnInternalStateEquationId):
            self.isothermal_work_on_internal_state_equation = IsothermalWorkOnInternalStateEquationId(self.isothermal_work_on_internal_state_equation)

        if self.isochoric_volume_equation is not None and not isinstance(self.isochoric_volume_equation, IsochoricVolumeEquationId):
            self.isochoric_volume_equation = IsochoricVolumeEquationId(self.isochoric_volume_equation)

        if self.isochoric_specific_volume_equation is not None and not isinstance(self.isochoric_specific_volume_equation, IsochoricSpecificVolumeEquationId):
            self.isochoric_specific_volume_equation = IsochoricSpecificVolumeEquationId(self.isochoric_specific_volume_equation)

        if self.isochoric_specific_work_on_internal_state_equation is not None and not isinstance(self.isochoric_specific_work_on_internal_state_equation, IsochoricSpecificWorkOnInternalStateEquationId):
            self.isochoric_specific_work_on_internal_state_equation = IsochoricSpecificWorkOnInternalStateEquationId(self.isochoric_specific_work_on_internal_state_equation)

        if self.isochoric_work_on_internal_state_equation is not None and not isinstance(self.isochoric_work_on_internal_state_equation, IsochoricWorkOnInternalStateEquationId):
            self.isochoric_work_on_internal_state_equation = IsochoricWorkOnInternalStateEquationId(self.isochoric_work_on_internal_state_equation)

        if self.isochoric_technical_work_equation is not None and not isinstance(self.isochoric_technical_work_equation, IsochoricTechnicalWorkEquationId):
            self.isochoric_technical_work_equation = IsochoricTechnicalWorkEquationId(self.isochoric_technical_work_equation)

        if self.del_T_equation is not None and not isinstance(self.del_T_equation, DelTEquationId):
            self.del_T_equation = DelTEquationId(self.del_T_equation)

        if self.del_p_equation is not None and not isinstance(self.del_p_equation, DelPEquationId):
            self.del_p_equation = DelPEquationId(self.del_p_equation)

        if self.del_V_equation is not None and not isinstance(self.del_V_equation, DelVEquationId):
            self.del_V_equation = DelVEquationId(self.del_V_equation)

        if self.del_v_equation is not None and not isinstance(self.del_v_equation, DelvEquationId):
            self.del_v_equation = DelvEquationId(self.del_v_equation)

        if self.del_U_equation is not None and not isinstance(self.del_U_equation, DelUEquationId):
            self.del_U_equation = DelUEquationId(self.del_U_equation)

        if self.del_u_equation is not None and not isinstance(self.del_u_equation, DeluEquationId):
            self.del_u_equation = DeluEquationId(self.del_u_equation)

        if self.del_H_equation is not None and not isinstance(self.del_H_equation, DelHEquationId):
            self.del_H_equation = DelHEquationId(self.del_H_equation)

        if self.del_h_equation is not None and not isinstance(self.del_h_equation, DelhEquationId):
            self.del_h_equation = DelhEquationId(self.del_h_equation)

        if self.del_S_equation is not None and not isinstance(self.del_S_equation, DelSEquationId):
            self.del_S_equation = DelSEquationId(self.del_S_equation)

        if self.del_s_equation is not None and not isinstance(self.del_s_equation, DelsEquationId):
            self.del_s_equation = DelsEquationId(self.del_s_equation)

        if self.del_sm_equation is not None and not isinstance(self.del_sm_equation, DelsmEquationId):
            self.del_sm_equation = DelsmEquationId(self.del_sm_equation)

        if self.del_c_equation is not None and not isinstance(self.del_c_equation, DelCEquationId):
            self.del_c_equation = DelCEquationId(self.del_c_equation)

        if self.del_z_equation is not None and not isinstance(self.del_z_equation, DelZEquationId):
            self.del_z_equation = DelZEquationId(self.del_z_equation)

        if self.del_E_Kin_equation is not None and not isinstance(self.del_E_Kin_equation, DelEKinEquationId):
            self.del_E_Kin_equation = DelEKinEquationId(self.del_E_Kin_equation)

        if self.del_E_Pot_equation is not None and not isinstance(self.del_E_Pot_equation, DelEPotEquationId):
            self.del_E_Pot_equation = DelEPotEquationId(self.del_E_Pot_equation)

        if self.del_e_Kin_equation is not None and not isinstance(self.del_e_Kin_equation, DeleKinEquationId):
            self.del_e_Kin_equation = DeleKinEquationId(self.del_e_Kin_equation)

        if self.del_e_Pot_equation is not None and not isinstance(self.del_e_Pot_equation, DelePotEquationId):
            self.del_e_Pot_equation = DelePotEquationId(self.del_e_Pot_equation)

        if self.ratio_pressure_equation is not None and not isinstance(self.ratio_pressure_equation, RatioPressureEquationId):
            self.ratio_pressure_equation = RatioPressureEquationId(self.ratio_pressure_equation)

        if self.ratio_volume_equation is not None and not isinstance(self.ratio_volume_equation, RatioVolumeEquationId):
            self.ratio_volume_equation = RatioVolumeEquationId(self.ratio_volume_equation)

        if self.ratio_temperature_equation is not None and not isinstance(self.ratio_temperature_equation, RatioTemperatureEquationId):
            self.ratio_temperature_equation = RatioTemperatureEquationId(self.ratio_temperature_equation)

        if self.isobaric_polytropic_exponent_equation is not None and not isinstance(self.isobaric_polytropic_exponent_equation, IsobaricPolytropicExponentEquationId):
            self.isobaric_polytropic_exponent_equation = IsobaricPolytropicExponentEquationId(self.isobaric_polytropic_exponent_equation)

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Variable(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Variable"]
    class_class_curie: ClassVar[str] = "thmo_variables:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Variable")

    value: Optional[float] = None
    is_required: Optional[Union[bool, Bool]] = None
    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.is_required is not None and not isinstance(self.is_required, Bool):
            self.is_required = Bool(self.is_required)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


class VariableConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VariableConcept"]
    class_class_curie: ClassVar[str] = "thmo_variables:VariableConcept"
    class_name: ClassVar[str] = "VariableConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VariableConcept")


class DerivedVariable(VariableConcept):
    """
    A variable which can be mathematically derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["DerivedVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:DerivedVariable"
    class_name: ClassVar[str] = "DerivedVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DerivedVariable")


class Difference(DerivedVariable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Difference"]
    class_class_curie: ClassVar[str] = "thmo_variables:Difference"
    class_name: ClassVar[str] = "Difference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Difference")


class Ratio(DerivedVariable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Ratio"]
    class_class_curie: ClassVar[str] = "thmo_variables:Ratio"
    class_name: ClassVar[str] = "Ratio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Ratio")


class StateVariable(VariableConcept):
    """
    A state variable is a macroscopic measurable property that characterises a state of a system .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["StateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:StateVariable"
    class_name: ClassVar[str] = "StateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StateVariable")


class ChangeOfStateVariable(VariableConcept):
    """
    Calculable variables that characterize the change of state of a system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["ChangeOfStateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:ChangeOfStateVariable"
    class_name: ClassVar[str] = "ChangeOfStateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ChangeOfStateVariable")


class MaterialProperty(VariableConcept):
    """
    Properties that describe a material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MaterialProperty"]
    class_class_curie: ClassVar[str] = "thmo_variables:MaterialProperty"
    class_name: ClassVar[str] = "MaterialProperty"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MaterialProperty")


class UniversalQuantity(VariableConcept):
    """
    Variable that always has the same value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["UniversalQuantity"]
    class_class_curie: ClassVar[str] = "thmo_variables:UniversalQuantity"
    class_name: ClassVar[str] = "UniversalQuantity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/UniversalQuantity")


class SpecificProperty(VariableConcept):
    """
    Specific properties are extensive properties per unit mass.  We denote them by lower case letters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificProperty"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificProperty"
    class_name: ClassVar[str] = "SpecificProperty"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificProperty")


class MolarProperty(VariableConcept):
    """
    Molar properties are extensive properties per mol.  We denote them by lower case letters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarProperty"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarProperty"
    class_name: ClassVar[str] = "MolarProperty"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarProperty")


class ExtensiveStateVariable(VariableConcept):
    """
    The value of an extensive property of a homogenous system is proportional to the mass of the system. We denote
    them by upper case letters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["ExtensiveStateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:ExtensiveStateVariable"
    class_name: ClassVar[str] = "ExtensiveStateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ExtensiveStateVariable")


class IntensiveStateVariable(VariableConcept):
    """
    The value of an intensive property of a homogenous system does  not vary with the mass of the system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["IntensiveStateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:IntensiveStateVariable"
    class_name: ClassVar[str] = "IntensiveStateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IntensiveStateVariable")


class InternalStateVariable(StateVariable):
    """
    Describes the state of a system that does not move.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["InternalStateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:InternalStateVariable"
    class_name: ClassVar[str] = "InternalStateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/InternalStateVariable")


class ExternalStateVariable(StateVariable):
    """
    External state variables are state variables that depend on the internal state variables of the systems and its
    interactions with the surroundings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["ExternalStateVariable"]
    class_class_curie: ClassVar[str] = "thmo_variables:ExternalStateVariable"
    class_name: ClassVar[str] = "ExternalStateVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ExternalStateVariable")


class Mass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Mass"]
    class_class_curie: ClassVar[str] = "thmo_variables:Mass"
    class_name: ClassVar[str] = "Mass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Mass")


class MolarMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarMass"
    class_name: ClassVar[str] = "MolarMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarMass")


class Temperature(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Temperature"]
    class_class_curie: ClassVar[str] = "thmo_variables:Temperature"
    class_name: ClassVar[str] = "Temperature"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Temperature")


@dataclass(repr=False)
class StandardTemperature(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["StandardTemperature"]
    class_class_curie: ClassVar[str] = "thmo_variables:StandardTemperature"
    class_name: ClassVar[str] = "StandardTemperature"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StandardTemperature")

    value: Optional[float] = 273.15

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


class Pressure(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Pressure"]
    class_class_curie: ClassVar[str] = "thmo_variables:Pressure"
    class_name: ClassVar[str] = "Pressure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Pressure")


@dataclass(repr=False)
class StandardPressure(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["StandardPressure"]
    class_class_curie: ClassVar[str] = "thmo_variables:StandardPressure"
    class_name: ClassVar[str] = "StandardPressure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StandardPressure")

    value: Optional[float] = 101325

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


class Volume(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Volume"]
    class_class_curie: ClassVar[str] = "thmo_variables:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Volume")


class SpecificVolume(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificVolume"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificVolume"
    class_name: ClassVar[str] = "SpecificVolume"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificVolume")


class SurfaceArea(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SurfaceArea"]
    class_class_curie: ClassVar[str] = "thmo_variables:SurfaceArea"
    class_name: ClassVar[str] = "SurfaceArea"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SurfaceArea")


class InternalEnergy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["InternalEnergy"]
    class_class_curie: ClassVar[str] = "thmo_variables:InternalEnergy"
    class_name: ClassVar[str] = "InternalEnergy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/InternalEnergy")


class SpecificInternalEnergy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificInternalEnergy"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificInternalEnergy"
    class_name: ClassVar[str] = "SpecificInternalEnergy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificInternalEnergy")


class Enthalpy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Enthalpy"]
    class_class_curie: ClassVar[str] = "thmo_variables:Enthalpy"
    class_name: ClassVar[str] = "Enthalpy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Enthalpy")


class SpecificEnthalpy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificEnthalpy"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificEnthalpy"
    class_name: ClassVar[str] = "SpecificEnthalpy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificEnthalpy")


class Entropy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Entropy"]
    class_class_curie: ClassVar[str] = "thmo_variables:Entropy"
    class_name: ClassVar[str] = "Entropy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Entropy")


class SpecificEntropy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificEntropy"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificEntropy"
    class_name: ClassVar[str] = "SpecificEntropy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificEntropy")


class MolarEntropy(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarEntropy"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarEntropy"
    class_name: ClassVar[str] = "MolarEntropy"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarEntropy")


class SpecificDensity(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificDensity"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificDensity"
    class_name: ClassVar[str] = "SpecificDensity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificDensity")


class MolarDensity(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarDensity"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarDensity"
    class_name: ClassVar[str] = "MolarDensity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarDensity")


class PositionCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PositionCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:PositionCenterMass"
    class_name: ClassVar[str] = "PositionCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PositionCenterMass")


class VelocityCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VelocityCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:VelocityCenterMass"
    class_name: ClassVar[str] = "VelocityCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VelocityCenterMass")


class PotentialEnergyCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PotentialEnergyCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:PotentialEnergyCenterMass"
    class_name: ClassVar[str] = "PotentialEnergyCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PotentialEnergyCenterMass")


class SpecificPotentialEnergyCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificPotentialEnergyCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificPotentialEnergyCenterMass"
    class_name: ClassVar[str] = "SpecificPotentialEnergyCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificPotentialEnergyCenterMass")


class KineticEnergyCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["KineticEnergyCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:KineticEnergyCenterMass"
    class_name: ClassVar[str] = "KineticEnergyCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/KineticEnergyCenterMass")


class SpecificKineticEnergyCenterMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificKineticEnergyCenterMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificKineticEnergyCenterMass"
    class_name: ClassVar[str] = "SpecificKineticEnergyCenterMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificKineticEnergyCenterMass")


class AmountOfSubstance(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["AmountOfSubstance"]
    class_class_curie: ClassVar[str] = "thmo_variables:AmountOfSubstance"
    class_name: ClassVar[str] = "AmountOfSubstance"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AmountOfSubstance")


class IndividualGasConstant(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["IndividualGasConstant"]
    class_class_curie: ClassVar[str] = "thmo_variables:IndividualGasConstant"
    class_name: ClassVar[str] = "IndividualGasConstant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IndividualGasConstant")


class SpecificHeatCapacityConstantPressure(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificHeatCapacityConstantPressure"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificHeatCapacityConstantPressure"
    class_name: ClassVar[str] = "SpecificHeatCapacityConstantPressure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificHeatCapacityConstantPressure")


class SpecificHeatCapacityConstantVolume(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificHeatCapacityConstantVolume"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificHeatCapacityConstantVolume"
    class_name: ClassVar[str] = "SpecificHeatCapacityConstantVolume"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificHeatCapacityConstantVolume")


class MolarHeatCapacityConstantPressure(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarHeatCapacityConstantPressure"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarHeatCapacityConstantPressure"
    class_name: ClassVar[str] = "MolarHeatCapacityConstantPressure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarHeatCapacityConstantPressure")


class MolarHeatCapacityConstantVolume(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarHeatCapacityConstantVolume"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarHeatCapacityConstantVolume"
    class_name: ClassVar[str] = "MolarHeatCapacityConstantVolume"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarHeatCapacityConstantVolume")


class HeatCapacityRatio(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["HeatCapacityRatio"]
    class_class_curie: ClassVar[str] = "thmo_variables:HeatCapacityRatio"
    class_name: ClassVar[str] = "HeatCapacityRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/HeatCapacityRatio")


@dataclass(repr=False)
class UniversalGasConstant(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["UniversalGasConstant"]
    class_class_curie: ClassVar[str] = "thmo_variables:UniversalGasConstant"
    class_name: ClassVar[str] = "UniversalGasConstant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/UniversalGasConstant")

    value: Optional[float] = 8.31446261815324

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GravitationalAcceleration(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["GravitationalAcceleration"]
    class_class_curie: ClassVar[str] = "thmo_variables:GravitationalAcceleration"
    class_name: ClassVar[str] = "GravitationalAcceleration"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/GravitationalAcceleration")

    value: Optional[float] = 9.8067

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


class Heat(Variable):
    """
    Heat is energy transferred due to temperature differences only.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Heat"]
    class_class_curie: ClassVar[str] = "thmo_variables:Heat"
    class_name: ClassVar[str] = "Heat"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Heat")


class HeatPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["HeatPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:HeatPerMass"
    class_name: ClassVar[str] = "HeatPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/HeatPerMass")


class Work(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["Work"]
    class_class_curie: ClassVar[str] = "thmo_variables:Work"
    class_name: ClassVar[str] = "Work"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Work")


class WorkPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["WorkPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:WorkPerMass"
    class_name: ClassVar[str] = "WorkPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkPerMass")


class WorkOnInternalState(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["WorkOnInternalState"]
    class_class_curie: ClassVar[str] = "thmo_variables:WorkOnInternalState"
    class_name: ClassVar[str] = "WorkOnInternalState"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnInternalState")


@dataclass(repr=False)
class WorkOnExternalState(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["WorkOnExternalState"]
    class_class_curie: ClassVar[str] = "thmo_variables:WorkOnExternalState"
    class_name: ClassVar[str] = "WorkOnExternalState"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnExternalState")

    value: Optional[float] = 0

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


class WorkOnInternalStatePerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["WorkOnInternalStatePerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:WorkOnInternalStatePerMass"
    class_name: ClassVar[str] = "WorkOnInternalStatePerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnInternalStatePerMass")


class WorkOnExternalStatePerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["WorkOnExternalStatePerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:WorkOnExternalStatePerMass"
    class_name: ClassVar[str] = "WorkOnExternalStatePerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnExternalStatePerMass")


class TechnicalWorkPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["TechnicalWorkPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:TechnicalWorkPerMass"
    class_name: ClassVar[str] = "TechnicalWorkPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/TechnicalWorkPerMass")


class VolumeChangeWork(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VolumeChangeWork"]
    class_class_curie: ClassVar[str] = "thmo_variables:VolumeChangeWork"
    class_name: ClassVar[str] = "VolumeChangeWork"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VolumeChangeWork")


class VolumeChangeWorkPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VolumeChangeWorkPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:VolumeChangeWorkPerMass"
    class_name: ClassVar[str] = "VolumeChangeWorkPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VolumeChangeWorkPerMass")


class StirringWork(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["StirringWork"]
    class_class_curie: ClassVar[str] = "thmo_variables:StirringWork"
    class_name: ClassVar[str] = "StirringWork"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StirringWork")


class StirringWorkPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["StirringWorkPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:StirringWorkPerMass"
    class_name: ClassVar[str] = "StirringWorkPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StirringWorkPerMass")


class ElectricalWork(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["ElectricalWork"]
    class_class_curie: ClassVar[str] = "thmo_variables:ElectricalWork"
    class_name: ClassVar[str] = "ElectricalWork"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ElectricalWork")


class ElectricalWorkPerMass(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["ElectricalWorkPerMass"]
    class_class_curie: ClassVar[str] = "thmo_variables:ElectricalWorkPerMass"
    class_name: ClassVar[str] = "ElectricalWorkPerMass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ElectricalWorkPerMass")


class TemperatureDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["TemperatureDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:TemperatureDifference"
    class_name: ClassVar[str] = "TemperatureDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/TemperatureDifference")


class PressureDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PressureDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:PressureDifference"
    class_name: ClassVar[str] = "PressureDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PressureDifference")


class VolumeDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VolumeDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:VolumeDifference"
    class_name: ClassVar[str] = "VolumeDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VolumeDifference")


class SpecificVolumeDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificVolumeDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificVolumeDifference"
    class_name: ClassVar[str] = "SpecificVolumeDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificVolumeDifference")


class InternalEnergyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["InternalEnergyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:InternalEnergyDifference"
    class_name: ClassVar[str] = "InternalEnergyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/InternalEnergyDifference")


class SpecificInternalEnergyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificInternalEnergyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificInternalEnergyDifference"
    class_name: ClassVar[str] = "SpecificInternalEnergyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificInternalEnergyDifference")


class EnthalpyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["EnthalpyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:EnthalpyDifference"
    class_name: ClassVar[str] = "EnthalpyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/EnthalpyDifference")


class SpecificEnthalpyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificEnthalpyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificEnthalpyDifference"
    class_name: ClassVar[str] = "SpecificEnthalpyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificEnthalpyDifference")


class EntropyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["EntropyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:EntropyDifference"
    class_name: ClassVar[str] = "EntropyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/EntropyDifference")


class SpecificEntropyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificEntropyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificEntropyDifference"
    class_name: ClassVar[str] = "SpecificEntropyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificEntropyDifference")


class MolarEntropyDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["MolarEntropyDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:MolarEntropyDifference"
    class_name: ClassVar[str] = "MolarEntropyDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarEntropyDifference")


class PositionCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PositionCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:PositionCenterMassDifference"
    class_name: ClassVar[str] = "PositionCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PositionCenterMassDifference")


class VelocityCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VelocityCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:VelocityCenterMassDifference"
    class_name: ClassVar[str] = "VelocityCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VelocityCenterMassDifference")


class KineticEnergyCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["KineticEnergyCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:KineticEnergyCenterMassDifference"
    class_name: ClassVar[str] = "KineticEnergyCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/KineticEnergyCenterMassDifference")


class SpecificKineticEnergyCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificKineticEnergyCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificKineticEnergyCenterMassDifference"
    class_name: ClassVar[str] = "SpecificKineticEnergyCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificKineticEnergyCenterMassDifference")


class PotentialEnergyCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PotentialEnergyCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:PotentialEnergyCenterMassDifference"
    class_name: ClassVar[str] = "PotentialEnergyCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PotentialEnergyCenterMassDifference")


class SpecificPotentialEnergyCenterMassDifference(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["SpecificPotentialEnergyCenterMassDifference"]
    class_class_curie: ClassVar[str] = "thmo_variables:SpecificPotentialEnergyCenterMassDifference"
    class_name: ClassVar[str] = "SpecificPotentialEnergyCenterMassDifference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificPotentialEnergyCenterMassDifference")


class PolytropicExponent(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PolytropicExponent"]
    class_class_curie: ClassVar[str] = "thmo_variables:PolytropicExponent"
    class_name: ClassVar[str] = "PolytropicExponent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PolytropicExponent")


class TemperatureRatio(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["TemperatureRatio"]
    class_class_curie: ClassVar[str] = "thmo_variables:TemperatureRatio"
    class_name: ClassVar[str] = "TemperatureRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/TemperatureRatio")


class PressureRatio(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["PressureRatio"]
    class_class_curie: ClassVar[str] = "thmo_variables:PressureRatio"
    class_name: ClassVar[str] = "PressureRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PressureRatio")


class VolumeRatio(Variable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_VARIABLES["VolumeRatio"]
    class_class_curie: ClassVar[str] = "thmo_variables:VolumeRatio"
    class_name: ClassVar[str] = "VolumeRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VolumeRatio")


@dataclass(repr=False)
class Equation(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["Equation"]
    class_class_curie: ClassVar[str] = "thmo_equations:Equation"
    class_name: ClassVar[str] = "Equation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Equation")

    id: Union[str, EquationId] = None
    as_text: Optional[str] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EquationId):
            self.id = EquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Inequality(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["Inequality"]
    class_class_curie: ClassVar[str] = "thmo_equations:Inequality"
    class_name: ClassVar[str] = "Inequality"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Inequality")

    id: Union[str, InequalityId] = None

@dataclass(repr=False)
class SecondLawAdiabaticIrreversible(Inequality):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SecondLawAdiabaticIrreversible"]
    class_class_curie: ClassVar[str] = "thmo_equations:SecondLawAdiabaticIrreversible"
    class_name: ClassVar[str] = "SecondLawAdiabaticIrreversible"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SecondLawAdiabaticIrreversible")

    id: Union[str, SecondLawAdiabaticIrreversibleId] = None
    change_of_state_id: Optional[Union[str, ChangeOfStateId]] = None
    as_text: Optional[str] = "s_{change_of_state#final_state} - s_{change_of_state#initial_state} > 0"
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecondLawAdiabaticIrreversibleId):
            self.id = SecondLawAdiabaticIrreversibleId(self.id)

        if self.change_of_state_id is not None and not isinstance(self.change_of_state_id, ChangeOfStateId):
            self.change_of_state_id = ChangeOfStateId(self.change_of_state_id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["BaseEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:BaseEquation"
    class_name: ClassVar[str] = "BaseEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/BaseEquation")

    id: Union[str, BaseEquationId] = None

@dataclass(repr=False)
class DefiningEquation(BaseEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DefiningEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DefiningEquation"
    class_name: ClassVar[str] = "DefiningEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DefiningEquation")

    id: Union[str, DefiningEquationId] = None

@dataclass(repr=False)
class AdditionalEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["AdditionalEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:AdditionalEquation"
    class_name: ClassVar[str] = "AdditionalEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AdditionalEquation")

    id: Union[str, AdditionalEquationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdditionalEquationId):
            self.id = AdditionalEquationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SystemEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SystemEquation"
    class_name: ClassVar[str] = "SystemEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SystemEquation")

    id: Union[str, SystemEquationId] = None
    system_id: Optional[Union[str, SystemId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.system_id is not None and not isinstance(self.system_id, SystemId):
            self.system_id = SystemId(self.system_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AmountOfSubstanceEquation(SystemEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["AmountOfSubstanceEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:AmountOfSubstanceEquation"
    class_name: ClassVar[str] = "AmountOfSubstanceEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AmountOfSubstanceEquation")

    id: Union[str, AmountOfSubstanceEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "m_{system} = M_{system#material}*n_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AmountOfSubstanceEquationId):
            self.id = AmountOfSubstanceEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["MaterialEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:MaterialEquation"
    class_name: ClassVar[str] = "MaterialEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MaterialEquation")

    id: Union[str, MaterialEquationId] = None
    material_id: Optional[Union[str, PureMaterialId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.material_id is not None and not isinstance(self.material_id, PureMaterialId):
            self.material_id = PureMaterialId(self.material_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolarHeatCapacityConstantPressureEquation(MaterialEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["MolarHeatCapacityConstantPressureEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:MolarHeatCapacityConstantPressureEquation"
    class_name: ClassVar[str] = "MolarHeatCapacityConstantPressureEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarHeatCapacityConstantPressureEquation")

    id: Union[str, MolarHeatCapacityConstantPressureEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "c_pm_{material} = c_p_{material} * M_{material}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolarHeatCapacityConstantPressureEquationId):
            self.id = MolarHeatCapacityConstantPressureEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolarHeatCapacityConstantVolumeEquation(MaterialEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["MolarHeatCapacityConstantVolumeEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:MolarHeatCapacityConstantVolumeEquation"
    class_name: ClassVar[str] = "MolarHeatCapacityConstantVolumeEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarHeatCapacityConstantVolumeEquation")

    id: Union[str, MolarHeatCapacityConstantVolumeEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "c_vm_{material} = c_v_{material} * M_{material}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolarHeatCapacityConstantVolumeEquationId):
            self.id = MolarHeatCapacityConstantVolumeEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KappaPolytropicExponentEquation(MaterialEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["KappaPolytropicExponentEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:KappaPolytropicExponentEquation"
    class_name: ClassVar[str] = "KappaPolytropicExponentEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/KappaPolytropicExponentEquation")

    id: Union[str, KappaPolytropicExponentEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "kappa_{material} = c_p_{material}/c_v_{material}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KappaPolytropicExponentEquationId):
            self.id = KappaPolytropicExponentEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasEquation(MaterialEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasEquation"
    class_name: ClassVar[str] = "IdealGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasEquation")

    id: Union[str, IdealGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CaloricEquationOfStateIdealGas(IdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["CaloricEquationOfStateIdealGas"]
    class_class_curie: ClassVar[str] = "thmo_equations:CaloricEquationOfStateIdealGas"
    class_name: ClassVar[str] = "CaloricEquationOfStateIdealGas"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/CaloricEquationOfStateIdealGas")

    id: Union[str, CaloricEquationOfStateIdealGasId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "R_{material} = c_p_{material} - c_v_{material}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaloricEquationOfStateIdealGasId):
            self.id = CaloricEquationOfStateIdealGasId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificGasConstantEquation(IdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificGasConstantEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificGasConstantEquation"
    class_name: ClassVar[str] = "SpecificGasConstantEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificGasConstantEquation")

    id: Union[str, SpecificGasConstantEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "R_{material} = Rbar_{material} / M_{material}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificGasConstantEquationId):
            self.id = SpecificGasConstantEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StateEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["StateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:StateEquation"
    class_name: ClassVar[str] = "StateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/StateEquation")

    id: Union[str, StateEquationId] = None
    state_id: Optional[Union[str, StateId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.state_id is not None and not isinstance(self.state_id, StateId):
            self.state_id = StateId(self.state_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnthalpyEquation(StateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["EnthalpyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:EnthalpyEquation"
    class_name: ClassVar[str] = "EnthalpyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/EnthalpyEquation")

    id: Union[str, EnthalpyEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "H_{state} = U_{state} + p_{state}*V_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnthalpyEquationId):
            self.id = EnthalpyEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificEnthalpyEquation(StateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificEnthalpyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificEnthalpyEquation"
    class_name: ClassVar[str] = "SpecificEnthalpyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificEnthalpyEquation")

    id: Union[str, SpecificEnthalpyEquationId] = None
    as_text: Optional[str] = "h_{state} = u_{state} + p_{state}*v_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificEnthalpyEquationId):
            self.id = SpecificEnthalpyEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThermalDensityEquation(StateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["ThermalDensityEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:ThermalDensityEquation"
    class_name: ClassVar[str] = "ThermalDensityEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ThermalDensityEquation")

    id: Union[str, ThermalDensityEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "rho_{state} = 1/v_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThermalDensityEquationId):
            self.id = ThermalDensityEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemInStateEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SystemInStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SystemInStateEquation"
    class_name: ClassVar[str] = "SystemInStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SystemInStateEquation")

    id: Union[str, SystemInStateEquationId] = None
    system_id: Optional[Union[str, SystemId]] = None
    state_id: Optional[Union[str, StateId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.system_id is not None and not isinstance(self.system_id, SystemId):
            self.system_id = SystemId(self.system_id)

        if self.state_id is not None and not isinstance(self.state_id, StateId):
            self.state_id = StateId(self.state_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificStateVariableVEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificStateVariableVEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificStateVariableVEquation"
    class_name: ClassVar[str] = "SpecificStateVariableVEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificStateVariableVEquation")

    id: Union[str, SpecificStateVariableVEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "v_{state} = V_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificStateVariableVEquationId):
            self.id = SpecificStateVariableVEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificStateVariableUEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificStateVariableUEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificStateVariableUEquation"
    class_name: ClassVar[str] = "SpecificStateVariableUEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificStateVariableUEquation")

    id: Union[str, SpecificStateVariableUEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "u_{state} = U_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificStateVariableUEquationId):
            self.id = SpecificStateVariableUEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificStateVariableHEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificStateVariableHEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificStateVariableHEquation"
    class_name: ClassVar[str] = "SpecificStateVariableHEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificStateVariableHEquation")

    id: Union[str, SpecificStateVariableHEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "h_{state} = H_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificStateVariableHEquationId):
            self.id = SpecificStateVariableHEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificStateVariableSEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificStateVariableSEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificStateVariableSEquation"
    class_name: ClassVar[str] = "SpecificStateVariableSEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificStateVariableSEquation")

    id: Union[str, SpecificStateVariableSEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "s_{state} = S_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificStateVariableSEquationId):
            self.id = SpecificStateVariableSEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolarStateVariableSEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["MolarStateVariableSEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:MolarStateVariableSEquation"
    class_name: ClassVar[str] = "MolarStateVariableSEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/MolarStateVariableSEquation")

    id: Union[str, MolarStateVariableSEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "sm_{state} = S_{state}/n_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolarStateVariableSEquationId):
            self.id = MolarStateVariableSEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificKineticEnergyCenterMassEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificKineticEnergyCenterMassEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificKineticEnergyCenterMassEquation"
    class_name: ClassVar[str] = "SpecificKineticEnergyCenterMassEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificKineticEnergyCenterMassEquation")

    id: Union[str, SpecificKineticEnergyCenterMassEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "e_kin_{state} = E_kin_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificKineticEnergyCenterMassEquationId):
            self.id = SpecificKineticEnergyCenterMassEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificPotentialEnergyCenterMassEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificPotentialEnergyCenterMassEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificPotentialEnergyCenterMassEquation"
    class_name: ClassVar[str] = "SpecificPotentialEnergyCenterMassEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificPotentialEnergyCenterMassEquation")

    id: Union[str, SpecificPotentialEnergyCenterMassEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "e_pot_{state} = E_pot_{state}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificPotentialEnergyCenterMassEquationId):
            self.id = SpecificPotentialEnergyCenterMassEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificDensityEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificDensityEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificDensityEquation"
    class_name: ClassVar[str] = "SpecificDensityEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificDensityEquation")

    id: Union[str, SpecificDensityEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "rho_{state} = m_{system}/V_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificDensityEquationId):
            self.id = SpecificDensityEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasSystemInStateEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasSystemInStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasSystemInStateEquation"
    class_name: ClassVar[str] = "IdealGasSystemInStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasSystemInStateEquation")

    id: Union[str, IdealGasSystemInStateEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasLaw(IdealGasSystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasLaw"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasLaw"
    class_name: ClassVar[str] = "IdealGasLaw"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasLaw")

    id: Union[str, IdealGasLawId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "p_{state} * V_{state} = m_{system} * R_{system#material} * T_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdealGasLawId):
            self.id = IdealGasLawId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificIdealGasLaw(IdealGasSystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificIdealGasLaw"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificIdealGasLaw"
    class_name: ClassVar[str] = "SpecificIdealGasLaw"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificIdealGasLaw")

    id: Union[str, SpecificIdealGasLawId] = None
    as_text: Optional[str] = "p_{state} * v_{state} = R_{system#material} * T_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificIdealGasLawId):
            self.id = SpecificIdealGasLawId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasLawAmountOfSubstance(IdealGasSystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasLawAmountOfSubstance"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasLawAmountOfSubstance"
    class_name: ClassVar[str] = "IdealGasLawAmountOfSubstance"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasLawAmountOfSubstance")

    id: Union[str, IdealGasLawAmountOfSubstanceId] = None
    as_text: Optional[str] = "p_{state} * V_{state} = n_{system} * Rbar_{system#material} * T_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdealGasLawAmountOfSubstanceId):
            self.id = IdealGasLawAmountOfSubstanceId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificVolumeDensityEquation(IdealGasSystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificVolumeDensityEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificVolumeDensityEquation"
    class_name: ClassVar[str] = "SpecificVolumeDensityEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificVolumeDensityEquation")

    id: Union[str, SpecificVolumeDensityEquationId] = None
    as_text: Optional[str] = "h_{state} = u_{state} + R_{system#material}*T_{state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificVolumeDensityEquationId):
            self.id = SpecificVolumeDensityEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PerfectGasSystemInStateEquation(SystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["PerfectGasSystemInStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:PerfectGasSystemInStateEquation"
    class_name: ClassVar[str] = "PerfectGasSystemInStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PerfectGasSystemInStateEquation")

    id: Union[str, PerfectGasSystemInStateEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternalEnergyEquation(PerfectGasSystemInStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["InternalEnergyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:InternalEnergyEquation"
    class_name: ClassVar[str] = "InternalEnergyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/InternalEnergyEquation")

    id: Union[str, InternalEnergyEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "u_{state} = c_v_{system#material} * "

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternalEnergyEquationId):
            self.id = InternalEnergyEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChangeOfStateEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["ChangeOfStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:ChangeOfStateEquation"
    class_name: ClassVar[str] = "ChangeOfStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ChangeOfStateEquation")

    id: Union[str, ChangeOfStateEquationId] = None
    change_of_state_id: Optional[Union[str, ChangeOfStateId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.change_of_state_id is not None and not isinstance(self.change_of_state_id, ChangeOfStateId):
            self.change_of_state_id = ChangeOfStateId(self.change_of_state_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChangeOfStateDifferenceEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["ChangeOfStateDifferenceEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:ChangeOfStateDifferenceEquation"
    class_name: ClassVar[str] = "ChangeOfStateDifferenceEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/ChangeOfStateDifferenceEquation")

    id: Union[str, ChangeOfStateDifferenceEquationId] = None

@dataclass(repr=False)
class DelTEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelTEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelTEquation"
    class_name: ClassVar[str] = "DelTEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelTEquation")

    id: Union[str, DelTEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_T_{change_of_state#transition} = T_{change_of_state#final_state} - T_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelTEquationId):
            self.id = DelTEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelPEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelPEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelPEquation"
    class_name: ClassVar[str] = "DelPEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelPEquation")

    id: Union[str, DelPEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_p_{change_of_state#transition} = p_{change_of_state#final_state} - p_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelPEquationId):
            self.id = DelPEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelVEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelVEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelVEquation"
    class_name: ClassVar[str] = "DelVEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelVEquation")

    id: Union[str, DelVEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_V_{change_of_state#transition} = V_{change_of_state#final_state} - V_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelVEquationId):
            self.id = DelVEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelvEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelvEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelvEquation"
    class_name: ClassVar[str] = "DelvEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelvEquation")

    id: Union[str, DelvEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_v_{change_of_state#transition} = v_{change_of_state#final_state} - v_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelvEquationId):
            self.id = DelvEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelUEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelUEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelUEquation"
    class_name: ClassVar[str] = "DelUEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelUEquation")

    id: Union[str, DelUEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_U_{change_of_state#transition} = U_{change_of_state#final_state} - U_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelUEquationId):
            self.id = DelUEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeluEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DeluEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DeluEquation"
    class_name: ClassVar[str] = "DeluEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DeluEquation")

    id: Union[str, DeluEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_u_{change_of_state#transition} = u_{change_of_state#final_state} - u_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeluEquationId):
            self.id = DeluEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelHEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelHEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelHEquation"
    class_name: ClassVar[str] = "DelHEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelHEquation")

    id: Union[str, DelHEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_H_{change_of_state#transition} = H_{change_of_state#final_state} - H_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelHEquationId):
            self.id = DelHEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelhEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelhEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelhEquation"
    class_name: ClassVar[str] = "DelhEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelhEquation")

    id: Union[str, DelhEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_h_{change_of_state#transition} = h_{change_of_state#final_state} - h_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelhEquationId):
            self.id = DelhEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelSEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelSEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelSEquation"
    class_name: ClassVar[str] = "DelSEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelSEquation")

    id: Union[str, DelSEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_S_{change_of_state#transition} = S_{change_of_state#final_state} - S_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelSEquationId):
            self.id = DelSEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelsEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelsEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelsEquation"
    class_name: ClassVar[str] = "DelsEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelsEquation")

    id: Union[str, DelsEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_s_{change_of_state#transition} = s_{change_of_state#final_state} - s_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelsEquationId):
            self.id = DelsEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelsmEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelsmEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelsmEquation"
    class_name: ClassVar[str] = "DelsmEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelsmEquation")

    id: Union[str, DelsmEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_sm_{change_of_state#transition} = sm_{change_of_state#final_state} - sm_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelsmEquationId):
            self.id = DelsmEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelCEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelCEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelCEquation"
    class_name: ClassVar[str] = "DelCEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelCEquation")

    id: Union[str, DelCEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_c_{change_of_state#transition} = c_{change_of_state#final_state} - c_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelCEquationId):
            self.id = DelCEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelZEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelZEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelZEquation"
    class_name: ClassVar[str] = "DelZEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelZEquation")

    id: Union[str, DelZEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_z_{change_of_state#transition} = z_{change_of_state#final_state} - z_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelZEquationId):
            self.id = DelZEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelEKinEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelEKinEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelEKinEquation"
    class_name: ClassVar[str] = "DelEKinEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelEKinEquation")

    id: Union[str, DelEKinEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_E_kin_{change_of_state#transition} = E_kin_{change_of_state#final_state} - E_kin_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelEKinEquationId):
            self.id = DelEKinEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelEPotEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelEPotEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelEPotEquation"
    class_name: ClassVar[str] = "DelEPotEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelEPotEquation")

    id: Union[str, DelEPotEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_E_pot_{change_of_state#transition} = E_pot_{change_of_state#final_state} - E_pot_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelEPotEquationId):
            self.id = DelEPotEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeleKinEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DeleKinEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DeleKinEquation"
    class_name: ClassVar[str] = "DeleKinEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DeleKinEquation")

    id: Union[str, DeleKinEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_e_kin_{change_of_state#transition} = e_kin_{change_of_state#final_state} - e_kin_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeleKinEquationId):
            self.id = DeleKinEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelePotEquation(ChangeOfStateDifferenceEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelePotEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelePotEquation"
    class_name: ClassVar[str] = "DelePotEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelePotEquation")

    id: Union[str, DelePotEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_e_pot_{change_of_state#transition} = e_pot_{change_of_state#final_state} - e_pot_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelePotEquationId):
            self.id = DelePotEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolytropicExponentEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["PolytropicExponentEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:PolytropicExponentEquation"
    class_name: ClassVar[str] = "PolytropicExponentEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PolytropicExponentEquation")

    id: Union[str, PolytropicExponentEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "n_poly_{change_of_state#transition} = ln(p_{change_of_state#initial_state} / p_{change_of_state#final_state})/ln(v_{change_of_state#final_state} / v_{change_of_state#initial_state})"
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolytropicExponentEquationId):
            self.id = PolytropicExponentEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkOnInternalExternalStateEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["WorkOnInternalExternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:WorkOnInternalExternalStateEquation"
    class_name: ClassVar[str] = "WorkOnInternalExternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnInternalExternalStateEquation")

    id: Union[str, WorkOnInternalExternalStateEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "W_{change_of_state#transition} = W_i_{change_of_state#transition} + W_a_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkOnInternalExternalStateEquationId):
            self.id = WorkOnInternalExternalStateEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificWorkOnInternalExternalStateEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificWorkOnInternalExternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificWorkOnInternalExternalStateEquation"
    class_name: ClassVar[str] = "SpecificWorkOnInternalExternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificWorkOnInternalExternalStateEquation")

    id: Union[str, SpecificWorkOnInternalExternalStateEquationId] = None
    as_text: Optional[str] = "w_{change_of_state#transition} = w_i_{change_of_state#transition} + w_a_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificWorkOnInternalExternalStateEquationId):
            self.id = SpecificWorkOnInternalExternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VolumeStirringElectricalWorkEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["VolumeStirringElectricalWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:VolumeStirringElectricalWorkEquation"
    class_name: ClassVar[str] = "VolumeStirringElectricalWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/VolumeStirringElectricalWorkEquation")

    id: Union[str, VolumeStirringElectricalWorkEquationId] = None
    as_text: Optional[str] = "W_i_{change_of_state#transition} = W_vol_{change_of_state#transition} + W_stir_{change_of_state#transition} + W_electrical_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VolumeStirringElectricalWorkEquationId):
            self.id = VolumeStirringElectricalWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FirstLaw(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["FirstLaw"]
    class_class_curie: ClassVar[str] = "thmo_equations:FirstLaw"
    class_name: ClassVar[str] = "FirstLaw"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/FirstLaw")

    id: Union[str, FirstLawId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "Q_{change_of_state#transition} + W_{change_of_state#transition} = del_U_{change_of_state#transition} + del_E_kin_{change_of_state#transition} + del_E_pot_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FirstLawId):
            self.id = FirstLawId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FirstLawSpecific(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["FirstLawSpecific"]
    class_class_curie: ClassVar[str] = "thmo_equations:FirstLawSpecific"
    class_name: ClassVar[str] = "FirstLawSpecific"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/FirstLawSpecific")

    id: Union[str, FirstLawSpecificId] = None
    as_text: Optional[str] = "q_{change_of_state#transition} + w_{change_of_state#transition} = del_u_{change_of_state#transition}+ del_e_kin_{change_of_state#transition} + del_e_pot_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FirstLawSpecificId):
            self.id = FirstLawSpecificId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalWorkEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["TechnicalWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:TechnicalWorkEquation"
    class_name: ClassVar[str] = "TechnicalWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/TechnicalWorkEquation")

    id: Union[str, TechnicalWorkEquationId] = None
    as_text: Optional[str] = "w_t_{change_of_state#transition} = w_i_{change_of_state#transition} + w_a_{change_of_state#transition} + p_{change_of_state#final_state} * v_{change_of_state#final_state} - p_{change_of_state#initial_state} * v_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalWorkEquationId):
            self.id = TechnicalWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkOnExternalStateEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["WorkOnExternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:WorkOnExternalStateEquation"
    class_name: ClassVar[str] = "WorkOnExternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/WorkOnExternalStateEquation")

    id: Union[str, WorkOnExternalStateEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "W_a_{change_of_state#transition} = del_E_kin_{change_of_state#transition} + del_E_pot_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkOnExternalStateEquationId):
            self.id = WorkOnExternalStateEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RatioVolumeEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["RatioVolumeEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:RatioVolumeEquation"
    class_name: ClassVar[str] = "RatioVolumeEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/RatioVolumeEquation")

    id: Union[str, RatioVolumeEquationId] = None
    as_text: Optional[str] = "ratio_v_{change_of_state#transition} = v_{change_of_state#final_state} / v_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RatioVolumeEquationId):
            self.id = RatioVolumeEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RatioTemperatureEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["RatioTemperatureEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:RatioTemperatureEquation"
    class_name: ClassVar[str] = "RatioTemperatureEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/RatioTemperatureEquation")

    id: Union[str, RatioTemperatureEquationId] = None
    as_text: Optional[str] = "ratio_T_{change_of_state#transition} = T_{change_of_state#final_state} / T_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RatioTemperatureEquationId):
            self.id = RatioTemperatureEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RatioPressureEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["RatioPressureEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:RatioPressureEquation"
    class_name: ClassVar[str] = "RatioPressureEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/RatioPressureEquation")

    id: Union[str, RatioPressureEquationId] = None
    as_text: Optional[str] = "ratio_p_{change_of_state#transition} = p_{change_of_state#final_state} / p_{change_of_state#initial_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RatioPressureEquationId):
            self.id = RatioPressureEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemInChangeOfStateEquation(Equation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SystemInChangeOfStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SystemInChangeOfStateEquation"
    class_name: ClassVar[str] = "SystemInChangeOfStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SystemInChangeOfStateEquation")

    id: Union[str, SystemInChangeOfStateEquationId] = None
    system_id: Optional[Union[str, SystemId]] = None
    change_of_state_id: Optional[Union[str, ChangeOfStateId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.system_id is not None and not isinstance(self.system_id, SystemId):
            self.system_id = SystemId(self.system_id)

        if self.change_of_state_id is not None and not isinstance(self.change_of_state_id, ChangeOfStateId):
            self.change_of_state_id = ChangeOfStateId(self.change_of_state_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificHeatTransferEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificHeatTransferEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificHeatTransferEquation"
    class_name: ClassVar[str] = "SpecificHeatTransferEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificHeatTransferEquation")

    id: Union[str, SpecificHeatTransferEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "q_{change_of_state#transition} = Q_{change_of_state#transition}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificHeatTransferEquationId):
            self.id = SpecificHeatTransferEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificWorkTransferEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificWorkTransferEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificWorkTransferEquation"
    class_name: ClassVar[str] = "SpecificWorkTransferEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificWorkTransferEquation")

    id: Union[str, SpecificWorkTransferEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_{change_of_state#transition} = W_{change_of_state#transition}/m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificWorkTransferEquationId):
            self.id = SpecificWorkTransferEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificWorkOnInternalStateEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "SpecificWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificWorkOnInternalStateEquation")

    id: Union[str, SpecificWorkOnInternalStateEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_i_{change_of_state#transition} = W_i_{change_of_state#transition} / m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificWorkOnInternalStateEquationId):
            self.id = SpecificWorkOnInternalStateEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificWorkOnExternalStateEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificWorkOnExternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificWorkOnExternalStateEquation"
    class_name: ClassVar[str] = "SpecificWorkOnExternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificWorkOnExternalStateEquation")

    id: Union[str, SpecificWorkOnExternalStateEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_a_{change_of_state#transition} = W_a_{change_of_state#transition} / m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificWorkOnExternalStateEquationId):
            self.id = SpecificWorkOnExternalStateEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificVolumeChangeWorkEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificVolumeChangeWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificVolumeChangeWorkEquation"
    class_name: ClassVar[str] = "SpecificVolumeChangeWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificVolumeChangeWorkEquation")

    id: Union[str, SpecificVolumeChangeWorkEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_vol_{change_of_state#transition} = W_vol_{change_of_state#transition} / m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificVolumeChangeWorkEquationId):
            self.id = SpecificVolumeChangeWorkEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificStirringWorkEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificStirringWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificStirringWorkEquation"
    class_name: ClassVar[str] = "SpecificStirringWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificStirringWorkEquation")

    id: Union[str, SpecificStirringWorkEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_stir_{change_of_state#transition} = W_stir_{change_of_state#transition} / m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificStirringWorkEquationId):
            self.id = SpecificStirringWorkEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificElectricalWorkEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["SpecificElectricalWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:SpecificElectricalWorkEquation"
    class_name: ClassVar[str] = "SpecificElectricalWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SpecificElectricalWorkEquation")

    id: Union[str, SpecificElectricalWorkEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "w_electrical_{change_of_state#transition} = W_electrical_{change_of_state#transition} / m_{system}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificElectricalWorkEquationId):
            self.id = SpecificElectricalWorkEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PerfectGasChangeOfStateEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["PerfectGasChangeOfStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:PerfectGasChangeOfStateEquation"
    class_name: ClassVar[str] = "PerfectGasChangeOfStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PerfectGasChangeOfStateEquation")

    id: Union[str, PerfectGasChangeOfStateEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelHPerfectGasEquation(PerfectGasChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelHPerfectGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelHPerfectGasEquation"
    class_name: ClassVar[str] = "DelHPerfectGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelHPerfectGasEquation")

    id: Union[str, DelHPerfectGasEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_h_{change_of_state#transition} = c_p_{system#material} * del_T_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelHPerfectGasEquationId):
            self.id = DelHPerfectGasEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelUPerfectGasEquation(PerfectGasChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelUPerfectGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelUPerfectGasEquation"
    class_name: ClassVar[str] = "DelUPerfectGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelUPerfectGasEquation")

    id: Union[str, DelUPerfectGasEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_u_{change_of_state#transition} = c_v_{system#material} * del_T_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelUPerfectGasEquationId):
            self.id = DelUPerfectGasEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelSPerfectGasVolumeEquation(PerfectGasChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelSPerfectGasVolumeEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelSPerfectGasVolumeEquation"
    class_name: ClassVar[str] = "DelSPerfectGasVolumeEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelSPerfectGasVolumeEquation")

    id: Union[str, DelSPerfectGasVolumeEquationId] = None
    as_text: Optional[str] = "del_s_{change_of_state#transition} = c_v_{system#material} * ln"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelSPerfectGasVolumeEquationId):
            self.id = DelSPerfectGasVolumeEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DelSPerfectGasVolumeEquationII(PerfectGasChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["DelSPerfectGasVolumeEquationII"]
    class_class_curie: ClassVar[str] = "thmo_equations:DelSPerfectGasVolumeEquationII"
    class_name: ClassVar[str] = "DelSPerfectGasVolumeEquationII"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/DelSPerfectGasVolumeEquationII")

    id: Union[str, DelSPerfectGasVolumeEquationIIId] = None
    as_text: Optional[str] = "del_sm_{change_of_state#transition} = c_vm_{system#material} * ln"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DelSPerfectGasVolumeEquationIIId):
            self.id = DelSPerfectGasVolumeEquationIIId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricEquation"
    class_name: ClassVar[str] = "IsochoricEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricEquation")

    id: Union[str, IsochoricEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricVolumeEquation(IsochoricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricVolumeEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricVolumeEquation"
    class_name: ClassVar[str] = "IsochoricVolumeEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricVolumeEquation")

    id: Union[str, IsochoricVolumeEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "V_{change_of_state#final_state} - V_{change_of_state#initial_state} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricVolumeEquationId):
            self.id = IsochoricVolumeEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricSpecificVolumeEquation(IsochoricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricSpecificVolumeEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricSpecificVolumeEquation"
    class_name: ClassVar[str] = "IsochoricSpecificVolumeEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricSpecificVolumeEquation")

    id: Union[str, IsochoricSpecificVolumeEquationId] = None
    as_text: Optional[str] = "v_{change_of_state#final_state} - v_{change_of_state#initial_state} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricSpecificVolumeEquationId):
            self.id = IsochoricSpecificVolumeEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricSpecificWorkOnInternalStateEquation(IsochoricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricSpecificWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricSpecificWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsochoricSpecificWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricSpecificWorkOnInternalStateEquation")

    id: Union[str, IsochoricSpecificWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricSpecificWorkOnInternalStateEquationId):
            self.id = IsochoricSpecificWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricWorkOnInternalStateEquation(IsochoricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsochoricWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricWorkOnInternalStateEquation")

    id: Union[str, IsochoricWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "W_i_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricWorkOnInternalStateEquationId):
            self.id = IsochoricWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricTechnicalWorkEquation(IsochoricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricTechnicalWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricTechnicalWorkEquation"
    class_name: ClassVar[str] = "IsochoricTechnicalWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricTechnicalWorkEquation")

    id: Union[str, IsochoricTechnicalWorkEquationId] = None
    as_text: Optional[str] = "w_t_{change_of_state#transition} = v_{change_of_state#initial_state} * "

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricTechnicalWorkEquationId):
            self.id = IsochoricTechnicalWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricIdealGasEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricIdealGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricIdealGasEquation"
    class_name: ClassVar[str] = "IsochoricIdealGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricIdealGasEquation")

    id: Union[str, IsochoricIdealGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsochoricIdealGasPressureTemperatureRatio(IsochoricIdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsochoricIdealGasPressureTemperatureRatio"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsochoricIdealGasPressureTemperatureRatio"
    class_name: ClassVar[str] = "IsochoricIdealGasPressureTemperatureRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricIdealGasPressureTemperatureRatio")

    id: Union[str, IsochoricIdealGasPressureTemperatureRatioId] = None
    as_text: Optional[str] = "ratio_T_{change_of_state#transition} = ratio_p_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsochoricIdealGasPressureTemperatureRatioId):
            self.id = IsochoricIdealGasPressureTemperatureRatioId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalChangeOfStateEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalChangeOfStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalChangeOfStateEquation"
    class_name: ClassVar[str] = "IsothermalChangeOfStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalChangeOfStateEquation")

    id: Union[str, IsothermalChangeOfStateEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalProperties(IsothermalChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalProperties"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalProperties"
    class_name: ClassVar[str] = "IsothermalProperties"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalProperties")

    id: Union[str, IsothermalPropertiesId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "T_{change_of_state#final_state} - T_{change_of_state#initial_state} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalPropertiesId):
            self.id = IsothermalPropertiesId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalWorkOnInternalStateEquation(IsothermalChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsothermalWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalWorkOnInternalStateEquation")

    id: Union[str, IsothermalWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = del_u_{change_of_state#transition} - T_{change_of_state#initial_state} * del_s_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalWorkOnInternalStateEquationId):
            self.id = IsothermalWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalIdealGasEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalIdealGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalIdealGasEquation"
    class_name: ClassVar[str] = "IsothermalIdealGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalIdealGasEquation")

    id: Union[str, IsothermalIdealGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalIdealGasPressureVolumeRatio(IsothermalIdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalIdealGasPressureVolumeRatio"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalIdealGasPressureVolumeRatio"
    class_name: ClassVar[str] = "IsothermalIdealGasPressureVolumeRatio"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalIdealGasPressureVolumeRatio")

    id: Union[str, IsothermalIdealGasPressureVolumeRatioId] = None
    as_text: Optional[str] = "v_{change_of_state#final_state} / v_{change_of_state#initial_state} = p_{change_of_state#initial_state} / p_{change_of_state#final_state}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalIdealGasPressureVolumeRatioId):
            self.id = IsothermalIdealGasPressureVolumeRatioId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalIdealGasWorkEquation(IsothermalIdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalIdealGasWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalIdealGasWorkEquation"
    class_name: ClassVar[str] = "IsothermalIdealGasWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalIdealGasWorkEquation")

    id: Union[str, IsothermalIdealGasWorkEquationId] = None
    as_text: Optional[str] = "W_i_{change_of_state#transition} = p_{change_of_state#initial_state} * V_{change_of_state#initial_state} * ln"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalIdealGasWorkEquationId):
            self.id = IsothermalIdealGasWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalIdealGasWorkEquationII(IsothermalIdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalIdealGasWorkEquationII"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalIdealGasWorkEquationII"
    class_name: ClassVar[str] = "IsothermalIdealGasWorkEquationII"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalIdealGasWorkEquationII")

    id: Union[str, IsothermalIdealGasWorkEquationIIId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = R_{system#material} * T_{change_of_state#initial_state} * ln"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalIdealGasWorkEquationIIId):
            self.id = IsothermalIdealGasWorkEquationIIId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalIdealGasPolytropicExponentEquation(IsothermalIdealGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalIdealGasPolytropicExponentEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalIdealGasPolytropicExponentEquation"
    class_name: ClassVar[str] = "IsothermalIdealGasPolytropicExponentEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalIdealGasPolytropicExponentEquation")

    id: Union[str, IsothermalIdealGasPolytropicExponentEquationId] = None
    as_text: Optional[str] = "n_poly_{change_of_state#transition} = 1"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalIdealGasPolytropicExponentEquationId):
            self.id = IsothermalIdealGasPolytropicExponentEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalPerfectGasEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalPerfectGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalPerfectGasEquation"
    class_name: ClassVar[str] = "IsothermalPerfectGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalPerfectGasEquation")

    id: Union[str, IsothermalPerfectGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalPerfectGasEntropyEquation(IsothermalPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalPerfectGasEntropyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalPerfectGasEntropyEquation"
    class_name: ClassVar[str] = "IsothermalPerfectGasEntropyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalPerfectGasEntropyEquation")

    id: Union[str, IsothermalPerfectGasEntropyEquationId] = None
    as_text: Optional[str] = "del_s_{change_of_state#transition} = R_{system#material} * ln"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalPerfectGasEntropyEquationId):
            self.id = IsothermalPerfectGasEntropyEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsothermalPerfectGasWorkOnInternalStateEquation(IsothermalPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsothermalPerfectGasWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsothermalPerfectGasWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsothermalPerfectGasWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalPerfectGasWorkOnInternalStateEquation")

    id: Union[str, IsothermalPerfectGasWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = - T_{change_of_state#initial_state} * del_s_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsothermalPerfectGasWorkOnInternalStateEquationId):
            self.id = IsothermalPerfectGasWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricEquation"
    class_name: ClassVar[str] = "IsobaricEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricEquation")

    id: Union[str, IsobaricEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricProperties(IsobaricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricProperties"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricProperties"
    class_name: ClassVar[str] = "IsobaricProperties"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricProperties")

    id: Union[str, IsobaricPropertiesId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "p_{change_of_state#final_state} - p_{change_of_state#initial_state} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobaricPropertiesId):
            self.id = IsobaricPropertiesId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricWorkOnInternalStateEquation(IsobaricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsobaricWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricWorkOnInternalStateEquation")

    id: Union[str, IsobaricWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "W_i_{change_of_state#transition} = - p_{change_of_state#initial_state} * del_V_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobaricWorkOnInternalStateEquationId):
            self.id = IsobaricWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricSpecificWorkOnInternalStateEquation(IsobaricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricSpecificWorkOnInternalStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricSpecificWorkOnInternalStateEquation"
    class_name: ClassVar[str] = "IsobaricSpecificWorkOnInternalStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricSpecificWorkOnInternalStateEquation")

    id: Union[str, IsobaricSpecificWorkOnInternalStateEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = - p_{change_of_state#initial_state} * del_v_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobaricSpecificWorkOnInternalStateEquationId):
            self.id = IsobaricSpecificWorkOnInternalStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricPolytropicExponentEquation(IsobaricEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricPolytropicExponentEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricPolytropicExponentEquation"
    class_name: ClassVar[str] = "IsobaricPolytropicExponentEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricPolytropicExponentEquation")

    id: Union[str, IsobaricPolytropicExponentEquationId] = None
    as_text: Optional[str] = "n_poly_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobaricPolytropicExponentEquationId):
            self.id = IsobaricPolytropicExponentEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricPerfectGasEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricPerfectGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricPerfectGasEquation"
    class_name: ClassVar[str] = "IsobaricPerfectGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricPerfectGasEquation")

    id: Union[str, IsobaricPerfectGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsobaricPerfectGasHeatEquation(IsobaricPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsobaricPerfectGasHeatEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsobaricPerfectGasHeatEquation"
    class_name: ClassVar[str] = "IsobaricPerfectGasHeatEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricPerfectGasHeatEquation")

    id: Union[str, IsobaricPerfectGasHeatEquationId] = None
    as_text: Optional[str] = "q_{change_of_state#transition} = c_p_{system#material} * del_T_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsobaricPerfectGasHeatEquationId):
            self.id = IsobaricPerfectGasHeatEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdiabaticEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["AdiabaticEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:AdiabaticEquation"
    class_name: ClassVar[str] = "AdiabaticEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AdiabaticEquation")

    id: Union[str, AdiabaticEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdiabaticHeatEquation(AdiabaticEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["AdiabaticHeatEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:AdiabaticHeatEquation"
    class_name: ClassVar[str] = "AdiabaticHeatEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AdiabaticHeatEquation")

    id: Union[str, AdiabaticHeatEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "Q_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdiabaticHeatEquationId):
            self.id = AdiabaticHeatEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdiabaticSpecificHeatEquation(AdiabaticEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["AdiabaticSpecificHeatEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:AdiabaticSpecificHeatEquation"
    class_name: ClassVar[str] = "AdiabaticSpecificHeatEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AdiabaticSpecificHeatEquation")

    id: Union[str, AdiabaticSpecificHeatEquationId] = None
    as_text: Optional[str] = "q_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdiabaticSpecificHeatEquationId):
            self.id = AdiabaticSpecificHeatEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicEquation"
    class_name: ClassVar[str] = "IsentropicEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicEquation")

    id: Union[str, IsentropicEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicHeatEquation(IsentropicEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicHeatEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicHeatEquation"
    class_name: ClassVar[str] = "IsentropicHeatEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicHeatEquation")

    id: Union[str, IsentropicHeatEquationId] = None
    as_text: Optional[str] = "q_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicHeatEquationId):
            self.id = IsentropicHeatEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicEntropyEquation(IsentropicEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicEntropyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicEntropyEquation"
    class_name: ClassVar[str] = "IsentropicEntropyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicEntropyEquation")

    id: Union[str, IsentropicEntropyEquationId] = None
    as_text: Optional[str] = "del_s_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicEntropyEquationId):
            self.id = IsentropicEntropyEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicMolarEntropyEquation(IsentropicEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicMolarEntropyEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicMolarEntropyEquation"
    class_name: ClassVar[str] = "IsentropicMolarEntropyEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicMolarEntropyEquation")

    id: Union[str, IsentropicMolarEntropyEquationId] = None
    as_text: Optional[str] = "del_sm_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicMolarEntropyEquationId):
            self.id = IsentropicMolarEntropyEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicPerfectGasEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicPerfectGasEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicPerfectGasEquation"
    class_name: ClassVar[str] = "IsentropicPerfectGasEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicPerfectGasEquation")

    id: Union[str, IsentropicPerfectGasEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicPerfectGasPolytropicExponentEquation(IsentropicPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicPerfectGasPolytropicExponentEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicPerfectGasPolytropicExponentEquation"
    class_name: ClassVar[str] = "IsentropicPerfectGasPolytropicExponentEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicPerfectGasPolytropicExponentEquation")

    id: Union[str, IsentropicPerfectGasPolytropicExponentEquationId] = None
    as_text: Optional[str] = "kappa_{system#material} = n_poly_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicPerfectGasPolytropicExponentEquationId):
            self.id = IsentropicPerfectGasPolytropicExponentEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicPerfectGasTechnicalWorkEquation(IsentropicPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicPerfectGasTechnicalWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicPerfectGasTechnicalWorkEquation"
    class_name: ClassVar[str] = "IsentropicPerfectGasTechnicalWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicPerfectGasTechnicalWorkEquation")

    id: Union[str, IsentropicPerfectGasTechnicalWorkEquationId] = None
    as_text: Optional[str] = "w_t_{change_of_state} = kappa_{system#material} * w_i_{change_of_state#transition}"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicPerfectGasTechnicalWorkEquationId):
            self.id = IsentropicPerfectGasTechnicalWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicPerfectGasWorkEquation(IsentropicPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicPerfectGasWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicPerfectGasWorkEquation"
    class_name: ClassVar[str] = "IsentropicPerfectGasWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicPerfectGasWorkEquation")

    id: Union[str, IsentropicPerfectGasWorkEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = "

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicPerfectGasWorkEquationId):
            self.id = IsentropicPerfectGasWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsentropicPerfectGasTemperatureEquation(IsentropicPerfectGasEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IsentropicPerfectGasTemperatureEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IsentropicPerfectGasTemperatureEquation"
    class_name: ClassVar[str] = "IsentropicPerfectGasTemperatureEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicPerfectGasTemperatureEquation")

    id: Union[str, IsentropicPerfectGasTemperatureEquationId] = None
    as_text: Optional[str] = "T_{change_of_state#initial_state} / T_{change_of_state#final_state} = "

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IsentropicPerfectGasTemperatureEquationId):
            self.id = IsentropicPerfectGasTemperatureEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolytropicEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["PolytropicEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:PolytropicEquation"
    class_name: ClassVar[str] = "PolytropicEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PolytropicEquation")

    id: Union[str, PolytropicEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolytropicWorkEquation(PolytropicEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["PolytropicWorkEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:PolytropicWorkEquation"
    class_name: ClassVar[str] = "PolytropicWorkEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PolytropicWorkEquation")

    id: Union[str, PolytropicWorkEquationId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition} = "

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolytropicWorkEquationId):
            self.id = PolytropicWorkEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasPolytropicChangeOfStateEquation(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasPolytropicChangeOfStateEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasPolytropicChangeOfStateEquation"
    class_name: ClassVar[str] = "IdealGasPolytropicChangeOfStateEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasPolytropicChangeOfStateEquation")

    id: Union[str, IdealGasPolytropicChangeOfStateEquationId] = None
    as_text: Optional[str] = "T_{change_of_state#final_state} / T_{change_of_state#initial_state} = "
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdealGasPolytropicChangeOfStateEquationId):
            self.id = IdealGasPolytropicChangeOfStateEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdealGasPolytropicChangeOfStateEquationII(SystemInChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["IdealGasPolytropicChangeOfStateEquationII"]
    class_class_curie: ClassVar[str] = "thmo_equations:IdealGasPolytropicChangeOfStateEquationII"
    class_name: ClassVar[str] = "IdealGasPolytropicChangeOfStateEquationII"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasPolytropicChangeOfStateEquationII")

    id: Union[str, IdealGasPolytropicChangeOfStateEquationIIId] = None
    as_text: Optional[str] = "w_i_{change_of_state#transition}  = R_{system#material} * "
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdealGasPolytropicChangeOfStateEquationIIId):
            self.id = IdealGasPolytropicChangeOfStateEquationIIId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionEquation(ChangeOfStateEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionEquation"
    class_name: ClassVar[str] = "NotInMotionEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionEquation")

    id: Union[str, NotInMotionEquationId] = None
    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelCEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelCEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelCEquation"
    class_name: ClassVar[str] = "NotInMotionDelCEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelCEquation")

    id: Union[str, NotInMotionDelCEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_c_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelCEquationId):
            self.id = NotInMotionDelCEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelZEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelZEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelZEquation"
    class_name: ClassVar[str] = "NotInMotionDelZEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelZEquation")

    id: Union[str, NotInMotionDelZEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_z_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelZEquationId):
            self.id = NotInMotionDelZEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelEkinEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelEkinEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelEkinEquation"
    class_name: ClassVar[str] = "NotInMotionDelEkinEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelEkinEquation")

    id: Union[str, NotInMotionDelEkinEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_E_kin_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelEkinEquationId):
            self.id = NotInMotionDelEkinEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelekinEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelekinEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelekinEquation"
    class_name: ClassVar[str] = "NotInMotionDelekinEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelekinEquation")

    id: Union[str, NotInMotionDelekinEquationId] = None
    as_text: Optional[str] = "del_e_kin_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelekinEquationId):
            self.id = NotInMotionDelekinEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelEpotEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelEpotEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelEpotEquation"
    class_name: ClassVar[str] = "NotInMotionDelEpotEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelEpotEquation")

    id: Union[str, NotInMotionDelEpotEquationId] = None
    related_variables: Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]] = empty_list()
    as_text: Optional[str] = "del_E_pot_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelEpotEquationId):
            self.id = NotInMotionDelEpotEquationId(self.id)

        if not isinstance(self.related_variables, list):
            self.related_variables = [self.related_variables] if self.related_variables is not None else []
        self.related_variables = [v if isinstance(v, Variable) else Variable(**as_dict(v)) for v in self.related_variables]

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInMotionDelepotEquation(NotInMotionEquation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_EQUATIONS["NotInMotionDelepotEquation"]
    class_class_curie: ClassVar[str] = "thmo_equations:NotInMotionDelepotEquation"
    class_name: ClassVar[str] = "NotInMotionDelepotEquation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionDelepotEquation")

    id: Union[str, NotInMotionDelepotEquationId] = None
    as_text: Optional[str] = "del_e_pot_{change_of_state#transition} = 0"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInMotionDelepotEquationId):
            self.id = NotInMotionDelepotEquationId(self.id)

        if self.as_text is not None and not isinstance(self.as_text, str):
            self.as_text = str(self.as_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rule(Element):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["Rule"]
    class_class_curie: ClassVar[str] = "thmo_rules:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Rule")

    satisfied: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.satisfied is not None and not isinstance(self.satisfied, Bool):
            self.satisfied = Bool(self.satisfied)

        super().__post_init__(**kwargs)


class SystemRules(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["SystemRules"]
    class_class_curie: ClassVar[str] = "thmo_rules:SystemRules"
    class_name: ClassVar[str] = "SystemRules"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SystemRules")


class IdealGasMaterialRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IdealGasMaterialRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IdealGasMaterialRule"
    class_name: ClassVar[str] = "IdealGasMaterialRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasMaterialRule")


class PerfectGasMaterialRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["PerfectGasMaterialRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:PerfectGasMaterialRule"
    class_name: ClassVar[str] = "PerfectGasMaterialRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PerfectGasMaterialRule")


class IdealGasRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IdealGasRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IdealGasRule"
    class_name: ClassVar[str] = "IdealGasRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IdealGasRule")


class PerfectGasRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["PerfectGasRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:PerfectGasRule"
    class_name: ClassVar[str] = "PerfectGasRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PerfectGasRule")


class IsochoricRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IsochoricRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IsochoricRule"
    class_name: ClassVar[str] = "IsochoricRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsochoricRule")


class IsothermalRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IsothermalRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IsothermalRule"
    class_name: ClassVar[str] = "IsothermalRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsothermalRule")


class IsobaricRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IsobaricRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IsobaricRule"
    class_name: ClassVar[str] = "IsobaricRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsobaricRule")


class IsentropicRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IsentropicRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IsentropicRule"
    class_name: ClassVar[str] = "IsentropicRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IsentropicRule")


class PolytropicRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["PolytropicRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:PolytropicRule"
    class_name: ClassVar[str] = "PolytropicRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/PolytropicRule")


class NotInMotionRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["NotInMotionRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:NotInMotionRule"
    class_name: ClassVar[str] = "NotInMotionRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/NotInMotionRule")


class AdiabaticRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["AdiabaticRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:AdiabaticRule"
    class_name: ClassVar[str] = "AdiabaticRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/AdiabaticRule")


class IrreversibleRule(Rule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_RULES["IrreversibleRule"]
    class_class_curie: ClassVar[str] = "thmo_rules:IrreversibleRule"
    class_name: ClassVar[str] = "IrreversibleRule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/IrreversibleRule")


@dataclass(repr=False)
class Problem(YAMLRoot):
    """
    Basic Problem with manually entered additional equations and required variables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["Problem"]
    class_class_curie: ClassVar[str] = "thmo_problems:Problem"
    class_name: ClassVar[str] = "Problem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Problem")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    additional_equations: Optional[Union[str, List[str]]] = empty_list()
    valid_problem: Optional[Union[bool, Bool]] = None
    invalid_problem: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.required_variables):
            self.MissingRequiredField("required_variables")
        if not isinstance(self.required_variables, list):
            self.required_variables = [self.required_variables] if self.required_variables is not None else []
        self.required_variables = [v if isinstance(v, str) else str(v) for v in self.required_variables]

        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)

        if not isinstance(self.additional_equations, list):
            self.additional_equations = [self.additional_equations] if self.additional_equations is not None else []
        self.additional_equations = [v if isinstance(v, str) else str(v) for v in self.additional_equations]

        if self.valid_problem is not None and not isinstance(self.valid_problem, Bool):
            self.valid_problem = Bool(self.valid_problem)

        if self.invalid_problem is not None and not isinstance(self.invalid_problem, Bool):
            self.invalid_problem = Bool(self.invalid_problem)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "problem_class"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class SystemProblem(Problem):
    """
    Basic Problem covering one system with manually entered additional equations and required variables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["SystemProblem"]
    class_class_curie: ClassVar[str] = "thmo_problems:SystemProblem"
    class_name: ClassVar[str] = "SystemProblem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SystemProblem")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    system: Union[dict, System] = None
    pureMaterial: Optional[Union[dict, PureMaterial]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, System):
            self.system = System(**as_dict(self.system))

        if self.pureMaterial is not None and not isinstance(self.pureMaterial, PureMaterial):
            self.pureMaterial = PureMaterial(**as_dict(self.pureMaterial))

        super().__post_init__(**kwargs)
        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)


@dataclass(repr=False)
class Equilibrium(SystemProblem):
    """
    Problem that contains a system, material, equation of state, one state and no change of state or transition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["Equilibrium"]
    class_class_curie: ClassVar[str] = "thmo_problems:Equilibrium"
    class_name: ClassVar[str] = "Equilibrium"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/Equilibrium")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    system: Union[dict, System] = None
    state: Union[dict, State] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, State):
            self.state = State(**as_dict(self.state))

        super().__post_init__(**kwargs)
        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)


@dataclass(repr=False)
class SingleStep(SystemProblem):
    """
    Problem that describes a system that transitions from one state to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["SingleStep"]
    class_class_curie: ClassVar[str] = "thmo_problems:SingleStep"
    class_name: ClassVar[str] = "SingleStep"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SingleStep")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    system: Union[dict, System] = None
    states: Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]] = empty_dict()
    change_of_state: Union[dict, ChangeOfState] = None
    valid_problem: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.states):
            self.MissingRequiredField("states")
        self._normalize_inlined_as_list(slot_name="states", slot_type=State, key_name="id", keyed=True)

        if self._is_empty(self.change_of_state):
            self.MissingRequiredField("change_of_state")
        if not isinstance(self.change_of_state, ChangeOfState):
            self.change_of_state = ChangeOfState(**as_dict(self.change_of_state))

        if self.valid_problem is not None and not isinstance(self.valid_problem, Bool):
            self.valid_problem = Bool(self.valid_problem)

        super().__post_init__(**kwargs)
        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)


@dataclass(repr=False)
class SequentialSteps(SystemProblem):
    """
    Problem that describes a system that transitions between multiple states sequentially.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["SequentialSteps"]
    class_class_curie: ClassVar[str] = "thmo_problems:SequentialSteps"
    class_name: ClassVar[str] = "SequentialSteps"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/SequentialSteps")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    system: Union[dict, System] = None
    states: Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]] = empty_dict()
    change_of_states: Union[Dict[Union[str, ChangeOfStateId], Union[dict, ChangeOfState]], List[Union[dict, ChangeOfState]]] = empty_dict()
    valid_problem: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.states):
            self.MissingRequiredField("states")
        self._normalize_inlined_as_list(slot_name="states", slot_type=State, key_name="id", keyed=True)

        if self._is_empty(self.change_of_states):
            self.MissingRequiredField("change_of_states")
        self._normalize_inlined_as_list(slot_name="change_of_states", slot_type=ChangeOfState, key_name="id", keyed=True)

        if self.valid_problem is not None and not isinstance(self.valid_problem, Bool):
            self.valid_problem = Bool(self.valid_problem)

        super().__post_init__(**kwargs)
        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)


@dataclass(repr=False)
class CyclicProcess(SystemProblem):
    """
    Problem that describes a system that transitions between multiple states in a cyclic manner.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = THMO_PROBLEMS["CyclicProcess"]
    class_class_curie: ClassVar[str] = "thmo_problems:CyclicProcess"
    class_name: ClassVar[str] = "CyclicProcess"
    class_model_uri: ClassVar[URIRef] = URIRef("https://gitlab.rhrk.uni-kl.de/knowtd/knowtd/-/blob/main/Ontology/thermodynamics_ontology.yaml/CyclicProcess")

    required_variables: Union[str, List[str]] = None
    problem_class: str = None
    system: Union[dict, System] = None
    states: Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]] = empty_dict()
    change_of_states: Union[Dict[Union[str, ChangeOfStateId], Union[dict, ChangeOfState]], List[Union[dict, ChangeOfState]]] = empty_dict()
    valid_problem: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.states):
            self.MissingRequiredField("states")
        self._normalize_inlined_as_list(slot_name="states", slot_type=State, key_name="id", keyed=True)

        if self._is_empty(self.change_of_states):
            self.MissingRequiredField("change_of_states")
        self._normalize_inlined_as_list(slot_name="change_of_states", slot_type=ChangeOfState, key_name="id", keyed=True)

        if self.valid_problem is not None and not isinstance(self.valid_problem, Bool):
            self.valid_problem = Bool(self.valid_problem)

        super().__post_init__(**kwargs)
        if self._is_empty(self.problem_class):
            self.MissingRequiredField("problem_class")
        self.problem_class = str(self.class_name)


# Enumerations
class EquationOfStateModels(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EquationOfStateModels",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ideal gas",
            PermissibleValue(text="ideal gas"))
        setattr(cls, "van der Waals",
            PermissibleValue(text="van der Waals"))
        setattr(cls, "perfect gas",
            PermissibleValue(text="perfect gas"))

# Slots
class slots:
    pass

slots.id = Slot(uri=THMO_CONCEPTS.id, name="id", curie=THMO_CONCEPTS.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.related_changes_and_states = Slot(uri=THMO_CONCEPTS.related_changes_and_states, name="related_changes_and_states", curie=THMO_CONCEPTS.curie('related_changes_and_states'),
                   model_uri=DEFAULT_.related_changes_and_states, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.related_changes = Slot(uri=THMO_CONCEPTS.related_changes, name="related_changes", curie=THMO_CONCEPTS.curie('related_changes'),
                   model_uri=DEFAULT_.related_changes, domain=None, range=Optional[Union[Union[str, ChangeOfStateId], List[Union[str, ChangeOfStateId]]]])

slots.related_states = Slot(uri=THMO_CONCEPTS.related_states, name="related_states", curie=THMO_CONCEPTS.curie('related_states'),
                   model_uri=DEFAULT_.related_states, domain=None, range=Optional[Union[Union[str, StateId], List[Union[str, StateId]]]])

slots.material = Slot(uri=THMO_CONCEPTS.material, name="material", curie=THMO_CONCEPTS.curie('material'),
                   model_uri=DEFAULT_.material, domain=None, range=Optional[Union[str, PureMaterialId]])

slots.equation_of_state = Slot(uri=THMO_CONCEPTS.equation_of_state, name="equation_of_state", curie=THMO_CONCEPTS.curie('equation_of_state'),
                   model_uri=DEFAULT_.equation_of_state, domain=None, range=Optional[Union[dict, EquationOfState]])

slots.system = Slot(uri=THMO_CONCEPTS.system, name="system", curie=THMO_CONCEPTS.curie('system'),
                   model_uri=DEFAULT_.system, domain=None, range=Optional[Union[dict, System]])

slots.state = Slot(uri=THMO_CONCEPTS.state, name="state", curie=THMO_CONCEPTS.curie('state'),
                   model_uri=DEFAULT_.state, domain=None, range=Optional[Union[dict, State]])

slots.initial_state = Slot(uri=THMO_CONCEPTS.initial_state, name="initial_state", curie=THMO_CONCEPTS.curie('initial_state'),
                   model_uri=DEFAULT_.initial_state, domain=None, range=Optional[Union[str, StateId]])

slots.final_state = Slot(uri=THMO_CONCEPTS.final_state, name="final_state", curie=THMO_CONCEPTS.curie('final_state'),
                   model_uri=DEFAULT_.final_state, domain=None, range=Optional[Union[str, StateId]])

slots.transition = Slot(uri=THMO_CONCEPTS.transition, name="transition", curie=THMO_CONCEPTS.curie('transition'),
                   model_uri=DEFAULT_.transition, domain=None, range=Optional[Union[dict, Transition]])

slots.change_of_state = Slot(uri=THMO_CONCEPTS.change_of_state, name="change_of_state", curie=THMO_CONCEPTS.curie('change_of_state'),
                   model_uri=DEFAULT_.change_of_state, domain=None, range=Optional[Union[dict, ChangeOfState]])

slots.variable_slot = Slot(uri=THMO_VARIABLES.variable_slot, name="variable_slot", curie=THMO_VARIABLES.curie('variable_slot'),
                   model_uri=DEFAULT_.variable_slot, domain=None, range=Optional[str])

slots.value = Slot(uri=THMO_VARIABLES.value, name="value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.value, domain=None, range=Optional[float])

slots.is_required = Slot(uri=THMO_VARIABLES.is_required, name="is_required", curie=THMO_VARIABLES.curie('is_required'),
                   model_uri=DEFAULT_.is_required, domain=None, range=Optional[Union[bool, Bool]])

slots.m = Slot(uri=THMO_VARIABLES.m, name="m", curie=THMO_VARIABLES.curie('m'),
                   model_uri=DEFAULT_.m, domain=None, range=Optional[Union[dict, Mass]])

slots.M = Slot(uri=THMO_VARIABLES.M, name="M", curie=THMO_VARIABLES.curie('M'),
                   model_uri=DEFAULT_.M, domain=None, range=Optional[Union[dict, MolarMass]])

slots.n = Slot(uri=THMO_VARIABLES.n, name="n", curie=THMO_VARIABLES.curie('n'),
                   model_uri=DEFAULT_.n, domain=None, range=Optional[Union[dict, AmountOfSubstance]])

slots.R = Slot(uri=THMO_VARIABLES.R, name="R", curie=THMO_VARIABLES.curie('R'),
                   model_uri=DEFAULT_.R, domain=None, range=Optional[Union[dict, IndividualGasConstant]])

slots.c_p = Slot(uri=THMO_VARIABLES.c_p, name="c_p", curie=THMO_VARIABLES.curie('c_p'),
                   model_uri=DEFAULT_.c_p, domain=None, range=Optional[Union[dict, SpecificHeatCapacityConstantPressure]])

slots.c_v = Slot(uri=THMO_VARIABLES.c_v, name="c_v", curie=THMO_VARIABLES.curie('c_v'),
                   model_uri=DEFAULT_.c_v, domain=None, range=Optional[Union[dict, SpecificHeatCapacityConstantVolume]])

slots.c_pm = Slot(uri=THMO_VARIABLES.c_pm, name="c_pm", curie=THMO_VARIABLES.curie('c_pm'),
                   model_uri=DEFAULT_.c_pm, domain=None, range=Optional[Union[dict, MolarHeatCapacityConstantPressure]])

slots.c_vm = Slot(uri=THMO_VARIABLES.c_vm, name="c_vm", curie=THMO_VARIABLES.curie('c_vm'),
                   model_uri=DEFAULT_.c_vm, domain=None, range=Optional[Union[dict, MolarHeatCapacityConstantVolume]])

slots.kappa = Slot(uri=THMO_VARIABLES.kappa, name="kappa", curie=THMO_VARIABLES.curie('kappa'),
                   model_uri=DEFAULT_.kappa, domain=None, range=Optional[Union[dict, HeatCapacityRatio]])

slots.Rbar = Slot(uri=THMO_VARIABLES.Rbar, name="Rbar", curie=THMO_VARIABLES.curie('Rbar'),
                   model_uri=DEFAULT_.Rbar, domain=None, range=Optional[Union[dict, UniversalGasConstant]])

slots.g = Slot(uri=THMO_VARIABLES.g, name="g", curie=THMO_VARIABLES.curie('g'),
                   model_uri=DEFAULT_.g, domain=None, range=Optional[Union[dict, GravitationalAcceleration]])

slots.T = Slot(uri=THMO_VARIABLES.T, name="T", curie=THMO_VARIABLES.curie('T'),
                   model_uri=DEFAULT_.T, domain=None, range=Optional[Union[dict, Temperature]])

slots.T0 = Slot(uri=THMO_VARIABLES.T0, name="T0", curie=THMO_VARIABLES.curie('T0'),
                   model_uri=DEFAULT_.T0, domain=None, range=Optional[Union[dict, StandardTemperature]])

slots.p = Slot(uri=THMO_VARIABLES.p, name="p", curie=THMO_VARIABLES.curie('p'),
                   model_uri=DEFAULT_.p, domain=None, range=Optional[Union[dict, Pressure]])

slots.V = Slot(uri=THMO_VARIABLES.V, name="V", curie=THMO_VARIABLES.curie('V'),
                   model_uri=DEFAULT_.V, domain=None, range=Optional[Union[dict, Volume]])

slots.v = Slot(uri=THMO_VARIABLES.v, name="v", curie=THMO_VARIABLES.curie('v'),
                   model_uri=DEFAULT_.v, domain=None, range=Optional[Union[dict, SpecificVolume]])

slots.SA = Slot(uri=THMO_VARIABLES.SA, name="SA", curie=THMO_VARIABLES.curie('SA'),
                   model_uri=DEFAULT_.SA, domain=None, range=Optional[Union[dict, SurfaceArea]])

slots.U = Slot(uri=THMO_VARIABLES.U, name="U", curie=THMO_VARIABLES.curie('U'),
                   model_uri=DEFAULT_.U, domain=None, range=Optional[Union[dict, InternalEnergy]])

slots.u = Slot(uri=THMO_VARIABLES.u, name="u", curie=THMO_VARIABLES.curie('u'),
                   model_uri=DEFAULT_.u, domain=None, range=Optional[Union[dict, SpecificInternalEnergy]])

slots.H = Slot(uri=THMO_VARIABLES.H, name="H", curie=THMO_VARIABLES.curie('H'),
                   model_uri=DEFAULT_.H, domain=None, range=Optional[Union[dict, Enthalpy]])

slots.h = Slot(uri=THMO_VARIABLES.h, name="h", curie=THMO_VARIABLES.curie('h'),
                   model_uri=DEFAULT_.h, domain=None, range=Optional[Union[dict, SpecificEnthalpy]])

slots.S = Slot(uri=THMO_VARIABLES.S, name="S", curie=THMO_VARIABLES.curie('S'),
                   model_uri=DEFAULT_.S, domain=None, range=Optional[Union[dict, Entropy]])

slots.s = Slot(uri=THMO_VARIABLES.s, name="s", curie=THMO_VARIABLES.curie('s'),
                   model_uri=DEFAULT_.s, domain=None, range=Optional[Union[dict, SpecificEntropy]])

slots.sm = Slot(uri=THMO_VARIABLES.sm, name="sm", curie=THMO_VARIABLES.curie('sm'),
                   model_uri=DEFAULT_.sm, domain=None, range=Optional[Union[dict, MolarEntropy]])

slots.rho = Slot(uri=THMO_VARIABLES.rho, name="rho", curie=THMO_VARIABLES.curie('rho'),
                   model_uri=DEFAULT_.rho, domain=None, range=Optional[Union[dict, SpecificDensity]])

slots.z = Slot(uri=THMO_VARIABLES.z, name="z", curie=THMO_VARIABLES.curie('z'),
                   model_uri=DEFAULT_.z, domain=None, range=Optional[Union[dict, PositionCenterMass]])

slots.c = Slot(uri=THMO_VARIABLES.c, name="c", curie=THMO_VARIABLES.curie('c'),
                   model_uri=DEFAULT_.c, domain=None, range=Optional[Union[dict, VelocityCenterMass]])

slots.E_kin = Slot(uri=THMO_VARIABLES.E_kin, name="E_kin", curie=THMO_VARIABLES.curie('E_kin'),
                   model_uri=DEFAULT_.E_kin, domain=None, range=Optional[Union[dict, KineticEnergyCenterMass]])

slots.e_kin = Slot(uri=THMO_VARIABLES.e_kin, name="e_kin", curie=THMO_VARIABLES.curie('e_kin'),
                   model_uri=DEFAULT_.e_kin, domain=None, range=Optional[Union[dict, SpecificKineticEnergyCenterMass]])

slots.E_pot = Slot(uri=THMO_VARIABLES.E_pot, name="E_pot", curie=THMO_VARIABLES.curie('E_pot'),
                   model_uri=DEFAULT_.E_pot, domain=None, range=Optional[Union[dict, PotentialEnergyCenterMass]])

slots.e_pot = Slot(uri=THMO_VARIABLES.e_pot, name="e_pot", curie=THMO_VARIABLES.curie('e_pot'),
                   model_uri=DEFAULT_.e_pot, domain=None, range=Optional[Union[dict, SpecificPotentialEnergyCenterMass]])

slots.Q = Slot(uri=THMO_VARIABLES.Q, name="Q", curie=THMO_VARIABLES.curie('Q'),
                   model_uri=DEFAULT_.Q, domain=None, range=Optional[Union[dict, Heat]])

slots.q = Slot(uri=THMO_VARIABLES.q, name="q", curie=THMO_VARIABLES.curie('q'),
                   model_uri=DEFAULT_.q, domain=None, range=Optional[Union[dict, HeatPerMass]])

slots.W = Slot(uri=THMO_VARIABLES.W, name="W", curie=THMO_VARIABLES.curie('W'),
                   model_uri=DEFAULT_.W, domain=None, range=Optional[Union[dict, Work]])

slots.w = Slot(uri=THMO_VARIABLES.w, name="w", curie=THMO_VARIABLES.curie('w'),
                   model_uri=DEFAULT_.w, domain=None, range=Optional[Union[dict, WorkPerMass]])

slots.W_i = Slot(uri=THMO_VARIABLES.W_i, name="W_i", curie=THMO_VARIABLES.curie('W_i'),
                   model_uri=DEFAULT_.W_i, domain=None, range=Optional[Union[dict, WorkOnInternalState]])

slots.W_a = Slot(uri=THMO_VARIABLES.W_a, name="W_a", curie=THMO_VARIABLES.curie('W_a'),
                   model_uri=DEFAULT_.W_a, domain=None, range=Optional[Union[dict, WorkOnExternalState]])

slots.w_i = Slot(uri=THMO_VARIABLES.w_i, name="w_i", curie=THMO_VARIABLES.curie('w_i'),
                   model_uri=DEFAULT_.w_i, domain=None, range=Optional[Union[dict, WorkOnInternalStatePerMass]])

slots.w_a = Slot(uri=THMO_VARIABLES.w_a, name="w_a", curie=THMO_VARIABLES.curie('w_a'),
                   model_uri=DEFAULT_.w_a, domain=None, range=Optional[Union[dict, WorkOnExternalStatePerMass]])

slots.w_t = Slot(uri=THMO_VARIABLES.w_t, name="w_t", curie=THMO_VARIABLES.curie('w_t'),
                   model_uri=DEFAULT_.w_t, domain=None, range=Optional[Union[dict, TechnicalWorkPerMass]])

slots.W_vol = Slot(uri=THMO_VARIABLES.W_vol, name="W_vol", curie=THMO_VARIABLES.curie('W_vol'),
                   model_uri=DEFAULT_.W_vol, domain=None, range=Optional[Union[dict, VolumeChangeWork]])

slots.w_vol = Slot(uri=THMO_VARIABLES.w_vol, name="w_vol", curie=THMO_VARIABLES.curie('w_vol'),
                   model_uri=DEFAULT_.w_vol, domain=None, range=Optional[Union[dict, VolumeChangeWorkPerMass]])

slots.W_stir = Slot(uri=THMO_VARIABLES.W_stir, name="W_stir", curie=THMO_VARIABLES.curie('W_stir'),
                   model_uri=DEFAULT_.W_stir, domain=None, range=Optional[Union[dict, StirringWork]])

slots.w_stir = Slot(uri=THMO_VARIABLES.w_stir, name="w_stir", curie=THMO_VARIABLES.curie('w_stir'),
                   model_uri=DEFAULT_.w_stir, domain=None, range=Optional[Union[dict, StirringWorkPerMass]])

slots.W_electrical = Slot(uri=THMO_VARIABLES.W_electrical, name="W_electrical", curie=THMO_VARIABLES.curie('W_electrical'),
                   model_uri=DEFAULT_.W_electrical, domain=None, range=Optional[Union[dict, ElectricalWork]])

slots.w_electrical = Slot(uri=THMO_VARIABLES.w_electrical, name="w_electrical", curie=THMO_VARIABLES.curie('w_electrical'),
                   model_uri=DEFAULT_.w_electrical, domain=None, range=Optional[Union[dict, ElectricalWorkPerMass]])

slots.del_T = Slot(uri=THMO_VARIABLES.del_T, name="del_T", curie=THMO_VARIABLES.curie('del_T'),
                   model_uri=DEFAULT_.del_T, domain=None, range=Optional[Union[dict, TemperatureDifference]])

slots.del_p = Slot(uri=THMO_VARIABLES.del_p, name="del_p", curie=THMO_VARIABLES.curie('del_p'),
                   model_uri=DEFAULT_.del_p, domain=None, range=Optional[Union[dict, PressureDifference]])

slots.del_V = Slot(uri=THMO_VARIABLES.del_V, name="del_V", curie=THMO_VARIABLES.curie('del_V'),
                   model_uri=DEFAULT_.del_V, domain=None, range=Optional[Union[dict, VolumeDifference]])

slots.del_v = Slot(uri=THMO_VARIABLES.del_v, name="del_v", curie=THMO_VARIABLES.curie('del_v'),
                   model_uri=DEFAULT_.del_v, domain=None, range=Optional[Union[dict, SpecificVolumeDifference]])

slots.del_U = Slot(uri=THMO_VARIABLES.del_U, name="del_U", curie=THMO_VARIABLES.curie('del_U'),
                   model_uri=DEFAULT_.del_U, domain=None, range=Optional[Union[dict, InternalEnergyDifference]])

slots.del_u = Slot(uri=THMO_VARIABLES.del_u, name="del_u", curie=THMO_VARIABLES.curie('del_u'),
                   model_uri=DEFAULT_.del_u, domain=None, range=Optional[Union[dict, SpecificInternalEnergyDifference]])

slots.del_H = Slot(uri=THMO_VARIABLES.del_H, name="del_H", curie=THMO_VARIABLES.curie('del_H'),
                   model_uri=DEFAULT_.del_H, domain=None, range=Optional[Union[dict, EnthalpyDifference]])

slots.del_h = Slot(uri=THMO_VARIABLES.del_h, name="del_h", curie=THMO_VARIABLES.curie('del_h'),
                   model_uri=DEFAULT_.del_h, domain=None, range=Optional[Union[dict, SpecificEnthalpyDifference]])

slots.del_S = Slot(uri=THMO_VARIABLES.del_S, name="del_S", curie=THMO_VARIABLES.curie('del_S'),
                   model_uri=DEFAULT_.del_S, domain=None, range=Optional[Union[dict, EntropyDifference]])

slots.del_s = Slot(uri=THMO_VARIABLES.del_s, name="del_s", curie=THMO_VARIABLES.curie('del_s'),
                   model_uri=DEFAULT_.del_s, domain=None, range=Optional[Union[dict, SpecificEntropyDifference]])

slots.del_sm = Slot(uri=THMO_VARIABLES.del_sm, name="del_sm", curie=THMO_VARIABLES.curie('del_sm'),
                   model_uri=DEFAULT_.del_sm, domain=None, range=Optional[Union[dict, MolarEntropyDifference]])

slots.del_z = Slot(uri=THMO_VARIABLES.del_z, name="del_z", curie=THMO_VARIABLES.curie('del_z'),
                   model_uri=DEFAULT_.del_z, domain=None, range=Optional[Union[dict, PositionCenterMassDifference]])

slots.del_c = Slot(uri=THMO_VARIABLES.del_c, name="del_c", curie=THMO_VARIABLES.curie('del_c'),
                   model_uri=DEFAULT_.del_c, domain=None, range=Optional[Union[dict, VelocityCenterMassDifference]])

slots.del_E_kin = Slot(uri=THMO_VARIABLES.del_E_kin, name="del_E_kin", curie=THMO_VARIABLES.curie('del_E_kin'),
                   model_uri=DEFAULT_.del_E_kin, domain=None, range=Optional[Union[dict, KineticEnergyCenterMassDifference]])

slots.del_e_kin = Slot(uri=THMO_VARIABLES.del_e_kin, name="del_e_kin", curie=THMO_VARIABLES.curie('del_e_kin'),
                   model_uri=DEFAULT_.del_e_kin, domain=None, range=Optional[Union[dict, SpecificKineticEnergyCenterMassDifference]])

slots.del_E_pot = Slot(uri=THMO_VARIABLES.del_E_pot, name="del_E_pot", curie=THMO_VARIABLES.curie('del_E_pot'),
                   model_uri=DEFAULT_.del_E_pot, domain=None, range=Optional[Union[dict, PotentialEnergyCenterMassDifference]])

slots.del_e_pot = Slot(uri=THMO_VARIABLES.del_e_pot, name="del_e_pot", curie=THMO_VARIABLES.curie('del_e_pot'),
                   model_uri=DEFAULT_.del_e_pot, domain=None, range=Optional[Union[dict, SpecificPotentialEnergyCenterMassDifference]])

slots.T_const = Slot(uri=THMO_VARIABLES.T_const, name="T_const", curie=THMO_VARIABLES.curie('T_const'),
                   model_uri=DEFAULT_.T_const, domain=None, range=Optional[Union[bool, Bool]])

slots.n_poly = Slot(uri=THMO_VARIABLES.n_poly, name="n_poly", curie=THMO_VARIABLES.curie('n_poly'),
                   model_uri=DEFAULT_.n_poly, domain=None, range=Optional[Union[dict, PolytropicExponent]])

slots.ratio_T = Slot(uri=THMO_VARIABLES.ratio_T, name="ratio_T", curie=THMO_VARIABLES.curie('ratio_T'),
                   model_uri=DEFAULT_.ratio_T, domain=None, range=Optional[Union[dict, TemperatureRatio]])

slots.ratio_p = Slot(uri=THMO_VARIABLES.ratio_p, name="ratio_p", curie=THMO_VARIABLES.curie('ratio_p'),
                   model_uri=DEFAULT_.ratio_p, domain=None, range=Optional[Union[dict, PressureRatio]])

slots.ratio_v = Slot(uri=THMO_VARIABLES.ratio_v, name="ratio_v", curie=THMO_VARIABLES.curie('ratio_v'),
                   model_uri=DEFAULT_.ratio_v, domain=None, range=Optional[Union[dict, VolumeRatio]])

slots.equilibrium = Slot(uri=THMO_ATTRIBUTES.equilibrium, name="equilibrium", curie=THMO_ATTRIBUTES.curie('equilibrium'),
                   model_uri=DEFAULT_.equilibrium, domain=None, range=Optional[Union[bool, Bool]])

slots.closed = Slot(uri=THMO_ATTRIBUTES.closed, name="closed", curie=THMO_ATTRIBUTES.curie('closed'),
                   model_uri=DEFAULT_.closed, domain=None, range=Optional[Union[bool, Bool]])

slots.motion = Slot(uri=THMO_ATTRIBUTES.motion, name="motion", curie=THMO_ATTRIBUTES.curie('motion'),
                   model_uri=DEFAULT_.motion, domain=None, range=Optional[Union[bool, Bool]])

slots.homogeneous = Slot(uri=THMO_ATTRIBUTES.homogeneous, name="homogeneous", curie=THMO_ATTRIBUTES.curie('homogeneous'),
                   model_uri=DEFAULT_.homogeneous, domain=None, range=Optional[Union[bool, Bool]])

slots.pure = Slot(uri=THMO_ATTRIBUTES.pure, name="pure", curie=THMO_ATTRIBUTES.curie('pure'),
                   model_uri=DEFAULT_.pure, domain=None, range=Optional[Union[bool, Bool]])

slots.mixed = Slot(uri=THMO_ATTRIBUTES.mixed, name="mixed", curie=THMO_ATTRIBUTES.curie('mixed'),
                   model_uri=DEFAULT_.mixed, domain=None, range=Optional[Union[bool, Bool]])

slots.adiabatic = Slot(uri=THMO_ATTRIBUTES.adiabatic, name="adiabatic", curie=THMO_ATTRIBUTES.curie('adiabatic'),
                   model_uri=DEFAULT_.adiabatic, domain=None, range=Optional[Union[bool, Bool]])

slots.reversible = Slot(uri=THMO_ATTRIBUTES.reversible, name="reversible", curie=THMO_ATTRIBUTES.curie('reversible'),
                   model_uri=DEFAULT_.reversible, domain=None, range=Optional[Union[bool, Bool]])

slots.is_isothermal = Slot(uri=THMO_ATTRIBUTES.is_isothermal, name="is_isothermal", curie=THMO_ATTRIBUTES.curie('is_isothermal'),
                   model_uri=DEFAULT_.is_isothermal, domain=None, range=Optional[Union[bool, Bool]])

slots.is_isochoric = Slot(uri=THMO_ATTRIBUTES.is_isochoric, name="is_isochoric", curie=THMO_ATTRIBUTES.curie('is_isochoric'),
                   model_uri=DEFAULT_.is_isochoric, domain=None, range=Optional[Union[bool, Bool]])

slots.is_polytropic = Slot(uri=THMO_ATTRIBUTES.is_polytropic, name="is_polytropic", curie=THMO_ATTRIBUTES.curie('is_polytropic'),
                   model_uri=DEFAULT_.is_polytropic, domain=None, range=Optional[Union[bool, Bool]])

slots.is_isobaric = Slot(uri=THMO_ATTRIBUTES.is_isobaric, name="is_isobaric", curie=THMO_ATTRIBUTES.curie('is_isobaric'),
                   model_uri=DEFAULT_.is_isobaric, domain=None, range=Optional[Union[bool, Bool]])

slots.is_isenthalpic = Slot(uri=THMO_ATTRIBUTES.is_isenthalpic, name="is_isenthalpic", curie=THMO_ATTRIBUTES.curie('is_isenthalpic'),
                   model_uri=DEFAULT_.is_isenthalpic, domain=None, range=Optional[Union[bool, Bool]])

slots.is_isentropic = Slot(uri=THMO_ATTRIBUTES.is_isentropic, name="is_isentropic", curie=THMO_ATTRIBUTES.curie('is_isentropic'),
                   model_uri=DEFAULT_.is_isentropic, domain=None, range=Optional[Union[bool, Bool]])

slots.model = Slot(uri=THMO_ATTRIBUTES.model, name="model", curie=THMO_ATTRIBUTES.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.as_text = Slot(uri=THMO_EQUATIONS.as_text, name="as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.as_text, domain=None, range=Optional[str])

slots.related_variables = Slot(uri=THMO_EQUATIONS.related_variables, name="related_variables", curie=THMO_EQUATIONS.curie('related_variables'),
                   model_uri=DEFAULT_.related_variables, domain=None, range=Optional[Union[Union[dict, Variable], List[Union[dict, Variable]]]])

slots.system_id = Slot(uri=THMO_EQUATIONS.system_id, name="system_id", curie=THMO_EQUATIONS.curie('system_id'),
                   model_uri=DEFAULT_.system_id, domain=None, range=Optional[Union[str, SystemId]])

slots.change_of_state_id = Slot(uri=THMO_EQUATIONS.change_of_state_id, name="change_of_state_id", curie=THMO_EQUATIONS.curie('change_of_state_id'),
                   model_uri=DEFAULT_.change_of_state_id, domain=None, range=Optional[Union[str, ChangeOfStateId]])

slots.state_id = Slot(uri=THMO_EQUATIONS.state_id, name="state_id", curie=THMO_EQUATIONS.curie('state_id'),
                   model_uri=DEFAULT_.state_id, domain=None, range=Optional[Union[str, StateId]])

slots.material_id = Slot(uri=THMO_EQUATIONS.material_id, name="material_id", curie=THMO_EQUATIONS.curie('material_id'),
                   model_uri=DEFAULT_.material_id, domain=None, range=Optional[Union[str, PureMaterialId]])

slots.amount_of_substance_equation = Slot(uri=THMO_EQUATIONS.amount_of_substance_equation, name="amount_of_substance_equation", curie=THMO_EQUATIONS.curie('amount_of_substance_equation'),
                   model_uri=DEFAULT_.amount_of_substance_equation, domain=None, range=Optional[Union[str, AmountOfSubstanceEquationId]])

slots.specific_gas_constant_equation = Slot(uri=THMO_EQUATIONS.specific_gas_constant_equation, name="specific_gas_constant_equation", curie=THMO_EQUATIONS.curie('specific_gas_constant_equation'),
                   model_uri=DEFAULT_.specific_gas_constant_equation, domain=None, range=Optional[Union[str, SpecificGasConstantEquationId]])

slots.kappa_polytropic_exponent_equation = Slot(uri=THMO_EQUATIONS.kappa_polytropic_exponent_equation, name="kappa_polytropic_exponent_equation", curie=THMO_EQUATIONS.curie('kappa_polytropic_exponent_equation'),
                   model_uri=DEFAULT_.kappa_polytropic_exponent_equation, domain=None, range=Optional[Union[str, KappaPolytropicExponentEquationId]])

slots.caloric_equation_of_state_ideal_gas = Slot(uri=THMO_EQUATIONS.caloric_equation_of_state_ideal_gas, name="caloric_equation_of_state_ideal_gas", curie=THMO_EQUATIONS.curie('caloric_equation_of_state_ideal_gas'),
                   model_uri=DEFAULT_.caloric_equation_of_state_ideal_gas, domain=None, range=Optional[Union[str, CaloricEquationOfStateIdealGasId]])

slots.molar_heat_capacity_constant_pressure_equation = Slot(uri=THMO_EQUATIONS.molar_heat_capacity_constant_pressure_equation, name="molar_heat_capacity_constant_pressure_equation", curie=THMO_EQUATIONS.curie('molar_heat_capacity_constant_pressure_equation'),
                   model_uri=DEFAULT_.molar_heat_capacity_constant_pressure_equation, domain=None, range=Optional[Union[str, MolarHeatCapacityConstantPressureEquationId]])

slots.molar_heat_capacity_constant_volume_equation = Slot(uri=THMO_EQUATIONS.molar_heat_capacity_constant_volume_equation, name="molar_heat_capacity_constant_volume_equation", curie=THMO_EQUATIONS.curie('molar_heat_capacity_constant_volume_equation'),
                   model_uri=DEFAULT_.molar_heat_capacity_constant_volume_equation, domain=None, range=Optional[Union[str, MolarHeatCapacityConstantVolumeEquationId]])

slots.enthalpy_equation = Slot(uri=THMO_EQUATIONS.enthalpy_equation, name="enthalpy_equation", curie=THMO_EQUATIONS.curie('enthalpy_equation'),
                   model_uri=DEFAULT_.enthalpy_equation, domain=None, range=Optional[Union[str, EnthalpyEquationId]])

slots.specific_enthalpy_equation = Slot(uri=THMO_EQUATIONS.specific_enthalpy_equation, name="specific_enthalpy_equation", curie=THMO_EQUATIONS.curie('specific_enthalpy_equation'),
                   model_uri=DEFAULT_.specific_enthalpy_equation, domain=None, range=Optional[Union[str, SpecificEnthalpyEquationId]])

slots.thermal_density_equation = Slot(uri=THMO_EQUATIONS.thermal_density_equation, name="thermal_density_equation", curie=THMO_EQUATIONS.curie('thermal_density_equation'),
                   model_uri=DEFAULT_.thermal_density_equation, domain=None, range=Optional[Union[str, ThermalDensityEquationId]])

slots.polytropic_exponent_equation = Slot(uri=THMO_EQUATIONS.polytropic_exponent_equation, name="polytropic_exponent_equation", curie=THMO_EQUATIONS.curie('polytropic_exponent_equation'),
                   model_uri=DEFAULT_.polytropic_exponent_equation, domain=None, range=Optional[Union[str, PolytropicExponentEquationId]])

slots.work_on_internal_external_state_equation = Slot(uri=THMO_EQUATIONS.work_on_internal_external_state_equation, name="work_on_internal_external_state_equation", curie=THMO_EQUATIONS.curie('work_on_internal_external_state_equation'),
                   model_uri=DEFAULT_.work_on_internal_external_state_equation, domain=None, range=Optional[Union[str, WorkOnInternalExternalStateEquationId]])

slots.specific_work_on_internal_external_state_equation = Slot(uri=THMO_EQUATIONS.specific_work_on_internal_external_state_equation, name="specific_work_on_internal_external_state_equation", curie=THMO_EQUATIONS.curie('specific_work_on_internal_external_state_equation'),
                   model_uri=DEFAULT_.specific_work_on_internal_external_state_equation, domain=None, range=Optional[Union[str, SpecificWorkOnInternalExternalStateEquationId]])

slots.volume_stirring_electrical_work_equation = Slot(uri=THMO_EQUATIONS.volume_stirring_electrical_work_equation, name="volume_stirring_electrical_work_equation", curie=THMO_EQUATIONS.curie('volume_stirring_electrical_work_equation'),
                   model_uri=DEFAULT_.volume_stirring_electrical_work_equation, domain=None, range=Optional[Union[str, VolumeStirringElectricalWorkEquationId]])

slots.first_law = Slot(uri=THMO_EQUATIONS.first_law, name="first_law", curie=THMO_EQUATIONS.curie('first_law'),
                   model_uri=DEFAULT_.first_law, domain=None, range=Optional[Union[str, FirstLawId]])

slots.first_law_specific = Slot(uri=THMO_EQUATIONS.first_law_specific, name="first_law_specific", curie=THMO_EQUATIONS.curie('first_law_specific'),
                   model_uri=DEFAULT_.first_law_specific, domain=None, range=Optional[Union[str, FirstLawSpecificId]])

slots.technical_work_equation = Slot(uri=THMO_EQUATIONS.technical_work_equation, name="technical_work_equation", curie=THMO_EQUATIONS.curie('technical_work_equation'),
                   model_uri=DEFAULT_.technical_work_equation, domain=None, range=Optional[Union[str, TechnicalWorkEquationId]])

slots.work_on_external_state_equation = Slot(uri=THMO_EQUATIONS.work_on_external_state_equation, name="work_on_external_state_equation", curie=THMO_EQUATIONS.curie('work_on_external_state_equation'),
                   model_uri=DEFAULT_.work_on_external_state_equation, domain=None, range=Optional[Union[str, WorkOnExternalStateEquationId]])

slots.not_in_motion_del_c_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_c_equation, name="not_in_motion_del_c_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_c_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_c_equation, domain=None, range=Optional[Union[str, NotInMotionDelCEquationId]])

slots.not_in_motion_del_z_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_z_equation, name="not_in_motion_del_z_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_z_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_z_equation, domain=None, range=Optional[Union[str, NotInMotionDelZEquationId]])

slots.not_in_motion_del_E_kin_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_E_kin_equation, name="not_in_motion_del_E_kin_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_E_kin_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_E_kin_equation, domain=None, range=Optional[Union[str, NotInMotionDelEkinEquationId]])

slots.not_in_motion_del_e_kin_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_e_kin_equation, name="not_in_motion_del_e_kin_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_e_kin_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_e_kin_equation, domain=None, range=Optional[Union[str, NotInMotionDelekinEquationId]])

slots.not_in_motion_del_E_pot_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_E_pot_equation, name="not_in_motion_del_E_pot_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_E_pot_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_E_pot_equation, domain=None, range=Optional[Union[str, NotInMotionDelEpotEquationId]])

slots.not_in_motion_del_e_pot_equation = Slot(uri=THMO_EQUATIONS.not_in_motion_del_e_pot_equation, name="not_in_motion_del_e_pot_equation", curie=THMO_EQUATIONS.curie('not_in_motion_del_e_pot_equation'),
                   model_uri=DEFAULT_.not_in_motion_del_e_pot_equation, domain=None, range=Optional[Union[str, NotInMotionDelepotEquationId]])

slots.adiabatic_heat_equation = Slot(uri=THMO_EQUATIONS.adiabatic_heat_equation, name="adiabatic_heat_equation", curie=THMO_EQUATIONS.curie('adiabatic_heat_equation'),
                   model_uri=DEFAULT_.adiabatic_heat_equation, domain=None, range=Optional[Union[str, AdiabaticHeatEquationId]])

slots.adiabatic_specific_heat_equation = Slot(uri=THMO_EQUATIONS.adiabatic_specific_heat_equation, name="adiabatic_specific_heat_equation", curie=THMO_EQUATIONS.curie('adiabatic_specific_heat_equation'),
                   model_uri=DEFAULT_.adiabatic_specific_heat_equation, domain=None, range=Optional[Union[str, AdiabaticSpecificHeatEquationId]])

slots.isentropic_heat_equation = Slot(uri=THMO_EQUATIONS.isentropic_heat_equation, name="isentropic_heat_equation", curie=THMO_EQUATIONS.curie('isentropic_heat_equation'),
                   model_uri=DEFAULT_.isentropic_heat_equation, domain=None, range=Optional[Union[str, IsentropicHeatEquationId]])

slots.isentropic_entropy_equation = Slot(uri=THMO_EQUATIONS.isentropic_entropy_equation, name="isentropic_entropy_equation", curie=THMO_EQUATIONS.curie('isentropic_entropy_equation'),
                   model_uri=DEFAULT_.isentropic_entropy_equation, domain=None, range=Optional[Union[str, IsentropicEntropyEquationId]])

slots.isentropic_molar_entropy_equation = Slot(uri=THMO_EQUATIONS.isentropic_molar_entropy_equation, name="isentropic_molar_entropy_equation", curie=THMO_EQUATIONS.curie('isentropic_molar_entropy_equation'),
                   model_uri=DEFAULT_.isentropic_molar_entropy_equation, domain=None, range=Optional[Union[str, IsentropicMolarEntropyEquationId]])

slots.isobaric_properties = Slot(uri=THMO_EQUATIONS.isobaric_properties, name="isobaric_properties", curie=THMO_EQUATIONS.curie('isobaric_properties'),
                   model_uri=DEFAULT_.isobaric_properties, domain=None, range=Optional[Union[str, IsobaricPropertiesId]])

slots.isobaric_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isobaric_work_on_internal_state_equation, name="isobaric_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isobaric_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isobaric_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsobaricWorkOnInternalStateEquationId]])

slots.isobaric_specific_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isobaric_specific_work_on_internal_state_equation, name="isobaric_specific_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isobaric_specific_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isobaric_specific_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsobaricSpecificWorkOnInternalStateEquationId]])

slots.isothermal_properties = Slot(uri=THMO_EQUATIONS.isothermal_properties, name="isothermal_properties", curie=THMO_EQUATIONS.curie('isothermal_properties'),
                   model_uri=DEFAULT_.isothermal_properties, domain=None, range=Optional[Union[str, IsothermalPropertiesId]])

slots.isothermal_perfect_gas_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isothermal_perfect_gas_work_on_internal_state_equation, name="isothermal_perfect_gas_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isothermal_perfect_gas_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isothermal_perfect_gas_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsothermalPerfectGasWorkOnInternalStateEquationId]])

slots.isothermal_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isothermal_work_on_internal_state_equation, name="isothermal_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isothermal_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isothermal_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsothermalWorkOnInternalStateEquationId]])

slots.isochoric_volume_equation = Slot(uri=THMO_EQUATIONS.isochoric_volume_equation, name="isochoric_volume_equation", curie=THMO_EQUATIONS.curie('isochoric_volume_equation'),
                   model_uri=DEFAULT_.isochoric_volume_equation, domain=None, range=Optional[Union[str, IsochoricVolumeEquationId]])

slots.isochoric_specific_volume_equation = Slot(uri=THMO_EQUATIONS.isochoric_specific_volume_equation, name="isochoric_specific_volume_equation", curie=THMO_EQUATIONS.curie('isochoric_specific_volume_equation'),
                   model_uri=DEFAULT_.isochoric_specific_volume_equation, domain=None, range=Optional[Union[str, IsochoricSpecificVolumeEquationId]])

slots.isochoric_specific_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isochoric_specific_work_on_internal_state_equation, name="isochoric_specific_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isochoric_specific_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isochoric_specific_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsochoricSpecificWorkOnInternalStateEquationId]])

slots.isochoric_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.isochoric_work_on_internal_state_equation, name="isochoric_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('isochoric_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.isochoric_work_on_internal_state_equation, domain=None, range=Optional[Union[str, IsochoricWorkOnInternalStateEquationId]])

slots.isochoric_technical_work_equation = Slot(uri=THMO_EQUATIONS.isochoric_technical_work_equation, name="isochoric_technical_work_equation", curie=THMO_EQUATIONS.curie('isochoric_technical_work_equation'),
                   model_uri=DEFAULT_.isochoric_technical_work_equation, domain=None, range=Optional[Union[str, IsochoricTechnicalWorkEquationId]])

slots.del_T_equation = Slot(uri=THMO_EQUATIONS.del_T_equation, name="del_T_equation", curie=THMO_EQUATIONS.curie('del_T_equation'),
                   model_uri=DEFAULT_.del_T_equation, domain=None, range=Optional[Union[str, DelTEquationId]])

slots.del_p_equation = Slot(uri=THMO_EQUATIONS.del_p_equation, name="del_p_equation", curie=THMO_EQUATIONS.curie('del_p_equation'),
                   model_uri=DEFAULT_.del_p_equation, domain=None, range=Optional[Union[str, DelPEquationId]])

slots.del_V_equation = Slot(uri=THMO_EQUATIONS.del_V_equation, name="del_V_equation", curie=THMO_EQUATIONS.curie('del_V_equation'),
                   model_uri=DEFAULT_.del_V_equation, domain=None, range=Optional[Union[str, DelVEquationId]])

slots.del_v_equation = Slot(uri=THMO_EQUATIONS.del_v_equation, name="del_v_equation", curie=THMO_EQUATIONS.curie('del_v_equation'),
                   model_uri=DEFAULT_.del_v_equation, domain=None, range=Optional[Union[str, DelvEquationId]])

slots.del_U_equation = Slot(uri=THMO_EQUATIONS.del_U_equation, name="del_U_equation", curie=THMO_EQUATIONS.curie('del_U_equation'),
                   model_uri=DEFAULT_.del_U_equation, domain=None, range=Optional[Union[str, DelUEquationId]])

slots.del_u_equation = Slot(uri=THMO_EQUATIONS.del_u_equation, name="del_u_equation", curie=THMO_EQUATIONS.curie('del_u_equation'),
                   model_uri=DEFAULT_.del_u_equation, domain=None, range=Optional[Union[str, DeluEquationId]])

slots.del_H_equation = Slot(uri=THMO_EQUATIONS.del_H_equation, name="del_H_equation", curie=THMO_EQUATIONS.curie('del_H_equation'),
                   model_uri=DEFAULT_.del_H_equation, domain=None, range=Optional[Union[str, DelHEquationId]])

slots.del_h_equation = Slot(uri=THMO_EQUATIONS.del_h_equation, name="del_h_equation", curie=THMO_EQUATIONS.curie('del_h_equation'),
                   model_uri=DEFAULT_.del_h_equation, domain=None, range=Optional[Union[str, DelhEquationId]])

slots.del_S_equation = Slot(uri=THMO_EQUATIONS.del_S_equation, name="del_S_equation", curie=THMO_EQUATIONS.curie('del_S_equation'),
                   model_uri=DEFAULT_.del_S_equation, domain=None, range=Optional[Union[str, DelSEquationId]])

slots.del_s_equation = Slot(uri=THMO_EQUATIONS.del_s_equation, name="del_s_equation", curie=THMO_EQUATIONS.curie('del_s_equation'),
                   model_uri=DEFAULT_.del_s_equation, domain=None, range=Optional[Union[str, DelsEquationId]])

slots.del_sm_equation = Slot(uri=THMO_EQUATIONS.del_sm_equation, name="del_sm_equation", curie=THMO_EQUATIONS.curie('del_sm_equation'),
                   model_uri=DEFAULT_.del_sm_equation, domain=None, range=Optional[Union[str, DelsmEquationId]])

slots.del_c_equation = Slot(uri=THMO_EQUATIONS.del_c_equation, name="del_c_equation", curie=THMO_EQUATIONS.curie('del_c_equation'),
                   model_uri=DEFAULT_.del_c_equation, domain=None, range=Optional[Union[str, DelCEquationId]])

slots.del_z_equation = Slot(uri=THMO_EQUATIONS.del_z_equation, name="del_z_equation", curie=THMO_EQUATIONS.curie('del_z_equation'),
                   model_uri=DEFAULT_.del_z_equation, domain=None, range=Optional[Union[str, DelZEquationId]])

slots.del_E_Kin_equation = Slot(uri=THMO_EQUATIONS.del_E_Kin_equation, name="del_E_Kin_equation", curie=THMO_EQUATIONS.curie('del_E_Kin_equation'),
                   model_uri=DEFAULT_.del_E_Kin_equation, domain=None, range=Optional[Union[str, DelEKinEquationId]])

slots.del_E_Pot_equation = Slot(uri=THMO_EQUATIONS.del_E_Pot_equation, name="del_E_Pot_equation", curie=THMO_EQUATIONS.curie('del_E_Pot_equation'),
                   model_uri=DEFAULT_.del_E_Pot_equation, domain=None, range=Optional[Union[str, DelEPotEquationId]])

slots.del_e_Kin_equation = Slot(uri=THMO_EQUATIONS.del_e_Kin_equation, name="del_e_Kin_equation", curie=THMO_EQUATIONS.curie('del_e_Kin_equation'),
                   model_uri=DEFAULT_.del_e_Kin_equation, domain=None, range=Optional[Union[str, DeleKinEquationId]])

slots.del_e_Pot_equation = Slot(uri=THMO_EQUATIONS.del_e_Pot_equation, name="del_e_Pot_equation", curie=THMO_EQUATIONS.curie('del_e_Pot_equation'),
                   model_uri=DEFAULT_.del_e_Pot_equation, domain=None, range=Optional[Union[str, DelePotEquationId]])

slots.ratio_volume_equation = Slot(uri=THMO_EQUATIONS.ratio_volume_equation, name="ratio_volume_equation", curie=THMO_EQUATIONS.curie('ratio_volume_equation'),
                   model_uri=DEFAULT_.ratio_volume_equation, domain=None, range=Optional[Union[str, RatioVolumeEquationId]])

slots.ratio_temperature_equation = Slot(uri=THMO_EQUATIONS.ratio_temperature_equation, name="ratio_temperature_equation", curie=THMO_EQUATIONS.curie('ratio_temperature_equation'),
                   model_uri=DEFAULT_.ratio_temperature_equation, domain=None, range=Optional[Union[str, RatioTemperatureEquationId]])

slots.ratio_pressure_equation = Slot(uri=THMO_EQUATIONS.ratio_pressure_equation, name="ratio_pressure_equation", curie=THMO_EQUATIONS.curie('ratio_pressure_equation'),
                   model_uri=DEFAULT_.ratio_pressure_equation, domain=None, range=Optional[Union[str, RatioPressureEquationId]])

slots.specific_state_variable_v_equation = Slot(uri=THMO_EQUATIONS.specific_state_variable_v_equation, name="specific_state_variable_v_equation", curie=THMO_EQUATIONS.curie('specific_state_variable_v_equation'),
                   model_uri=DEFAULT_.specific_state_variable_v_equation, domain=None, range=Optional[Union[str, SpecificStateVariableVEquationId]])

slots.specific_state_variable_u_equation = Slot(uri=THMO_EQUATIONS.specific_state_variable_u_equation, name="specific_state_variable_u_equation", curie=THMO_EQUATIONS.curie('specific_state_variable_u_equation'),
                   model_uri=DEFAULT_.specific_state_variable_u_equation, domain=None, range=Optional[Union[str, SpecificStateVariableUEquationId]])

slots.specific_state_variable_h_equation = Slot(uri=THMO_EQUATIONS.specific_state_variable_h_equation, name="specific_state_variable_h_equation", curie=THMO_EQUATIONS.curie('specific_state_variable_h_equation'),
                   model_uri=DEFAULT_.specific_state_variable_h_equation, domain=None, range=Optional[Union[str, SpecificStateVariableHEquationId]])

slots.specific_state_variable_s_equation = Slot(uri=THMO_EQUATIONS.specific_state_variable_s_equation, name="specific_state_variable_s_equation", curie=THMO_EQUATIONS.curie('specific_state_variable_s_equation'),
                   model_uri=DEFAULT_.specific_state_variable_s_equation, domain=None, range=Optional[Union[str, SpecificStateVariableSEquationId]])

slots.molar_state_variable_s_equation = Slot(uri=THMO_EQUATIONS.molar_state_variable_s_equation, name="molar_state_variable_s_equation", curie=THMO_EQUATIONS.curie('molar_state_variable_s_equation'),
                   model_uri=DEFAULT_.molar_state_variable_s_equation, domain=None, range=Optional[Union[str, MolarStateVariableSEquationId]])

slots.specific_kinetic_energy_center_mass_equation = Slot(uri=THMO_EQUATIONS.specific_kinetic_energy_center_mass_equation, name="specific_kinetic_energy_center_mass_equation", curie=THMO_EQUATIONS.curie('specific_kinetic_energy_center_mass_equation'),
                   model_uri=DEFAULT_.specific_kinetic_energy_center_mass_equation, domain=None, range=Optional[Union[str, SpecificKineticEnergyCenterMassEquationId]])

slots.specific_potential_energy_center_mass_equation = Slot(uri=THMO_EQUATIONS.specific_potential_energy_center_mass_equation, name="specific_potential_energy_center_mass_equation", curie=THMO_EQUATIONS.curie('specific_potential_energy_center_mass_equation'),
                   model_uri=DEFAULT_.specific_potential_energy_center_mass_equation, domain=None, range=Optional[Union[str, SpecificPotentialEnergyCenterMassEquationId]])

slots.specific_density_equation = Slot(uri=THMO_EQUATIONS.specific_density_equation, name="specific_density_equation", curie=THMO_EQUATIONS.curie('specific_density_equation'),
                   model_uri=DEFAULT_.specific_density_equation, domain=None, range=Optional[Union[str, SpecificDensityEquationId]])

slots.ideal_gas_law = Slot(uri=THMO_EQUATIONS.ideal_gas_law, name="ideal_gas_law", curie=THMO_EQUATIONS.curie('ideal_gas_law'),
                   model_uri=DEFAULT_.ideal_gas_law, domain=None, range=Optional[Union[str, IdealGasLawId]])

slots.specific_ideal_gas_law = Slot(uri=THMO_EQUATIONS.specific_ideal_gas_law, name="specific_ideal_gas_law", curie=THMO_EQUATIONS.curie('specific_ideal_gas_law'),
                   model_uri=DEFAULT_.specific_ideal_gas_law, domain=None, range=Optional[Union[str, SpecificIdealGasLawId]])

slots.ideal_gas_law_amount_of_substance = Slot(uri=THMO_EQUATIONS.ideal_gas_law_amount_of_substance, name="ideal_gas_law_amount_of_substance", curie=THMO_EQUATIONS.curie('ideal_gas_law_amount_of_substance'),
                   model_uri=DEFAULT_.ideal_gas_law_amount_of_substance, domain=None, range=Optional[Union[str, IdealGasLawAmountOfSubstanceId]])

slots.internal_energy_equation = Slot(uri=THMO_EQUATIONS.internal_energy_equation, name="internal_energy_equation", curie=THMO_EQUATIONS.curie('internal_energy_equation'),
                   model_uri=DEFAULT_.internal_energy_equation, domain=None, range=Optional[Union[str, InternalEnergyEquationId]])

slots.specific_volume_density_equation = Slot(uri=THMO_EQUATIONS.specific_volume_density_equation, name="specific_volume_density_equation", curie=THMO_EQUATIONS.curie('specific_volume_density_equation'),
                   model_uri=DEFAULT_.specific_volume_density_equation, domain=None, range=Optional[Union[str, SpecificVolumeDensityEquationId]])

slots.specific_heat_transfer_equation = Slot(uri=THMO_EQUATIONS.specific_heat_transfer_equation, name="specific_heat_transfer_equation", curie=THMO_EQUATIONS.curie('specific_heat_transfer_equation'),
                   model_uri=DEFAULT_.specific_heat_transfer_equation, domain=None, range=Optional[Union[str, SpecificHeatTransferEquationId]])

slots.specific_work_transfer_equation = Slot(uri=THMO_EQUATIONS.specific_work_transfer_equation, name="specific_work_transfer_equation", curie=THMO_EQUATIONS.curie('specific_work_transfer_equation'),
                   model_uri=DEFAULT_.specific_work_transfer_equation, domain=None, range=Optional[Union[str, SpecificWorkTransferEquationId]])

slots.specific_work_on_internal_state_equation = Slot(uri=THMO_EQUATIONS.specific_work_on_internal_state_equation, name="specific_work_on_internal_state_equation", curie=THMO_EQUATIONS.curie('specific_work_on_internal_state_equation'),
                   model_uri=DEFAULT_.specific_work_on_internal_state_equation, domain=None, range=Optional[Union[str, SpecificWorkOnInternalStateEquationId]])

slots.specific_work_on_external_state_equation = Slot(uri=THMO_EQUATIONS.specific_work_on_external_state_equation, name="specific_work_on_external_state_equation", curie=THMO_EQUATIONS.curie('specific_work_on_external_state_equation'),
                   model_uri=DEFAULT_.specific_work_on_external_state_equation, domain=None, range=Optional[Union[str, SpecificWorkOnExternalStateEquationId]])

slots.specific_volume_change_work_equation = Slot(uri=THMO_EQUATIONS.specific_volume_change_work_equation, name="specific_volume_change_work_equation", curie=THMO_EQUATIONS.curie('specific_volume_change_work_equation'),
                   model_uri=DEFAULT_.specific_volume_change_work_equation, domain=None, range=Optional[Union[str, SpecificVolumeChangeWorkEquationId]])

slots.specific_stirring_work_equation = Slot(uri=THMO_EQUATIONS.specific_stirring_work_equation, name="specific_stirring_work_equation", curie=THMO_EQUATIONS.curie('specific_stirring_work_equation'),
                   model_uri=DEFAULT_.specific_stirring_work_equation, domain=None, range=Optional[Union[str, SpecificStirringWorkEquationId]])

slots.specific_electrical_work_equation = Slot(uri=THMO_EQUATIONS.specific_electrical_work_equation, name="specific_electrical_work_equation", curie=THMO_EQUATIONS.curie('specific_electrical_work_equation'),
                   model_uri=DEFAULT_.specific_electrical_work_equation, domain=None, range=Optional[Union[str, SpecificElectricalWorkEquationId]])

slots.ideal_gas_polytropic_change_of_state_equation = Slot(uri=THMO_EQUATIONS.ideal_gas_polytropic_change_of_state_equation, name="ideal_gas_polytropic_change_of_state_equation", curie=THMO_EQUATIONS.curie('ideal_gas_polytropic_change_of_state_equation'),
                   model_uri=DEFAULT_.ideal_gas_polytropic_change_of_state_equation, domain=None, range=Optional[Union[str, IdealGasPolytropicChangeOfStateEquationId]])

slots.ideal_gas_polytropic_change_of_state_equationII = Slot(uri=THMO_EQUATIONS.ideal_gas_polytropic_change_of_state_equationII, name="ideal_gas_polytropic_change_of_state_equationII", curie=THMO_EQUATIONS.curie('ideal_gas_polytropic_change_of_state_equationII'),
                   model_uri=DEFAULT_.ideal_gas_polytropic_change_of_state_equationII, domain=None, range=Optional[Union[str, IdealGasPolytropicChangeOfStateEquationIIId]])

slots.polytropic_work_equation = Slot(uri=THMO_EQUATIONS.polytropic_work_equation, name="polytropic_work_equation", curie=THMO_EQUATIONS.curie('polytropic_work_equation'),
                   model_uri=DEFAULT_.polytropic_work_equation, domain=None, range=Optional[Union[str, PolytropicWorkEquationId]])

slots.isentropic_perfect_gas_polytropic_exponent_equation = Slot(uri=THMO_EQUATIONS.isentropic_perfect_gas_polytropic_exponent_equation, name="isentropic_perfect_gas_polytropic_exponent_equation", curie=THMO_EQUATIONS.curie('isentropic_perfect_gas_polytropic_exponent_equation'),
                   model_uri=DEFAULT_.isentropic_perfect_gas_polytropic_exponent_equation, domain=None, range=Optional[Union[str, IsentropicPerfectGasPolytropicExponentEquationId]])

slots.isentropic_perfect_gas_work_equation = Slot(uri=THMO_EQUATIONS.isentropic_perfect_gas_work_equation, name="isentropic_perfect_gas_work_equation", curie=THMO_EQUATIONS.curie('isentropic_perfect_gas_work_equation'),
                   model_uri=DEFAULT_.isentropic_perfect_gas_work_equation, domain=None, range=Optional[Union[str, IsentropicPerfectGasWorkEquationId]])

slots.isentropic_perfect_gas_temperature_equation = Slot(uri=THMO_EQUATIONS.isentropic_perfect_gas_temperature_equation, name="isentropic_perfect_gas_temperature_equation", curie=THMO_EQUATIONS.curie('isentropic_perfect_gas_temperature_equation'),
                   model_uri=DEFAULT_.isentropic_perfect_gas_temperature_equation, domain=None, range=Optional[Union[str, IsentropicPerfectGasTemperatureEquationId]])

slots.isobaric_perfect_gas_heat_equation = Slot(uri=THMO_EQUATIONS.isobaric_perfect_gas_heat_equation, name="isobaric_perfect_gas_heat_equation", curie=THMO_EQUATIONS.curie('isobaric_perfect_gas_heat_equation'),
                   model_uri=DEFAULT_.isobaric_perfect_gas_heat_equation, domain=None, range=Optional[Union[str, IsobaricPerfectGasHeatEquationId]])

slots.isobaric_polytropic_exponent_equation = Slot(uri=THMO_EQUATIONS.isobaric_polytropic_exponent_equation, name="isobaric_polytropic_exponent_equation", curie=THMO_EQUATIONS.curie('isobaric_polytropic_exponent_equation'),
                   model_uri=DEFAULT_.isobaric_polytropic_exponent_equation, domain=None, range=Optional[Union[str, IsobaricPolytropicExponentEquationId]])

slots.isothermal_ideal_gas_pressure_volume_ratio = Slot(uri=THMO_EQUATIONS.isothermal_ideal_gas_pressure_volume_ratio, name="isothermal_ideal_gas_pressure_volume_ratio", curie=THMO_EQUATIONS.curie('isothermal_ideal_gas_pressure_volume_ratio'),
                   model_uri=DEFAULT_.isothermal_ideal_gas_pressure_volume_ratio, domain=None, range=Optional[Union[str, IsothermalIdealGasPressureVolumeRatioId]])

slots.isothermal_ideal_gas_work_equation = Slot(uri=THMO_EQUATIONS.isothermal_ideal_gas_work_equation, name="isothermal_ideal_gas_work_equation", curie=THMO_EQUATIONS.curie('isothermal_ideal_gas_work_equation'),
                   model_uri=DEFAULT_.isothermal_ideal_gas_work_equation, domain=None, range=Optional[Union[str, IsothermalIdealGasWorkEquationId]])

slots.isothermal_ideal_gas_work_equation_II = Slot(uri=THMO_EQUATIONS.isothermal_ideal_gas_work_equation_II, name="isothermal_ideal_gas_work_equation_II", curie=THMO_EQUATIONS.curie('isothermal_ideal_gas_work_equation_II'),
                   model_uri=DEFAULT_.isothermal_ideal_gas_work_equation_II, domain=None, range=Optional[Union[str, IsothermalIdealGasWorkEquationIIId]])

slots.isothermal_ideal_gas_polytropic_exponent_equation = Slot(uri=THMO_EQUATIONS.isothermal_ideal_gas_polytropic_exponent_equation, name="isothermal_ideal_gas_polytropic_exponent_equation", curie=THMO_EQUATIONS.curie('isothermal_ideal_gas_polytropic_exponent_equation'),
                   model_uri=DEFAULT_.isothermal_ideal_gas_polytropic_exponent_equation, domain=None, range=Optional[Union[str, IsothermalIdealGasPolytropicExponentEquationId]])

slots.isothermal_perfect_gas_entropy_equation = Slot(uri=THMO_EQUATIONS.isothermal_perfect_gas_entropy_equation, name="isothermal_perfect_gas_entropy_equation", curie=THMO_EQUATIONS.curie('isothermal_perfect_gas_entropy_equation'),
                   model_uri=DEFAULT_.isothermal_perfect_gas_entropy_equation, domain=None, range=Optional[Union[str, IsothermalPerfectGasEntropyEquationId]])

slots.isochoric_ideal_gas_pressure_temperature_ratio = Slot(uri=THMO_EQUATIONS.isochoric_ideal_gas_pressure_temperature_ratio, name="isochoric_ideal_gas_pressure_temperature_ratio", curie=THMO_EQUATIONS.curie('isochoric_ideal_gas_pressure_temperature_ratio'),
                   model_uri=DEFAULT_.isochoric_ideal_gas_pressure_temperature_ratio, domain=None, range=Optional[Union[str, IsochoricIdealGasPressureTemperatureRatioId]])

slots.del_H_perfect_gas_equation = Slot(uri=THMO_EQUATIONS.del_H_perfect_gas_equation, name="del_H_perfect_gas_equation", curie=THMO_EQUATIONS.curie('del_H_perfect_gas_equation'),
                   model_uri=DEFAULT_.del_H_perfect_gas_equation, domain=None, range=Optional[Union[str, DelHPerfectGasEquationId]])

slots.del_U_perfect_gas_equation = Slot(uri=THMO_EQUATIONS.del_U_perfect_gas_equation, name="del_U_perfect_gas_equation", curie=THMO_EQUATIONS.curie('del_U_perfect_gas_equation'),
                   model_uri=DEFAULT_.del_U_perfect_gas_equation, domain=None, range=Optional[Union[str, DelUPerfectGasEquationId]])

slots.del_S_perfect_gas_volume_equation = Slot(uri=THMO_EQUATIONS.del_S_perfect_gas_volume_equation, name="del_S_perfect_gas_volume_equation", curie=THMO_EQUATIONS.curie('del_S_perfect_gas_volume_equation'),
                   model_uri=DEFAULT_.del_S_perfect_gas_volume_equation, domain=None, range=Optional[Union[str, DelSPerfectGasVolumeEquationId]])

slots.del_S_perfect_gas_volume_equation_ii = Slot(uri=THMO_EQUATIONS.del_S_perfect_gas_volume_equation_ii, name="del_S_perfect_gas_volume_equation_ii", curie=THMO_EQUATIONS.curie('del_S_perfect_gas_volume_equation_ii'),
                   model_uri=DEFAULT_.del_S_perfect_gas_volume_equation_ii, domain=None, range=Optional[Union[str, DelSPerfectGasVolumeEquationIIId]])

slots.satisfied = Slot(uri=THMO_RULES.satisfied, name="satisfied", curie=THMO_RULES.curie('satisfied'),
                   model_uri=DEFAULT_.satisfied, domain=None, range=Optional[Union[bool, Bool]])

slots.required_variables = Slot(uri=THMO_PROBLEMS.required_variables, name="required_variables", curie=THMO_PROBLEMS.curie('required_variables'),
                   model_uri=DEFAULT_.required_variables, domain=None, range=Union[str, List[str]])

slots.additional_equations = Slot(uri=THMO_PROBLEMS.additional_equations, name="additional_equations", curie=THMO_PROBLEMS.curie('additional_equations'),
                   model_uri=DEFAULT_.additional_equations, domain=None, range=Optional[Union[str, List[str]]])

slots.problem_class = Slot(uri=THMO_PROBLEMS.problem_class, name="problem_class", curie=THMO_PROBLEMS.curie('problem_class'),
                   model_uri=DEFAULT_.problem_class, domain=None, range=str)

slots.pureMaterial = Slot(uri=THMO_PROBLEMS.pureMaterial, name="pureMaterial", curie=THMO_PROBLEMS.curie('pureMaterial'),
                   model_uri=DEFAULT_.pureMaterial, domain=None, range=Optional[Union[dict, PureMaterial]])

slots.states = Slot(uri=THMO_PROBLEMS.states, name="states", curie=THMO_PROBLEMS.curie('states'),
                   model_uri=DEFAULT_.states, domain=None, range=Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]])

slots.change_of_states = Slot(uri=THMO_PROBLEMS.change_of_states, name="change_of_states", curie=THMO_PROBLEMS.curie('change_of_states'),
                   model_uri=DEFAULT_.change_of_states, domain=None, range=Union[Dict[Union[str, ChangeOfStateId], Union[dict, ChangeOfState]], List[Union[dict, ChangeOfState]]])

slots.valid_problem = Slot(uri=THMO_PROBLEMS.valid_problem, name="valid_problem", curie=THMO_PROBLEMS.curie('valid_problem'),
                   model_uri=DEFAULT_.valid_problem, domain=None, range=Optional[Union[bool, Bool]])

slots.invalid_problem = Slot(uri=THMO_PROBLEMS.invalid_problem, name="invalid_problem", curie=THMO_PROBLEMS.curie('invalid_problem'),
                   model_uri=DEFAULT_.invalid_problem, domain=None, range=Optional[Union[bool, Bool]])

slots.variable__id = Slot(uri=THMO_VARIABLES.Variable_id, name="variable__id", curie=THMO_VARIABLES.curie('Variable_id'),
                   model_uri=DEFAULT_.variable__id, domain=None, range=Optional[str])

slots.System_equilibrium = Slot(uri=THMO_ATTRIBUTES.equilibrium, name="System_equilibrium", curie=THMO_ATTRIBUTES.curie('equilibrium'),
                   model_uri=DEFAULT_.System_equilibrium, domain=System, range=Optional[Union[bool, Bool]])

slots.PureMaterial_homogeneous = Slot(uri=THMO_ATTRIBUTES.homogeneous, name="PureMaterial_homogeneous", curie=THMO_ATTRIBUTES.curie('homogeneous'),
                   model_uri=DEFAULT_.PureMaterial_homogeneous, domain=PureMaterial, range=Optional[Union[bool, Bool]])

slots.PureMaterial_pure = Slot(uri=THMO_ATTRIBUTES.pure, name="PureMaterial_pure", curie=THMO_ATTRIBUTES.curie('pure'),
                   model_uri=DEFAULT_.PureMaterial_pure, domain=PureMaterial, range=Optional[Union[bool, Bool]])

slots.Mixture_mixed = Slot(uri=THMO_ATTRIBUTES.mixed, name="Mixture_mixed", curie=THMO_ATTRIBUTES.curie('mixed'),
                   model_uri=DEFAULT_.Mixture_mixed, domain=Mixture, range=Optional[Union[bool, Bool]])

slots.State_equilibrium = Slot(uri=THMO_ATTRIBUTES.equilibrium, name="State_equilibrium", curie=THMO_ATTRIBUTES.curie('equilibrium'),
                   model_uri=DEFAULT_.State_equilibrium, domain=State, range=Optional[Union[bool, Bool]])

slots.StandardTemperature_value = Slot(uri=THMO_VARIABLES.value, name="StandardTemperature_value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.StandardTemperature_value, domain=StandardTemperature, range=Optional[float])

slots.StandardPressure_value = Slot(uri=THMO_VARIABLES.value, name="StandardPressure_value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.StandardPressure_value, domain=StandardPressure, range=Optional[float])

slots.UniversalGasConstant_value = Slot(uri=THMO_VARIABLES.value, name="UniversalGasConstant_value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.UniversalGasConstant_value, domain=UniversalGasConstant, range=Optional[float])

slots.GravitationalAcceleration_value = Slot(uri=THMO_VARIABLES.value, name="GravitationalAcceleration_value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.GravitationalAcceleration_value, domain=GravitationalAcceleration, range=Optional[float])

slots.WorkOnExternalState_value = Slot(uri=THMO_VARIABLES.value, name="WorkOnExternalState_value", curie=THMO_VARIABLES.curie('value'),
                   model_uri=DEFAULT_.WorkOnExternalState_value, domain=WorkOnExternalState, range=Optional[float])

slots.SecondLawAdiabaticIrreversible_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SecondLawAdiabaticIrreversible_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SecondLawAdiabaticIrreversible_as_text, domain=SecondLawAdiabaticIrreversible, range=Optional[str])

slots.AmountOfSubstanceEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="AmountOfSubstanceEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.AmountOfSubstanceEquation_as_text, domain=AmountOfSubstanceEquation, range=Optional[str])

slots.MolarHeatCapacityConstantPressureEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="MolarHeatCapacityConstantPressureEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.MolarHeatCapacityConstantPressureEquation_as_text, domain=MolarHeatCapacityConstantPressureEquation, range=Optional[str])

slots.MolarHeatCapacityConstantVolumeEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="MolarHeatCapacityConstantVolumeEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.MolarHeatCapacityConstantVolumeEquation_as_text, domain=MolarHeatCapacityConstantVolumeEquation, range=Optional[str])

slots.KappaPolytropicExponentEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="KappaPolytropicExponentEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.KappaPolytropicExponentEquation_as_text, domain=KappaPolytropicExponentEquation, range=Optional[str])

slots.CaloricEquationOfStateIdealGas_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="CaloricEquationOfStateIdealGas_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.CaloricEquationOfStateIdealGas_as_text, domain=CaloricEquationOfStateIdealGas, range=Optional[str])

slots.SpecificGasConstantEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificGasConstantEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificGasConstantEquation_as_text, domain=SpecificGasConstantEquation, range=Optional[str])

slots.EnthalpyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="EnthalpyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.EnthalpyEquation_as_text, domain=EnthalpyEquation, range=Optional[str])

slots.SpecificEnthalpyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificEnthalpyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificEnthalpyEquation_as_text, domain=SpecificEnthalpyEquation, range=Optional[str])

slots.ThermalDensityEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="ThermalDensityEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.ThermalDensityEquation_as_text, domain=ThermalDensityEquation, range=Optional[str])

slots.SpecificStateVariableVEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificStateVariableVEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificStateVariableVEquation_as_text, domain=SpecificStateVariableVEquation, range=Optional[str])

slots.SpecificStateVariableUEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificStateVariableUEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificStateVariableUEquation_as_text, domain=SpecificStateVariableUEquation, range=Optional[str])

slots.SpecificStateVariableHEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificStateVariableHEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificStateVariableHEquation_as_text, domain=SpecificStateVariableHEquation, range=Optional[str])

slots.SpecificStateVariableSEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificStateVariableSEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificStateVariableSEquation_as_text, domain=SpecificStateVariableSEquation, range=Optional[str])

slots.MolarStateVariableSEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="MolarStateVariableSEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.MolarStateVariableSEquation_as_text, domain=MolarStateVariableSEquation, range=Optional[str])

slots.SpecificKineticEnergyCenterMassEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificKineticEnergyCenterMassEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificKineticEnergyCenterMassEquation_as_text, domain=SpecificKineticEnergyCenterMassEquation, range=Optional[str])

slots.SpecificPotentialEnergyCenterMassEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificPotentialEnergyCenterMassEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificPotentialEnergyCenterMassEquation_as_text, domain=SpecificPotentialEnergyCenterMassEquation, range=Optional[str])

slots.SpecificDensityEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificDensityEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificDensityEquation_as_text, domain=SpecificDensityEquation, range=Optional[str])

slots.IdealGasLaw_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IdealGasLaw_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IdealGasLaw_as_text, domain=IdealGasLaw, range=Optional[str])

slots.SpecificIdealGasLaw_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificIdealGasLaw_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificIdealGasLaw_as_text, domain=SpecificIdealGasLaw, range=Optional[str])

slots.IdealGasLawAmountOfSubstance_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IdealGasLawAmountOfSubstance_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IdealGasLawAmountOfSubstance_as_text, domain=IdealGasLawAmountOfSubstance, range=Optional[str])

slots.SpecificVolumeDensityEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificVolumeDensityEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificVolumeDensityEquation_as_text, domain=SpecificVolumeDensityEquation, range=Optional[str])

slots.InternalEnergyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="InternalEnergyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.InternalEnergyEquation_as_text, domain=InternalEnergyEquation, range=Optional[str])

slots.DelTEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelTEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelTEquation_as_text, domain=DelTEquation, range=Optional[str])

slots.DelPEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelPEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelPEquation_as_text, domain=DelPEquation, range=Optional[str])

slots.DelVEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelVEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelVEquation_as_text, domain=DelVEquation, range=Optional[str])

slots.DelvEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelvEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelvEquation_as_text, domain=DelvEquation, range=Optional[str])

slots.DelUEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelUEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelUEquation_as_text, domain=DelUEquation, range=Optional[str])

slots.DeluEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DeluEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DeluEquation_as_text, domain=DeluEquation, range=Optional[str])

slots.DelHEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelHEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelHEquation_as_text, domain=DelHEquation, range=Optional[str])

slots.DelhEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelhEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelhEquation_as_text, domain=DelhEquation, range=Optional[str])

slots.DelSEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelSEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelSEquation_as_text, domain=DelSEquation, range=Optional[str])

slots.DelsEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelsEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelsEquation_as_text, domain=DelsEquation, range=Optional[str])

slots.DelsmEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelsmEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelsmEquation_as_text, domain=DelsmEquation, range=Optional[str])

slots.DelCEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelCEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelCEquation_as_text, domain=DelCEquation, range=Optional[str])

slots.DelZEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelZEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelZEquation_as_text, domain=DelZEquation, range=Optional[str])

slots.DelEKinEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelEKinEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelEKinEquation_as_text, domain=DelEKinEquation, range=Optional[str])

slots.DelEPotEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelEPotEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelEPotEquation_as_text, domain=DelEPotEquation, range=Optional[str])

slots.DeleKinEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DeleKinEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DeleKinEquation_as_text, domain=DeleKinEquation, range=Optional[str])

slots.DelePotEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelePotEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelePotEquation_as_text, domain=DelePotEquation, range=Optional[str])

slots.PolytropicExponentEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="PolytropicExponentEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.PolytropicExponentEquation_as_text, domain=PolytropicExponentEquation, range=Optional[str])

slots.WorkOnInternalExternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="WorkOnInternalExternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.WorkOnInternalExternalStateEquation_as_text, domain=WorkOnInternalExternalStateEquation, range=Optional[str])

slots.SpecificWorkOnInternalExternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificWorkOnInternalExternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificWorkOnInternalExternalStateEquation_as_text, domain=SpecificWorkOnInternalExternalStateEquation, range=Optional[str])

slots.VolumeStirringElectricalWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="VolumeStirringElectricalWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.VolumeStirringElectricalWorkEquation_as_text, domain=VolumeStirringElectricalWorkEquation, range=Optional[str])

slots.FirstLaw_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="FirstLaw_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.FirstLaw_as_text, domain=FirstLaw, range=Optional[str])

slots.FirstLawSpecific_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="FirstLawSpecific_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.FirstLawSpecific_as_text, domain=FirstLawSpecific, range=Optional[str])

slots.TechnicalWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="TechnicalWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.TechnicalWorkEquation_as_text, domain=TechnicalWorkEquation, range=Optional[str])

slots.WorkOnExternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="WorkOnExternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.WorkOnExternalStateEquation_as_text, domain=WorkOnExternalStateEquation, range=Optional[str])

slots.RatioVolumeEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="RatioVolumeEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.RatioVolumeEquation_as_text, domain=RatioVolumeEquation, range=Optional[str])

slots.RatioTemperatureEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="RatioTemperatureEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.RatioTemperatureEquation_as_text, domain=RatioTemperatureEquation, range=Optional[str])

slots.RatioPressureEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="RatioPressureEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.RatioPressureEquation_as_text, domain=RatioPressureEquation, range=Optional[str])

slots.SpecificHeatTransferEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificHeatTransferEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificHeatTransferEquation_as_text, domain=SpecificHeatTransferEquation, range=Optional[str])

slots.SpecificWorkTransferEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificWorkTransferEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificWorkTransferEquation_as_text, domain=SpecificWorkTransferEquation, range=Optional[str])

slots.SpecificWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificWorkOnInternalStateEquation_as_text, domain=SpecificWorkOnInternalStateEquation, range=Optional[str])

slots.SpecificWorkOnExternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificWorkOnExternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificWorkOnExternalStateEquation_as_text, domain=SpecificWorkOnExternalStateEquation, range=Optional[str])

slots.SpecificVolumeChangeWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificVolumeChangeWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificVolumeChangeWorkEquation_as_text, domain=SpecificVolumeChangeWorkEquation, range=Optional[str])

slots.SpecificStirringWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificStirringWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificStirringWorkEquation_as_text, domain=SpecificStirringWorkEquation, range=Optional[str])

slots.SpecificElectricalWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="SpecificElectricalWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.SpecificElectricalWorkEquation_as_text, domain=SpecificElectricalWorkEquation, range=Optional[str])

slots.DelHPerfectGasEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelHPerfectGasEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelHPerfectGasEquation_as_text, domain=DelHPerfectGasEquation, range=Optional[str])

slots.DelUPerfectGasEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelUPerfectGasEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelUPerfectGasEquation_as_text, domain=DelUPerfectGasEquation, range=Optional[str])

slots.DelSPerfectGasVolumeEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelSPerfectGasVolumeEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelSPerfectGasVolumeEquation_as_text, domain=DelSPerfectGasVolumeEquation, range=Optional[str])

slots.DelSPerfectGasVolumeEquationII_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="DelSPerfectGasVolumeEquationII_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.DelSPerfectGasVolumeEquationII_as_text, domain=DelSPerfectGasVolumeEquationII, range=Optional[str])

slots.IsochoricVolumeEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricVolumeEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricVolumeEquation_as_text, domain=IsochoricVolumeEquation, range=Optional[str])

slots.IsochoricSpecificVolumeEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricSpecificVolumeEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricSpecificVolumeEquation_as_text, domain=IsochoricSpecificVolumeEquation, range=Optional[str])

slots.IsochoricSpecificWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricSpecificWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricSpecificWorkOnInternalStateEquation_as_text, domain=IsochoricSpecificWorkOnInternalStateEquation, range=Optional[str])

slots.IsochoricWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricWorkOnInternalStateEquation_as_text, domain=IsochoricWorkOnInternalStateEquation, range=Optional[str])

slots.IsochoricTechnicalWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricTechnicalWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricTechnicalWorkEquation_as_text, domain=IsochoricTechnicalWorkEquation, range=Optional[str])

slots.IsochoricIdealGasPressureTemperatureRatio_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsochoricIdealGasPressureTemperatureRatio_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsochoricIdealGasPressureTemperatureRatio_as_text, domain=IsochoricIdealGasPressureTemperatureRatio, range=Optional[str])

slots.IsothermalProperties_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalProperties_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalProperties_as_text, domain=IsothermalProperties, range=Optional[str])

slots.IsothermalWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalWorkOnInternalStateEquation_as_text, domain=IsothermalWorkOnInternalStateEquation, range=Optional[str])

slots.IsothermalIdealGasPressureVolumeRatio_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalIdealGasPressureVolumeRatio_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalIdealGasPressureVolumeRatio_as_text, domain=IsothermalIdealGasPressureVolumeRatio, range=Optional[str])

slots.IsothermalIdealGasWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalIdealGasWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalIdealGasWorkEquation_as_text, domain=IsothermalIdealGasWorkEquation, range=Optional[str])

slots.IsothermalIdealGasWorkEquationII_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalIdealGasWorkEquationII_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalIdealGasWorkEquationII_as_text, domain=IsothermalIdealGasWorkEquationII, range=Optional[str])

slots.IsothermalIdealGasPolytropicExponentEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalIdealGasPolytropicExponentEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalIdealGasPolytropicExponentEquation_as_text, domain=IsothermalIdealGasPolytropicExponentEquation, range=Optional[str])

slots.IsothermalPerfectGasEntropyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalPerfectGasEntropyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalPerfectGasEntropyEquation_as_text, domain=IsothermalPerfectGasEntropyEquation, range=Optional[str])

slots.IsothermalPerfectGasWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsothermalPerfectGasWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsothermalPerfectGasWorkOnInternalStateEquation_as_text, domain=IsothermalPerfectGasWorkOnInternalStateEquation, range=Optional[str])

slots.IsobaricProperties_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsobaricProperties_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsobaricProperties_as_text, domain=IsobaricProperties, range=Optional[str])

slots.IsobaricWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsobaricWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsobaricWorkOnInternalStateEquation_as_text, domain=IsobaricWorkOnInternalStateEquation, range=Optional[str])

slots.IsobaricSpecificWorkOnInternalStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsobaricSpecificWorkOnInternalStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsobaricSpecificWorkOnInternalStateEquation_as_text, domain=IsobaricSpecificWorkOnInternalStateEquation, range=Optional[str])

slots.IsobaricPolytropicExponentEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsobaricPolytropicExponentEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsobaricPolytropicExponentEquation_as_text, domain=IsobaricPolytropicExponentEquation, range=Optional[str])

slots.IsobaricPerfectGasHeatEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsobaricPerfectGasHeatEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsobaricPerfectGasHeatEquation_as_text, domain=IsobaricPerfectGasHeatEquation, range=Optional[str])

slots.AdiabaticHeatEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="AdiabaticHeatEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.AdiabaticHeatEquation_as_text, domain=AdiabaticHeatEquation, range=Optional[str])

slots.AdiabaticSpecificHeatEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="AdiabaticSpecificHeatEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.AdiabaticSpecificHeatEquation_as_text, domain=AdiabaticSpecificHeatEquation, range=Optional[str])

slots.IsentropicHeatEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicHeatEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicHeatEquation_as_text, domain=IsentropicHeatEquation, range=Optional[str])

slots.IsentropicEntropyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicEntropyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicEntropyEquation_as_text, domain=IsentropicEntropyEquation, range=Optional[str])

slots.IsentropicMolarEntropyEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicMolarEntropyEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicMolarEntropyEquation_as_text, domain=IsentropicMolarEntropyEquation, range=Optional[str])

slots.IsentropicPerfectGasPolytropicExponentEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicPerfectGasPolytropicExponentEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicPerfectGasPolytropicExponentEquation_as_text, domain=IsentropicPerfectGasPolytropicExponentEquation, range=Optional[str])

slots.IsentropicPerfectGasTechnicalWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicPerfectGasTechnicalWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicPerfectGasTechnicalWorkEquation_as_text, domain=IsentropicPerfectGasTechnicalWorkEquation, range=Optional[str])

slots.IsentropicPerfectGasWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicPerfectGasWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicPerfectGasWorkEquation_as_text, domain=IsentropicPerfectGasWorkEquation, range=Optional[str])

slots.IsentropicPerfectGasTemperatureEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IsentropicPerfectGasTemperatureEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IsentropicPerfectGasTemperatureEquation_as_text, domain=IsentropicPerfectGasTemperatureEquation, range=Optional[str])

slots.PolytropicWorkEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="PolytropicWorkEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.PolytropicWorkEquation_as_text, domain=PolytropicWorkEquation, range=Optional[str])

slots.IdealGasPolytropicChangeOfStateEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IdealGasPolytropicChangeOfStateEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IdealGasPolytropicChangeOfStateEquation_as_text, domain=IdealGasPolytropicChangeOfStateEquation, range=Optional[str])

slots.IdealGasPolytropicChangeOfStateEquationII_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="IdealGasPolytropicChangeOfStateEquationII_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.IdealGasPolytropicChangeOfStateEquationII_as_text, domain=IdealGasPolytropicChangeOfStateEquationII, range=Optional[str])

slots.NotInMotionDelCEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelCEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelCEquation_as_text, domain=NotInMotionDelCEquation, range=Optional[str])

slots.NotInMotionDelZEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelZEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelZEquation_as_text, domain=NotInMotionDelZEquation, range=Optional[str])

slots.NotInMotionDelEkinEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelEkinEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelEkinEquation_as_text, domain=NotInMotionDelEkinEquation, range=Optional[str])

slots.NotInMotionDelekinEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelekinEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelekinEquation_as_text, domain=NotInMotionDelekinEquation, range=Optional[str])

slots.NotInMotionDelEpotEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelEpotEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelEpotEquation_as_text, domain=NotInMotionDelEpotEquation, range=Optional[str])

slots.NotInMotionDelepotEquation_as_text = Slot(uri=THMO_EQUATIONS.as_text, name="NotInMotionDelepotEquation_as_text", curie=THMO_EQUATIONS.curie('as_text'),
                   model_uri=DEFAULT_.NotInMotionDelepotEquation_as_text, domain=NotInMotionDelepotEquation, range=Optional[str])

slots.SystemProblem_system = Slot(uri=THMO_CONCEPTS.system, name="SystemProblem_system", curie=THMO_CONCEPTS.curie('system'),
                   model_uri=DEFAULT_.SystemProblem_system, domain=SystemProblem, range=Union[dict, System])

slots.Equilibrium_state = Slot(uri=THMO_CONCEPTS.state, name="Equilibrium_state", curie=THMO_CONCEPTS.curie('state'),
                   model_uri=DEFAULT_.Equilibrium_state, domain=Equilibrium, range=Union[dict, State])

slots.SingleStep_states = Slot(uri=THMO_PROBLEMS.states, name="SingleStep_states", curie=THMO_PROBLEMS.curie('states'),
                   model_uri=DEFAULT_.SingleStep_states, domain=SingleStep, range=Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]])

slots.SingleStep_change_of_state = Slot(uri=THMO_CONCEPTS.change_of_state, name="SingleStep_change_of_state", curie=THMO_CONCEPTS.curie('change_of_state'),
                   model_uri=DEFAULT_.SingleStep_change_of_state, domain=SingleStep, range=Union[dict, ChangeOfState])

slots.SingleStep_valid_problem = Slot(uri=THMO_PROBLEMS.valid_problem, name="SingleStep_valid_problem", curie=THMO_PROBLEMS.curie('valid_problem'),
                   model_uri=DEFAULT_.SingleStep_valid_problem, domain=SingleStep, range=Optional[Union[bool, Bool]])

slots.SequentialSteps_states = Slot(uri=THMO_PROBLEMS.states, name="SequentialSteps_states", curie=THMO_PROBLEMS.curie('states'),
                   model_uri=DEFAULT_.SequentialSteps_states, domain=SequentialSteps, range=Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]])

slots.SequentialSteps_change_of_states = Slot(uri=THMO_PROBLEMS.change_of_states, name="SequentialSteps_change_of_states", curie=THMO_PROBLEMS.curie('change_of_states'),
                   model_uri=DEFAULT_.SequentialSteps_change_of_states, domain=SequentialSteps, range=Union[Dict[Union[str, ChangeOfStateId], Union[dict, ChangeOfState]], List[Union[dict, ChangeOfState]]])

slots.SequentialSteps_valid_problem = Slot(uri=THMO_PROBLEMS.valid_problem, name="SequentialSteps_valid_problem", curie=THMO_PROBLEMS.curie('valid_problem'),
                   model_uri=DEFAULT_.SequentialSteps_valid_problem, domain=SequentialSteps, range=Optional[Union[bool, Bool]])

slots.CyclicProcess_states = Slot(uri=THMO_PROBLEMS.states, name="CyclicProcess_states", curie=THMO_PROBLEMS.curie('states'),
                   model_uri=DEFAULT_.CyclicProcess_states, domain=CyclicProcess, range=Union[Dict[Union[str, StateId], Union[dict, State]], List[Union[dict, State]]])

slots.CyclicProcess_change_of_states = Slot(uri=THMO_PROBLEMS.change_of_states, name="CyclicProcess_change_of_states", curie=THMO_PROBLEMS.curie('change_of_states'),
                   model_uri=DEFAULT_.CyclicProcess_change_of_states, domain=CyclicProcess, range=Union[Dict[Union[str, ChangeOfStateId], Union[dict, ChangeOfState]], List[Union[dict, ChangeOfState]]])

slots.CyclicProcess_valid_problem = Slot(uri=THMO_PROBLEMS.valid_problem, name="CyclicProcess_valid_problem", curie=THMO_PROBLEMS.curie('valid_problem'),
                   model_uri=DEFAULT_.CyclicProcess_valid_problem, domain=CyclicProcess, range=Optional[Union[bool, Bool]])
