regim = input("Введите режим шифрования SH(шифрование)/DESH(дешифрование): ")
k = int(input("Введите ключ K :"))
message = input("Введите сообщение: ").upper()
alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
itog = ''
if regim == "SH":
    for i in message:
        x = alfavit.find(i)
        if x + k < len(alfavit):
            itog += alfavit[x+k]
        else:
            itog += alfavit[k - len(alfavit) +x]
else:
    for i in message:
        x = alfavit.find(i)
        if x - k >= 0:
            itog += alfavit[x-k]
        else:
            itog += alfavit[len(alfavit)+k-x] 
print(itog)

