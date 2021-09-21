def roman_to_int(s: str) -> int:
    s = s + "\0"
    number = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == "I":
            if s[i + 1] == "V":
                number += 4
                i += 2
                continue
            if s[i + 1] == "X":
                number += 9
                i += 2
                continue
            number += 1
            i += 1
            continue
        if s[i] == "V":
            number += 5
            i += 1
            continue
        if s[i] == "X":
            if s[i + 1] == "L":
                number += 40
                i += 2
                continue
            if s[i + 1] == "C":
                number += 90
                i += 2
                continue
            number += 10
            i += 1
            continue
        if s[i] == "L":
            number += 50
            i += 1
            continue
        if s[i] == "C":
            if s[i + 1] == "D":
                number += 400
                i += 2
                continue
            if s[i + 1] == "M":
                number += 900
                i += 2
                continue
            number += 100
            i += 1
            continue
        if s[i] == "D":
            number += 500
            i += 1
            continue
        if s[i] == "M":
            number += 1000
            i += 1
            continue
        if s[i] == "\0":
            break

        assert False

    return number
