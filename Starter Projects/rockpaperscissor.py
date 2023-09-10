# Author: Anshul Jagtap
# Project Name: Rock Paper Scissor Games
# Description: Fun game of rock paper scissor which we play since we were children
# Concepts: importing sys, Random function, classes, instantiating, functions, methods, String formating, While loop, if-else.

import random
import sys

class rock_paper_scissor:

    def __init__(self):
        print('Welcome to Rock Paper Scissor game!!!')

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissor': '✄'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.score_user = 0
        self.scoreAi= 0

    def gameplay(self):
        user_move: str = input('Rock, Paper, or Scissor?(To quit game enter \'exit\') >>').lower()

        if user_move == 'exit':
            print('Thank you for playing:)')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move :(. Try again with correct input')
            return self.gameplay()  
        
        player_ai: str = random.choice(self.valid_moves)

        self.display_moves(user_move, player_ai)
        self.check_moves(user_move, player_ai)

    def display_moves(self, user_move: str, player_ai: str):
        print('-----')
        print(f'You:{self.moves[user_move]}')
        print(f'AI:{self.moves[player_ai]}')
        print('-----')

    def check_moves(self, user_move: str, player_ai: str): 

        if user_move == player_ai:
            print(f'It\'s a tie![Score-> user:{self.score_user}| AI:{self.scoreAi}]')

        elif user_move == 'rock' and player_ai == 'scissor':
            self.score_user +=1
            print(f'You won :) [Score-> user:{self.score_user}| AI:{self.scoreAi}]')

        elif user_move == 'scissor' and player_ai == 'paper':
            self.score_user +=1
            print(f'You won :) [Score-> user:{self.score_user}| AI:{self.scoreAi}]')
            
        elif user_move == 'paper' and player_ai == 'rock':
            self.score_user +=1
            print(f'You won :) [Score-> user:{self.score_user}| AI:{self.scoreAi}]')
            
        else:
            self.scoreAi +=1 
            print(f'You lost :( [Score-> user:{self.score_user}| AI: {self.scoreAi}]')

if __name__ ==  '__main__':
    rps = rock_paper_scissor()

    while True:
        rps.gameplay()
