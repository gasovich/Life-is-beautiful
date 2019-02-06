# Игра "Жизнь" (игра Конвея)

import graphics as gr
import math as m
import random as r

def paint_cell(p, q, sz):
	live_cell = gr.Rectangle(gr.Point(p * sz, q * sz),gr.Point((p + 1) * sz, (q + 1) * sz))
	live_cell.setFill('green')
	live_cell.setOutline('red')
	live_cell.draw(graph_window)

field_width = 50 # Ширина игрового поля (чмсло ячеек по горизонтали)
field_lenght = 30 # Длина игрового поля (число ячеек по вертикали)
cell_size = 10 # Размер ячейки (сторона квадрата)

win_widht = field_width * cell_size # Высота окна
win_lenght = field_lenght * cell_size # Ширина окна
grid_step = 20 # Шаг сетки
grid_color = 'blue'

# Отрисовка главного окна
graph_window = gr.GraphWin("*** Ж И З Н Ь ***", win_widht, win_lenght)

# Инициализация массивов, представляющих игровое поле. 
# False озеачает пустую (мертвую) клетку
A_field = [[False for i in range(field_lenght)] for j in range(field_width)] # Поле текущего состояния
B_field = [[False for i in range(field_lenght)] for j in range(field_width)] # Поле следующего хода
Neighbour_field =  [[0 for i in range(field_lenght)] for j in range(field_width)] # Количество соседей у клетки

# Заполняем поле А случайными логическими значениями. Это будет стартовая конффигурация
# Если ячейка равна True, то она сразу зарисовывается
r.seed()
for i in range(0, field_width):
	for j in range(0, field_lenght):
		A_field[i][j] = r.randint(0,1) == 0
		if A_field[i][j]:
			paint_cell(i, j, cell_size)

#------------Считаем число соседей для каждой клетки в поле текущего хода

# 	Левый верхний угол
counter = 0
if A_field[0][1]:
	counter += 1
if A_field[1][1]:
	counter += 1
if A_field[1][0]:
	counter += 1
Neighbour_field[0][0] = counter

#	Правый верхний угол
counter = 0
if A_field[field_width - 2][0]:
	counter += 1
if A_field[field_width - 2][1]:
	counter += 1
if A_field[field_width - 1][1]:
	counter += 1
Neighbour_field[field_width - 1][0] = counter

#	Правый нижний угол
counter = 0
if A_field[field_width - 2][field_lenght - 1]:
	counter += 1
if A_field[field_width - 2][field_lenght - 2]:
	counter += 1
if A_field[field_width - 1][field_lenght - 2]:
	counter += 1
Neighbour_field[field_width - 1][field_lenght - 1] = counter

#	Левый нижний угол
counter = 0
if A_field[1][field_lenght - 1]:
	counter += 1
if A_field[1][field_lenght - 2]:
	counter += 1
if A_field[0][field_lenght - 2]:
	counter += 1
Neighbour_field[0][field_lenght - 1] = counter

#	Подсчет соседей по верхней стороне поля
for i in range(1, field_lenght - 1):
	counter = 0
	if A_field[0][i + 1]:
		counter += 1
	if A_field[1][i + 1]:
		counter += 1
	if A_field[1][i]:
		counter += 1
	if A_field[1][i - 1]:
		counter += 1
	if A_field[0][i - 1]:
		counter += 1
	Neighbour_field[0][i] = counter

# Подсчет соседей по правой стороне поля
for i in range(1, field_width - 1):
	counter = 0
	if A_field[i - 1][field_lenght - 1]:
		counter += 1
	if A_field[i - 1][field_lenght - 2]:
		counter += 1
	if A_field[i][field_lenght - 2]:
		counter += 1
	if A_field[i + 1][field_lenght - 2]:
		counter += 1
	if A_field[i + 1][field_lenght - 1]:
		counter += 1
	Neighbour_field[i][field_lenght - 1] = counter

# Подсчет соседей по нижней стороне поля
for i in range(1, field_lenght - 1):
	counter = 0
	if A_field[field_width - 1][i + 1]:
		counter += 1
	if A_field[field_width - 2][i + 1]:
		counter += 1
	if A_field[field_width - 2][i]:
		counter += 1
	if A_field[field_width - 2][i - 1]:
		counter += 1
	if A_field[field_width - 1][i - 1]:
		counter += 1
	Neighbour_field[field_width - 1][i] = counter

# Подсчет соседей по левой стороне поля
for i in range(1, field_width - 1):
	counter = 0
	if A_field[i - 1][0]:
		counter += 1
	if A_field[i - 1][1]:
		counter += 1
	if A_field[i][1]:
		counter += 1
	if A_field[i + 1][1]:
		counter += 1
	if A_field[i + 1][0]:
		counter += 1
	Neighbour_field[i][0] = counter

#	Подсчет соседей для внутренних ячеек игрового поля
for i in range(1, field_width -1):
	for j in range(1, field_lenght - 1):
		counter = 0
		if A_field[i - 1][j - 1]:
			counter += 1
		if A_field[i - 1][j]:
			counter += 1
		if A_field[i - 1][j + 1]:
			counter += 1
		if A_field[i][j - 1]:
			counter += 1
		if A_field[i][j + 1]:
			counter += 1
		if A_field[i + 1][j - 1]:
			counter += 1
		if A_field[i + 1][j]:
			counter += 1
		if A_field[i + 1][j + 1]:
			counter += 1
		Neighbour_field[i][j] = counter
#------------Подсчет числа соседей закончен----------------------------

# Копируем игровое поле для расчета следующего хода
B_field[i][j] = [[A_field[i][j] for i in range(field_width)] for j in range(field_lenght)]

# Рассчет следующей конфнурации в буферном массиве
for i in range(field_width):
	for j in range(field_lenght):
		if A_field[i][j]: # Если клетка живая
			if Neighbour_field[i][j] in [0, 1, 4, 5, 6, 7, 8]:
				B_field[i][j] = False # Кдетка умирает от одиночества или перенаселения
		else: # Если клетка  мертвая
			if Neighbour_field[i][j] == 3:
				Neighbour_field[i][j] = True # Клетка оживает

A_field[i][j] = [[A_field[i][j] for i in range(field_width)] for j in range(field_lenght)]
		
		
			

# print(Neighbour_field)

# print(A_field)

graph_window.getMouse()
