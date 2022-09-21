from glob import glob
import tkinter

key = ""

def key_down(e) :
    global key
    key = e.keysym
    
def main_proc() :
    label['text'] = key
    root.after(100, main_proc)
    
root = tkinter.Tk()
root.title("실시칸 키입력")
# 키를 눌렀을 떄 실행되는 함수 ->KeyPress 는 틀리면 안된다.
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=('Times New Roman', 80))
label.pack()
main_proc()
root.mainloop()