import pytest

from mytypes import ParseError
from parse_exp import parse_exp


def test_parse():
    assert parse_exp("") == []
    assert parse_exp("1") == [1]
    assert parse_exp("1+1") == [1, "+", 1]
    assert parse_exp(" 123 + 456 ") == [123, "+", 456]
    assert parse_exp("-+*/") == ["-", "+", "*", "/"]
    assert parse_exp(" - + * / ") == ["-", "+", "*", "/"]
    assert parse_exp(",-,+,*,/,") == ["-", "+", "*", "/"]

    with pytest.raises(ParseError, match=r'Error at index 6, unexpected char "="'):
        parse_exp("1 + 1 = ")
    with pytest.raises(ParseError, match=r'Error at index 0, unexpected char "I"'):
        parse_exp("I want to calculate 2 : 2")
