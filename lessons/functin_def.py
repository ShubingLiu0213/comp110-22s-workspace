def drink_list(age: int, pref: str):
    """Drink suggestions."""
    if age < 21:
        menu("kids")
    else:
        if pref == "wine":
            print("Have a glass of wine, please.")
            menu("adult")
        if pref == "beer":
            print("Enjoy your beer!")
            menu("adult")


def menu(pref: str):
    """Here is the menu."""
    if pref == "kid":
        print("nuggets")
    if pref == "adult":
        print("P and Qs")


a: int = 24
print(drink_list(a, "beer"))
