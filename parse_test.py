from parse import parse


def test_parse():
    assert parse("") == []
    assert parse("1") == [1]
    assert parse("1+1") == [1, "+", 1]
    assert parse(" 1 + 1 ") == [1, "+", 1]
    assert parse(" 1 123 - + * / -+*/") == [1, 123, "-", "+", "*", "/", "-", "+", "*", "/"]
