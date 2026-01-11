import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Прогрессбар")

progress = ttk.Progressbar(root, length=200)
progress.pack(pady=20)
def start():
    print "111"
    progress.start(10)
    i=0
    while true:
        print i
        i+=1

def stop():
    progress.stop()
    print "123"

tk.Button(root, text="Старт", command=start).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Стоп", command=stop).pack(side=tk.RIGHT, padx=10)

root.mainloop()
