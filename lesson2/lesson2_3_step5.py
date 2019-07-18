import itertools


def primes():
    ret = 2
    while True:
        if all(ret % div != 0 for div in range(2, ret - 1)):
            yield ret
        ret += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
