from tkinter import *
t=Tk()
t.geometry("400x400")
t.resizable(0,0)
t.title("Tic Tac Toe : Shivam")
x=StringVar()
y=StringVar()
z=StringVar()
q=0
t.configure(background="#091e42")

def set():
    p1=x.get()
    p2=y.get()
    z.set(p1 + " vs " + p2)

def game(u):
    global q
    if q%2==0 :
        u["text"] = "X"
    else :
        u["text"] = "O"
    q = q + 1

def res(*r):
    if (r[0]["text"]==r[1]["text"] and r[1]["text"]==r[2]["text"]):
        z.set(r[0]["text"] + " wins the game")
    if (r[3]["text"]==r[4]["text"] and r[4]["text"]==r[5]["text"]):
        z.set(r[3]["text"] + " wins the game")
    if (r[6]["text"]==r[7]["text"] and r[7]["text"]==r[8]["text"]):
        z.set(r[6]["text"] + " wins the game")
    if (r[0]["text"]==r[3]["text"] and r[3]["text"]==r[6]["text"]):
        z.set(r[0]["text"] + " wins the game")
    if (r[1]["text"]==r[4]["text"] and r[4]["text"]==r[7]["text"]):
        z.set(r[1]["text"] + " wins the game")
    if (r[2]["text"]==r[5]["text"] and r[5]["text"]==r[8]["text"]):
        z.set(r[2]["text"] + " wins the game")
    if (r[0]["text"]==r[4]["text"] and r[4]["text"]==r[8]["text"]):
        z.set(r[0]["text"] + " wins the game")
    if (r[2]["text"]==r[4]["text"] and r[4]["text"]==r[6]["text"]):
        z.set(r[2]["text"] + " wins the game")

    for i in r:
        i["text"]=""
    global q
    q=0


un = Label(t,text="Tic Tac Toe",font=("Times New Roman",14),width="18",height="2",bg="#091e42",fg="white")
un.grid(row=0,column=0,columnspan=2)

un2 = Label(t,text="First Player X",font=("Arial",14),width="18",bg="#091e42",fg="white")
un2.grid(row=1,column=0,pady=10,sticky=W)

e1 = Entry(t,font=("Arial",10),textvariable=x)
e1.grid(row=1,column=1)

un1 = Label(t,text="Second Player O",font=("Arial",14),width="18",bg="#091e42",fg="white")
un1.grid(row=2,column=0,pady=5,sticky=W)

e2 = Entry(t,font=("Arial",10),textvariable=y)
e2.grid(row=2,column=1)

b = Button(t,text="Start",font=("Arial",12),command=set,bg="#091e42",fg="white")
b.grid(row=3,column=0,columnspan=2)

b1 = Button(t,text="",font=("Arial",15),command= lambda : game(b1),bg="#091e42",fg="white")
b1.place(x=70, y=180, width=80, height=40)

b2 = Button(t,text="",font=("Arial",15),command= lambda : game(b2),bg="#091e42",fg="white")
b2.place(x=155, y=180, width=80, height=40)

b3 = Button(t,text="",font=("Arial",15),command= lambda : game(b3),bg="#091e42",fg="white")
b3.place(x=240, y=180, width=80, height=40)

b4 = Button(t,text="",font=("Arial",15),command= lambda : game(b4),bg="#091e42",fg="white")
b4.place(x=70, y=220, width=80, height=40)

b5 = Button(t,text="",font=("Arial",15),command= lambda : game(b5),bg="#091e42",fg="white")
b5.place(x=155, y=220, width=80, height=40)

b6 = Button(t,text="",font=("Arial",15),command= lambda : game(b6),bg="#091e42",fg="white")
b6.place(x=240, y=220, width=80, height=40)

b7 = Button(t,text="",font=("Arial",15),command= lambda : game(b7),bg="#091e42",fg="white")
b7.place(x=70, y=260, width=80, height=40)

b8 = Button(t,text="",font=("Arial",15),command= lambda : game(b8),bg="#091e42",fg="white")
b8.place(x=155, y=260, width=80, height=40)

b9 = Button(t,text="",font=("Arial",15),command= lambda : game(b9),bg="#091e42",fg="white")
b9.place(x=240, y=260, width=80, height=40)

b10 = Button(t,text="Result/Reset",font=("Arial",10),command= lambda : res(b1,b2,b3,b4,b5,b6,b7,b8,b9),bg="#091e42",fg="white")
b10.place(x=300, y=330, width=90, height=40)

un3 = Label(t,text="Play Now",font=("Arial",14),width="30",textvariable=z,bg="#091e42",fg="white")
un3.place(x=100,y=320,width=160,height=50)

t.mainloop()