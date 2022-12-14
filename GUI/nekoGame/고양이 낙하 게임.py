import tkinter as tk

import random

neko = [[0 for _ in range(8)] for _ in range(10)] 

CX = 912
CY = 768

index = 0
timer = 0
score = 0
tsugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0


def draw_neko() :
    cvs.delete("NEKO")
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
    ck = True
    for y in range(8,-1,-1) :
        for x in range(8) :
            if neko[y][x] != 0 and neko[y+1][x] == 0 :
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                ck = False
    return ck
                
def check_neko() :
    visited = [[0 for _ in range(8)] for _ in range(10)]
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]
    
    def in_range(y,x) :
        if x < 0 or x >= 8 or y < 0 or y >= 10 : return False
        return True
    
    def bfs(y,x) :
        ck = neko[y][x]
        visited[y][x] = 1
        arr = [[y,x]]
        q = [[y,x]]
        while q :
            cy = q[0][0]
            cx = q[0][1]
            q.pop(0)
            
            for i in range(4) :
                ny = cy + dy[i]
                nx = cx + dx[i]
                if not in_range(ny, nx) or visited[ny][nx] or neko[ny][nx] != ck : continue
                visited[ny][nx] = 1
                q.append([ny,nx])
                arr.append([ny,nx])
                
        if len(arr) >= 3 :
            for y,x in arr :
                visited[y][x] = 2
                neko[y][x] = 7
                
    for y in range(10) :
        for x in range(8) :
            if visited[y][x] or neko[y][x] == 0 : continue
            bfs(y,x)
        

def sweep_neko() :
    num = 0
    for y in range(9,-1,-1) :
        cnt = 0
        for x in range(8) :
            if neko[y][x] == 7 : cnt += 1
        
        if cnt >= 8 :
            for x in range(8) :
                neko[y][x] = 0
            num += 1 
                
    return num

def over_neko() :
    for x in range(8) :
        if neko[0][x] > 0 :
            return True
    return False    

def set_neko() :
    for x in range(8) :
        neko[0][x] = random.randint(0,6)
        
def draw_txt(txt, x, y, size, col, tg) :
    fnt = ("Times New Roman", size, 'bold')
    cvs.create_text(x+2,y+2, text=txt, fill='black', font=fnt, tag=tg)
    cvs.create_text(x,y, text=txt, fill=col, font=fnt, tag=tg)

    
def game_main() :
    global index, timer, score, tsugi
    global cursor_x, cursor_y, mouse_c
    print(index)
    
    # ????????? ?????? ????????? ???????????? index 1 ??? ????????????.
    if index == 0 :
        draw_txt("????????????", 312,240,100,'violet', 'TITLE')
        draw_txt("Click to start", 312, 560, 80, 'violet', 'TITLE')
        index = 1 
        mouse_c = 0
        
    # ?????? ????????? ?????? ????????? ????????????. ????????? index 2 ??? ????????????.
    elif index == 1 :
        if mouse_c == 1 :
            for y in range(10) :
                for x in range(8) :
                    neko[y][x] = 0
                    
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    
    # ?????? ???????????? ??????????????? ?????? ???????????? index3 ??? ????????????.
    elif index == 2 :
        if drop_neko() :
            index = 3
        draw_neko()
        
    elif index == 3 :
        check_neko()
        draw_neko()
        index = 4
        
    elif index == 4 :
        sc = sweep_neko()
        score += sc*10
        if sc > 0 : 
            index = 2
        else :
            if over_neko() == False :
                tsugi = random.randint(1,6)
                index = 5
            else :
                index = 6
                timer = 0
        draw_neko()
    elif index == 5 :
        if 24 <= mouse_x < 24 + 72*8 and 24 <= mouse_y < 24 + 72*10 :
            cursor_x = int((mouse_x-24) / 72)
            cursor_y = int((mouse_y-24) / 72)
            if mouse_c == 1 and mouse_y < 24 + 72*2 and neko[cursor_y][cursor_x] == 0 :
                mouse_c = 0
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2
        cvs.delete('CURSOR')
        cvs.create_image(cursor_x*72 + 60, cursor_y*72+60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6 :
        timer += 1
        if timer == 1 :
            draw_txt("GAME_OVER", 312, 348, 60, 'red', 'OVER')
        if timer == 50 :
            cvs.delete("OVER")
            index = 0
        
    cvs.delete("INFO")
    draw_txt("SCORE  " + str(score), 160, 60, 32, 'blue', 'INFO')
    
    if tsugi > 0 :
        cvs.create_image(752, 128, image=img_neko[tsugi], tag='INFO')
    
    root.after(100, game_main)
                

root = tk.Tk()
root.title("????????? ???????????????")
root.resizable(False, False)

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

cvs = tk.Canvas(root, width=CX, height=CY)
cvs.pack()
bg = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko_bg.png')     
cvs.create_image(CX/2, CY/2, image=bg)

root.bind('<Motion>', mouse_move)
root.bind('<ButtonPress>', mouse_press)
cursor = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\\neko_cursor.png')

draw_neko()
game_main()
root.mainloop()