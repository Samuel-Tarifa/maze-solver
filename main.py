from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(602, 602)

    maze=Maze(2,2,20,20,30,30,win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
