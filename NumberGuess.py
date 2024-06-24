import random
import tkinter as tk
import sys

rnum = random.randint(1, 1000)
gnum = 0
score = 0

def guess():
    
    global rnum
    global gnum
    global score
    
    #while(rnum != gnum):
    gnum = int(ent1.get())
    print(gnum)
    #int(input(" Number Guess: "))
    score += 1
    if(gnum > rnum):
        #print("Number guess is high!")
        txt1.insert(tk.END, "Number is high!: ")
        txt1.insert(tk.END, gnum)
        txt1.insert(tk.END, "\n")
    elif(gnum < rnum):
        #print("Number guess is low!")
        txt1.insert(tk.END, "Number is low!: ")
        txt1.insert(tk.END, gnum)
        txt1.insert(tk.END, "\n")
    else:
        #print("Correct!!!")
        txt1.insert(tk.END, "\nCorrect!\n")
        txt1.insert(tk.END, gnum)
        txt1.insert(tk.END, "\n")
        
    #print("Score is: ", score)
    txt1.insert(tk.END, "Score is: ")
    txt1.insert(tk.END, score)
    txt1.insert(tk.END, "\n")
    ent1.delete(0, tk.END)
    
def exit():
    sys.exit()
        
wnd = tk.Tk()
wnd.title = ("Number Guess Game")
wnd.configure(bg = "blue")
wnd.geometry("300x300")

ent1 = tk.Entry(wnd)
ent1.pack(padx = 10, pady = 10)

btn1 = tk.Button(wnd, text = "Submit", command=guess)
btn1.pack(padx = 10, pady = 10)

btn2 = tk.Button(wnd, text = "exit", command=exit)
btn2.pack(padx = 10, pady = 10)

txt1 = tk.Text(wnd, bg = 'cyan', fg = 'black')
txt1.pack(padx = 10, pady = 10)
        
print("Final score is: ", score)

wnd.mainloop()
