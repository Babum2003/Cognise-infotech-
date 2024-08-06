import tkinter as tk
from tkinter import messagebox
import time

def countdown():
    remaining_time = int(entry.get())
    while remaining_time > 0:
        mins, secs = divmod(remaining_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timeformat)
        root.update()
        time.sleep(1)
        remaining_time -= 1
    messagebox.showinfo("Countdown Timer", "Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root, font=('Helvetica', 48))
label.pack(padx=20, pady=20)

entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack(padx=20, pady=20)

start_button = tk.Button(root, text="Start Countdown", command=countdown)
start_button.pack(padx=20, pady=20)

root.mainloop()
