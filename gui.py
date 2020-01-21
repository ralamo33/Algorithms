"""The graphic user interface."""

from tkinter import *
import time

from PIL import ImageTk
from PIL import Image, ImageOps
import algorithms

class Window(Frame):
    def __init__(self, master=None, width=500, height=500):
        Frame.__init__(self, master)
        self.master = master
        self.width = 450
        self.height = 450
        self.history = []
        self.init_labels()
        self.pack(fill=BOTH, expand=1)
        self.init_buttons()
        self.init_menus()



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
        grid = algorithms.MyGrid()
        background = Image.new("RGB", (self.width, self.height), color="red")
        vertex_width = int(self.width / grid.cols)
        vertex_height = int(self.height / grid.rows)
        for vertex in grid.vertices:
            vertex_image = Image.new("RGB", (vertex_width, vertex_height), color=vertex.color)
            vertex_image = ImageOps.expand(vertex_image, 1)
            background.paste(vertex_image, (100, 100))
        render = ImageTk.PhotoImage(background)
        label = Label(self, text="Hello", image=render)
        label.image = render
        label.place(x=0, y=0)
        return render


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