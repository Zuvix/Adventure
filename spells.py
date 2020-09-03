from adventurelib import when
import cfg,Players,dice
from colorama import Fore,Style

spells=dict()
class Spell:
    def __init__(self, name, description, typ ,gold_cost, rarity, concentration,mc, magic_attributes,magic_functions):
        self.name=name
        self.description=description
        self.typ=typ
        self.concentration=concentration
        self.gold_cost=gold_cost
        self.rarity=rarity
        self.mc=mc
        self.magic_attributes=magic_attributes
        self.magic_functions=magic_functions
    
    def cast_spell(self, target, caster):
        print("")
        print(caster.name+ " casts "+Style.DIM+self.name+Style.RESET_ALL)
        if isinstance(caster,Players.Player):
            if caster.MP>self.mc:
                caster.MP-=self.mc
                print("You pay "+Fore.CYAN+"{} MP".format(self.mc)+Style.RESET_ALL+" you have"+Fore.CYAN+" {}/{} MP".format(caster.MP,caster.MaxMP)+Style.RESET_ALL+ " left")
                print("Required concentration for spell = {}".format(self.concentration))
                result=dice.roll(20,1,show_result=False)
                if result>=self.concentration:
                    print(Fore.LIGHTGREEN_EX+"Casting succesful, you concentration was: {} + {} (MIND) = {}".format(result,caster.MIND,result+caster.MIND)+Style.RESET_ALL)
                    for x in self.magic_functions:
                        x(caster,target,self.name)
                else:
                    print(Fore.LIGHTRED_EX+"Failure, your concentration was too low: {} + {} (MIND) = {}".format(result,caster.MIND,result+caster.MIND)+Style.RESET_ALL)
                
def deal_flat_damage(caster,target,spell_name):
    damage=spells[spell_name]. magic_attributes["flat_dmg"]["dmg"]
    if spells[spell_name]. magic_attributes["flat_dmg"]["scaling"]:
        scaling=spells[spell_name]. magic_attributes["flat_dmg"]["scaling"]
        scaled_dmg=damage+scaling*caster.FORCE
        print("{} deals {} + {} x {} (FORCE) = {} dmg to {}".format(spell_name,damage,scaling,caster.FORCE,scaled_dmg,target.name))
        target.take_damage(damage)
    else:
        print("{} deals {} dmg to {}".format(spell_name,damage,target.name))
        target.take_damage(damage)


#Generate Spells From Cfg
for magic in cfg.spell_stats:
    x=cfg.spell_stats[magic]
    new_spell=Spell(x.spell_name,"",x.typ,x.gold_cost,x.rarity,x.concentration,x.mc,x.magic_attributes,[])
    for atr in x.magic_attributes:
        if atr=="flat_dmg":
            new_spell.magic_functions.append(deal_flat_damage)
    spells[x.spell_name]=new_spell


#player=Players.Player("Zuvo",[],[])
#spells["Rock Throw"].cast_spell(player,player)




