import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:   
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)
delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)
root.mainloop()