from mytypes import ArgList, ParseError

S_INITIAL = 0
S_NUM_INT_DIGIT = 1
S_NUM_FRAC_DOT = 2
S_NUM_FRAC_DIGIT = 3


def parse_exp(s: str) -> ArgList:
    args = []
    state = S_INITIAL
    start = 0
    for i, c in enumerate(s + "\0"):
        char = ord(c)
        is_space = char in [32, 44]
        is_digit = 48 <= char <= 57
        is_operator = char in [42, 43, 45, 47]
        is_dot = char == 46

        def error_message():
            if char == 0:
                char_name = f"end of string"
            else:
                char_name = f'char "{c}"'
            return f"Error at index {i}, unexpected {char_name}"

        if state == S_INITIAL:
            if char == 0 or is_space:
                state = S_INITIAL
                continue

            if is_digit:
                state = S_NUM_INT_DIGIT
                start = i
                continue

            if is_operator:
                state = S_INITIAL
                args.append(s[i])
                continue

            raise ParseError(error_message())

        if state == S_NUM_INT_DIGIT:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(int(s[start:i]))
                continue

            if is_digit:
                state = S_NUM_INT_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(int(s[start:i]))
                args.append(s[i])
                continue

            if is_dot:
                state = S_NUM_FRAC_DOT
                continue

            raise ParseError(error_message())

        if state == S_NUM_FRAC_DOT:
            if is_digit:
                state = S_NUM_FRAC_DIGIT
                continue

            raise ParseError(error_message())

        if state == S_NUM_FRAC_DIGIT:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(float(s[start:i]))
                continue

            if is_digit:
                state = S_NUM_FRAC_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(float(s[start:i]))
                args.append(s[i])
                continue

            raise ParseError(error_message())

        assert False  # Unreachable code.

    return args
