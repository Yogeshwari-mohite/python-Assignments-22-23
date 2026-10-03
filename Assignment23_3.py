from multiprocessing import Pool
import os

def EvenCount(n):
    count = 0

    for i in range(1,n + 1):
        if i % 2 == 0:
            count = count +1

    print("Process Id:",os.getpid())

    print("input number:",n)
    print("Even number count:",count)
    print()

if __name__ == "__main__":
    Data = [100000,200000,300000,400000]

    with Pool(4) as p : p.map(EvenCount,Data)
