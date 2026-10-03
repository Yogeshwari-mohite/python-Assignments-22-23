from multiprocessing import pool
import time
def sum_power(n):
    return sum(i**5 for i in range(1,n+1))

if __name__ == "__main__":
    numbers = [100000,200000,300000]

    start = time.time()
    with Pool() as p: result = p.map(sum_power,numbers)

    end = time.time()

    print(result)
    print("Execution Time:",end - start,"Seconds")