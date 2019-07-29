import re
import sys

#pattern = "(\W+|\s+|^)cat(\W+|\s+|$)"
#pattern = r"(\b|\W+)(\w+)\2(\b|\W+)"
pattern = r"(\w)(\1)+"
repl = r"\1"


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, repl, line))
