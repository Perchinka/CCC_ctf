import mazelib
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator


def generate_maze(height=70, width=70):
    maze = mazelib.Maze()
    maze.generator = BacktrackingGenerator(height, width)
    maze.generate()
    maze.generate_entrances()

    maze.grid[maze.start[0]][maze.start[1]] = 0
    maze.grid[maze.end[0]][maze.end[1]] = 0

    return maze.grid.tolist(), maze.start, maze.end


def possible_moves(grid, x_coord, y_coord):
    moves = {
        "up": False,
        "down": False,
        "left": False,
        "right": False
    }

    if x_coord > 0 and grid[y_coord][x_coord-1] == 0:
        moves["left"] = True
    if x_coord < len(grid[0])-1 and grid[y_coord][x_coord+1] == 0:
        moves["right"] = True
    if y_coord > 0 and grid[y_coord-1][x_coord] == 0:
        moves["up"] = True
    if y_coord < len(grid)-1 and grid[y_coord+1][x_coord] == 0:
        moves["down"] = True

    return moves

def move(grid, x_coord, y_coord, direction):
    if direction == "up":
        return x_coord, y_coord-1
    if direction == "down":
        return x_coord, y_coord+1
    if direction == "left":
        return x_coord-1, y_coord
    if direction == "right":
        return x_coord+1, y_coord
