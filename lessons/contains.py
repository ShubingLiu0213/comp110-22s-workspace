"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting the secret club...")
    else:
        print("Go back to Davis")


def contains(needle: str, haystack: list[str]) -> bool:
    for i in haystack:
        if i == needle:
            return True
    return False