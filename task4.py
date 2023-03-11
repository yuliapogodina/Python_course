"""Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10"""

sum = int(input('Введите, сколько журавликов всего сделано: '))
if sum % 6 != 0:
    print("Решения нет")
else:
    x = sum // 6
    print(f'Сделали журавликов: Петя - {x}, Катя - {x*4}, Сережа - {x}')