from adventurelib import start, when
import adventurelib
import dice
from colorama import init, Fore, Back, Style
import descriptions

init(convert=True)
print(descriptions.intro)


#Global commands
@when("help")
def h():
    adventurelib.help()


dice.roll(6, 1)
start(help=False)
