import tkinter as tk

root = tk.Tk()
root.title("고양이 진단 게임")
root.resizable(False, False)

# 사진이 800x600 이므로 해당 픽셀로 고정
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tk.PhotoImage(file='C:\WorkSpace\PyGame\GUI\images\mina.png')
canvas.create_image(400, 300, image=gazou)

KEKKA = [
    '전생에 고양이었을 가능성은 매우 낮습니다.',
    '보통 사람입니다.',
    '특별히 이상한 곳은 없습니다.',
    '꽤 고양이다운 구석이 있습니다.',
    '고양이와 비슷한 성격 같습니다.',
    '고양이와 근접한 성격입니다.',
    '전생에 고양이었을지도 모릅니다.',
    '겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다.',
]

def click_btn() :
    cnt = 0
    for i in range(7) :
        if bvar[i].get() == True :
            cnt+=1
    text.delete(1.0, tk.END)
    nekodo = int(100 * cnt / 7)
    text.insert(1.0, f"<진단결과>\n 당신의 고양이 지수는 {nekodo}% 입니다.\n{KEKKA[cnt]}")

button = tk.Button(text='진단하기', font=("Times New Roman", 32), bg='lightgreen',
                   command=click_btn)
button.place(x=400, y=480)

text = tk.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None] * 7
cbtn = [None] * 7
ITEM = [
    '높은 곳이 좋다.',
    '공을 보면 굴리고 싶어진다.',
    '깜짝 놀라면 털이 곤두선다.',
    '쥐구멍이 마음에 든다.',
    '개에게 적대감을 느낀다.',
    '생선 뼈를 발라 먹고 싶다.',
    '밤, 기운이 난다.'
]

for i in range(7) :
    bvar[i] = tk.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tk.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), 
                             variable=bvar[i], bg='#dfe')
    cbtn[i].place(x=400, y=160 + 40*i)

root.mainloop()