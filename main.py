import tkinter as tk
from tkinter import ttk
from modules.classes import *
from modules.functions import *
from modules.elements import *
from modules.styles import *

    
talents = read_bin("talents")

root = tk.Tk()
root.title("WTOW")
root.geometry("400x250")

styles()
menu(root, lambda: open_new_window(root, "Talents", "600x150", talent_list, talents))

root.mainloop()
