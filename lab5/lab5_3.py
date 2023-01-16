import random
n = 7
r = 3
n0 = 2**S * r
a = random.randint(2,n-3)
y = a**r % n
if y != 1 and y != n-1:
    j = 1
    if j <= S-1 and y != n-1:
        y = y**2 % n
        if y == 1:
            print(f'Число {n} составное')
        j += 1
    elif y != n-1:
        print(f'Число {n} составное')
else:
    print(f'Число {n},вероятно,простое')