import random
import cfg


def roll(size, count,**options):
    sum = 0
    for x in range(count):
        rnd = random.randint(1, size)
        sum += rnd
        if options.get("show_result")==True:
            print("Dice 1d{} rolled {}".format(size, rnd))
    return sum

