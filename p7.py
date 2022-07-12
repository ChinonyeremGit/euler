import math
def primefactors():
    lst= []
    num = 2
    while len(lst) != 10001:
        isprime = True
        for potentialfactor in range(2, int(math.sqrt(num)) + 1):
            if num%potentialfactor == 0:
                isprime = False
                break
        if isprime:
            lst.append(num)
        num += 1

    return lst
print(primefactors()[-1])
