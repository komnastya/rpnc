chars = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(s: str) -> int:
    number = 0

    prev_value = 0
    for i in range(len(s) - 1, -1, -1):
        cur_value = chars[s[i]]
        if cur_value >= prev_value:
            number += cur_value
        else:
            number -= cur_value

        prev_value = cur_value

    return number
