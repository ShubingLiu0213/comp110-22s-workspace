"""Classic ordered searching algorithm."""
low: int = 1
high: int = 100
print("Think of a number between 1 t0 100")
input("press enter to continue ")
play: bool = True
while play and high >= low:
    guess: int = (high + low) // 2
    print(str(guess) + "?")
    result: str = input("Reply yes, higher, lower: ")
    if result == "yes":
        print("Woo!")
        play = False
    elif result == "higher":
        low = guess + 1
    elif result == "lower":
        high = guess - 1


