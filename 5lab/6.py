import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Прогрессбар")

progress = ttk.Progressbar(root, length=200)
progress.pack(pady=20)

def start():
    progress.start(10)

def stop():
    progress.stop()

tk.Button(root, text="Старт", command=start).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Стоп", command=stop).pack(side=tk.RIGHT, padx=10)

root.mainloop()
