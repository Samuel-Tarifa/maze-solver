from line import draw_line
from config import primary


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        if x1 < 0 or x2 > win.width or y1 < 0 or y2 > win.height:
            raise Exception("Invalid coordinates: Out of bounds")
        if x1 > x2 or y1 > y2:
            raise Exception("Invalid coordinates: incorrect order")
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        canvas = self._win.canvas
        color = primary
        top_y = self._y1
        left_x = self._x1
        bot_y = self._y2
        right_x = self._x2

        if self.has_bottom_wall:
            draw_line(left_x, bot_y, right_x, bot_y, canvas, color)
        if self.has_left_wall:
            draw_line(left_x, top_y, left_x, bot_y, canvas, color)
        if self.has_right_wall:
            draw_line(right_x, top_y, right_x, bot_y, canvas, color)
        if self.has_top_wall:
            draw_line(left_x, top_y, right_x, top_y, canvas, color)
