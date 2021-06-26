import random
from tkinter import *
from tkinter import messagebox

lis = ["ability", "about", "above", "abroad", "absence", "absolute","basic","body","bomb",
       "apple","group","java","python","kids","mango","boy","common","catch","center","every","failure","fair",
       "kite","hairs","one","acid","attract","background","bank","famous","makeup","meeting"]


def random_word():
    global r,jumbled,count
    r = random.choice(lis)
    random_word = random.sample(r, len(r))
    jumbled = ''.join(random_word)


random_word()

def check():
    count = 0
    a=ans.get()
    if a == r:
        messagebox.showinfo("Success", "right answer")
        reverse()
    else:
        messagebox.showerror("Error", "wrong answer the answer is "+r)
        reverse()

def exit():
    quit()


root=Tk()
frame = Frame(root,
               bg = "#DADCFF",
               height = "150")
frame.pack(fill = X)

width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


root.title("Jumble words game")
ans = StringVar()
var = StringVar()
var.set(jumbled)

l1=Label(root,text="Jumble word game",font=("optima",49,"bold"))
l2=Label(root,font=("arial",49,"bold"),textvariable = var,bg="skyblue")
l3=Label(root,text="Guess the\n Right word",font=("arial",40,"bold"))
l4=Label(root,text="made by atul Sharma",font=("chiller",30,"italic"),bg="lightgreen")


e1=Entry(root,font=("arial",49,"bold"),textvariable=ans)
b1=Button(root,text="Check",height=5,width=20,bd=15,font=("arial",12,"bold")
          ,activebackground="#03FF42",command=check)
b2=Button(root,text="Exit",height=5,width=20,bd=15,font=("arial",12,"bold")
          ,activebackground="red",command=exit)


def reverse():
    random_word()
    var.set(jumbled)
    e1.delete(0, END)

l1.place(x=500,y=10)
l2.place(x=700,y=200)
l3.place(x=0,y=270)
l4.place(x=0,y=700)
e1.place(x=400,y=300)
b1.place(x=500,y=500)
b2.place(x=850,y=500)

root.mainloop()


