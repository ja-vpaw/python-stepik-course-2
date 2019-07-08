def closest_mod_5(x):
    if int(x):
        x=int(x)
        while x % 5 != 0:
            x += 1
        return x
    else:
        return "x is not int"

b = input("Введите целое число: ")
print(closest_mod_5(b))
