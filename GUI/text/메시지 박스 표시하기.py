import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("메시지 박스 생성하기")
root.geometry("400x200")

def click() :
    messagebox.showinfo("메세지", "메시지가 나왔습니다.")

btn = tk.Button(text='메시지를 보여주세요', command=click)
btn.pack()

root.mainloop()