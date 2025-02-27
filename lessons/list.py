"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

rolls.pop(len(rolls) - 1)
print(rolls)

i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total sore: {sum}")

for roll in rolls:
    print(roll)


def contains(needle: str, haystack: list[str]) -> bool:
    for i in haystack:
        if i == needle:
            return True
    return False
