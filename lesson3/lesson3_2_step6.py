n = 0

# s = "abab"
# a = "ab"
# b = "ba"

s = str(input())
a = str(input())
b = str(input())

while a in s:
    if n > 1000:
        print('Impossible')
        break
    n +=1
    #print(s.replace(a,b))
    s = s.replace(a,b)
else:
    print(n)


# s, a, b, count = input(), input(), input(), 0
# while (s.__contains__(a) and not b.__contains__(a)) and not a.__eq__(b):
#     s = s.replace(a, b)
#     count += 1
# print("Impossible") if (b == a or b.__contains__(a)) and s.__contains__(a) else print(count)