from tkinter import *

win = Tk()
win.option_add("*font","Consolas 14")

f = Frame(win)
w=3   # Buttonbreite
h=1   # Buttonhöhe

def taste(t):
    anzeige.config(state="normal")
    anzeige.insert(END, t)
    anzeige.config(state="readonly")

def berechnen():
    try:
        a = eval(anzeige.get())  # Auslesen aus anzeige und berechnen
    except:
        a = "Error"
    anzeige.config(state="normal")
    anzeige.delete(0, END)   # anzeige löschen
    anzeige.insert(0, a)     # anzeige schreiben
    anzeige.config(state="readonly")

def clear():
    anzeige.config(state="normal")
    anzeige.delete(0, END)   # anzeige löschen
    anzeige.config(state="readonly")

anzeige = Entry(font="Consolas 22", readonlybackground="white", width=12, justify="right")
#anzeige.insert(0, "0.00")
anzeige.config(state="readonly")

anzeige.grid(columnspan=5 , column=0, row=0, pady=5)
#for i in anzeige.keys(): print(i, ":", anzeige[i])

btn7 = Button(text="7", width=w, height=h, command=lambda:taste("7"))
btn8 = Button(text="8", width=w, height=h, command=lambda:taste("8"))
btn9 = Button(text="9", width=w, height=h, command=lambda:taste("7"))
btnplus = Button(text="+", width=w, height=h, command=lambda:taste("+"))
btnminus = Button(text="-", width=w, height=h, command=lambda:taste("-"))

btn4 = Button(text="4", width=w, height=h, command=lambda:taste("4"))
btn5 = Button(text="5", width=w, height=h, command=lambda:taste("5"))
btn6 = Button(text="6", width=w, height=h, command=lambda:taste("6"))
btnmult = Button(text="*", width=w, height=h, command=lambda:taste("*"))
btndiv = Button(text="/", width=w, height=h, command=lambda:taste("/"))

btn1 = Button(text="1", width=w, height=h, command=lambda:taste("1"))
btn2 = Button(text="2", width=w, height=h, command=lambda:taste("2"))
btn3 = Button(text="3", width=w, height=h, command=lambda:taste("3"))
btnkl1 = Button(text="(", width=w, height=h, command=lambda:taste("("))
btnkl2 = Button(text=")", width=w, height=h, command=lambda:taste(")"))

btn0 = Button(text="0", width=w, height=h, command=lambda:taste("0"))
btnkomma = Button(text=".", width=w, height=h, command=lambda:taste("."))
btnenter = Button(text="=", width=w, height=h, command=berechnen)
btnclr = Button(text="CE", width=w, height=h, bg="red", command=clear)

btn7.grid(column=0, row=1) 
btn8.grid(column=1, row=1) 
btn9.grid(column=2, row=1) 
btnplus.grid(column=3, row=1) 
btnminus.grid(column=4, row=1) 

btn4.grid(column=0, row=2) 
btn5.grid(column=1, row=2) 
btn6.grid(column=2, row=2) 
btnmult.grid(column=3, row=2) 
btndiv.grid(column=4, row=2) 

btn1.grid(column=0, row=3) 
btn2.grid(column=1, row=3) 
btn3.grid(column=2, row=3) 
btnkl1.grid(column=3, row=3)
btnkl2.grid(column=4, row=3)

btn0.grid(column=0, row=4) 
btnkomma.grid(column=1, row=4) 
btnenter.grid(column=2, row=4) 
btnclr.grid(column=3, row=4)

win.mainloop()