import pyglet
import random



CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE


window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
fps = 10


grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def update_grid(dt):
    global grid
    new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            live_neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    ny = (y + dy) % GRID_HEIGHT
                    nx = (x + dx) % GRID_WIDTH
                    live_neighbors += grid[ny][nx]
            if grid[y][x] == 1:
                new_grid[y][x] = 1 if live_neighbors in [2, 3] else 0
            else:
                new_grid[y][x] = 1 if live_neighbors == 3 else 0

    grid = new_grid


@window.event
def on_draw():
    window.clear()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                square = pyglet.shapes.Rectangle(
                    x * CELL_SIZE, y * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE,
                    color=(0, 255, 0)
                )
                square.draw()


pyglet.clock.schedule_interval(update_grid, 1 / fps)


pyglet.app.run()
