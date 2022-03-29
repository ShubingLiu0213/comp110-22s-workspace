def double_char(str):
    i: int = 0
    result: str = ""
    if i < len(str):
        result += str[i]
        result += str[i]
        i += 1
    return result