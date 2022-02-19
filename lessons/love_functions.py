def love(name: str) -> str:
    """Given a name as a parameter, returns a  loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """generates a  string that repeats a loving message n times"""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note


def length_again(x: str, y: int) -> str:
    i: int = 0
    h: int = 0
    result: str = ""
    while i < len(x):
        while h < y:
            result += x[i]
            h += 1
        i += 1
        h = 0
    return result

