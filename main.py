from calc import calc
from parse import parse

assert calc(parse("3 5 + 7 2 – *")) == 40
