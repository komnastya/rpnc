from mytypes import ArgList, ParseError

S_INITIAL = 0
S_NUM = 1


def parse_exp(s: str) -> ArgList:
    args = []
    state = S_INITIAL
    start = 0
    for i, c in enumerate(s + "\0"):
        char = ord(c)
        is_space = char in [32, 44]
        is_digit = 48 <= char <= 57
        is_operator = char in [42, 43, 45, 47]

        def error_message():
            return f'Error at index {i}, unexpected char "{c}"'

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

            raise ParseError(error_message())

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

            raise ParseError(error_message())

        assert False  # Unreachable code.

    return args
