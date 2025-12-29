import tkinter as tk
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        print(f"Выбран: {filename}")

def save_file():
    filename = filedialog.asksaveasfilename()
    if filename:
        print(f"Сохранить как: {filename}")

root = tk.Tk()
root.title("Выбор файла")

tk.Button(root, text="Открыть файл", command=open_file, width=20).pack(pady=10)
tk.Button(root, text="Сохранить файл", command=save_file, width=20).pack()

root.mainloop()