import tkinter
import tkinter.font

def click_btn() :
    button["text"] = "Clicked"

root = tkinter.Tk()
root.title("첫번째 윈도우")
root.geometry("800x600")

button = tkinter.Button(root, text='Button', font = ("Times New Roman",24), command=click_btn)
button.place(x=200, y=100)

root.mainloop()
