# TODO: Create the logic for your GUI application

# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


# class block
class TypingTest(Tk):

    def __init__(self):
        """Initialize the application"""
        # inheritance from the Tk class
        super().__init__()

        # root configuration
        self.title("Typing Test")
        self.resizable(width=True, height=True)
        self.iconbitmap("assets/icons/icon.ico")

        # global frame for the application
        self.global_frame = ttk.Frame(self)
        self.global_frame.grid(column=0, row=0)

        # style for the program
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # test label
        self.my_label = ttk.Label(self.global_frame, text="Typing Test App")
        self.my_label.grid(column=1, row=1)

        # mainloop
        self.mainloop()

