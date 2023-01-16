import random
n = 23
a = random.randint(2,n-2)
r = a**(n-1) % n
if r == 1:
    print(f'Число {n}, вероятно, простое')
else:
    print(f'Число {n} составное')