from multiprocessing import Pool
import os

def Factorial(n):
    fact = 1

    for i in range(1,n + 1):
        fact = fact * i

    print("Process Id:",os.getpid())

    print("input number:",n)
    print("Factorial:",fact)
    print()

if __name__ == "__main__":
    Data = [10,15,20,25]

    with Pool(4) as p : p.map(Factorial,Data)
