'''
Даны два целых числа A и В, A>B.
Выведите все нечётные числа от A до B включительно, в порядке убывания.
В этой задаче можно обойтись без инструкции if.
'''

a = int(input())
b = int(input())

if a > b:
    if a % 2 == 0 and b % 2 == 0:
        a -= 1
        print(a)
        while a != b + 1:
            a -= 2
            print(a)

    if a % 2 != 0 and b % 2 == 0:
        print(a)
        while a != b + 1:
            a -= 2
            print(a)

    if a % 2 == 0 and b % 2 != 0:
        a -= 1
        print(a)
        while a != b:
            a -= 2
            print(a)

    if a % 2 != 0 and b % 2 != 0:
        print(a)
        while a != b:
            a -= 2
            print(a)


'''
как без if сделать наверное и не представляю
'''