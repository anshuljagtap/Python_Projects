# Author: Anshul Jagtap
# Project Name: Madlibs
# Description: Simple fun game to enter words to make a story sound funny or sometimes makes no sense :)
# concepts: Functions, String formating 

def get_input (word_type: str):
    user_input: str = input(f"Enter a {word_type}:") #getting general input
    return user_input

noun_1 = get_input("noun")
verb_1 = get_input("verb")
noun_2 = get_input("noun")
verb_2 = get_input("verb")

story = f""" In a quiet forest, there was a curious squirrel named {noun_1} and a playful butterfly named {noun_2}. {noun_1} loved to climb trees, while {noun_2}  enjoyed flitting around in the meadows.

One sunny day, {noun_1} decided to {verb_1} a mysterious noise deep in the woods. With a swift leap, he ventured into the dense foliage and found a hidden cave filled with sparkling crystals.

Meanwhile, {noun_2} was {verb_2} around, spreading colorful joy. Her graceful {verb_1} and vibrant colors brought smiles to all who saw her.

When {noun_1} returned from the cave, he showed {noun_2} the dazzling crystals. Together, they decided to {verb_2} more of the forest's secrets and dance beneath the canopy of leaves, sharing their magical discoveries with the world.

THE END!!!
"""

print (story)

