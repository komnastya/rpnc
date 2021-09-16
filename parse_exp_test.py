import pytest

from mytypes import ParseError
from parse_exp import parse_exp


def test_parse():
    assert parse_exp("") == []
    assert parse_exp("1") == [1]
    assert parse_exp("1+1") == [1, "+", 1]
    assert parse_exp("1.1 + 1.1") == [1.1, "+", 1.1]
    assert parse_exp("1.1+1.1") == [1.1, "+", 1.1]
    assert parse_exp("1,1+1,1") == [1, 1, "+", 1, 1]
    assert parse_exp(" 123 + 456 ") == [123, "+", 456]
    assert parse_exp("-+*/") == ["-", "+", "*", "/"]
    assert parse_exp(" - + * / ") == ["-", "+", "*", "/"]
    assert parse_exp(",-,+,*,/,") == ["-", "+", "*", "/"]
    assert parse_exp("1e2") == [100.0]
    assert parse_exp("1E2") == [100.0]
    assert parse_exp("1.1e2") == [110.0]
    assert parse_exp("1.1E2") == [110.0]
    assert parse_exp("1e+2") == [100.0]
    assert parse_exp("1E+2") == [100.0]
    assert parse_exp("1.1e+2") == [110.0]
    assert parse_exp("1.1E+2") == [110.0]
    assert parse_exp("1e-2") == [0.01]
    assert parse_exp("1E-2") == [0.01]
    assert parse_exp("1.1E-2") == [0.011]
    assert parse_exp("1.1e-2") == [0.011]

    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "="'):
        parse_exp("1 + 1 = ")
    with pytest.raises(ParseError, match=r'Error at index 0, unexpected char "I"'):
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
