from calc import calc
from mytypes import ArgError, ParseError
from parse import parse

print("Hello!")
print("Welcome to the calculator!")


def main():
    while True:
        input_exp = input(
            "Please, input the expression in Reversed Polish Notation: "
        ).strip()
        if input_exp == "stop":
            print("Good bye!")
            break
        else:
            try:
                print(f"The result of '{input_exp}' is {calc(parse(input_exp))}")
            except (ParseError, ArgError):
                print("There is an invalid input")
                print("Please, enter correct expression")
                continue


main()
