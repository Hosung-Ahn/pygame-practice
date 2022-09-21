import tkinter
import tkinter.messagebox

idx = 0
tmr = 0
stage = 1
ir = 0
rc = 0
key = 0

def key_down(e) :
    global key
    key = e.keysym
    
def key_up(e) :
    global key 
    key = 0
    
maze = []

def stage_data() :
    global ir, rc
    global maze
    if stage == 1 :
        ir = 1
        ic = 1
        maze = [
            [9,9,9,9,9,9,9,9,9,9],
            [9,0,9,0,0,0,9,0,0,9],
            [9,0,9,0,9,0,9,0,0,9],
            [9,0,9,0,9,0,9,0,9,9],
            [9,0,9,0,9,0,9,0,0,9],
            [9,0,0,0,9,0,0,0,0,9],
            [9,9,9,9,9,9,9,9,9,9]
        ]
    
    if stage == 2 :
        ir = 8
        ic = 6
        maze = [
            [9,9,9,9,9,9,9,9,9,9],
            [9,0,0,0,0,0,0,0,0,9],
            [9,0,0,0,0,0,0,9,0,9],
            [9,0,0,9,9,0,0,9,0,9],
            []
        ]