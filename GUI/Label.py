import encodings
import tkinter
import tkinter.font

root = tkinter.Tk()
root.title("첫번째 윈도우")
root.geometry("800x600")

label = tkinter.Label(root, text='Label', font = ("Times New Roman",24))
label.place(x=200, y=100)
root.mainloop()

# print(tkinter.font.families())