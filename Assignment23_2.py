from multiprocessing import Pool
import os

def Odd_Sum(n):
    odd = 0

    for i in range(1,n+1,2):
        odd = odd + i
        
    print("PID:",os.getpid())
    print("Sum of Odd Numbers:",odd)
    return odd


if __name__ == "__main__":
    
    numbers = [10]
    with Pool (1) as p: result = p.map(Odd_Sum,numbers)

    print("result=",result)