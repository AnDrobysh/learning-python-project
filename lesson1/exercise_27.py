'''
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
'''

print('Программа остановится если ввести stop')
a = []
a1 = 0

while True:
    a1 = input('введите число: ')
    if a1 == 'stop':
        break
    a.append(a1)

i = 0
while i < len(a):
    print(a[i])
    i = i + 2