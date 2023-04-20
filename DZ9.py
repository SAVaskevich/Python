# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8

n = int(input("Введите размер: "))
array = list()
for i in range(n):
    temp = int(input("Введите записываемое значение: "))
    array.append(temp)

search = int(input("Введите число для поика: "))

temp_1 = abs(search - array[0])

number = array[0]

for i in range(1, len(array)):
    if temp_1 > abs(array[i] - search):
        temp_1 = abs(array[i] - search)
        number = array[i]
print("Ближайшее число ->", number)