from typing import Iterable, Union

from mytypes import Arg, ArgError


def calc(args: Iterable[Arg]) -> Union[int, float]:
    stack = []
    for arg in args:
        if type(arg) == int or type(arg) == float:
            stack.append(arg)
        elif arg in ["+", "-", "*", "/"] and len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            if arg == "+":
                c = a + b
            elif arg == "-":
                c = b - a
            elif arg == "*":
                c = a * b
            elif arg == "/":
                c = b / a
            stack.append(c)
        else:
            raise ArgError
    if len(stack) != 1:
        raise ArgError
    return stack[0]
