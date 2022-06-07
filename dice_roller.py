import random

#Variable defination
dicerolls = 2
sum_dice = 0

#loop to iterate and add the values of the dice rolls
for i in range(0, dicerolls):
     roll = random.randint(1, 6)
     sum_dice += roll
     print(f'You rolled a {roll}')

#Conditional to print comments with the rolls
if sum_dice <= 6 :
    print(f'You have rolled a total of {sum_dice}, Big fail')
else:
    print(f'You have rolled a total of {sum_dice}, Whopee')
  
