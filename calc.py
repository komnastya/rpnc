from typing import Iterable, Union

from mytypes import Arg, ArgError


def calc(args: Iterable[Arg]) -> Union[int, float]:
    stack = []
    for arg in args:
        if type(arg) == int or type(arg) == float:
            stack.append(arg)
        else:
            if arg == "+" and len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            elif arg == "-" and len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif arg == "*" and len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            elif arg == "/" and len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                c = b / a
                stack.append(c)
            else:
                raise ArgError
    if len(stack) != 1:
        raise ArgError
    return stack[0]
