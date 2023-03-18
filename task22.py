'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.'''

n = int(input('кол-во элементов 1 множества: '))
m = int(input('кол-во элементов 2 множества: '))
x = {int(input('Число 1 набора: ')) for _ in range(0, n)}
y = {int(input('Число 2 набора: ')) for _ in range(0, m)}
z = x.intersection(y)
res = []
for i in z:
    res.append(i)
res.sort()
print(res)
