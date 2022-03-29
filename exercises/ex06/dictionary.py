"""Some dictionary functions."""

__author__ = "730508266"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary."""
    new_dict: dict[str, str] = {}
    if len(old_dict) > 1:
        for k in old_dict:
            new_dict[old_dict[k]] = k
            for i in new_dict:
                if len(new_dict[i]) > 1:
                    raise KeyError
        return new_dict
    else:
        for k in old_dict:
            new_dict[old_dict[k]] = k
    return new_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns the favorite color in a dictionary."""
    counter = []
    new_dict: dict[str, int] = {}
    for key in color:
        counter.append(color[key])
    print(counter)
    if len(counter) == 1:
        return counter[0]

    for item in counter:        
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] += 1
    v = list(new_dict.values())
    i: int = 1
    count = 1
    large = v[0]
    while i < len(v):
        if v[i] > large:
            large = v[i]
            count = i
        else:
            count = 0
        i += 1
    return counter[count]
    
    
def count(counter: list[str]) -> dict[str, int]:
    """Counts number of occurrences of an item."""
    new_dict: dict[str, int] = {}
    for item in counter:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict
