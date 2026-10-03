from multiprocessing import Pool

def prime_count(n):
    count = 0

    for num in range(2,n + 1):
        prime = True

        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                prime = False
                break

        if prime:
                count += 1

    return count
    
if __name__ == "__main__":
    numbers = [10,20,30]
    with Pool() as p: result = p.map(prime_count,numbers)

    for n,c in zip(numbers,result):
        print("prime numbers between 1 and", n,"=",c)