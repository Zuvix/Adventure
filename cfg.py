from typing import NamedTuple
Enemy = None
Player = None

#Stats
start_life=20
start_mana=30


start_VIT=0
start_INT=0
start_MIND=0
start_FORCE=5

HP_per_lvl=4
MP_per_lvl=4
MP_reg_lvl=0.5
HP_reg_lvl=0.5
default_inventory_size=8
inventory_per_lvl=2
default_spell_cast_chance=0
spell_cast_per_lvl=1

class Magic(NamedTuple):
    spell_name: str
    mc: int
    typ: str
    rarity: str
    gold_cost:int
    concentration: int
    magic_attributes: dict

spell_stats={}
#Magic(name="",mc=0,typ="",rarity="",gold_cost=0,concentration=0,magic_attributes={})

#Rock Throw
spell_stats["rock throw"]=Magic(
    spell_name="rock throw",
    mc=0,
    typ="offensive",
    rarity="none",
    gold_cost=0,
    concentration=5,
    magic_attributes={"flat_dmg":{"dmg": 3,"scaling": 2}}
)