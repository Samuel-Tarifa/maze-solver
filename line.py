from point import Point


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)


def draw_line(x1, y1, x2, y2, canvas, color):
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    line = Line(point1, point2)
    line.draw(canvas, color)
