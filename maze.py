from cell import Cell
import time,random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                x1 = i * self.cell_size_x + self.x1
                x2 = (i + 1) * self.cell_size_x + self.x1
                y1 = j * self.cell_size_y + self.y1
                y2 = (j + 1) * self.cell_size_y + self.y1
                cell = Cell(x1, y1, x2, y2, self.win)
                col.append(cell)
                if self.win:
                    cell.draw()
                    self._animate()
            self._cells.append(col)

    def _animate(self):
        if self.win is None:
            return

        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        self._animate()
        exit_cell.has_bottom_wall = False
        exit_cell.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited=True
        self._cells[i][j].draw()
        self._animate()
        while True:
            to_visit=[]
            if i > 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1,j))
            if i < self.num_cols-1 and not self._cells[i+1][j]._visited:
                to_visit.append((i+1,j))
            if j > 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i,j-1))
            if j < self.num_rows-1 and not self._cells[i][j+1]._visited:
                to_visit.append((i,j+1))
            if len(to_visit)==0:
                return
            next_cell = random.choice(to_visit)
            ni,nj = next_cell
            if nj < j:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            elif nj > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif ni < i:    
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif ni > i:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            self._break_walls_r(ni,nj)
        

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell._visited = True
        if i== self.num_cols-1 and j == self.num_rows-1:
            return True
        
        if i > 0 and not self._cells[i-1][j]._visited and not current_cell.has_left_wall:
            current_cell.draw_move(self._cells[i-1][j])
            result=self._solve_r(i-1,j)
            if result:
                return True
            current_cell.draw_move(self._cells[i-1][j],undo=True)
        if i < self.num_cols-1 and not self._cells[i+1][j]._visited and not current_cell.has_right_wall:
            current_cell.draw_move(self._cells[i+1][j])
            result=self._solve_r(i+1,j)
            if result:
                return True
            current_cell.draw_move(self._cells[i+1][j],undo=True)
        if j > 0 and not self._cells[i][j-1]._visited and not current_cell.has_top_wall:
            current_cell.draw_move(self._cells[i][j-1])
            result=self._solve_r(i,j-1)
            if result:
                return True
            current_cell.draw_move(self._cells[i][j-1],undo=True)
        if j < self.num_rows-1 and not self._cells[i][j+1]._visited and not current_cell.has_bottom_wall:
            current_cell.draw_move(self._cells[i][j+1])
            result=self._solve_r(i,j+1)
            if result:
                return True
            current_cell.draw_move(self._cells[i][j+1],undo=True)
        return False