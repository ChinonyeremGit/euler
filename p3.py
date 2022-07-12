n = 600851475143
l = []
i = 2
while i*i<n:
    if n%i ==0:
        l.append(i)
        n = int(n/i)
    i+=1
print(n)
import math
def factors(num):
    factor = []
    for i in range(1, int(math.sqrt(num))+1):
        if num%i ==0:
            factor.append(i)
            factor.append(int(num/i))
    return factor
def isPrime(num):
    return len(factors(num)) == 2
largest_prime = 0
for i in factors(600851475143):
    if isPrime(i) and i > largest_prime:
        largest_prime = i
print(largest_prime)
