from decimal import Decimal
from typing import Iterable, Union

from mytypes import Arg, ArgError


def calc(args: Iterable[Arg]) -> Union[Decimal]:
    stack = []
    for arg in args:

        def check_stack_len(num_args):
            if len(stack) < num_args:
                raise ArgError(f"Not enough arguments for operator {arg}")

        if type(arg) == Decimal:
            stack.append(arg)
        else:
            if arg == "+":
                check_stack_len(2)
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)
            elif arg == "-":
                check_stack_len(2)
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)
            elif arg == "*":
                check_stack_len(2)
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            elif arg == "/":
                check_stack_len(2)
                b = stack.pop()
                a = stack.pop()
                c = a / b
                stack.append(c)
            else:
                raise AssertionError(f"Unknown operator [{arg}]")
    if len(stack) != 1:
        raise ArgError("Not enough operators")
    return stack[0]
