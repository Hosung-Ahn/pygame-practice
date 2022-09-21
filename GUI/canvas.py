import tkinter
from PIL import ImageTk

root = tkinter.Tk()
root.title("첫번째 윈도우")
# root.geometry("800x600")

# canvas 를 pack을 통해 열면 canvas크기에 맞춰 윈도우의 크기가 결정된다.
canvas = tkinter.Canvas(root, width = 400, height= 600, bg = 'skyblue')
canvas.pack()
# canvas.place(x=0,y=0)


# f=open('C:\WorkSpace\PyGame\GUI\images\cagua.png',"rb")
# print(img)
imgPath = ImageTk.PhotoImage(file = r"C:\WorkSpace\PyGame\GUI\images\cagua.png")
canvas.create_image(200,300, image = imgPath)
root.mainloop()
