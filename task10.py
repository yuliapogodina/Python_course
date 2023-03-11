'''На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть'''

n = int(input('Сколько монет на столе: '))
count = 0
for i in range(n):
    face = int(input('Введите 1 если орел, иначе 0: '))
    if face != 0:
        count += 1
if count <= (n - count):
    print(f'Надо перевернуть {count} монет')
else:
    print(f'Надо перевернуть {n - count} монет')