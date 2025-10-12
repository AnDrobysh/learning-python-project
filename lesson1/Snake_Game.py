from _pyrepl.commands import clear_screen
import keyboard
import numpy as np
import time
import os
clear = lambda: os.system('cls')


matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],])
'''
def right():
    
def left():
    
def up():

def down():    
'''
iteration = 0
snake_length = 2
lose = 0
position_column = 0
position_line = 0
current_key = ''
up_count = 0
left_count = 0
down_count = 0
right_count = 0
print('позиция в линии в самом начале: ', position_line)
print('right_count в самом начале: ', right_count)
print('snake_length в самом начале: ', snake_length)
while lose != 1:
    # print('позиция в линии с которой заходим в циклы: ', position_line)
    # print('right_count с которой заходим в циклы: ', right_count)
    # print('snake_length с которой заходим в циклы: ', snake_length)
    if keyboard.is_pressed('w'):
        current_key = 'up'
    elif keyboard.is_pressed('a'):
        current_key = 'left'
    elif keyboard.is_pressed('s'):
        current_key = 'down'
        print('зарегестрированна S')
    elif keyboard.is_pressed('d'):
        current_key = 'right'
        print('зарегестрированна D')

    # print('current key: ', current_key)

    if current_key == 'up':
        matrix[position_line][position_column] += 1

    elif current_key == 'left':
        if left_count != snake_length:
            matrix[position_line][(position_column + 1) - snake_length] = 0
            position_line += 1
            matrix[position_line][position_column] += 1
            matrix[position_line - snake_length][position_column] = 0
            down_count += 1
            if position_line > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break
        elif left_count >= 0:
            position_line += 1
            matrix[position_line - snake_length][position_column] = 0
            matrix[position_line][position_column] += 1
            if position_line > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break

    elif current_key == 'down':
        if down_count != snake_length:
            matrix[position_line][(position_column + 1) - snake_length] = 0
            position_line += 1
            matrix[position_line][position_column] += 1
            matrix[position_line - snake_length][position_column] = 0
            down_count += 1
            if position_line > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break
        elif down_count >= 0:
            position_line += 1
            matrix[position_line - snake_length][position_column] = 0
            matrix[position_line][position_column] += 1
            if position_line > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break

    elif current_key == 'right':
        if right_count != snake_length:
            position_column += 1
            right_count += 1
            matrix[position_line][position_column] += 1
            if position_column > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break
        elif right_count >= 0:
            position_column += 1
            matrix[position_line][position_column - snake_length] = 0
            matrix[position_line][position_column] += 1
            if position_column > len(matrix) + 1:
                print('ВЫ ПРОИГРАЛИ')
                break
    time.sleep(0.5)
    print("\n" * 5)
    print(matrix)


