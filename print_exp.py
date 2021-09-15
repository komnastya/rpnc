from mytypes import ArgList


def print_exp(args: ArgList) -> str:
    s = ""
    for arg in args:
        s = s + str(arg) + " "
    return s.strip()
