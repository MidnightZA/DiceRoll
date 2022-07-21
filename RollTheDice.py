# Function to roll a single 6 sided die and return the result
import random

diceValues = [1,2,3,4,5,6]

def rollTheDice():

    y = random.choice(diceValues)

    return y

