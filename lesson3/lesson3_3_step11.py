import re
import sys

#pattern = "(\W+|\s+|^)cat(\W+|\s+|$)"
#pattern = r"(\b|\W+)(\w+)\2(\b|\W+)"

for line in sys.stdin:
    line = line.rstrip()
    #print(re.findall(pattern, line))
    if re.findall('human', line, re.IGNORECASE):
        print(re.sub('human', 'computer', line))
