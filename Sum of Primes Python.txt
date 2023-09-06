import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

primeSums = 0

for x in range(2,2000000):
    if isPrime(x) == True:
        primeSums += x

print("Sums of primes under 2000000 is =", primeSums)