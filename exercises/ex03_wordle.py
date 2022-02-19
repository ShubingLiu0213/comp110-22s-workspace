"""Ex03 - wordle - a game loop."""

__author__ = "730508266"


def contains_char(guess: str, one: str) -> bool:
    """Looking for one in the string of guess."""
    assert len(one) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == one:
            return True
        i += 1
    return False
    

def emojified(secret: str, guess: str) -> str:
    """Return a string of emoji."""
    assert len(guess) == len(secret)
    k: int = 0
    result: str = ""
    while k < len(guess):
        if guess[k] == secret[k]:
            result += "\U0001F7E9"
        else:
            if contains_char(guess, secret[k]):
                result += "\U0001F7E8"
            else:
                result += "\U00002B1C"
        k += 1
    return result


def input_guess(length: int) -> str:
    """Input an expected length guess."""
    guess: str = ""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess
       

def main() -> None:
    """The entrypoint of the program and main game loop."""
    count: int = 1
    secret: str = "doyou"
    right: str = ""
    i: int = 0
    while i < len(secret):
        right += "\U0001F7E9"
        i += 1
    play: bool = False
    while count <= 6 and not play:
        print(f"=== Turn {count}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, "doyou")
        print(result)
        if result != right:
            count += 1
        else:
            play = True
    if count <= 6:
        print(f"You won in {count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

    
           
       
        
           





    
