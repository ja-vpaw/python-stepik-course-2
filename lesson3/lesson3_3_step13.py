import re
import sys

#pattern = "(\W+|\s+|^)cat(\W+|\s+|$)"
#pattern = r"(\b|\W+)(\w+)\2(\b|\W+)"
pattern = r"(\b)\w\w+(\b)"


for line in sys.stdin:
    line = line.rstrip()
    words_start = [m.start() for m in re.finditer(pattern, line)]
    # print(words_start)
    for i in words_start:
        line = line[:i]+line[i+1]+line[i]+line[i+2:]

    print(line)

# for line in sys.stdin:
#     line = line.strip()
#     line = re.sub(r"\b(\w)(\w)", r"\2\1", line)
#     print(line)
