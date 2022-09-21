import tkinter as tk
import random
from PIL import ImageTk

main = tk.Tk()
main.title("제비 뽑기 게임")

lst = ["대길", "중길", "소길", "흉"]

def click_button() :
    label['text'] = random.choice(lst)
    label.update()

canvas = tk.Canvas(main, width = 800, height= 600)
canvas.pack()

imgPath = ImageTk.PhotoImage(file = r"C:\WorkSpace\PyGame\GUI\images\miko.png")
canvas.create_image(400,300,image = imgPath)

button = tk.Button(main, text='내 운을 보여줘!', font = ("Times New Roman",24),
                   command=click_button)
button.place(x=400,y=400)

label = tk.Label(main, text = '??', font = ("Times New Roman",70))
label.place(x = 450, y=200)

main.mainloop()
