import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("420x260")

choice = tk.StringVar(value="SC")
for option in ["SC", "BC", "GEN"]:
    ttk.Radiobutton(root, text=option, value=option, variable=choice).pack(anchor="w", padx=20)
ttk.Label(root, textvariable=choice).pack(pady=10)

root.mainloop()
