import pytest

from mytypes import ParseError
from parse import parse


def test_parse():
    assert parse("") == []
    assert parse("1") == [1]
    assert parse("1+1") == [1, "+", 1]
    assert parse(" 1 + 1 ") == [1, "+", 1]
    assert parse(" 1 123 - + * / -+*/") == [1, 123, "-", "+", "*", "/", "-", "+", "*", "/"]
    with pytest.raises(ParseError):
        parse('1 + 1 = ')
    with pytest.raises(ParseError):
        parse('I want to calculate 2 : 2')
