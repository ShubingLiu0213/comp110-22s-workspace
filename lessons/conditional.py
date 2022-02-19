"""An examp;e of conditional(if-else) statements."""

from random import randint


SECRET: int = 3

print("I'm thinking of  a number between 1-5,what is it?")
guess: int = int(input("What is  your guess?"))

if guess == SECRET:
    print("YOu guessed correctly!!!") 
else:
    print("Sorry, you guessed incorrectly :(")
    print("Try running the program again.")
                                     
print("Game over.")
randint(1, 100)
