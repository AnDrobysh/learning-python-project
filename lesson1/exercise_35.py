import random
from operator import index

array = []
index = 0

for i in range(1, 30):
    num = random.randint(1, 30)
    array.append(num)

print(array)
i = 0
j = 0
array_not_simple = []
array_simple = array
for i in array:
    for j in range(2, i - 1):
        if i % j == 0:
            array_not_simple.append(i)
            print('lll', i)
            break

for i in array_not_simple:

    for j in array:

        if i == j:
            array.remove(i)
            print('remove: ', i)


print(array)