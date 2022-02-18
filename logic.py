# TODO: Create the logic for your GUI application

# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

import keyboard
from keyboard import is_pressed
import time
import os
import random


# class block
class TypingTest(Tk):

    def __init__(self):
        """Initialize the application"""
        # inheritance from the Tk class
        super().__init__()

        # easy window init
        self.easy_window = None
        self.easy_mainframe = None
        self.easy_text_entry = None
        self.easy_rules_label = None
        self.easy_sentence_label = None
        self.easy_label_style = None

        # medium window init
        self.medium_window = None
        self.medium_mainframe = None
        self.medium_text_entry = None
        self.medium_sentence_label = None
        self.medium_rules_label = None
        self.medium_label_style = None

        # hard window init
        self.hard_window = None
        self.hard_mainframe = None
        self.hard_text_entry = None
        self.hard_rules_label = None
        self.hard_sentence_label = None
        self.hard_label_style = None

        # result variables
        self.start_time = 0
        self.total_time = 0
        self.accuracy = 0
        self.wpm = 0

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
        # index variable for identifying the window
        index = 0

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

        self.easy_label_style = ttk.Style()
        self.easy_label_style.configure("Labels.TLabel", background="#F9ED69", foreground="#F08A5D", font=("Arial", 14))

        # create a main frame for the window
        self.easy_mainframe = ttk.Frame(self.easy_window, style="MainFrame.TFrame")
        self.easy_mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(self.easy_mainframe, text="Start", padding=1, command=lambda: self.main(index),
                                  style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(self.easy_mainframe, text="Exit", padding=1, command=lambda: self.close_window(index),
                                 style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        font_for_the_entry = Font(family="Arial", size=14)
        self.easy_text_entry = ttk.Entry(self.easy_mainframe, width=60, font=font_for_the_entry)
        self.easy_text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        self.easy_rules_label = ttk.Label(self.easy_mainframe,
                                          text="Press Start to Begin the Test. Press Enter to Complete It.",
                                          style="Labels.TLabel")
        self.easy_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.easy_sentence_label = ttk.Label(self.easy_mainframe, text="Your Test Sentence Will be Here",
                                             style="Labels.TLabel")
        self.easy_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def medium(self):
        """
        This method implements medium mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        # index variable for identifying the window
        index = 1

        # hide the main window, till the TopLevel is not closed
        self.iconify()
        self.easy_button.configure(state=DISABLED)
        self.medium_button.configure(state=DISABLED)
        self.hard_button.configure(state=DISABLED)

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

        self.medium_label_style = ttk.Style()
        self.medium_label_style.configure("Labels.TLabel", background="#222831", foreground="#00ADB5",
                                          font=("Arial", 14))

        # create a main frame for the window
        self.medium_mainframe = ttk.Frame(self.medium_window, style="MainFrame.TFrame")
        self.medium_mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(self.medium_mainframe, text="Start", padding=1,
                                  command=lambda: self.main(index),
                                  style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(self.medium_mainframe, text="Exit", padding=1,
                                 command=lambda: self.close_window(index),
                                 style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        font_for_the_entry = Font(family="Arial", size=14)
        self.medium_text_entry = ttk.Entry(self.medium_mainframe, width=60, font=font_for_the_entry)
        self.medium_text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        self.medium_rules_label = ttk.Label(self.medium_mainframe,
                                            text="Press Start to Begin the Test. Press Enter to Complete It.",
                                            style="Labels.TLabel")
        self.medium_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.medium_sentence_label = ttk.Label(self.medium_mainframe, text="Your Test Sentence Will be Here",
                                               style="Labels.TLabel")
        self.medium_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def hard(self):
        """
        This method implements hard mode for the Typing Test App.
        Opens in a new Tkinter Window.
        :return: nothing
        """
        # index variable for identifying the window
        index = 2

        # hide the main window, till the TopLevel is not closed
        self.iconify()
        self.easy_button.configure(state=DISABLED)
        self.medium_button.configure(state=DISABLED)
        self.hard_button.configure(state=DISABLED)

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

        self.hard_label_style = ttk.Style()
        self.hard_label_style.configure("Labels.TLabel", background="#252A34", foreground="#FF2E63", font=("Arial", 14))

        # create a main frame for the window
        self.hard_mainframe = ttk.Frame(self.hard_window, style="MainFrame.TFrame")
        self.hard_mainframe.grid(column=0, row=0)

        # buttons
        start_button = ttk.Button(self.hard_mainframe, text="Start", padding=1, command=lambda: self.main(index),
                                  style="Buttons.TButton")
        start_button.grid(column=0, row=3, padx=10, pady=10)

        exit_button = ttk.Button(self.hard_mainframe, text="Exit", padding=1, command=lambda: self.close_window(index),
                                 style="Buttons.TButton")
        exit_button.grid(column=1, row=3, padx=10, pady=10)

        # entries
        font_for_the_entry = Font(family="Arial", size=14)
        self.hard_text_entry = ttk.Entry(self.hard_mainframe, width=60, font=font_for_the_entry)
        self.hard_text_entry.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

        # labels
        self.hard_rules_label = ttk.Label(self.hard_mainframe,
                                          text="Press Start to Begin the Test. Press Enter to Complete It.",
                                          style="Labels.TLabel")
        self.hard_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.hard_sentence_label = ttk.Label(self.hard_mainframe, text="Your Test Sentence Will be Here",
                                             style="Labels.TLabel")
        self.hard_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

    def main(self, index):
        """
        This is the main function of the Typing Test App. Here will the test start and end.
        :return: nothing
        """
        # check the index, to determine which type of the test will be taken
        if index == 0:
            # get a random sentence from data/easy_mode.txt
            with open("data/easy_mode.txt", "r", encoding="utf-8") as hard_file:
                # read the file
                sentences = hard_file.read().split("\n")

                # get a random sentence
                random_sentence = random.choice(sentences)

            # start the timer
            self.start_time = time.time()

            # display this sentence on the label
            self.easy_sentence_label.grid_forget()
            self.easy_sentence_label = ttk.Label(self.easy_mainframe, text=random_sentence, style="Labels.TLabel")
            self.easy_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

            # check if the Enter key was pressed, if it was than we need to calculate the results
            self.easy_window.bind("<Return>",
                                  lambda sentence=random_sentence, id_index=index: self.display_results(sentence,
                                                                                                        index))
        elif index == 1:
            # get a random sentence from data/easy_mode.txt
            with open("data/medium_mode.txt", "r", encoding="utf-8") as medium_file:
                # read the file
                sentences = medium_file.read().split("\n")

                # get a random sentence
                random_sentence = random.choice(sentences)

            # start the timer
            self.start_time = time.time()

            # display this sentence on the label
            self.medium_sentence_label.grid_forget()
            self.medium_sentence_label = ttk.Label(self.medium_mainframe, text=random_sentence, style="Labels.TLabel")
            self.medium_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

            # check if the Enter key was pressed, if it was than we need to calculate the results
            self.medium_window.bind("<Return>",
                                    lambda sentence=random_sentence, id_index=index: self.display_results(sentence,
                                                                                                          index))
        else:
            # get a random sentence from data/easy_mode.txt
            with open("data/hard_mode.txt", "r", encoding="utf-8") as hard_file:
                # read the file
                sentences = hard_file.read().split("\n")

                # get a random sentence
                random_sentence = random.choice(sentences)

            # start the timer
            self.start_time = time.time()

            # display this sentence on the label
            self.hard_sentence_label.grid_forget()
            self.hard_sentence_label = ttk.Label(self.hard_mainframe, text=random_sentence, style="Labels.TLabel")
            self.hard_sentence_label.grid(column=0, row=0, padx=10, pady=20, columnspan=2)

            # check if the Enter key was pressed, if it was than we need to calculate the results
            self.hard_window.bind("<Return>",
                                  lambda sentence=random_sentence, id_index=index: self.display_results(sentence,
                                                                                                        index))

    def display_results(self, sentence, index):
        """
        This method calculates all the results from the Typing Test.
        :param event: event that is passed from tkinter.bind(seq, func) method
        :param sentence: sentence that was given to user as a test
        :param index: index to identify the mode of the test
        :return: None
        """
        # calculate time
        self.total_time = time.time() - self.start_time

        # calculate accuracy
        count = 0
        user_input = self.easy_text_entry.get()
        for i, char in enumerate(sentence):
            try:
                if user_input[i] == char:
                    count += 1
            except Exception:
                pass
        self.accuracy = count / len(user_input) * 100

        # calculate words per minute
        self.wpm = len(user_input) * 60 / (5 * self.total_time)

        # check the index that was passed to the method to identify what mode of test is being taken
        if index == 0:
            # display the results in easy window
            self.easy_rules_label.grid_forget()
            self.easy_rules_label = ttk.Label(self.easy_mainframe,
                                              text=f"Time:{round(self.total_time)} seconds Accuracy:{round(self.accuracy)}% Wpm:{round(self.wpm)}",
                                              style="Labels.TLabel")
            self.easy_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        elif index == 1:
            # display the results in medium window
            self.medium_rules_label.grid_forget()
            self.medium_rules_label = ttk.Label(self.medium_mainframe,
                                                text=f"Time:{round(self.total_time)} seconds Accuracy:{round(self.accuracy)}% Wpm:{round(self.wpm)}",
                                                style="Labels.TLabel")
            self.medium_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        else:
            # display the results in hard window
            self.hard_rules_label.grid_forget()
            self.hard_rules_label = ttk.Label(self.hard_mainframe,
                                              text=f"Time:{round(self.total_time)} seconds Accuracy:{round(self.accuracy)}% Wpm:{round(self.wpm)}",
                                              style="Labels.TLabel")
            self.hard_rules_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

    def close_window(self, index):
        """
        This function closes the window.
        :parameter index: index that will allow us to identify which needs to be closed
        :return: nothing
        """
        # closing the window, that associates with the given index
        if index == 0:
            self.easy_window.destroy()
        elif index == 1:
            self.medium_window.destroy()
        else:
            self.hard_window.destroy()

        # changing the state of the buttons back to normal
        self.easy_button.configure(state=NORMAL)
        self.medium_button.configure(state=NORMAL)
        self.hard_button.configure(state=NORMAL)

        # returning the root window back to the screen
        self.deiconify()
