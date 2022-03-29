beverage: dict[str, int] = {}
beverage["soy milk"] = 1
beverage["spirit"] = 3
beverage["water"] = 12


def favoriate(d: dict[str, str]) -> str:
    counter: list[str] = list()
    new_dict: dict[str, int] = {}
    i: int = 0
    for key in d:
        counter.append(key)
    for item in counter:
        if item in new_dict:
            new_dict[item] += 1
        if item not in new_dict:
            new_dict[item] = 1
        a = []
        a.append(new_dict[item])
        max = a[0]
        while i < len(a):
            if a[i] > max:
                max = a[i]
            i += 1
    return counter[i]


def vowels(a: str) -> str:
    i: int = 0
    result: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    while i < len(a):
        is_vowels: bool = False
        j = 0
        while j < 5:
            if vowels[j] == a[i]:
                is_vowels = True
            j += 1
        if is_vowels and i % 3 != 0:
            result += a[i]
        elif not is_vowels and i % 3 == 0:
            result += a[i]
        i += 1
    return result  


def average(a: dict[str, list[int]]) -> dict[str, float]:
    new_dict: dict[str, float] = {}
    for key in a:
        total: int = 0
        for grade in a[key]:
            total += grade
        new_dict[key] = total / len(new_dict)
    return new_dict
        
