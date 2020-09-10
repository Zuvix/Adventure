from adventurelib import when,say
import cfg,Players,dice
from colorama import Fore,Style,Back

def color_spell_name(typ,name):
    special_name=name
    if typ=="offensive" or typ=="RED":
        special_name=Fore.LIGHTRED_EX+name+Style.RESET_ALL
    elif typ=="protective" or typ=="GREEN":
        special_name=Fore.GREEN+name+Style.RESET_ALL
    elif typ=="curse" or typ=="MAGENTA":
        special_name=Fore.MAGENTA+name+Style.RESET_ALL
    elif typ=="trick"or typ=="BLUE":
        special_name=Fore.BLUE+name+Style.RESET_ALL
    return special_name

spells=dict()
class Spell:
    def __init__(self, name, description, typ ,gold_cost, rarity, concentration,mc,magic_function):
        self.name=name
        self.description=description
        self.typ=typ
        self.concentration=concentration
        self.gold_cost=gold_cost
        self.rarity=rarity
        self.mc=mc
        self.magic_function=magic_function
    
    def describe(self):
        print("")
        print(color_spell_name(self.typ,self.name))
        print("Type = {},".format(self.typ)+Fore.BLUE+" MP = {},".format(self.mc)+Style.RESET_ALL+" Concentration = {}, Rarity = {}".format(self.concentration,self.rarity))
        print(self.description)

    def cast_spell(self, target, caster):
        print("")
        special_name=color_spell_name(self.typ,self.name)   
        print(caster.name+ " tries to cast "+special_name)
        if isinstance(caster,Players.Player):
            if caster.MP>=self.mc:
                caster.MP-=self.mc
                print("pays: ".format(caster.name)+Fore.BLUE+"{} MP".format(self.mc)+Style.RESET_ALL+" mana left:"+Fore.BLUE+" {}/{} MP".format(caster.MP,caster.MaxMP)+Style.RESET_ALL)
                #print("Required concentration for spell = {}".format(self.concentration))
                result=dice.roll(20,1,show_result=False)
                if result+caster.MIND>=self.concentration:
                    print(Fore.LIGHTGREEN_EX+"Succes, concentration {} is >= {}".format(result+caster.MIND,self.concentration)+Style.RESET_ALL)
                    self.magic_function(caster,target,self.name)
                else:
                    print(Fore.LIGHTRED_EX+"Failure, concentration {} is < {}".format(result+caster.MIND,self.concentration)+Style.RESET_ALL)

#Magic Functions for spells                
magic_functions={}

def rock_throw(caster,target,spell_name):
    damage=1+int(caster.level/2)
    print("{} deals 1 + {} (lvl/2) = {} dmg to {}".format(spell_name,int(caster.level/2),damage,target.name))
    target.take_damage(damage)
magic_functions["rock throw"]=rock_throw

def fire_bolt(caster,target,spell_name):
    dice_count=int(caster.FORCE/3)
    if isinstance(caster,Players.Player):
        damage=dice.roll(6,1,show_result=True)
        damage+=dice.roll(4,dice_count,show_result=True)
    else:
        damage=dice.roll(6,1,show_result=False)
        damage+=dice.roll(4,dice_count,show_result=False)
    print("{} deals {} dmg to {}".format(spell_name,damage,target.name))
    target.take_damage(damage)
magic_functions["firebolt"]=fire_bolt

#Generate Spells From Cfg
for magic in cfg.spell_stats:
    x=cfg.spell_stats[magic]
    new_spell=Spell(x.spell_name,x.description,x.typ,x.gold_cost,x.rarity,x.concentration,x.mc,magic_functions[x.spell_name])
    spells[x.spell_name]=new_spell


