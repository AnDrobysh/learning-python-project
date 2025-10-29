import random
game_over = [False]
field = []
snake = [[1, 1], [1,2]]
apple = [None, None]
is_there_an_apple = [False]
snake_last_cell = [None, None]

'''Функция вывода ячейки'''
def print_cell(cymboll):
    print(cymboll, end='  ')

'''Функция получения ячейки по координате'''
def get_cell(x, y, field):
    for cell in field:
        if cell[0] == x and cell[1] == y:
            return cell
    return None

'''Функция создания змеи'''
def create_snake(snake, field):
    for i in snake:
        cell = get_cell(i[0], i[1], field)
        cell[2] = True

'''Функция создания яблока'''
def create_apple(is_there_an_apple, field):
    if not is_there_an_apple[0]:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        cell = get_cell(x, y, field)
        if cell[2]:
            create_apple(is_there_an_apple, field)
        cell[3] = True
        is_there_an_apple[0] = True
        apple[0] = x
        apple[1] = y

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

'''Функция на наличие змеи в змее'''
def is_snake_in_snake(snake):
    for i in range(1, len(snake)):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over[0] = True
            print('Вы врезались в себя')

'''Функция проверки на стену'''
def is_there_a_wall(snake):
    if snake[0][0] == 11 or snake[0][1] == 11 or snake[0][0] == 0 or snake[0][1] == 0:
        game_over[0] = True
        print('Вы врезались в стенку')


'''Функция передвижения змейки'''
def snake_move(snake):
    current_key = input('Введите wasd')
    if current_key != 's' and current_key != 'w' and current_key != 'a' and current_key != 'd':
        print('Введите корректное значение')
        snake_move(snake)
    snake_last_cell[0] = snake[-1][0]
    snake_last_cell[1] = snake[-1][1]

    for i in range(len(snake) - 1, 0, -1):
        snake[i][0] = snake[i - 1][0]
        snake[i][1] = snake[i - 1][1]

    match current_key:
        case 'w':
            snake[0][1] = snake[0][1] + 1
        case 'a':
            snake[0][0] = snake[0][0] - 1
        case 'd':
            snake[0][0] = snake[0][0] + 1
        case 's':
            snake[0][1] = snake[0][1] - 1

    eat_apple(apple, snake_last_cell, snake, field)

'''Функция поедания яблока'''
def eat_apple(apple, snake_last_cell, snake, field):
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        for cell in field:
            if snake[0] == apple:
                cell[3] = False
        snake.append([snake_last_cell[0], snake_last_cell[1]]); '''вот тут была ошибка, добавляли по ссылке а не по значению'''
        is_there_an_apple[0] = False

'''Функция очищения змейки'''
def clear_snake(field):
    for cell in field:
        cell[2] = False

'''Выполнение кода'''
create_field(10, 10)
while not game_over[0]:
    create_snake(snake, field)
    create_apple(is_there_an_apple, field)
    print_field(field)
    clear_snake(field)
    snake_move(snake)
    is_there_a_wall(snake)
    is_snake_in_snake(snake)

print('Вы проиграли! Счёт: ', len(snake))