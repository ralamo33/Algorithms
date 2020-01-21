"""The graphic user interface."""

from tkinter import *
import time

from PIL import ImageTk as tk
from PIL import Image as im
import algorithms

class Window(Frame):
    def __init__(self, master=None, width=500, height=500):
        Frame.__init__(self, master)
        self.master = master
        self.width = 500
        self.height = 500
        self.history = []
        self.pack(fill=BOTH, expand=1)
        self.init_buttons()
        self.init_menus()
        self.init_labels()

    def init_buttons(self):
        """Intilize buttons for self."""
        self.exitButton = Button(self, text="Exit", command=self.click_exit_button)
        self.exitButton.place(x=0, y=0)

    def init_menus(self):
        """Initialize menus for self."""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.game_mode = Menu(self.menu)
        self.game_mode.add_command(label="Search everything.")
        self.game_mode.add_command(label="Search islands.")
        self.game_mode.add_command(label="Search for gold.")
        self.menu.add_cascade(label="Game Mode", menu=self.game_mode)
        self.algorithm = Menu(self.menu)
        self.algorithm.add_command(label="Exit", command=self.click_exit_button)
        self.menu.add_cascade(label="Algorithm", menu=self.algorithm)

    def init_labels(self):
        """Initialize labels for self."""
        """self.instructions = Label(self, text="Choose a game mode and an algorithm\n and find what you are seeking!", 
                                  fg="red", font=("Times New Roman", 20))"""
        self.display_graph(algorithms.MyGrid())


    def display_graph(self, grid):
        """
        Display the given grid.
        :param grid: (Grid) A grid represented as a graph of verticies and edges.
        :return: Image
        """
        background = im.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        self.grid = Label(self, image=background)
        self.grid.image = background
        vertex_width = int(self.width / grid.cols)
        vertex_height = int(self.height / grid.rows)
        for vertex in grid.vertices:
            vertex_image = im.new("RGB", (vertex_width, vertex_height), vertex.color)
            background.paste(vertex_image, (vertex.x * vertex_width, vertex.y * vertex_height))
        self.history.append(background)
        self.grid.image = background

    def click_exit_button(self):
        exit()

root = Tk()
width = 500
height = 500
app = Window(root, width, height)
root.wm_title("Seekers")
root.geometry(str(width) + "x" + str(height))
root.mainloop()

if __name__ == "__main__":
    root.mainloop()