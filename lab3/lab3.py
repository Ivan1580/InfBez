alfavit = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
slovo = 'приказ'
gamma = 'гаммаг'
itog = ''
for i in range(len(slovo)):
    print(alfavit.find(slovo[i]),alfavit.find(gamma[i]))
    itog += alfavit[(alfavit.find(slovo[i])+1 + (alfavit.find(gamma[i])+1) % 33)-1]
print(itog)