# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int (input ("Веедите число: "))
sum = 0
while n > 0:
    temp = n % 10
    sum = sum + temp
    n = n // 10
print(sum)

