import random
field = []
snake = [[1, 1]]
is_there_an_apple = False

'''Функция вывода ячейки'''
def print_cell(cymboll):
    print(cymboll, end='  ')

'''Функция получения ячейки по координате'''
def get_cell(x, y, field):
    for cell in field:
        if cell[0] == x and cell[1] == y:
            return cell
    return None

'''Функция создания змею'''
def create_snake(snake, field):
    for i in snake:
        cell = get_cell(i[0], i[1], field)
        cell[2] = True

'''Функция создания яблока'''
def create_apple(is_there_an_apple, field):
    if not is_there_an_apple:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        cell = get_cell(x, y, field)
        if cell[2]:
            create_apple(is_there_an_apple, field)
        cell[3] = True
        return field

'''Функция создания поля'''
def create_field(x, y):
    for i in range(y, 0, -1):
        for j in range(1, x + 1):
            field.append([j, i, False, False])

'''Функция прорисовки поля'''
def print_field(field):
    for cell in field:
        if cell[2]:
            print_cell('s')
        elif cell[3]:
            print_cell('*')
        else:
            print_cell('0')
        if cell[0] % 10 == 0:
            print()

'''Выполнение кода'''
create_field(10, 10)
create_snake(snake, field)
create_apple(is_there_an_apple, field)
print_field(field)
