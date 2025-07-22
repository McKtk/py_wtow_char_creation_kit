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

talent_list(root, talents)

root.mainloop()
