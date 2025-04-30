from tkinter import Tk, BOTH, Canvas
from config import background


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.canvas = Canvas(self.root, bg=background, width=width, height=height)
        self.width = width
        self.height = height
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
