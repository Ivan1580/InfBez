k = 'Нельзя недооценивать противника'.lower()
k2 = ''
alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n = 6
m = 5
l = []
key = 'пароль'
itog = ''
for i in k:
    if i not in alfavit:
        continue
    else:
        k2 += i
if len(k2) < n*m:
    k2 += alfavit[:n*m-len(k2)]
print(k2)

for i in range(m):
    l.append([i for i in k2[i*n:i*n+n]])
dic = {}
for i in range(len(key)):
    dic.setdefault(key[i],i)
sorted_dic = dict(sorted(dic.items()))   
x = ''
for key, value in sorted_dic.items():
    for i in range(m):
        x += l[i][value]
    itog += x
    x = ''
print(itog)
