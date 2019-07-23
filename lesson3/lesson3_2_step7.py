n = 0
slice = []

# s = "abababa"
# t = "aba"

s, t = str(input()), str(input())

while len(s) >= len(t):
    slice.append(s[:len(t)])
    s = s[1:]

print(slice.count(t))

#print(len([i for i in range(0, len(s) - len(t) + 1) if s[i: i + len(t)] == t]))