import spells
import cfg
class Player:
    def __init__(self, name, inventory,HP,MP,VIT,INT,MIND,FORCE,spells):
        self.name=name
        self.exp=0
        self.level=1
        self.HP=HP
        self.MP=MP
        self.VIT=VIT
        self.INT=INT
        self.MIND=MIND
        self.FORCE=FORCE
        self.spells=spells

    def levelup(self):
        print("LEVEL UP!")
        self.level+=1
        print("Now you are level {}".format(self.level))
        print("Your stats: VIT {} INT {} MIND {} FORCE {}".format(self.VIT,self.INT,self.MIND,self.FORCE))
        print("Type one of the stats to upgrade")
        print("VIT, INT, MIND, FORCE")
        inp=input("")
        while inp.lower()!="vit" and inp.lower()!="int" and inp.lower()!="mind" and inp.lower()!="force":
            print("Type one of the stats!")
            print("VIT, INT, MIND, FORCE")
            inp=input("")
        if inp.lower()=="vit":
            self.VIT+=1
            print("Vitality increased, your maximum life is increased by {}".format(cfg.HP_per_lvl))
        if inp.lower()=="int":
            self.INT+=1
            print("Inteligence increased")
        if inp.lower()=="mind":
            self.MIND+=1
            print("Mind stat increased")
        if inp.lower()=="FORCE":
            self.FORCE+=1
            print("FORCE increased")
        print("")