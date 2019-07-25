import re
import sys

#pattern = r"[\s*\w*]*(cat)[\s*\w*]*(\1)[\s*\w*]*"
pattern = r".*cat.*cat.*"

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)

    print(line.count('cat'))
