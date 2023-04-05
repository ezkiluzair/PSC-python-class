#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Guess the music genre!")

    #listing out all the genres in a list called genres with their corresponding clues in a list called clues **in the same order**
    genres = ["Classical", "KPOP", "JPOP", "Jazz", "Rock", "Traditional", "Country"]
    clues = ["Orchestra", "TWICE", "Yoasobi", "Louis Armstrong", "MCR", "Gamelan", "Acoustic guitar with southern accent"]
    
    #letting the computer choose one specific genre and *automatically* choose the clue that correspond to that genre
    s = len(genres) - 1
    x = random.randint(0, s)
    genre = genres[x].lower() #lower() makes the genres[x] become all lowercase 
    clue = clues[x]
    
    user_guess = "nothing"
    token = 3 #to provide a method to determine how many times the user has answered

    while user_guess.lower() != genre: #to lowercase user's input i.e. to make user input not case sensitive
        user_guess = str(input("What genre of music am I thinking of? "))
        token -= 1 #every time the user take a guess, one token is taken away
        
        if user_guess.lower() == genre:
            print("Congratulations you got it right! The genre is {}.".format(genres[x]))
            break
        
        elif token > 0: #giving the user 3 chances to guess without any clue
            print("Sorry, {} is wrong. Please try again.".format(user_guess))
            
        elif token >= 0: #giving the user clue after 3 times of guessing wrong
            print("You have guessed three times and the answer is not {}. Here's a clue: {}. Try again.".format(user_guess, clue))

        else: #being mean to user if they still fail to guess although the clue has been given
            print("Can't believe you still guessed wrong.")

main()