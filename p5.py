def isdivisible1to20(num):
    for i in range(2, 21):
        if num%i != 0:
            return False
    return True

number = 20
while True:
    if isdivisible1to20(number):
        break
    number+=20
print(number)
