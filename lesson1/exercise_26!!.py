'''
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
'''

print('Программа остановится если ввести Enter')
a = []
a1 = 0
i = 0


while True:
    a1 = input('введите число: ')
    if a1 == '':
        break
    a.append(int(a1))

scores = [0, 0, 0]
s = 0
position = 0
while i < len(a) - 1:
    if a[i] == a[i + 1]:
        time = i
        scores[position] += 2
        i += 1
        while time + 1 < len(a) - 1 and a[time + 1] == a[time + 2]:
            scores[position] += 1
            time += 1
        position += 1
    i += 1
    time = 0

print('Наибольшее число подряд идущих элементов этой последовательности: ', max(scores))