"""The graphic user interface. This operates as the View."""

from tkinter import *
import time
from controller import Controller

from PIL import ImageTk
from PIL import Image, ImageOps
import math

class Window(Frame):
    def __init__(self, master, control, width=100, height=100):
        Frame.__init__(self, master)
        self.master = master
        self.controller = control
        self.vertex_width = 0;
        self.vertex_height = 0;
        self.history = []
        self.init_menus()
        self.label = Label(self)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label.bind('<Button-1>', self.mutate_vertex)
        self.label.bind('<B1-Motion>', self.mutate_vertex)
        self.pack(fill=BOTH, expand=1)
        self.update_graph()

    def init_menus(self):
        """Initialize menus for self."""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.game_mode = Menu(self.menu)
        self.game_mode.add_command(label="Run", command=self.controller.run)
        self.game_mode.add_command(label="Solve Now!", command=self.controller.immediate_update)
        self.game_mode.add_command(label="Reset All", command=self.controller.reset_all)
        self.game_mode.add_command(label="Reset", command=self.controller.reset)
        self.menu.add_cascade(label="Game", menu=self.game_mode)
        self.algorithm = Menu(self.menu)
        self.algorithm.add_command(label="Breadth First Search", command=self.controller.set_bfs)
        self.algorithm.add_command(label="Depth First Search", command=self.controller.set_dfs)
        self.algorithm.add_command(label="Prim Algorithm", command=self.controller.set_prim)
        self.algorithm.add_command(label="Dijkstra Algorithm", command=self.controller.set_dijkstra)
        self.algorithm.add_command(label="A Star Algorithm", command=self.controller.set_a_star)
        self.menu.add_cascade(label="Algorithm", menu=self.algorithm)
        self.selector = Menu(self.menu)
        self.selector.add_command(label="Make target", command=self.controller.set_target)
        self.selector.add_command(label="Make obstacle", command=self.controller.set_obstacle)
        self.selector.add_command(label="Make unsearched", command=self.controller.set_normal)
        self.selector.add_command(label="Make start", command=self.controller.set_start)
        self.menu.add_cascade(label="Selector", menu=self.selector)

    def update_graph(self):
        """Initialize labels for self."""
        #TODO: Replace with self.grid from controller.
        #TODO: Replace with grid manager.
        total_width = self.label.winfo_width()
        total_height = self.label.winfo_height()
        self.vertex_width = math.floor(total_width / self.controller.get_cols())
        self.vertex_height = math.floor(total_height / self.controller.get_rows())
        background = Image.new("RGB", (total_width, total_height), color="white")
        for vertex in self.controller.get_verticies():
            vertex_image = Image.new("RGB", (self.vertex_width, self.vertex_height), color=vertex.get_color())
            if vertex.is_visited():
                vertex_image.paste(Image.new("RGB", (int(self.vertex_width / 5), int(self.vertex_height / 5)), color="black"),
                                   (round(self.vertex_width / 2), round(self.vertex_height / 2)))
            vertex_image = ImageOps.expand(vertex_image, 1)
            background.paste(vertex_image, (self.vertex_width * vertex.x, self.vertex_height * vertex.y))
        render = ImageTk.PhotoImage(background)
        self.label.configure(image=render)
        self.label.image = render
        self.after(1, self.update_graph)
        return render

    def click_exit_button(self):
        exit()

    def mutate_vertex(self, event):
        """
        Mutate the vertex that was clicked on.
        :param event: The clicking of a vertex on the grid.
        :return: None
        """
        x = int(event.x / self.vertex_width)
        y = int(event.y / self.vertex_height)
        self.controller.mutate(x, y)


def make_view(show=False, controller=Controller()):
    #TODO: Do this in intialize or figure out pretty way fro this implementation.
    """Start the view."""
    root = Tk()
    width = 500
    height = 500
    root.geometry("{width}x{height}".format(width=width, height=height))
    app = Window(root, controller, width, height)
    root.wm_title("Seekers")
    root.geometry(str(width) + "x" + str(height))
    if show:
        root.mainloop()
    return app

if __name__ == "__main__":
    make_view(True)