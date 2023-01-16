def nod(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = nod(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
a = nod(426, 334)
print(f'Делитель равен {a[0]}, x = {a[1]}, y = {a[2]}')