import re
import sys

#pattern = "(\W+|\s+|^)cat(\W+|\s+|$)"
#pattern = r"(\b|\W+)(\w+)\2(\b|\W+)"
pattern = r"(\b)a+(\b)"


for line in sys.stdin:
    line = line.rstrip()
    sub_pattern = re.search(pattern, line, re.IGNORECASE)
    # print(sub_pattern.group())
    if sub_pattern:
        print(re.sub(sub_pattern.group(), "argh", line, count=1))


#[print(re.sub(r"\b([Aa]+)\b", "argh", line, 1).rstrip()) for line in sys.stdin]
