from decimal import Decimal
from typing import cast

from mytypes import ArgList, Operator, ParseError
from romantoint import roman_to_int

S_INITIAL = 0
S_NUM_INT_DIGIT = 1
S_NUM_FRAC_DOT = 2
S_NUM_FRAC_DIGIT = 3
S_NUM_EXP = 4
S_NUM_EXP_SIGN = 5
S_NUM_EXP_DIGIT = 6
S_ROMAN_DIGIT = 7


def parse_exp(s: str) -> ArgList:
    args: ArgList = []
    state = S_INITIAL
    start = 0
    for i, c in enumerate(s + "\0"):
        char = ord(c)
        is_space = char in [32, 44]
        is_digit = 48 <= char <= 57
        is_operator = char in [42, 43, 45, 47]
        is_dot = char == 46
        is_exp = char in [69, 101]
        is_exp_sign = char in [43, 45]
        is_roman = char in [67, 68, 73, 76, 77, 86, 88]

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
                args.append(cast(Operator, s[i]))
                continue

            if is_roman:
                state = S_ROMAN_DIGIT
                start = i
                continue

            raise ParseError(error_message())

        if state == S_NUM_INT_DIGIT:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(Decimal(s[start:i]))
                continue

            if is_digit:
                state = S_NUM_INT_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(Decimal(s[start:i]))
                args.append(cast(Operator, s[i]))
                continue

            if is_dot:
                state = S_NUM_FRAC_DOT
                continue

            if is_exp:
                state = S_NUM_EXP
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
                args.append(Decimal(s[start:i]))
                continue

            if is_digit:
                state = S_NUM_FRAC_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(Decimal(s[start:i]))
                args.append(cast(Operator, s[i]))
                continue

            if is_exp:
                state = S_NUM_EXP
                continue

            raise ParseError(error_message())

        if state == S_NUM_EXP:
            if is_digit:
                state = S_NUM_EXP_DIGIT
                continue

            if is_exp_sign:
                state = S_NUM_EXP_SIGN
                continue

            raise ParseError(error_message())

        if state == S_NUM_EXP_SIGN:
            if is_digit:
                state = S_NUM_EXP_DIGIT
                continue

            raise ParseError(error_message())

        if state == S_NUM_EXP_DIGIT:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(Decimal(s[start:i]))
                continue

            if is_digit:
                state = S_NUM_EXP_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(Decimal(s[start:i]))
                args.append(cast(Operator, s[i]))
                continue

            raise ParseError(error_message())

        if state == S_ROMAN_DIGIT:
            if char == 0 or is_space:
                state = S_INITIAL
                args.append(Decimal(roman_to_int(s[start:i])))
                continue

            if is_roman:
                state = S_ROMAN_DIGIT
                continue

            if is_operator:
                state = S_INITIAL
                args.append(Decimal(roman_to_int(s[start:i])))
                args.append(cast(Operator, s[i]))
                continue

        assert False  # Unreachable code.

    return args
