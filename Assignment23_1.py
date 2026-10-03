from multiprocessing import Pool
import os

def SumEven(n):
    sum = 0

    for i in range(2,n+1,2):
        sum = sum + i
        
    print("PID:",os.getpid(),"sum:",sum)
    return sum


if __name__ == "__main__":
    p = Pool(4)
    numbers = [10,20,30,40]
    with Pool (processes = 4) as p: result = p.map(SumEven,numbers)

    print("result=",result)