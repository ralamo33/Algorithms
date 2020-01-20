"""The graphic user interface."""

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.click_exit_button)

        exitButton.place(x=0, y=0)

    def click_exit_button(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Seekers")
root.geometry("320x200")
root.mainloop()

if __name__ == "__main__":
    root.mainloop()