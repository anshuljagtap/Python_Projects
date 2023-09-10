# Author: Anshul Jagtap
# Project Name: Number Guessing game
# Description: Guessing game to pass time where in friends can guess a number which the game has randomly chossen.
# Concepts: Random function, Exception handling, String formating, While loop, if-else.


from random import randint

tries = 5
lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num} within {tries} tries')


while True:
    if tries>0:
        try:
            user_guess = int(input("Enter your Guess:"))
            print()
        except ValueError as e:
            print('WRONG INPUT! Kindly enter a valid number:')

        if user_guess > random_number:
            tries =tries - 1
            print('The number is lower')
            print('Number tries left are:',tries,'\n')
            
        elif user_guess < random_number:
            tries =tries - 1
            print('The number is higher')
            print('Number tries left are:',tries,'\n')
        else:
            print('You Won! You guessed right!')
            break
    else:
        print('You lost, you ran out of turns :(')
        break




    