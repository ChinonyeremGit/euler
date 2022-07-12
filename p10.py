import math
def primes(num):
    k = 2
    j = 3
    while j <= num:
        isprime = True
        for i in range(2, int(math.sqrt(j)) + 1):
            if j%i == 0:
                isprime = False
                break
        if isprime:
            k += j
        j += 2
    return k
print(primes(2000000))
