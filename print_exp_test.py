from print_exp import print_exp


def test_print_exp():
    assert print_exp([]) == ""
    assert print_exp([1]) == "1"
    assert print_exp([1, 2, "+"]) == "1 2 +"
    assert print_exp([1, 123, "-", "+", "*", "/", "-", "+", "*", "/"]) == ("1 123 - + * / - + * /")
