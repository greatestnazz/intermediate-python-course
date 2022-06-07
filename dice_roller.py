import random

dicerolls = 2
sum_dice = 0

for i in range(0, dicerolls):
     roll = random.randint(1, 6)
     sum_dice += roll
     print(f'You rolled a {roll}')
print(f'You have rolled a total of {sum_dice}')
  
