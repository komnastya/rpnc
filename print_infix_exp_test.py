from decimal import Decimal

import pytest

from mytypes import ArgError
from print_infix_exp import print_infix_exp


def test_print_infix_exp():
    assert print_infix_exp([]) == ""
    assert print_infix_exp([Decimal(1)]) == "1"
    assert print_infix_exp([Decimal(1), Decimal(2), "+"]) == "(1 + 2)"
    assert print_infix_exp([Decimal(1), Decimal(2), "+", Decimal(3), "*"]) == "((1 + 2) * 3)"
    assert (
            print_infix_exp([Decimal(1), Decimal(2), "+", Decimal(3), "*", Decimal(3), Decimal(3), "*", "*"])
            == "(((1 + 2) * 3) * (3 * 3))"
    )

    with pytest.raises(ArgError):
        print_infix_exp([Decimal(1), Decimal(2)])

    with pytest.raises(ArgError):
        print_infix_exp([Decimal(1), "+"])
