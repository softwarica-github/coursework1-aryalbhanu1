# gui.py

from tkinter import Tk

# Function to initialize the GUI
def initialize_gui():
    window = Tk()
    window.title("Encryptstego")
    window.geometry('800x500')
    window.resizable(False, False)
    return window