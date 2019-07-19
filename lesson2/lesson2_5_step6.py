def mod_checker_no_lambda(x, mod=0):
    def l(y):
        if y % x == mod:
            return True
        else:
            return False
    return l


def mod_checker(x, mod=0):
    return lambda y: y % x  == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True

# В одну строку
mod_checker = lambda x, mod=0: lambda y: y % x == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
