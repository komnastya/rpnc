from decimal import Decimal

import pytest

from calc import calc
from mytypes import ArgError


def test_calc():
    with pytest.raises(ArgError, match=r"Not enough operators"):
        calc([])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \+"):
        calc(["+"])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \*"):
        calc([Decimal(1), "*"])
    with pytest.raises(ArgError, match=r"Not enough operators"):
        calc([Decimal(1), Decimal(2), Decimal(3), "+"])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \+"):
        calc([Decimal(1), Decimal(2), "+", "+"])

    assert calc([Decimal(1)]) == 1
    assert calc([Decimal(1.1)]) == 1.1
    assert calc([Decimal(3), Decimal(2), "+"]) == 5
    assert calc([Decimal(3), Decimal(2), "-"]) == 1
    assert calc([Decimal(3), Decimal(2), "*"]) == 6
    assert calc([Decimal(3), Decimal(2), "/"]) == 1.5

    assert calc([Decimal(3), Decimal(4), "*", Decimal(2), "/"]) == 6
    assert calc([Decimal(3), Decimal(11), Decimal(5), "+", "-"]) == -13
    assert calc([Decimal(5), Decimal(9), Decimal(2), "*", "+"]) == 23
    assert calc([Decimal(1), Decimal(2), "*", Decimal(3), Decimal(4), "*", "+"]) == 14

    with pytest.raises(AssertionError, match=r"Unknown operator \[x\]"):
        assert calc([Decimal(3), Decimal(4), "x"])
