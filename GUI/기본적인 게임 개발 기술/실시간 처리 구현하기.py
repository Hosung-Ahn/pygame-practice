from glob import glob
import tkinter as tk

tmr = 0
def count_up() :
    global tmr
    tmr += 1
    label['text'] = tmr
    root.after(1000, count_up)
    
root = tk.Tk()
label = tk.Label(font=('Times New Roman', 80))
label.pack()
root.after(1000, count_up)
root.mainloop()