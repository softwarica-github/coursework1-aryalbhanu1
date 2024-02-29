# main.py

# Importing required libraries
from tkinter import *

# Defining global variables to track if two child windows -
# for encoding, decoding and help window are in opened or closed state
encode_opened = True
decode_opened = True
help_opened = True
# Defining a variable to track if the program is running on Windows OS or not
# To make all the functionalities to work properly,
# the value of windows must be set to 'False' for other environments than Windows OS
windows = True

# Function to open encode window
def open_encode_window():
    global encode_opened
    encode_opened = True

# Function to open decode window
def open_decode_window():
    global decode_opened
    decode_opened = True

# Function to open help window
def open_help_window():
    global help_opened
    help_opened = True