import curses
from random import randint

# Инициализация окна
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # Создаём новое окно
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.timeout(100)

# Параметры змейки
snake_x = 15
snake_y = 10
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Параметры еды
food = [randint(1, 18), randint(1, 58)]
win.addch(food[0], food[1], '*')

# Клавиши управления
key = curses.KEY_RIGHT
score = 0

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Проверка на проигрыш
    if (
        snake[0][0] in [0, 19] or
        snake[0][1] in [0, 59] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        print(f"Game Over! Score: {score}")
        break

    # Логика движения змейки
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Проверка на поедание еды
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                randint(1, 18),
                randint(1, 58)
            ]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], '#')
