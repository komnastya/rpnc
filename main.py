from calc import calc
from mytypes import ArgError, ParseError
from parse_exp import parse_exp
from print_exp import print_exp

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
                parsed_exp = parse_exp(input_exp)
                print(f"The result of '{print_exp(parsed_exp)}' is {calc(parsed_exp)}")
            except ParseError as error:
                print(error)
                print("Please, enter correct expression")
            except ArgError as error:
                print(error)  # TODO


if __name__ == "__main__":
    main()
