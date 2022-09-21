import tkinter as tk
import random

neko = [
    [1,0,0,0,0,0,7,7],
    [0,2,0,0,0,0,7,7],
    [0,0,3,0,0,0,0,0],
    [0,0,0,4,0,0,0,0],
    [0,0,0,0,5,0,0,0],
    [0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,2,3,4,5,6]
]

CX = 912
CY = 768

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

root = tk.Tk()
root.title("고양이 낙하시키기")
root.resizable(False, False)

cvs = tk.Canvas(root, width=CX, height=CY)
cvs.pack()
bg = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko_bg.png')     
cvs.create_image(CX/2, CY/2, image=bg)

img_neko = [
    None,
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko1.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko2.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko3.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko4.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko5.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko6.png'),
    tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko_niku.png')    
]

def draw_neko() :
    for y in range(10) :
        for x in range(8) :
            if neko[y][x] > 0 :
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag='NEKO')
    
def mouse_move(e) :
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
    
def mouse_press(e) :
    global mouse_c
    mouse_c = 1
    
def mouse_release(e) :
    global mouse_c
    mouse_c = 0
    
def drop_neko() :
    for y in range(8,-1,-1) :
        for x in range(8) :
            if neko[y][x] != 0 and neko[y+1][x] == 0 :
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

    
def game_main() :
    global cursor_x, cursor_y, mouse_c
    if 24 <= mouse_x < 24 + 72*8 and 24 <= mouse_y < 24 + 72*10 :
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        
        if mouse_c == 1 :
            mouse_c = 0
            if mouse_y < 24+72*2 and neko[cursor_y][cursor_x] == 0:
                neko[cursor_y][cursor_x] = random.randint(1,6)
    
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72 + 60, cursor_y*72 + 60, image=cursor, tag='CURSOR')
    
    drop_neko()
    cvs.delete("NEKO")
    draw_neko()
    
    root.after(100, game_main)
                

root.bind('<Motion>', mouse_move)
root.bind('<ButtonPress>', mouse_press)
cursor = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko_cursor.png')

draw_neko()
game_main()
root.mainloop()