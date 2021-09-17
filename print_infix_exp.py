from decimal import Decimal
from typing import List

from mytypes import ArgError, ArgList


def print_infix_exp(args: ArgList) -> str:
    stack: List[str] = []
    if len(args) == 0:
        return ""
    if len(args) == 1:
        return str(args[0])
    for arg in args:
        if type(arg) == Decimal:
            stack.append(str(arg))
        else:
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                c = f"({a} {arg} {b})"
                stack.append(c)
            else:
                raise ArgError(f"Not enough arguments for operator {arg}")
    if len(stack) != 1:
        raise ArgError("Not enough operators")
    return stack[0]
