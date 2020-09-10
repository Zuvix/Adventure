import cfg
from colorama import init, Fore, Back, Style


class Player:
    def __init__(self, name,spells,items):
        self.name=name
        self.exp=0
        self.level=1
       
        self.inventory_size=cfg.default_inventory_size=8
        self.items=items
        self.MaxHP=cfg.start_life
        self.MaxMP=cfg.start_mana
        self.HP=self.MaxHP
        self.MP=self.MaxMP
        self.VIT=cfg.start_VIT
        self.INT=cfg.start_INT
        self.MIND=cfg.start_MIND
        self.FORCE=cfg.start_FORCE
       
        self.spell_cast_chance=cfg.default_spell_cast_chance
        self.spells=spells

    def update_stat(self,stat_name,change):
        if stat_name.lower()=="vit":
            self.MaxHP+=cfg.HP_per_lvl*change
            self.VIT+=change
            self.inventory_size+=cfg.inventory_per_lvl*change
            print("Your Vitality was changed by {}".format(change))
            print("Max HP is now {}".format(self.MaxHP))
            print("Inventory size is now {}".format(self.inventory_size))
        if stat_name.lower()=="int":
            self.INT+=change
            print("Your Inteligence was changed by {}".format(change))
        if stat_name.lower()=="mind":
            self.spell_cast_chance+=cfg.spell_cast_per_lvl*change
            self.MaxMP+=cfg.MP_per_lvl
            self.MIND+=change
            print("Your Mind was changed by {}".format(change))
            print("Max MP is now {}".format(self.MaxMP))
        if stat_name.lower()=="force":
            self.FORCE+=change
            print("Your Force was changed by {}".format(change))


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
            self.update_stat("vit",1)
        if inp.lower()=="int":
            self.update_stat("int",1)
        if inp.lower()=="mind":
            self.update_stat("mind",1)
        if inp.lower()=="force":
            self.update_stat("force",1)
        print("")

    def die(self):
        print("""

▓██   ██▓ ▒█████   █    ██  ██▀███       ██████ ▄▄▄█████▓ ▒█████   ██▀███  ▓██   ██▓    ██▓  ██████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒   ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒ ▒██  ██▒   ▓██▒▒██    ▒    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒   ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒  ▒██ ██░   ▒██▒░ ▓██▄      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░▒██▀▀█▄       ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄    ░ ▐██▓░   ░██░  ▒   ██▒   ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
  ░ ██▒▓░░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒   ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒  ░ ██▒▓░   ░██░▒██████▒▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ██▒▒▒    ░▓  ▒ ▒▓▒ ▒ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░ ▓██ ░▒░     ▒ ░░ ░▒  ░ ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░    ░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░  ▒ ▒ ░░      ▒ ░░  ░  ░     ░ ░ ░ ▒       ░░     ░     ░░   ░ 
 ░ ░         ░ ░     ░        ░              ░               ░ ░     ░      ░ ░         ░        ░         ░ ░        ░     ░  ░   ░     
 ░ ░                                                                        ░ ░                                      ░                   

 """)
    def take_damage(self,damage):
        self.HP-=damage
        print("You lose "+Fore.RED+"{} HP".format(damage)+Style.RESET_ALL+", you have"+Fore.RED+" {}/{} HP".format(self.HP,self.MaxHP)+Style.RESET_ALL)
        if self.HP<=0:
            self.die()
    def heal(self, heal):
        to_heal=heal
        if self.HP+heal>self.MaxHP:
            to_heal=self.MaxHP-self.HP
        self.HP+=to_heal
        if to_heal>0: 
            print("You are healed for "+Fore.GREEN+"{} HP".format(to_heal)+Style.RESET_ALL+", you have {}/{} HP".format(self.HP,self.MaxHP))
        else:
            print("You can't heal, if you are at MAX HP.")
    