from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)

    cell = Cell(400, 400, 420, 420, win)
    cell.has_right_wall = False
    to_cell = Cell(440, 400, 460, 420, win)
    to_cell.has_left_wall = False
    cell.draw()
    to_cell.draw()
    cell.draw_move(to_cell, undo=True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
