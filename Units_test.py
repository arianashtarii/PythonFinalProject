#برنامه تست انتخاب واحد دانشجویان

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("انتخاب واحد")
window.geometry("300x350")

units = 0
max_units = 20

courses = [
    ["ریاضی", 3],
    ["فیزیک", 3],
    ["برنامه‌نویسی", 3],
    ["زبان", 2],
    ["ورزش", 1]
]


def submit():
    global units
    units = 0
    selected = []

    for i in range(len(courses)):
        if vars[i].get() == 1:
            units += courses[i][1]
            selected.append(courses[i][0])

    if units > max_units:
        messagebox.showerror("خطا", f"بیش از {max_units} واحد انتخاب کرده‌اید!")
        return

    if selected:
        units_label.config(text=f"واحدها: {units}/{max_units}")
        messagebox.showinfo("انجام شد", f"{len(selected)} درس انتخاب کردید\n{units} واحد")
    else:
        messagebox.showwarning("هشدار", "هیچ درسی انتخاب نکردید")


def clear():
    global units
    units = 0
    for var in vars:
        var.set(0)
    units_label.config(text=f"واحدها: 0/{max_units}")
    messagebox.showinfo("پاک شد", "همه انتخاب‌ها پاک شد")


title = tk.Label(window, text="انتخاب واحد", font=("B Nazanin", 14))
title.pack(pady=10)

units_label = tk.Label(window, text=f"واحدها: 0/{max_units}")
units_label.pack()

vars = []
for name, credit in courses:
    var = tk.IntVar()
    cb = tk.Checkbutton(window, text=f"{name} ({credit} واحد)", variable=var)
    cb.pack(pady=2)
    vars.append(var)

tk.Button(window, text="ثبت", command=submit).pack(pady=10)
tk.Button(window, text="پاک کردن", command=clear).pack()

window.mainloop()
