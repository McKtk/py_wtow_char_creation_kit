import tkinter as tk
from tkinter import ttk
from modules.classes import *
import pickle, random

def on_select(event):
    for item in tree.get_children():
        tree.item(item, tags=())
    selected = tree.selection()
    for item in selected:
        tree.item(item, tags=("selected"))


def read_bin(filename):
    filename = "./bin/"+filename+".bin"
    with open(filename, "rb") as f:
        return(pickle.load(f))
    
talents = read_bin("talents")

root = tk.Tk()
root.title("WTOW")
root.geometry("400x250")

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 10))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
style.map("Treeview", background=[("selected", "#069682")])
style.configure("selected.Treeview", font=("Segoe UI", 11, "bold"))

columns = ("Name", "Cost in XP", "Requirements")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.pack(fill=tk.BOTH, expand=True)

tree.heading("Name", text="Name")
tree.heading("Cost in XP", text="Cost in XP")
tree.heading("Requirements", text="Requirements")

for l in talents:
    tree.insert("", tk.END, values=(l.name, l.cost, l.req))
    
tree.tag_configure("selected", font=("Segoe UI", 11, "bold"))

tree.bind("<<TreeviewSelect>>", on_select)
root.mainloop()