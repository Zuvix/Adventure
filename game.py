from adventurelib import start, when,set_context
import adventurelib
import dice,cfg
from colorama import init, Fore, Back, Style
import descriptions
import Players,spells_logic
Enemy=None
#print("Who are you?")
#hero_name=input("")
player=Players.Player("hero_name",["rock throw","firebolt"],[])
init(convert=True)
print(descriptions.intro)

#Global commands
@when("help")
def h():
    adventurelib.help()

@when("show SOMETHING")
def show(something):
    x=something
    if x=="":
        print("Use this command to learn information about the game elements.")
        print("as SOMETHING you can type:")
        print("spells - to get complete information about the spells you control.")
        print("stats - shows your stats and what they mean.")
    if x=="spells":
        for spell in player.spells:
             spells_logic.spells[spell].describe()
    if x=="stats":
        print("VIT : {}  INT : {}  MIND: {}  FORCE : {}".format(player.VIT,player.INT,player.MIND,player.FORCE))
@when('cast SPELL',context="combat")
def casting(spell):
    if spell in player.spells:
        if spell in spells_logic.spells:
            spells_logic.spells[spell].cast_spell(player,player)
    else:
        print("Invalid casting instructions.")



#set_context("combat")
start(help=False)
