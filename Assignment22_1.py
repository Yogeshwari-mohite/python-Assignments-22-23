from multiprocessing import Pool

def Sum_Square(n):
    total = 0

    for i in range(1, n + 1):
        total += i * i
    return total

if __name__ == "__main__":
        numbers = [1000000,2000000,3000000]
        with Pool () as p : result = p.map(Sum_Square,numbers)
        print(result)