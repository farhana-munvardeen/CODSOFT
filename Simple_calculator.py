import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")


entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)


btn_frame = tk.Frame(root)
btn_frame.pack()


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    for btn_text in row:
        button = tk.Button(btn_frame, text=btn_text, font="Arial 18", width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)
    btn_frame = tk.Frame(root)
    btn_frame.pack()

root.mainloop()
