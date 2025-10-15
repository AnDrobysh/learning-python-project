# есть ошибка которую нельзя решить без функций и рекурсии, какая?

import random

fields = []
number_on_field = 0
snake = [[0, 9]]
apple = [random.randint(2, 10), random.randint(1, 9)]
game_over = False
counter = 0
while True:
    fields = []
    for x in range(0, 10):
        for y in range(0, 10):
            fields.append([y, x, 0, 0])

    # установка яблока на поле
    for x in fields:
        if x[0] == apple[0] and x[1] == apple[1]:
            x[2] = 1

    # установка змеи на поле
    for y in snake:
        for x in fields:
            if x[0] == y[0] and x[1] == y[1]:
                x[3] = 1

    # рисование поля с учётом условий
    for x in range(0, 10):
        for y in range(0, 10):
            if fields[number_on_field][2] == 0 and fields[number_on_field][3] == 0:
                print("▢", end="  ")
            elif fields[number_on_field][2] == 1:
                print("A", end="  ")
            elif fields[number_on_field][3] == 1:
                print("S", end="  ")
            number_on_field = number_on_field + 1
        print()
    number_on_field = 0

    # обработать ввод
    direction = input('')
    for s in range(len(snake) - 1, -1, -1):
        if direction == "w" or "s" or "a" or "d" or "0":
            if direction == "0":
                game_over = "true"
            elif direction == "w" or "s" or "a" or "d":
                if s == 0:
                    if direction == "w":
                        snake[0][1] = snake[0][1] - 1
                        if snake[s][1] == 10:
                            snake[s][1] = 0
                        elif snake[s][1] == -1:
                            snake[s][1] = 9
                    elif direction == "s":
                        snake[s][1] = snake[s][1] + 1
                        if snake[s][1] == 10:
                            snake[s][1] = 0
                        elif snake[s][1] == -1:
                            snake[s][1] = 9
                    elif direction == "a":
                        snake[s][0] = snake[s][0] - 1
                        if snake[s][0] == 10:
                            snake[s][0] = 0
                        elif snake[s][0] == -1:
                            snake[s][0] = 9
                    elif direction == "d":
                        snake[s][0] = snake[s][0] + 1
                        if snake[s][0] == 10:
                            snake[s][0] = 0
                        elif snake[s][0] == -1:
                            snake[s][0] = 9
                else:
                    snake[s][0] = snake[s-1][0]
                    snake[s][1] = snake[s - 1][1]
        else:
            print("Enter correct number")

    # поедание яблок
    if apple[0] == snake[0][0] and apple[1] == snake[0][1]:
        apple = [random.randint(0, 9), random.randint(0, 9)]
        counter = counter + 1
        if direction == "w":
            snake.append([snake[len(snake) - 1][0], snake[len(snake) - 1][1] + 1])
        elif direction == "s":
            snake.append([snake[len(snake) - 1][0], snake[len(snake) - 1][1] - 1])
        elif direction == "a":
            snake.append([snake[len(snake) - 1][0] + 1, snake[len(snake) - 1][1] - 1])
        elif direction == "d":
            snake.append([snake[len(snake) - 1][0] - 1, snake[len(snake) - 1][1] - 1])

    if game_over:
        print("Ваш счёт " + str(counter))
        break
