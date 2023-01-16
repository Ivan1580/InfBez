message = input("Введите сообщение: ").upper()
alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
itog = ''
for i in message:
    x = alfavit.find(i)
    itog += alfavit[len(alfavit)-x-1]
print(itog)
