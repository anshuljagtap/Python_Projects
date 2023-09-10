# Author: Anshul Jagtap
# Project Name: Dice simulator
# Description: Rolling n number of dice which can be used for board games.
# Concepts: Random function, Exception handling, While loop, if-else, break, raising error.

import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    rolls_sum = 0
    for a in range (amount):
        random_roll: int = random.randint(1,6)
        rolls.append(random_roll)

    for i in rolls:
        rolls_sum += i
    
    return rolls, rolls_sum

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? (If you want to stop type exit) \n')

            if user_input.lower() == "exit":
                print('Thank you for playing!')
                break

            print(roll_dice(int(user_input)))
        except ValueError:
            print("Please enter a Valid Number")
            print ('If you want to stop type exit')

if __name__ == '__main__':
    main()





