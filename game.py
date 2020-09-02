from adventurelib import start, when
import adventurelib
import dice,cfg
from colorama import init, Fore, Back, Style
import descriptions
import Players

init(convert=True)
print(descriptions.intro)


#Global commands
@when("help")
def h():
    adventurelib.help()


player=Players.Player("Zuvo",8,cfg.start_life,cfg.start_mana,0,0,0,0,{})
print(player.level)
start(help=False)
