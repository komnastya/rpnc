from mytypes import ArgList, ParseError

S_INITIAL = 0
S_NUM = 1


def parse(s: str) -> ArgList:
    args = []
    state = S_INITIAL
    start = 0
    for i, c in enumerate(s + "\0"):
        char = ord(c)
        is_space = char in [32, 44]  # пробел или запятая как разделитель
        is_digit = 48 <= char <= 57
        is_operator = char in [42, 43, 45, 47]

        if state == S_INITIAL:
            if char == 0 or is_space:
                state = S_INITIAL
                continue

            if is_digit:
                state = S_NUM
                start = i
                continue

            if is_operator:
                state = S_INITIAL
                args.append(s[i])
                continue

            raise ParseError(f"Error at index {i}")

        if state == S_NUM:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(int(s[start:i]))
                continue

            if is_digit:
                state = S_NUM
                continue

            if is_operator:
                state = S_INITIAL
                args.append(int(s[start:i]))
                args.append(s[i])
                continue

            raise ParseError(f"Error at index {i}")

        assert False  # Unreachable code.

    return args


print(parse("12 8 + 4 / 10 * "))  # [12, 8, '+', 4, '/', 10]
print(parse("20,8,+,4,/,"))  # [20, 8, '+', 4, '/'] = 5
print(parse("20, 8, +, 4, /, "))  # [20, 8, '+', 4, '/'] = 5
print(parse("20 5 / * 10 "))  # [20, 5.2, '/', '*', 10.1 ] = 40.4
print(parse("20 5 / 10 * / 2"))  # [20, 5.2, '/', '*', 10.1 ] = 40.4
