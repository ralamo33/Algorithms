"""The graphic user interface. This operates as the View."""

from tkinter import *
import time
from controller import Controller

from PIL import ImageTk
from PIL import Image, ImageOps
import algorithms as model

class Window(Frame):
    def __init__(self, master, control, width=500, height=500):
        Frame.__init__(self, master)
        self.master = master
        self.controller = control
        self.width = 500
        self.height = 500
        self.history = []
        self.init_labels()
        self.init_menus()
        self.pack(fill=BOTH, expand=1)
        #self.init_buttons()



    def init_buttons(self):
        """Intilize buttons for self."""
        self.exitButton = Button(self, text="Exit", command=self.click_exit_button)
        self.exitButton.place(x=0, y=0)

    def init_menus(self):
        """Initialize menus for self."""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.game_mode = Menu(self.menu)
        self.game_mode.add_command(label="Run", command=self.controller.run)
        self.game_mode.add_command(label="Search islands.")
        self.game_mode.add_command(label="Search for gold.")
        self.menu.add_cascade(label="Game Mode", menu=self.game_mode)
        self.algorithm = Menu(self.menu)
        self.algorithm.add_command(label="Breadth First Search", command=self.set_bfs)
        self.algorithm.add_command(label="Depth First Search", command=self.set_dfs)
        self.menu.add_cascade(label="Algorithm", menu=self.algorithm)

    def set_bfs(self):
        """Set the controller to Breadth First Search"""
        self.controller.algorithm = model.MyGrid.bfs

    def set_dfs(self):
        """Set the controller to Depth First Search"""
        self.controller.algorithm = model.MyGrid.dfs

    def init_labels(self):
        """Initialize labels for self."""
        grid = model.MyGrid()
        background = Image.new("RGB", (self.width, self.height), color="red")
        vertex_width = int(self.width / grid.cols)
        vertex_height = int(self.height / grid.rows)
        for vertex in grid.vertices:
            vertex_image = Image.new("RGB", (vertex_width - 1, vertex_height - 1), color=vertex.get_color())
            vertex_image = ImageOps.expand(vertex_image, 1)
            background.paste(vertex_image, (vertex.x * vertex_width, vertex.y * vertex_height))
        render = ImageTk.PhotoImage(background)
        self.label = Label(self, text="Hello", image=render)
        self.label.image = render
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        return render


    def click_exit_button(self):
        exit()

def make_view(show=False, controller=Controller()):
    #TODO: Do this in intialize or figure out pretty way fro this implementation.
    """Start the view."""
    root = Tk()
    width = 500
    height = 500
    app = Window(root, controller, width, height)
    root.wm_title("Seekers")
    root.geometry(str(width) + "x" + str(height))
    if show:
        root.mainloop()
    return app

if __name__ == "__main__":
    make_view(True)