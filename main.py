from words import word_database
import random
import string


def play():
    lives = 8
    word = random.choice(word_database).upper()
    word_letters = set(word)
    used_letters = set()

    while (lives > 0) and (len(used_letters) < len(word_letters)):
        printProcess(lives,word,used_letters)
        guess_letter = input("Guess a letter: ").upper()
        if(guess_letter in used_letters):
            print("You guessed that letter! Try again")
            lives = lives - 1
        else:
            if guess_letter in word_letters:
                used_letters.add(guess_letter)
            else:
                lives = lives - 1
    
    if(lives == 0):
        print("Sorry Your Lost Cuz You Dont Have Lives Anymore")
    else:
        print("Congrats You Guessed The Word Correctly")
        print("Current Word: ", end = " ")
        for letter in word:
            if letter in used_letters:
                print(letter,end = "")
            else:
                print("-",end = "")
        
def printProcess(lives,word,used_letters):
    print(f"You have {lives} lives left and you have used these letters: ", end = ' ')
    for used_letter in used_letters:
        print(used_letter, end = ' ')
        
    print()
    print("Current Word: ", end = " ")
    for letter in word:
        if letter in used_letters:
            print(letter,end = "")
        else:
            print("-",end = "")
    print()
    print()



play()