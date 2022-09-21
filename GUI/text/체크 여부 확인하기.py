import tkinter as tk
root = tk.Tk()
root.title("처음부터 체크된 상태 만들기")
root.geometry("400x200")

def check() :
    if cval.get() == True :
        print("체크되어 있습니다.")
    else :
        print("체크되어 있지 않습니다.")
    
    
cval = tk.BooleanVar()
cval.set(False)
cbtn = tk.Checkbutton(text='체크 버튼', variable=cval, command=check)
cbtn.pack()

root.mainloop()