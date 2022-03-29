"""A 'list' utility fuction."""

__author__ = "730508266"


def only_evens(numbers: list[int]) -> list[int]:
    """Finding out all even numbers."""
    result: list[int] = list()
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Sub list from initial list."""
    result: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 and (start > len(a_list) or end <= 0):
        return result
    i: int = start
    while i >= start and i < end:
        result.append(a_list[i])
        i += 1
    return result


def concat(first: list[int], second: list[int]) -> list[int]:
    """Combining two lists."""
    new_list: list[int] = []
    for i in first:
        new_list.append(i)
    for k in second:
        new_list.append(k)
    return new_list
    

            

    
