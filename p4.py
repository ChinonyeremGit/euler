def ispalindrome(num):
    return str(num) == str(num)[::-1]
m = 0
for first_num in range(100, 1000):
    for second_num in range(100, 1000):
        p = first_num * second_num
        if ispalindrome(p) and p > m:
            m = p

print(m)
def ispalindromes(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num%10
        rev = rev * 10 + dig
        num = num//10
    if temp == rev:
        print(rev)

ispalindromes(123321)
