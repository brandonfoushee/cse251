


def factorial_rec(n, values):
    
    #Base Case
    if n == 1:
        values[n] = 1
        return 1
    
    product = n * factorial_rec(n - 1, values)
    values[n] = product
    return product

values = {}

fac = factorial_rec(5, values)
# 5 * 4 * 3 * 2 * 1 = 120
assert fac == 120
print("It worked!")
print(values)

# n = 5 : product = 5 * fac(4)
# n = 4 : product = 4 * fac(3)
# n = 3 : product = 3 * fac(2)
# n = 2 : product = 2 * fac(1)
# n = 1 : return 1