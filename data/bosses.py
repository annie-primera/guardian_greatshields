from models import Boss, DamageType


ALL_BOSSES = {
    "Gladius, Beast of Night": Boss(
        name="Gladius, Beast of Night",
        damage_type=DamageType.fire_damage,
        weak_against=None,
    ),
    "Adel, Baron of Night": Boss(
        name="Adel, Baron of Night",
        damage_type=DamageType.lightning_damage,
        weak_against=None,
    ),
    "Gnoster, Wisdom of Night": Boss(
        name="Gnoster, Wisdom of Night",
        damage_type=DamageType.magic_damage,
        weak_against=None,
    ),
    "Caligo, Miasma of Night": Boss(
        name="Caligo, Miasma of Night",
        damage_type=DamageType.magic_damage,
        weak_against=None,
    ),
    "Maris, Fathom of Night": Boss(
        name="Maris, Fathom of Night",
        damage_type=DamageType.magic_damage,
        weak_against=None,
    ),
    "Libra, Creature of Night": Boss(
        name="Libra, Creature of Night",
        damage_type=DamageType.holy_damage,
        weak_against=None,
    ),
    "Fulghor, Champion of Nightglow": Boss(
        name="Fulghor, Champion of Nightglow",
        damage_type=DamageType.holy_damage,
        weak_against=None,
    ),
    "Heolstor, the Nightlord": Boss(
        name="Heolstor, the Nightlord",
        damage_type=DamageType.magic_damage,
        weak_against=None,
    ),
    "Weapon-bequeathed Harmonia": Boss(
        name="Weapon-bequeathed Harmonia",
        damage_type=DamageType.physical_damage,
        weak_against=None,
    ),
    "Traitorous Straaghess": Boss(
        name="Traitorous Straaghess",
        damage_type=DamageType.physical_damage,
        weak_against=None,
    ),
}