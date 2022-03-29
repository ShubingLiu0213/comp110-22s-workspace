a_list: list[int] = [4, 3, 5, 1, 3, 5, 5, 4]
a_list.sort()

print(a_list)


def swap_positions(a_list, pos1: int, pos2: int) -> list[int]:
    pos1 = 1
    pos2 = 3
    a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
    return a_list


for i in a_list:
    if a_list.count(i) >= 3:
        quit()


test_list = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
new_list = []
different = [(b - a) for a, b in test_list]
print(different)