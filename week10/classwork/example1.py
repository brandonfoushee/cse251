import multiprocessing as mp

SUM_RESULTS = []

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def product_all_values(x):
    product = 1
    for i in range(1, x + 1):
        product += i
    return product

def get_sum_cb(result):
    print(f'{result=}')
    SUM_RESULTS.append(result)

def main():
    
    pool_1 = mp.Pool(4)
    pool_2 = mp.Pool(4)
    pool_3 = mp.Pool(6)

    # results_sum = []
    # for x in range(3, 6):
    #     results_sum.append(pool_1.apply_async(sum_all_values, args=(x,)))
    
    # results_product = []
    # for x in range(3, 6):
    #     results_product.append(pool_2.apply_async(product_all_values, args=(x,)))
    
    # for result in results_sum:
    #     answer = result.get()
    #     print(f'sum {answer=}')
        
    # for result in results_product:
    #     answer = result.get()
    #     print(f'product {answer=}')
        
    for x in range(3, 6):
        pool_1.apply_async(func=sum_all_values, args=(x,), callback=get_sum_cb)
    
    pool_1.close()
    pool_1.join()
    print(f'SUM={SUM_RESULTS}')

if __name__ == "__main__":
    main()