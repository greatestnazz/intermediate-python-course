import random

def dice():
    #Variable defination
    player_name = input("What is your name: ")
    dicerolls = int(input("How many dice do you have: "))
    sum_dice = 0
    dice_sides = int(input("How many sides do the dice have eg 1,6,12: "))
    #loop to iterate and add the values of the dice rolls
    for i in range(0, dicerolls):
         roll = random.randint(1, dice_sides)
         sum_dice += roll
         print(f'You rolled a {roll}')
    

    #Conditional to print comments with the rolls
    if sum_dice <= 6 :
        print(f'{player_name} rolled a total of {sum_dice}, Big fail')
    else:
        print(f'{player_name} rolled a total of {sum_dice}, Whopee')
    
dice()
