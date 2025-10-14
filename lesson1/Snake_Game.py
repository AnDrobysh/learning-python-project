import random

'''Алгоритм создания поля'''
field = []
k = 0
for k in range(0, 10):
    field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

snake = [[0, 0]]
apple = 0

while True:
    '''Алгоритм создания яблока если прошлое съедено'''
    if apple == 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        field[x][y] = 2
        apple = 1

    '''Алгоритм вывода поля'''
    for i in field:
        print(i)

    '''Алгоритм приема цифры'''
    current_key = 0
    while current_key != '1' and current_key != '2' and current_key != '3' and current_key != '4':
        current_key = input()
    current_key = int(current_key)

    if current_key == 1:
        if snake[-1][1] == 9:
            last = snake[0]
            print(last)
            snake[-1][1] = 0
            if field[snake[-1][0]][snake[-1][1] + 1] != 1 and field[snake[-1][0]][snake[-1][1] + 1] != 2:
                print('popali v tot if')
                append = [snake[-1][0], snake[-1][1]]
                snake.append(append)
                field[last[0]][last[1]] = 0
                snake.remove(last)


            elif field[snake[-1][0]][snake[-1][1]] == 2:
                append = [snake[-1][0], snake[-1][1]]
                snake.append(append)

            elif field[snake[-1][0]][snake[-1][1]] == 1:
                print('Вы проиграли')
                print('Score: ', len(snake))
                break

        elif snake[-1][1] != 9:
            if field[snake[-1][0]][snake[-1][1] + 1] != 1 and field[snake[-1][0]][snake[-1][1] + 1] != 2:
                append = [snake[-1][0], snake[-1][1] + 1]
                snake.append(append)
                field[snake[0][0]][snake[0][1]] = 0
                snake.pop(0)

            elif field[snake[-1][0]][snake[-1][1] + 1] == 2:
                append = [snake[-1][0], snake[-1][1] + 1]
                snake.append(append)

    if current_key == 2:
        if field[snake[-1][0]][snake[-1][1] - 1] != 1 and field[snake[-1][0]][snake[-1][1] - 1] != 2:
            append = [snake[-1][0], snake[-1][1] - 1]
            snake.append(append)
            field[snake[0][0]][snake[0][1]] = 0
            snake.pop(0)

        elif field[snake[-1][0]][snake[-1][1] - 1] == 2:
            append = [snake[-1][0], snake[-1][1] - 1]
            snake.append(append)

        if field[snake[-1][0]][snake[-1][1] - 1] == 1 or snake[-1][1] < 0:
            print('Вы проиграли')
            print('Score: ', len(snake))
            break

    if current_key == 3:
        if snake[-1][0] == 9:
            print('Вы проиграли')
            print('Score: ', len(snake))
            break

        if field[snake[-1][0] + 1][snake[-1][1]] != 1 and field[snake[-1][0] + 1][snake[-1][1]] != 2:
            append = [snake[-1][0] + 1, snake[-1][1]]
            snake.append(append)
            field[snake[0][0]][snake[0][1]] = 0
            snake.pop(0)

        elif field[snake[-1][0] + 1][snake[-1][1]] == 2:
            append = [snake[-1][0] + 1, snake[-1][1]]
            snake.append(append)
        if snake[-1][0] != 9:
            if field[snake[-1][0] + 1][snake[-1][1]] == 1 or snake[-1][1] < 0:
                print('Вы проиграли')
                print('Score: ', len(snake))
                break

    if current_key == 4:

        if field[snake[-1][0] - 1][snake[-1][1]] == 2:
            append = [snake[-1][0] - 1, snake[-1][1]]
            snake.append(append)

        elif field[snake[-1][0] - 1][snake[-1][1]] != 1 and field[snake[-1][0] - 1][snake[-1][1]] != 2:
            append = [snake[-1][0] - 1, snake[-1][1]]
            snake.append(append)
            field[snake[0][0]][snake[0][1]] = 0
            snake.pop(0)

        if field[snake[-1][0] - 1][snake[-1][1]] == 1 or snake[-1][0] == -1:
            print('Вы проиграли')
            print('Score: ', len(snake))
            break

    '''Алгоритм отображающий змейку на поле'''
    i = 0
    for i in snake:
        field[i[0]][i[1]] = 1

    '''Алгоритм проверки съедено ли яблоко'''
    if field[x][y] != 2:
        apple = 0