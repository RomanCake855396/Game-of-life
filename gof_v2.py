import pyglet
import random

CELL_SIZE = 10
GRID_WIDTH = 50
GRID_HEIGHT = 50
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 10


class CellGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.random_grid()

    def random_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                count += self.grid[ny][nx]
        return count

    def update(self):
        new_grid = [[0] * self.width for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.grid[y][x] == 1 and neighbors in [2, 3]:
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1

        self.grid = new_grid


class GameOfLifeWindow(pyglet.window.Window):
    def __init__(self, cell_grid):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.cell_grid = cell_grid
        pyglet.clock.schedule_interval(self.update, 1 / FPS)

    def on_draw(self):
        self.clear()
        for y in range(self.cell_grid.height):
            for x in range(self.cell_grid.width):
                if self.cell_grid.grid[y][x] == 1:
                    square = pyglet.shapes.Rectangle(
                        x * CELL_SIZE, y * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE,
                        color=(0, 255, 0)
                    )
                    square.draw()

    def update(self, dt):
        self.cell_grid.update()


if __name__ == '__main__':
    grid = CellGrid(GRID_WIDTH, GRID_HEIGHT)
    window = GameOfLifeWindow(grid)
    pyglet.app.run()
