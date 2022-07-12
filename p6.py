def sum_of_squares():
    b = 0
    for i in range(1, 101):
        b+= i**2
    return b
    #return sum[i**2 for i in range(a, b)]
def square_of_sum():
    b = 0
    for i in range(1, 101):
        b+=i
    return b**2
    #return sum[i for i in range(a, b)]**2

num = square_of_sum() - sum_of_squares()
print(num)
