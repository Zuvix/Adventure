from adventurelib import *
from colorama import init, Fore, Back, Style
import time
import sys
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./12)
@when("brush teeth")
def brush_teeth():
    say("""
        You squirt a bit too much toothpaste onto your
        brush and dozily jiggle it round your mouth.
    """)
    print (f"This is a {Fore.GREEN}good item{Style.RESET_ALL}")
init(convert=True)
start()