for i in range(100, 500):
    for j in range(200,600):
        for k in range(300, 1000):
            if i + j + k == 1000 and i**2 + j**2 == k**2:
                print(i*j*k)
                break
