import tkinter as tk

key = ""

mx = 1
my = 1

maze =[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

def key_down(e) :
    global key
    key = e.keysym
    
def key_up(e) :
    global key
    key = ""

def main_proc() :
    global mx, my
    if key == 'Up' and maze[my-1][mx] == 0 :
        my -= 1
    if key == 'Down' and maze[my+1][mx] == 0 :
        my += 1
    if key == 'Left' and maze[my][mx-1] == 0 :
        mx -= 1
    if key == 'Right' and maze[my][mx+1] == 0 :
        mx += 1
        
    # 이미지의 위치를 다시 설정하는 함수
    canvas.coords("MYCHR", mx*80+40, my*80+40)
    root.after(100, main_proc)
    
    
root = tk.Tk()
root.title('미로 안 이동하기')
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tk.Canvas(width=800, height=560, bg='white')
canvas.pack()

for y in range(7) :
    for x in range(10) :
        if maze[y][x] == 1 : 
            canvas.create_rectangle(x*80,y*80,(x+1)*80,(y+1)*80, fill='skyblue')
            
img = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\mimi_s.png')
canvas.create_image(mx*80+40, my*80+40, image=img, tag='MYCHR')
main_proc()
root.mainloop()