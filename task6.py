'''Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет
с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no'''

num = input("Номер билета: ")
i = 0
a = 0
b = 0
j = len(num)
while i < j / 2:
    a += int(num[i])
    b += int(num[j - 1 - i])
    i = i + 1
if a == b:
    print("да")
else:
    print("нет")
