from tkinter import ttk

def styles():
    style = ttk.Style()
    style.configure("Treeview", font=("Segoe UI", 10))
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
    style.map("Treeview", background=[("selected", "#069682")])
    style.configure("selected.Treeview", font=("Segoe UI", 11, "bold"))