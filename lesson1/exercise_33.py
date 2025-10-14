'''
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.

Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
 После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
'''
from operator import index


print('Ввод чисел остановится если ввести stop')
array = []
enter_number = 0

while True:
    enter_number = input('введите число: ')

    if str(enter_number) == 'stop':
        break

    if 200 > int(enter_number) > 1:
        array.append(int(enter_number))
    else:
        print('Введите другое значение')

height = int(input('Введите рост Пети: '))
if height <= 200:
    array.append(height)

i = 0
j = 1
num = 0
quit_number = 0
empty_number = 0
while empty_number != len(array):
    empty_number += 1

    if array[i] < array[j]:
        array[i], array[j] = array[j], array[i]
        empty_number = 0

    i += 1
    j += 1
    if i == len(array) - 1:
        i = 0

    if j == len(array):
        j = 1

    num += 1
print('Список учеников по росту: ', array)
print('Место пети от начала: ', array.index(height) + 1)
