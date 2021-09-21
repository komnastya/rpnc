from romantoint import roman_to_int


def test_romantoint():
    assert roman_to_int("I") == 1
    assert roman_to_int("XV") == 15
    assert roman_to_int("CXV") == 115
    assert roman_to_int("CMXV") == 915
    assert roman_to_int("MXV") == 1015
