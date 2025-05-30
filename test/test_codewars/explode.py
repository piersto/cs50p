import re


def explode(s):
    x_end = ""
    for i in s:
        x = (i * int(i))
        x_end = x_end + x
    return x_end
