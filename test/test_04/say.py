import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trax("hello, " + sys.argv[1])
