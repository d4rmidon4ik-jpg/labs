import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=f"Вы ввели: {text}")

root = tk.Tk()
root.title("Ввод текста")
root.geometry("400x100")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Показать", command=show_text).pack()
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
