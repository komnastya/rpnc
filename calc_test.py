import pytest

from calc import calc
from mytypes import ArgError


def test_calc():
    with pytest.raises(ArgError, match=r"Not enough operators"):
        calc([])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \+"):
        calc(["+"])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \*"):
        calc([1, "*"])
    with pytest.raises(ArgError, match=r"Not enough operators"):
        calc([1, 2, 3, "+"])
    with pytest.raises(ArgError, match=r"Not enough arguments for operator \+"):
        calc([1, 2, "+", "+"])

    assert calc([1]) == 1
    assert calc([1.1]) == 1.1
    assert calc([3, 2, "+"]) == 5
    assert calc([3, 2, "-"]) == 1
    assert calc([3, 2, "*"]) == 6
    assert calc([3, 2, "/"]) == 1.5

    assert calc([3, 4, "*", 2, "/"]) == 6
    assert calc([3, 11, 5, "+", "-"]) == -13
    assert calc([5, 9, 2, "*", "+"]) == 23
    assert calc([1, 2, "*", 3, 4, "*", "+"]) == 14

    with pytest.raises(AssertionError, match=r"Unknown operator \[x\]"):
        assert calc([3, 4, "x"])
