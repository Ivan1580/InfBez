import random
n = 5
a = random.randint(0,n-1)
g = 1
if a < 0:
    a = -a
    if (n % 4 == 3):
        g = -g
if a == 1:
    print(g)
while(a):
    if (a<0):
        a = -a
        if (n % 4 == 3):
            g = -g
    while (a%2 ==0):
        a = a//2
        if (n% 8== 3 or n% 8 ==5):
            g = -g
    a,n = n,a
    if (a%4 == 3 and n%4 ==3):
        g = -g
    a = a%n
    if (a>n//2):
        a = a-n
if (n==1):
    print(g)
    
