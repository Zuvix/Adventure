from adventurelib import start, when,set_context
import adventurelib
import dice,cfg
from colorama import init, Fore, Back, Style
import descriptions
import Players,spells_logic
Enemy=None
print("Who are you?")
hero_name=input("")
player=Players.Player(hero_name,["rock throw","firebolt"],[])
init(convert=True)
print(descriptions.intro)

#Global commands
@when("help")
def h():
    adventurelib.help()

@when("show SOMETHING")
def show(something):
    x=something
    if x=="spells":
        print("")
        print("Concentration (chance to cast spell) is 1d20 + {} (MIND)".format(player.MIND))
        for spell in player.spells:
             spells_logic.spells[spell].describe()
        return
    if x=="stats":
        print("")
        print("Level: {}".format(player.level))
        print(Fore.RED+ "{}/{} HP".format(player.HP,player.MaxHP)+Fore.BLUE+"  {}/{} MP".format(player.MP,player.MaxMP)+Style.RESET_ALL)
        print("VIT : {}  INT : {}  MIND: {}  FORCE : {}".format(player.VIT,player.INT,player.MIND,player.FORCE))
        print("")
        print("VIT - Vitality increases your total life by {} and your inventory size by {}.".format(cfg.HP_per_lvl,cfg.inventory_per_lvl))
        print("INT - Inteligence allows you to craft better items or trick your enemies in combat.")
        print("MIND - Each point in Mind increases your total mana by {} and your concentration(chance to succesfully cast a spell) by 1".format(cfg.MP_per_lvl))
        print("FORCE - Makes most of your spells more powerfull.")
        return
    

    print("Use \"show SOMETHING\" command to learn information about the game elements.")
    print("As SOMETHING you can type:")
    print("spells - to get complete information about the spells you control.")
    print("stats - shows your stats and what they mean.")
set_context("combat")
@when('cast SPELL',context="combat")
def casting(spell):
    if spell in player.spells:
        if spell in spells_logic.spells:
            spells_logic.spells[spell].cast_spell(player,player)
    else:
        print("Invalid casting instructions.")



#set_context("combat")
start(help=False)
