from enum import Enum

from pydantic import BaseModel


class DamageType(Enum):
    fire_damage = "fire damage"
    lightning_damage = "lightning damage"
    holy_damage = "holy damage"
    magic_damage = "magic damage"
    physical_damage = "physical damage"


class Shield(BaseModel):
    name: str
    magic_damage: int
    fire_damage: int
    lightning_damage: int
    holy_damage: int
    guard_boost: int


class Boss(BaseModel):
    name: str
    damage_type: DamageType
    weak_against: DamageType | None
