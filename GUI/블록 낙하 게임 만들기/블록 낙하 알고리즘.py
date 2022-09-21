import tkinter as tk

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
                
def drop_neko_one_time() :
    ck = False
    for y in range(8,-1,-1) :
        for x in range(8) :
            if neko[y][x] != 0 and neko[y+1][x] == 0 :
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                ck = True
    return ck
                
def drop_neko() :
    cvs.delete("NEKO")
    ck = drop_neko_one_time()
    draw_neko()
    if ck : root.after(1000, drop_neko)
                

draw_neko()
drop_neko()
root.mainloop()