from enum import Enum

from pydantic import BaseModel


class DamageType(Enum):
    fire_damage = "fire damage"
    lightning_damage = "lightning damage"
    holy_damage = "holy damage"
    magic_damage = "magic damage"
    physical_damage = "physical damage"


class StatusEffect(Enum):
    poison = "poison"
    sleep = "sleep"
    frost = "frost"
    bleed = "bleed"
    madness = "madness"
    scarlet_rot = "scarlet rot"
    none = "none"
    all_of_them = "ALL OF THEM"


class Shield(BaseModel):
    name: str
    magic_damage: int
    fire_damage: int
    lightning_damage: int
    holy_damage: int
    physical_damage: int = 100
    guard_boost: int


class Boss(BaseModel):
    name: str
    damage_type: DamageType
    status_effect: StatusEffect
    weak_against: StatusEffect | DamageType
    fire_negation: int
    magic_negation: int
    lightning_negation: int
    holy_negation: int
    strike_resistance: int
    slash_resistance: int
    pierce_resistance: int
