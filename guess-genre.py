#!/usr/bin/env python

import random

def main():
    """Start a colour guessing game."""
    print("Guess the music genre!")

    genres = ["classical", "KPOP", "JPOP", "jazz", "rock", "folk", "country"]
    clues = ["Orchestra", "TWICE", "Yoasobi", "Louis Armstrong", "MCR", "Nyanyian Serambi", "Acoustic guitar with southern accent"]
    
    s = len(genres)
    x = random.randint(0, s)
    genre = genres[x]
    clue = clues[x]
    print(genre)
    
    user_guess = None
    token = 3

    while user_guess != genre:
        user_guess = str(input("What genre of music am I thinking of? "))
        token -= 1
        
        if user_guess == genre:
            print("Congratulations you got it right! The genre is {}.".format(genre))
            break
        
        elif token > 0:
            print("Sorry, {} is wrong. Please try again.".format(user_guess))
            
        elif token > -1:
            print("You have guessed three times and the answer is not {}. Here's a clue: {}. Try again".format(user_guess, clue))
        else:
            print("Can't believe you still guessed wrong.")

main()