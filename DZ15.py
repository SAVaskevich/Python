# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Ввведите первый элемент: "))
d = int(input("Введите второй элемент: "))
n = int(input("Введите лдинну массива: "))
mass = []
for i in range(n):
   temp = (a1 + i * d)
   mass.append(temp)
print("Итог -> ", mass)