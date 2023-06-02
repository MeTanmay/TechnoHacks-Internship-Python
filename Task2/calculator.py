import tkinter as tk
from tkinter import *

BLUE="#2E3840"
GREY="#B2B2B2"

window=tk.Tk()


# Display-size

window.geometry("400x520")
window.title("Tanmay's Calculator")
window.maxsize(400,530)
window.minsize(400,530)

window['bg']="#EEEEEE"


input=Entry(window, width=20,font=('Arial',18, 'bold'),borderwidth=10, relief=RIDGE,)
input.grid(pady=15, row=0,sticky="W", padx=20, ipady=15)


#Logic (functions to evaluate result)

def delete():
    a = input.get()
    input.delete(first=len(a)-1,last="end")
def fresult():
    if input.get() == "":
        pass
    elif input.get()[0] == "0":
        input.delete(0,"end")
    else: 
        c_res = input.get()
        c_res = eval(c_res)
        clearf()
        input.insert("end",c_res)
def clearf():
    input.delete(0,"end")


# Buttons

clean = Button(window,text="C",width=4,borderwidth=5,command=clearf,relief=RIDGE,font=('Arial',15, 'bold'),bg="#0E8388",fg="white")
clean.grid(pady=15,row=0,sticky="w",padx=325, ipady=15)


Char_nine = Button(text="9",width=5,command=lambda :input.insert("end","9"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_nine.grid(pady=10,row=1,sticky="w",padx=20, ipady=15)

Char_eight = Button(text="8",width=5,command=lambda :input.insert("end","8"),borderwidth=5,relief=RIDGE, font=('Arial',12, 'bold'))
Char_eight.grid(pady=10,row=1,sticky="w",padx=117, ipady=15)

Char_seven = Button(text="7",width=5,command=lambda :input.insert("end","7"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_seven.grid(pady=10,row=1,sticky="w",padx=214, ipady=15)

Char_plus = Button(text="+",width=5,command=lambda :input.insert("end","+"),borderwidth=5,relief=RIDGE, font=('Arial',12, 'bold'), bg=GREY,fg="black")
Char_plus.grid(pady=10,row=1,sticky="w",padx=322, ipady=15)

Char_six = Button(text="6",width=5,command=lambda :input.insert("end","6"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_six.grid(pady=5,row=2,sticky="w",padx=20, ipady=15)

Char_five = Button(text="5",width=5,command=lambda :input.insert("end","5"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_five.grid(pady=5,row=2,sticky="w",padx=117, ipady=15)

Char_four = Button(text="4",width=5,command=lambda :input.insert("end","4"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_four.grid(pady=5,row=2,sticky="w",padx=214, ipady=15)

Char_minus = Button(text="-",width=5,command=lambda :input.insert("end","-"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'), bg=GREY,fg="black")
Char_minus.grid(pady=5,row=2,sticky="w",padx=322, ipady=15)

Char_three = Button(text="3",width=5,command=lambda :input.insert("end","3"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_three.grid(pady=5,row=3,sticky="w",padx=20, ipady=15)

Char_two = Button(text="2",width=5,command=lambda :input.insert("end","2"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_two.grid(pady=5,row=3,sticky="w",padx=117, ipady=15)

Char_one = Button(text="1",width=5,command=lambda :input.insert("end","1"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_one.grid(pady=5,row=3,sticky="w",padx=214, ipady=15)

Char_Mul = Button(text="*",width=5,command=lambda :input.insert("end","*"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'), bg=GREY,fg="black")
Char_Mul.grid(pady=5,row=3,sticky="w",padx=322, ipady=15)

Char_zero = Button(text="0",width=5,command=lambda :input.insert("end","0"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_zero.grid(pady=5,row=4,sticky="w",padx=20, ipady=15)

Char_2zero = Button(text="00",width=5,command=lambda :input.insert("end","00"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_2zero.grid(pady=5,row=4,sticky="w",padx=117, ipady=15)

Char_dot = Button(text=".",width=5,command=lambda :input.insert("end","."),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
Char_dot.grid(pady=5,row=4,sticky="w",padx=214, ipady=15)

Char_Divide = Button(text="/",width=5,command=lambda :input.insert("end","/"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'),bg=GREY,fg="black")
Char_Divide.grid(pady=5,row=4,sticky="w",padx=322, ipady=15)

result =Button(window,text="=",width=15,command=fresult,bg="#0E8388",fg="white",borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
result.grid(row=5,sticky="w",padx=20,pady=10, ipady=15)

DEL= Button(window,text="del",width=5,command=delete,bg="#0E8388",fg="white",borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'))
DEL.grid(row=5,sticky="w",padx=214,pady=10, ipady=15)

Char_modulus = Button(window,text="%",width=5,command=lambda :input.insert("end","%"),borderwidth=5,relief=RIDGE,font=('Arial',12, 'bold'), bg=GREY,fg="black")
Char_modulus.grid(row=5,sticky="w",padx=322,pady=10, ipady=15,)



window.mainloop()
