from romantoint import roman_to_int


def test_roman_to_int():
    assert roman_to_int("") == 0
    assert roman_to_int("I") == 1
    assert roman_to_int("IV") == 4
    assert roman_to_int("VI") == 6
    assert roman_to_int("XV") == 15
    assert roman_to_int("CXV") == 115
    assert roman_to_int("CMXV") == 915
    assert roman_to_int("DCXXI") == 621
    assert roman_to_int("MCMXCIV") == 1994
