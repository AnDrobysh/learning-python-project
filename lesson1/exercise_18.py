'''
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
'''

a = []
print('введите 10 чисел: ')
for i in range (10):
    new_element = int(input())
    a.append(new_element)

print(a)
sum = sum(a)
print('summ: ', sum)