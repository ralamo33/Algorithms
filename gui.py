"""The graphic user interface."""

from tkinter import *
import time

from PIL import ImageTk

import algorithms
import PIL

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

        instructions = Label(self, text="Choose a game mode and an algorithm\n and find what you are seeking!", fg="red"
                             , font=("Times New Roman", 20))
        #instructions.place(relx=.08, rely=.4)
        self.time_played = Label(self, text="", fg="red", font=("Times New Roman", 20))
        self.time_played.place(x=200, y=200)
        self.update_time()

        #Display an image
        load = algorithms.Vertex("A").draw()
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=100)

    def update_time(self):
        """Update the amount of time the user has spent playing."""
        now = time.strftime("%H:%M:%S")
        self.time_played.configure(text=now)
        self.after(1000, self.update_time)


    def click_exit_button(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Seekers")
root.geometry("500x500")
root.after(1000, app.update_time())
root.mainloop()

if __name__ == "__main__":
    root.mainloop()