def dekorator(a, b, c):
    def f(x):
        return a*x**2 + b*x +c
    return f

f1 = dekorator(1, 2, 1)
print(f1(5))
def g(f):
    return f(0)

print(g(f1))