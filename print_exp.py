from mytypes import ArgList


def print_exp(args: ArgList) -> str:
    return " ".join((str(arg) for arg in args))
