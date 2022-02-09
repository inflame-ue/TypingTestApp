# TODO: Create the logic for your GUI application

# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import sys
import time
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

        # styles for the program
        font_for_the_buttons = Font(family="Arial", size=14)
        self.button_style = ttk.Style()
        self.button_style.theme_use("default")
        self.button_style.configure("FountainBlueButton.TButton",
                                    background="#FAE3D9",
                                    foreground="#61C0BF",
                                    font=font_for_the_buttons,
                                    width=15,
                                    borderwidth=1,
                                    focusthickness=3)

        self.frame_style = ttk.Style()
        self.frame_style.configure("BlueFrame.TFrame", background="#FAE3D9")

        self.label_style = ttk.Style()
        self.label_style.configure("DarkLabel.TLabel", background="#FAE3D9", foreground="#61C0BF")

        # global frame for the application
        self.global_frame = ttk.Frame(self, style="BlueFrame.TFrame")
        self.global_frame.grid(column=0, row=0)

        # labels
        font_for_the_title_label = Font(family="Arial", size=30, weight="bold")
        self.title_label = ttk.Label(self.global_frame,
                                     text="Test Your Typing", font=font_for_the_title_label, style="DarkLabel.TLabel")
        self.title_label.grid(column=1, row=0, padx=10, pady=10)

        font_for_the_diff_label = Font(family="Arial", size=18)
        self.diff_label = ttk.Label(self.global_frame,
                                    text="Choose Difficulty:", font=font_for_the_diff_label, style="DarkLabel.TLabel")
        self.diff_label.grid(column=1, row=2, padx=30, pady=30)

        # buttons
        self.easy_button = ttk.Button(self.global_frame, text="Easy", padding=10, style="FountainBlueButton.TButton")
        self.easy_button.grid(column=0, row=3, padx=10, pady=10)

        self.medium_button = ttk.Button(self.global_frame, text="Medium", padding=10,
                                        style="FountainBlueButton.TButton")
        self.medium_button.grid(column=1, row=3, padx=10, pady=10)

        self.hard_button = ttk.Button(self.global_frame, text="Hard", padding=10, style="FountainBlueButton.TButton")
        self.hard_button.grid(column=2, row=3, padx=10, pady=10)

        # mainloop
        self.mainloop()

    def easy(self):
        """
        This method implements easy mode for the Typing Test App.
        Opens in a new Tkinter window.
        :return: nothing
        """
        return None

    def medium(self):
        """
        This method implements medium mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        return None

    def hard(self):
        """
        This method implements hard mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        return None
