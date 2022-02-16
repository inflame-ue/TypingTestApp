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

        # variables
        self.easy_window = None
        self.medium_window = None
        self.hard_window = None

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
        self.easy_button = ttk.Button(self.global_frame, text="Easy", padding=10, style="FountainBlueButton.TButton",
                                      command=self.easy)
        self.easy_button.grid(column=0, row=3, padx=10, pady=10)

        self.medium_button = ttk.Button(self.global_frame, text="Medium", padding=10,
                                        style="FountainBlueButton.TButton",
                                        command=self.medium)
        self.medium_button.grid(column=1, row=3, padx=10, pady=10)

        self.hard_button = ttk.Button(self.global_frame, text="Hard", padding=10, style="FountainBlueButton.TButton",
                                      command=self.hard)
        self.hard_button.grid(column=2, row=3, padx=10, pady=10)

        # mainloop
        self.mainloop()

    def easy(self):
        """
        This method implements easy mode for the Typing Test App.
        Opens in a new Tkinter window.
        :return: nothing
        """
        # hide the main window, till the TopLevel is not closed
        self.iconify()
        self.easy_button.configure(state=DISABLED)
        self.medium_button.configure(state=DISABLED)
        self.hard_button.configure(state=DISABLED)

        # create a new window, where the easy mode of the game will be displayed
        self.easy_window = Toplevel()
        self.easy_window.title("Easy Mode")
        self.easy_window.resizable(width=True, height=True)
        self.easy_window.iconbitmap("assets/icons/icon.ico")

        # styles
        font_for_the_buttons = Font(family="Arial", size=14, weight="bold")
        buttons_style = ttk.Style()
        buttons_style.theme_use("default")
        buttons_style.configure("Buttons.TButton",
                                background="#F9ED69",
                                foreground="#F08A5D",
                                font=font_for_the_buttons,
                                width=10,
                                borderwidth=1,
                                focusthickness=3, )

        mainframe_style = ttk.Style()
        mainframe_style.configure("MainFrame.TFrame", background="#F9ED69")

        label_style = ttk.Style()
        label_style.configure("Labels.TLabel", background="#F9ED69", foreground="#F08A5D")

        # create a main frame for the window
        mainframe = ttk.Frame(self.easy_window, style="MainFrame.TFrame")
        mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(mainframe, text="Start", padding=1, command=self.start_test, style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(mainframe, text="Exit", padding=1, command=self.close_window, style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        text_entry = ttk.Entry(mainframe, width=60)
        text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        font_for_rules_label = Font(family="Arial", size=14)
        rules_label = ttk.Label(mainframe, text="Results",
                                style="Labels.TLabel", font=font_for_rules_label)
        rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        font_for_test_sentence_label = Font(family="Arial", size=14)
        test_sentence_label = ttk.Label(mainframe, text="Sentence",
                                        style="Labels.TLabel", font=font_for_test_sentence_label)
        test_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def medium(self):
        """
        This method implements medium mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        # hide the main window, till the TopLevel is not closed
        self.iconify()

        # create a new window, where the medium mode of the game will be displayed
        self.medium_window = Toplevel()
        self.medium_window.title("Medium Mode")
        self.medium_window.resizable(width=True, height=True)
        self.medium_window.iconbitmap("assets/icons/icon.ico")

        # styles
        font_for_the_buttons = Font(family="Arial", size=14, weight="bold")
        buttons_style = ttk.Style()
        buttons_style.theme_use("default")
        buttons_style.configure("Buttons.TButton",
                                background="#222831",
                                foreground="#00ADB5",
                                font=font_for_the_buttons,
                                width=10,
                                borderwidth=1,
                                focusthickness=3, )

        mainframe_style = ttk.Style()
        mainframe_style.configure("MainFrame.TFrame", background="#222831")

        label_style = ttk.Style()
        label_style.configure("Labels.TLabel", background="#222831", foreground="#00ADB5")

        # create a main frame for the window
        mainframe = ttk.Frame(self.medium_window, style="MainFrame.TFrame")
        mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(mainframe, text="Start", padding=1, command=self.start_test, style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(mainframe, text="Exit", padding=1, command=self.close_window, style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        text_entry = ttk.Entry(mainframe, width=60)
        text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        font_for_rules_label = Font(family="Arial", size=14)
        rules_label = ttk.Label(mainframe, text="Results",
                                style="Labels.TLabel", font=font_for_rules_label)
        rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        font_for_test_sentence_label = Font(family="Arial", size=14)
        test_sentence_label = ttk.Label(mainframe, text="Sentence",
                                        style="Labels.TLabel", font=font_for_test_sentence_label)
        test_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def hard(self):
        """
        This method implements hard mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        # hide the main window, till the TopLevel is not closed
        self.iconify()

        # create a new window, where the hard mode of the game will be displayed
        self.hard_window = Toplevel()
        self.hard_window.title("Hard Mode")
        self.hard_window.resizable(width=True, height=True)
        self.hard_window.iconbitmap("assets/icons/icon.ico")

        # styles
        font_for_the_buttons = Font(family="Arial", size=14, weight="bold")
        buttons_style = ttk.Style()
        buttons_style.theme_use("default")
        buttons_style.configure("Buttons.TButton",
                                background="#252A34",
                                foreground="#FF2E63",
                                font=font_for_the_buttons,
                                width=10,
                                borderwidth=1,
                                focusthickness=3, )

        mainframe_style = ttk.Style()
        mainframe_style.configure("MainFrame.TFrame", background="#252A34")

        label_style = ttk.Style()
        label_style.configure("Labels.TLabel", background="#252A34", foreground="#FF2E63")

        # create a main frame for the window
        mainframe = ttk.Frame(self.hard_window, style="MainFrame.TFrame")
        mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(mainframe, text="Start", padding=1, command=self.start_test, style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(mainframe, text="Exit", padding=1, command=self.close_window, style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        text_entry = ttk.Entry(mainframe, width=60)
        text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        font_for_rules_label = Font(family="Arial", size=14)
        rules_label = ttk.Label(mainframe, text="Results",
                                style="Labels.TLabel", font=font_for_rules_label)
        rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        font_for_test_sentence_label = Font(family="Arial", size=14)
        test_sentence_label = ttk.Label(mainframe, text="Sentence",
                                        style="Labels.TLabel", font=font_for_test_sentence_label)
        test_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def start_test(self):
        pass

    def close_window(self):
        pass
