def factorial(n, values):
    
    # base case
    if n == 1:
        return 1
    
    product = n * factorial(n-1, values)
    values[n] = product
    return product

values = {}
product = factorial(5, values)
print(f'{product=}')
print(f'{values=}')