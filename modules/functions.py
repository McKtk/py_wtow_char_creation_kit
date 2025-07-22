import pickle
import  tkinter as tk

def read_bin(filename):
    filename = "./bin/"+filename+".bin"
    with open(filename, "rb") as f:
        return(pickle.load(f))
    
def open_new_window(root: tk.Tk, title: str, size: str, elements, *args, **kwargs):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry(size)
    content_frame = tk.Frame(new_window)
    content_frame.pack(fill=tk.BOTH, expand=True)
    elements(content_frame, *args, **kwargs)