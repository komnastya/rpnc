from typing import List, Literal, Union

Operator = Literal["+", "-", "*", "/"]
Arg = Union[int, float, Operator]
ArgList = List[Arg]


class ArgError(ValueError):
    """An error which signals that an argument list is invalid."""

    pass


class ParseError(ValueError):
    # An error which signals that a string cannot be parsed to argument list.
    pass
