from typing import List, Literal, Union

Operator = Literal["+", "-", "*", "/"]
Arg = Union[float, Operator]
ArgList = List[Arg]
