from decimal import Decimal

import pytest

from mytypes import ParseError
from parse_exp import parse_exp


def test_parse():
    assert parse_exp("") == []
    assert parse_exp("1") == [1]
    assert parse_exp("1+1") == [1, "+", 1]
    assert parse_exp("1.1 + 1.1") == [Decimal("1.1"), "+", Decimal("1.1")]
    assert parse_exp("1.1+1.1") == [Decimal("1.1"), "+", Decimal("1.1")]
    assert parse_exp("1,1+1,1") == [Decimal(1), Decimal(1), "+", Decimal(1), Decimal(1)]
    assert parse_exp(" 123 + 456 ") == [Decimal(123), "+", Decimal(456)]
    assert parse_exp("-+*/") == ["-", "+", "*", "/"]
    assert parse_exp(" - + * / ") == ["-", "+", "*", "/"]
    assert parse_exp(",-,+,*,/,") == ["-", "+", "*", "/"]
    assert parse_exp("1e2") == [Decimal(100.0)]
    assert parse_exp("1E2") == [Decimal(100.0)]
    assert parse_exp("1.1e2") == [Decimal(110.0)]
    assert parse_exp("1.1E2") == [Decimal(110.0)]
    assert parse_exp("1e+2") == [Decimal(100.0)]
    assert parse_exp("1E+2") == [Decimal(100.0)]
    assert parse_exp("1.1e+2") == [Decimal(110.0)]
    assert parse_exp("1.1E+2") == [Decimal(110.0)]
    assert parse_exp("1e-2") == [Decimal("0.01")]
    assert parse_exp("1E-2") == [Decimal("0.01")]
    assert parse_exp("1.1E-2") == [Decimal("0.011")]
    assert parse_exp("1.1e-2") == [Decimal("0.011")]
    assert parse_exp("X X +") == [Decimal(10), Decimal(10), "+"]
    assert parse_exp("X X+") == [Decimal(10), Decimal(10), "+"]
    assert parse_exp("XX +") == [Decimal(20), "+"]
    assert parse_exp("XX+") == [Decimal(20), "+"]
    assert parse_exp("X 10 +") == [Decimal(10), Decimal(10), "+"]
    assert parse_exp("10,X,+") == [Decimal(10), Decimal(10), "+"]

    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "="'):
        parse_exp("1 + 1 = ")
    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "w"'):
        parse_exp("I want to calculate 2 : 2")

    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "\."'):
        parse_exp("1.1.")
    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "\."'):
        parse_exp("1..0")
    with pytest.raises(ParseError, match=r'Error at index 0, unexpected char "\."'):
        parse_exp(".1")
    with pytest.raises(ParseError, match=r"Error at index 2, unexpected end of string"):
        parse_exp("1.")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "\."'):
        parse_exp("1 + .1")

    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "e"'):
        parse_exp("1ee")
    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "E"'):
        parse_exp("1eE")
    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "e"'):
        parse_exp("1e1e")
    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "E"'):
        parse_exp("1E1E")
    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "\+"'):
        parse_exp("1e++")
    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "e"'):
        parse_exp("1+e")
    with pytest.raises(ParseError, match=r'Error at index 0, unexpected char "e"'):
        parse_exp("e")
    with pytest.raises(ParseError, match=r'Error at index 0, unexpected char "E"'):
        parse_exp("E")

    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "v"'):
        parse_exp("10 v")
    with pytest.raises(ParseError, match=r'Error at index 2, unexpected char "V"'):
        parse_exp("10V")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "V"'):
        parse_exp("10.1V")

    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "V"'):
        parse_exp("10EV")
    with pytest.raises(ParseError, match=r'Error at index 3, unexpected char "V"'):
        parse_exp("10eV")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "V"'):
        parse_exp("10E+V")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "V"'):
        parse_exp("10e+V")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "V"'):
        parse_exp("10E-V")
    with pytest.raises(ParseError, match=r'Error at index 4, unexpected char "V"'):
        parse_exp("10e-V")

    with pytest.raises(ParseError, match=r'Error at index 5, unexpected char "V"'):
        parse_exp("10.1EV")
    with pytest.raises(ParseError, match=r'Error at index 5, unexpected char "V"'):
        parse_exp("10.1eV")
    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "V"'):
        parse_exp("10.1E+V")
    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "V"'):
        parse_exp("10.1e+V")
    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "V"'):
        parse_exp("10.1E-V")
    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "V"'):
        parse_exp("10.1e-V")
