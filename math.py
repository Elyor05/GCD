from tkinter import *

okno = Tk()
okno.title("GCD")
okno.geometry("800x400")
okno.iconbitmap("math_icon_244051.ico")
okno.resizable(width=False, height=False)
okno.config(bg="#8D918D")


def gcd(f, s):
    maxi = max(f, s)
    mini = min(f, s)
    mul = maxi // mini
    ast = maxi - mul * mini
    answer.insert(END, (str(maxi) + ' = ' + str(mini) + ' * ' + str(mul) + ' + ' + str(ast) + "\n"))
    if ast != 0:
        gcd(mini, ast)
    else:
        answer.insert(END, ("Answer is " + str(mini)))


def deli():
    fst.delete(0, END)
    scd.delete(0, END)
    answer.delete(1.0, END)


fst = Entry(okno, width=20, font=("Arial", 18))
scd = Entry(okno, width=20, font=("Arial", 18))

fst.place(x=20, y=20, width=160)
scd.place(x=20, y=60, width=160)

calc = Button(okno, text="Calculate", command=lambda: gcd(int(fst.get()), int(scd.get())))
calc.place(x=40, y=100)

clear = Button(okno, text="Clear", command=deli)
clear.place(x=120, y=100)

answer = Text(okno, width=40, height=100, font=("Comic Sans MS", 18))
answer.place(x=200, y=20, width=580, height=340)

okno.mainloop()
