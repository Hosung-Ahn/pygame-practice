import tkinter as tk
key = 0
def key_down(e) :
    global key
    key = e.keycode
    print("Key: " + str(key))
    
root = tk.Tk()
root.title("키 코드 얻기")
root.bind("<KeyPress>", key_down)
root.mainloop()