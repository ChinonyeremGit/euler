l1= [1]
l2 = [2]
l = []
while sum(l) < 5000000:
    m1 = l1.pop()
    m2 = l2.pop()
    if m1 %2 == 0:
        l.append(m1)
    l1.append(m2)
    l2.append(m1+m2)
l.pop()
print(sum(l))
