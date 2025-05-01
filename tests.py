import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m1._cells[0][0]
        exit_cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertTrue(entrance_cell.has_top_wall)
        self.assertTrue(exit_cell.has_bottom_wall)
        m1._break_entrance_and_exit()
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
