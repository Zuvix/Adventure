import random
import cfg


def roll(size, count):
    sum = 0
    for x in range(count):
        rnd = random.randint(1, size)
        sum += rnd
        if cfg.print_dice_results:
            print("Dice 1d{} rolled {}".format(size, rnd))
    return sum
