text = 'криптографиясерьезнаянаука'
key = 'математикаматематикаматема'
alfavit = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
itog = ''

for i in range(len(text)):
    x1 = alfavit.find(text[i])
    x2 = alfavit.find(key[i])
    x3 = x1+x2
    if x3 < len(alfavit):
        itog += alfavit[x3]
    else:
        itog += alfavit[x2 + x1 - len(alfavit)]
print(itog)
