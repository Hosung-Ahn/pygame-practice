import tkinter as tk
root = tk.Tk()
root.title("미로 표시")
canvas = tk.Canvas(width=800, height=560, bg='white')
canvas.pack()

maze =[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

for y in range(7) :
    for x in range(10) :
        if maze[y][x] == 1 :
            canvas.create_rectangle(x*80, y*80, (x+1)*80, (y+1)*80, fill='gray')

root.mainloop()