import csv
from collections import Counter

list2015 = []

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if '/2015' in row['Date']:
            list2015.append(row['Primary Type'])

print(Counter(list2015).most_common())