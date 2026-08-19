import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Example")
root.geometry("420x260")

def on_combo_selected(event):
    print(course.get())

course = tk.StringVar()
combo = ttk.Combobox(root, textvariable=course, values=["Python", "Tkinter", "SQLite"], state="readonly")
combo.pack(padx=20, pady=20)
combo.bind("<<ComboboxSelected>>",on_combo_selected)
combo.set("Python")
print(course.get())

ttk.Label(root, textvariable=course).pack(pady=10)

root.mainloop()

# bind a dic with combo {"C":3500, "C++":500}