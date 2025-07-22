import tkinter as tk
from tkinter import ttk
from  .functions import *

def on_select(tree):
    for item in tree.get_children():
        tree.item(item, tags=())
    selected = tree.selection()
    for item in selected:
        tree.item(item, tags=("selected"))

def talent_list(parent, talents):
    columns = ("Name", "Cost in XP", "Requirements")
    tree = ttk.Treeview(parent, columns=columns, show="headings", height=10)
    tree.pack(fill=tk.BOTH, expand=True)

    tree.heading("Name", text="Name")
    tree.heading("Cost in XP", text="Cost in XP")
    tree.heading("Requirements", text="Requirements")

    for l in talents:
        tree.insert("", tk.END, values=(l.name, l.cost, l.req))

    tree.tag_configure("selected", font=("Segoe UI", 11, "bold"))
    tree.bind("<<TreeviewSelect>>", lambda event: on_select(tree))
    
def menu(parent, command):
    tk.Label(parent, text="Menu").pack(pady=10)
    tk.Button(parent, text="Talents", command=command).pack(pady=10)