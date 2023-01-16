a = 64
b = 28
def nod(a,b):
    g = 1
    while a % 2 == 0 or b % 2 == 0:
        a = a/2
        b = b/2
        g = g*2
    u = a
    v = b
    while u != 0:
        while u % 2 == 0:
            u = u/2
        while v % 2 == 0:
            v = v/2
        if u >= v:
            u = u-v
        else:
            v = v-u
    d = g*v
    return d

if a % 2 == 0 and b % 2 == 0:
    print('v1')
    print(2 * nod(a/2,b/2))
elif a % 2 == 1 and b % 2 == 0:
    print('v2')
    print(nod(a,b/2))
elif b % 2 == 1 and a % 2 == 0:
    print('v3')
    print(nod(b,a/2))
elif a % 2 == 1 and b % 2 == 1 and a > b:
    print('v4')
    print(nod(a-b,b))
elif a == b:
    print(a)