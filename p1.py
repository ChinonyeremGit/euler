l = []
for i in range(1, 1000):
    if i % 3 == 0:
        l.append(i)
for n in range(1, 1000):
    if n % 5 == 0:
        l.append(n)
print(sum(set(l)))
