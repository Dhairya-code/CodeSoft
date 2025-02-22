import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()
