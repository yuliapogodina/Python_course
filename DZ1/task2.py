"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""

a = int(input('Введите трехзначное число: '))
sumof = 0
while a > 0:
    sumof += a % 10
    a = a // 10
print(f'Сумма цифр числа = {sumof}')