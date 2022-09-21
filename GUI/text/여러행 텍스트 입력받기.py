from re import T
from textwrap import wrap
import tkinter
from tkinter import scrolledtext
from turtle import width

def click_btn():
    scroll_text.insert(tkinter.END, "몬스터가 나타났다!!")
    
root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")
button = tkinter.Button(text='메시지', command=click_btn)
button.pack()

# text = tkinter.Text()
# text.place(x=20, y=50, width=360, height=120)

scroll_text = scrolledtext.ScrolledText(root)
scroll_text.pack()
root.mainloop()