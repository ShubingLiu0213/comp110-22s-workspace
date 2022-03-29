

Ts = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
new_list = []
different = [(b - a) for a, b in Ts]


def get_time_interval(ls: list) -> list[float]:
    xs = list()
    for items in ls:
        xs.append(items[1] - items[0])
    return xs
   

def sort_importance(ls):
    length = len(ls)
    for i in range(0, length):

        for j in range(0, length - i - 1):
            if(ls[j][1] < ls[j + 1][1]):
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp
    return ls


def duration_matches(start: list, ls: list, at: list) -> list:
    sum: int = 0
    length = len(ls)
    while length > 0:
        length -= 1
        sum += length  
    for i in range(0, len(ls) - 1):
        ti = ls[i][3]
        j = 0
        while ti > at[j] and j:
            ti = ti - at[j]
            j += 1
        if j > len(at):
            exit("total time needed exceed avaliable time slot.")
        else:
            count: int = 0
            end_time = start[j - 1][1] + ti
        
            if end_time <= ls[i][4]:
                start[j - 1][1] = end_time
            else:
                if i < 0: 
                    exit(f"Sorry. You can finish {ls[i][0]} before {ls[i][3]}. ")
                else:
                    ls = swap_positions(ls, i, i - 11)
                    count += 1
        if count > sum:
            print("Sorry,You cannot finish everything in the given time")
        return [ls]
    return ls


def swap_positions(a_list, pos1: int, pos2: int) -> list[int]:
    pos1 = 1
    pos2 = 3
    a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
    return a_list