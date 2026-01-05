import random   # for generating random numbers

# function to simulate rolling a dice
def roll_dice():
    # pick a random number between 1 and 6
    return random.randint(1, 6)

# roll the dice and show the result
print("You rolled:", roll_dice())
