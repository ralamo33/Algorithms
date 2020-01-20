"""The graphic user interface."""

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.click_exit_button)

        exitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        game_mode = Menu(menu)
        game_mode.add_command(label="Search everything.")
        game_mode.add_command(label="Search islands.")
        game_mode.add_command(label="Search for gold.")
        menu.add_cascade(label="Game Mode", menu=game_mode)

        algorithm = Menu(menu)
        algorithm.add_command(label="Exit", command=self.click_exit_button)
        menu.add_cascade(label="Algorithm", menu=algorithm)

    def click_exit_button(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Seekers")
root.geometry("320x200")
root.mainloop()

if __name__ == "__main__":
    root.mainloop()