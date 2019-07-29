import re
import sys

#pattern = "(\W+|\s+|^)cat(\W+|\s+|$)"
#pattern = r"(\b|\W+)cat(\b|\W+)"
pattern = r"z(.{3})z"

for line in sys.stdin:
    line = line.rstrip()
    #print(re.findall(pattern, line))
    if re.findall(pattern, line):
        print(line)
