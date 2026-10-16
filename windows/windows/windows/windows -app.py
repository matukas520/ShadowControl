import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ShadowControl")
root.geometry("500x350")
root.minsize(400, 300)
root.configure(bg="#111318")

title = tk.Label(
    root,
    text="ShadowControl",
    font=("Segoe UI", 24, "bold"),
    fg="#65aaff",
    bg="#111318"
)
title.pack(pady=(35, 10))

subtitle = tk.Label(
    root,
    text="Windows Control Center",
    font=("Segoe UI", 11),
    fg="#b8bdc9",
    bg="#111318"
)
subtitle.pack(pady=5)

status = tk.Label(
    root,
    text="● Application ready",
    font=("Segoe UI", 12),
    fg="#65d69a",
    bg="#111318"
)
status.pack(pady=20)

def show_info():
    messagebox.showinfo(
        "ShadowControl",
        "Application is running.\n"
        "Remote connection is not configured yet."
    )

button = tk.Button(
    root,
    text="Connection status",
    command=show_info,
    font=("Segoe UI", 11),
    bg="#252b38",
    fg="white",
    activebackground="#343d50",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
button.pack(pady=10)

root.mainloop()
