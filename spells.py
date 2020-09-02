from adventurelib import when
import cfg 

class Spell:
    def __init__(self, name, description, typ, chance,mc):
        self.name=name
        self.description=description
        self.typ=typ
        self.chance=chance
        self.mc=mc

    
    def cast_spell(self, target, caster):
        print(caster+ "casts "+self.name)
            
class DamageSpell:
    def __init__(self, min_damage,max_damage, *args):
        self.min_damage=min_damage
        self.max_damage=max_damage
        super().__init__(*args)
    
    def cast_spell(self, target, damage):
        None
        #TODO

spells=dict()
spells["fireball"]=DamageSpell(0,1,)

@when('cast SPELL',context='combat')
def casting(spell):
    if spell in spells:
        spells[spell].cast_spell(cfg.Enemy,cfg.Player)
    else:
         print("Invalid casting instructions.")


