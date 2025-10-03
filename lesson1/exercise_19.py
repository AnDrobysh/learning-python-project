'''
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
'''

a = []
b = int(input('Введите количество чисел'))
print('введите', b, ' чисел: ')
for i in range (b):
    new_element = int(input())
    a.append(new_element)

sum = sum(a)
print('summ: ', sum)