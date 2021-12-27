import random
def roll_die():
    #
    return random.randint(1,6)
def roll_dice():
    print('Rolling')
    return  roll_die() + roll_die()
def main():
    # Perform the first roll to prime the loop.  We also set a counter to 2 to
    # prepare to count how many
    previous_rolls = roll_dice()
    current_rolls = roll_dice()
    counter = 2
    while previous_rolls != current_rolls:
        previous_rolls = \
            current_rolls
        current_rolls = roll_dice()
        counter +=1
        print("It took", counter, "rolls to repeat a roll of", current_rolls)
main()