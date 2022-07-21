import time

from HowManyDice import *
from RollTheDice import *


startTime = time.time()
noDice = howManyDice()
result = []

for i in range(0,noDice):
    result.append(rollTheDice())

sum = sum(result)
avg = sum/noDice

print(f'The sum of all results is: {sum}')
print(f'The average value is: {avg}')
print(f'It took {(time.time()-startTime)} seconds to roll a dice {noDice} times')