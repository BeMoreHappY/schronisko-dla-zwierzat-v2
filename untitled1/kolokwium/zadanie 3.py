def nieparzyste(n):
    for i in range(1, n, 2):
        yield i


def potegi(x):
    for i in range(0, x):
        yield i**2


def minus_plus(n):
    for i in range(n, 1):
        yield i
        a = minus_plus(i)
        if i != 0:
            print(a.__next__()*-1)



for i in minus_plus(-199):
    print(i)

for i in nieparzyste(10000):
    print(i)








