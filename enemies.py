from colorama import Fore,Style
import random
import math
class Enemy():
    def __init__(self, name, level, exp, gold, MaxHP, MaxMP, VIT, INT, MIND, FORCE, abilities, loot):
        self.name=name
        self.level=level
        self.exp=exp
        self.gold=gold
        self.default_HP=MaxHP
        self.HP=MaxHP
        self.MaxMP=MaxMP
        self.MP=MaxMP
        self.VIT=VIT
        self.INT=INT
        self.MIND=MIND
        self.FORCE=FORCE
        self.abilities=abilities
        self.loot=loot
        self.MaxHP=self.default_HP
        self.randomize_stats()
    
    def show_stats(self):
        print("")
        print("lvl {} ".format(self.level)+self.name)
        print("HP: {}-{}".format(math.floor(self.default_HP*0.8),math.ceil(self.default_HP*1.2))+"  MP: {}-{}".format(math.floor(self.MaxMP*0.8),math.ceil(self.MaxMP*1.2)))
        print("VIT : {}  INT : {}  MIND: {}  FORCE : {}".format(self.VIT,self.INT,self.MIND,self.FORCE))
        print("TODO abbilities")
        print("TODO loot chances")

    def heal(self, value):
        old_HP=self.HP
        self.HP+=value
        if self.HP>self.MaxHP:
            self.HP=self.MaxHP
        print("{} got healed for".format(self.name)+Fore.GREEN+" {} HP".format(self.HP-old_HP)+Style.RESET_ALL)


    def die(self):
        random_death=random.randint(0,1)
        if random_death==0:
            print("{} is DEAD.".format(self.name))
        else:
            print("R.I.P {}".format(self.name))
        print("Expirience gained: "+Fore.LIGHTWHITE_EX+"{}".format(self.exp)+Style.RESET_ALL)
        return [self.exp,self.gold,self.loot]

    def take_damage(self, value):
        self.HP-=value
        if self.HP>0:
            self.show_health()
            return
        self.die()
    

    def show_health(self):
        if self.HP>int(0.95*self.MaxHP):
            print("{} is making fun of your damage.".format(self.name))
            return
        if self.HP>int(0.85*self.MaxHP):
            print("{} is totally fine.".format(self.name))
            return
        if self.HP>int(0.6*self.MaxHP):
            print("{} is lightly damaged.".format(self.name))
            return
        if self.HP>int(0.4*self.MaxHP):
            print("{} is about half dead.".format(self.name))
            return
        if self.HP>int(0.2*self.MaxHP):
            print("{} is gravely wounded.".format(self.name))
            return
        if self.HP>1:
            print("{} is one foot in grave.".format(self.name))
            return
        if self.HP==1:
            print("{} has literally ".format(self.name)+Fore.RED+"1 HP "+Style.RESET_ALL+"left.")
            return
    

    def handle_combat(self):
        pass


    def randomize_stats(self):
        self.MaxHP=random.randint(math.floor(self.default_HP*0.8),math.ceil(self.default_HP*1.2))
        self.HP=self.MaxHP



slime=Enemy("slime",1,5,3,8,0,0,0,0,0,[],[])
slime.show_stats()
slime.take_damage(8)
slime.heal(5)