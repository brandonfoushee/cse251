def factorial_rec(n: int, values: dict):
    
    # Base Case
    if n == 1:
        values[n] = 1
        return 1
    
    product = n * factorial_rec(n - 1, values)
    values[n] = product
    return product
    

values = {}
product = factorial_rec(5, values)
print(f'{values=}')

# n = 5 : product = 5 * (fac(4) = 24) ---> returns 120
# n = 4 : product = 4 * (fac(3) = 6) --> 24
# n = 3 : product = 3 * (fac(2) = 2) --> 6
# n = 2 : product = 2 * (fac(1) = 1) --> 2
# n = 1 : return 1