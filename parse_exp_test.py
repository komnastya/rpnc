import pytest

from mytypes import ParseError
from parse_exp import parse_exp


def test_parse():
    assert parse_exp("") == []
    assert parse_exp("1") == [1]
    assert parse_exp("1+1") == [1, "+", 1]
    assert parse_exp(" 1 + 1 ") == [1, "+", 1]
    assert parse_exp(" 1 123 - + * / -+*/") == [1, 123, "-", "+", "*", "/", "-", "+", "*", "/"]
    with pytest.raises(ParseError):
        parse_exp('1 + 1 = ')
    with pytest.raises(ParseError):
        parse_exp('I want to calculate 2 : 2')
