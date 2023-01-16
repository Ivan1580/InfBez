a = 64
b = 28
def nod(a,b):
    r0 = a
    r1 = b
    i = 1
    ri = 1
    while ri != 0:
        ri  = r0%r1
        d = r1
        r0 = r1
        r1 = ri
    return d
print(nod(a,b))