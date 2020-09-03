from adventurelib import start, when
import adventurelib
import dice,cfg
from colorama import init, Fore, Back, Style
import descriptions
import Players,spells
Enemy=None
player=Players.Player("Zuvo",["rock throw"],[])
init(convert=True)
print(descriptions.intro)

#Global commands
@when("help")
def h():
    adventurelib.help()

print(player.spells)
@when('cast SPELL')
def casting(spell):
    if spell in player.spells:
        if spell in spells.spells:
            spells.spells[spell].cast_spell(player,player)
    else:
        print("Invalid casting instructions.")


start(help=False)
