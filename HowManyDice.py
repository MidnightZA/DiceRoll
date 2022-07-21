# Function to ask the player how many dices they would like to roll

def howManyDice():

    accept = False

    while accept is False:

        try:
            x = int(input('How many dice would you like to roll? '))
        except ValueError:
            print('Only numbers are accepted')
        if x in range(1,1000):
            print(f'One dice will be rolled {x} times')
            break
        elif x > 1000:
            print('Enter a number less than 1000')
        else:
            print('Enter a valid number')
            False

    return x
