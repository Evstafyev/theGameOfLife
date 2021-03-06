"""Главный скрипт проекта."""
import turtle
from random import choice

# Глобальный словарь для клеток игрового поля.
global_cells = {}


def initialize() -> None:
    """Процедура для случайной инциализации координат клеточных автоматов."""
    for x in range(-300, 300, 10):
        for y in range(-300, 300, 10):
            global_cells[x, y] = False
    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            global_cells[x, y] = choice([True, False])


def draw() -> None:
    """Процедура для отрисовки клеток."""
    step()
    turtle.clear()
    for (x, y), alive in global_cells.items():
        color = 'black' if alive else 'white'
        cell(x, y, 10, color)
    turtle.update()
    turtle.ontimer(draw, 100)


def step() -> None:
    """Процедура реализует процесс смены поколений (шагов) клеточных автоматов."""
    neighbours = {}  # словарь для определения соседских клеток

    for x in range(-290, 290, 10):
        for y in range(-290, 290, 10):
            count = -global_cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += global_cells[x+h, y+v]
            neighbours[x, y] = count

    for cell, count in neighbours.items():
        if global_cells[cell]:
            if count < 2 or count > 3:  # условие смерти клетки при наличии менее 2 или более 3 соседей
                global_cells[cell] = False
        elif count == 3:                # условие рождения новой клетки при налии трех соседей
            global_cells[cell] = True


def cell(x: int, y: int, size: int, name: str) -> None:
    """Процедура для создания клеточных автоматов.

    На вход принимаются координаты ячеек, длинна шага
    и имя ячейки(цвет) в зависмости от заданной роли(мертвая/живая)"""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


if __name__ == '__main__':
    turtle.title("The Game of Life")
    turtle.setup(500, 500)
    turtle.hideturtle()
    turtle.tracer(False)
    initialize()
    draw()
    turtle.done()
