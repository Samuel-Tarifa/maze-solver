from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze=Maze(2,2,10,10,40,40,win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
