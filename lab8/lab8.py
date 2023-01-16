import math

#1 
u = '12345'
v = '67898'
b = 10
n = 5
j = n
k = 0
w = []
for i in range(1,n+1):
    w.append((int(u[n-i])+int(v[n-i])+k)%b)
    k = (int(u[n-i])+int(v[n-i])+k) //b
    j -= 1
w.reverse()
print(w)

#2
u = '12345'
v = '67898'
j = n
k = 0
w = []
for i in range(1,n+1):
    w.append((int(u[n-i])+int(v[n-i])+k)%b)
    k = (int(u[n-i])+int(v[n-i])+k) //b
    j -= 1
w.reverse()
print(w)

#3
def s4():
    global k
    global t
    global i
    if i == n:
        i -= 1
    t = int(u[i]) * int(v[j]) + w[i+j] + k
    w[i+j] = t%b
    k = t%b
def s5():
    global i
    global w
    global j
    global k
    i = i-1
    if i > 0:
        s4()
    else:
        w[j] = k
def s6():
    global j
    global w
    j = j - 1
    if j> 0:
        s2()
    if j == 0:
        print(w)
s2()
i = 0
k = 0
t = 1
s4()
s5()
s6()
print(w)

#4
u = "123456789"
n = 7
v = "56789"
t = 4
b = 10
q = []
for j in range(n-t):
    q.append(0)
r = []
for j in range(t):
    r.append(0)

while int(u) >= int(v)*(b**(n-t)):
    q[n-t] = q[n-t] + 1
    u = int(u) - inv(v) * (b**(n-t))
u = str(u)
for i in range(n,t+1,-1):
    v = str(v)
    u = str(u)
    if int(u[i]) > int(v[t]):
        q[i-t-1] = b-1
    else:
        q[i-t-1] = math.floor((int(u[i])*b + int(u[i]))/int(v[t]))
    while (int(q[i-t-1])*(int(v[t])*b + int(v[t-1]))> int(u[i])*(b**2) + int(u[i-1])*b + int(u[i-2])):
        q[i-t-1] = q[i-t-1]-1
    u = int(u) - q[i-t-1]*b**(i-t-1)*int(v)
    if u<0:
        u = int(u) + int(v)*(b**(i-t-1))
        q[i-t-1] = q[i-t-1]-1
r =u 
print(q,r)
