"""Ex02 - Wordle - A Loop for guess game."""

__author__ = "730508266"
secret: str = "python"
length: int = len(secret)
guess: str = input(f"What is your {length}-letter guess? ")
while len(guess) != 6:
    print(f"That was not {length} letters! Try again: ")
    guess = input(f"What is your {length}-letter guess? ")
guess_index: int = 0
result: str = ""
if guess == secret:
    while guess_index < len(guess):
        if guess[guess_index] == secret[guess_index]:
            result += "\U0001F7E9"
        else:
            result += "\U00002B1C"
        guess_index += 1 
    print(result)
    print(" Woo! You got it!") 
else:
    while guess_index < len(guess):
        if guess[guess_index] == secret[guess_index]:
            result += "\U0001F7E9"
        else:
            play: bool = False
            index: int = 0
            while not play and index < len(secret):
                if secret[index] == guess[guess_index]:
                    play = True
                else:
                    index += 1
            if play:
                result += "\U0001F7E8"
            else:
                result += "\U00002B1C"
        guess_index += 1 
    print(result)
    print("Not quite. Play again soon!")
    
