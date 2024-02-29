# import unittest
# from unittest.mock import MagicMock
# import main

# class TestEncryptstegoApp(unittest.TestCase):
#     def setUp(self):
#         # Mocking functions
#         main.open_encode_window = MagicMock()
#         main.open_decode_window = MagicMock()
#         main.open_help_window = MagicMock()

#     def test_encode_window_open(self):
#         main.open_encode_window()
#         print("encode_opened:", main.encode_opened)
#         self.assertTrue(main.encode_opened)

#     def test_decode_window_open(self):
#         main.open_decode_window()
#         print("decode_opened:", main.decode_opened)
#         self.assertTrue(main.decode_opened)

#     def test_help_window_open(self):
#         main.open_help_window()
#         print("help_opened:", main.help_opened)
#         self.assertTrue(main.help_opened)

# if __name__ == '__main__':
#     unittest.main()
import unittest
import tkinter as tk
from tkinter import Toplevel
from encryptstego import open_encode_window, open_decode_window, help_menu

class TestEncryptStegoIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_open_encode_window(self):
        open_encode_window()

    def test_open_decode_window(self):
        open_decode_window()

    def test_help_menu(self):
        help_menu()

if __name__ == "__main__":
    unittest.main()
