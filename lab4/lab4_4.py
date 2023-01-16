a = 426
b = 334
g = 1
while a % 2 == 0 and b % 2 == 0:
    a = a/2
    b = b/2
    g = g*2
u = a
v = b
A,B,C,D = 1,0,0,1
while u != 0:
    while u % 2 == 0:
        u = u/2
        if A % 2 == 0 and B % 2 == 0:
            A = A/2
            B = B/2
        else:
            A = (A+b)/2
            B = (B-a)/2
    while v % 2 == 0:
        v = v/2
        if C % 2 == 0 and D % 2 == 0:
            C = C/2
            D = D/2
        else:
            C = (C+b)/2
            D = (D-a)/2
    if u>=v:
        u = u-v
        A = A-C
        B = B-D
    else:
        v = v-u
        C = C-A
        D = D-B
    d = g*v
    x = C
    y = D
print(d,x,y)
