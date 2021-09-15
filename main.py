from calc import calc
from mytypes import ArgError, ParseError
from parse_exp import parse_exp

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
                print(f"The result of '{input_exp}' is {calc(parse_exp(input_exp))}")
            except (ParseError, ArgError):
                print("There is an invalid input")
                print("Please, enter correct expression")


main()

if __name__ == "__main__":
    main()
