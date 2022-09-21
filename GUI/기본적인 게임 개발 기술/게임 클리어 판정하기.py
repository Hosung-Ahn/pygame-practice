import tkinter as tk
import tkinter.messagebox

key = ""

def key_down(e) :
    global key
    key = e.keysym
    
def key_up(e) :
    global key
    key = ""
    
mx = 1
my = 1
yuka = 0

maze =[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

def clear() :
    global mx, my, yuka
    mx = 1
    my = 1
    yuka = 0
    for r in range(7) :
        for c in range(10) :
            if maze[r][c] == 2 : maze[r][c] = 0
            
    canvas.delete('PAINT')

def main_proc() :
    global mx, my, yuka
    if key == "Up" and maze[my-1][mx] == 0 :
        my -= 1
    if key == "Down" and maze[my+1][mx] == 0 :
        my += 1
    if key == 'Left' and maze[my][mx-1] == 0 :
        mx -= 1
    if key == 'Right' and maze[my][mx+1] == 0 :
        mx += 1
    if maze[my][mx] == 0 :
        maze[my][mx] = 2
        yuka += 1
    if key == 'Shift_L' and yuka > 1 :
        clear()
        
    canvas.create_rectangle(mx*80,my*80,(mx+1)*80,(my+1)*80, fill='pink', tag='PAINT')
    canvas.delete("MYCHR")
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
    canvas.coords("MYCHR", mx*80+40,my*80+40)
    
    if yuka >= 30 :
        tkinter.messagebox.showinfo("END", "GAME CLEAR")
    else :
        root.after(100, main_proc)
        
root = tk.Tk()
root.title("미로를 칠한다냥")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tk.Canvas(width=800, height=560, bg='white')
canvas.pack()

for y in range(7) :
    for x in range(10) :
        if maze[y][x] == 1 : 
            canvas.create_rectangle(x*80,y*80,(x+1)*80,(y+1)*80, fill='skyblue')

img = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\mimi_s.png')
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")

main_proc()
root.mainloop()
