from tkinter import *

app = Tk()
app.title("My first project")
app.config(background="black")

e = Entry(app,width=35,borderwidth=5,bg="black",fg="white")
e.grid(row=0,column=0,columnspan=10,padx=20,pady=20)

#Funciones de los botones
def button_add(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

def number1():
    num1 = e.get()
    global num #global = The variable is can be used in others function
    num = int(num1)
    e.delete(0,END)


def button_equal():
    
    number2 = e.get()
    global snum
    snum = int(number2)
    e.delete(0,END)

    if operation == "plus":
        e.insert(0,num + snum)
    elif operation == "subtract":
        e.insert(0,num - snum)
    elif operation == "multi":
        e.insert(0,num * snum)
    elif operation == "divide":
        e.insert(0,num / snum)
    elif operation == "exp":
        e.insert(0,num**snum)

#Operation functions
def button_plus():
    global operation
    operation = "plus"
    number1()
    e.delete(0,END)

def button_rest():
    global operation
    operation = "subtract"
    number1()
    e.delete(0,END)

def button_multiply():
    global operation
    operation = "multi"
    number1()
    e.delete(0,END)

def button_divide():
    global operation
    operation = "divide"
    number1()
    e.delete(0,END)

def button_exp():
    global operation
    operation = "exp"
    number1()
    e.delete(0,END)


def delete():
    e.delete(0,END)


#Numbers
button1 = Button(app,fg="white",bg="#2B2422",text="1",padx=30,pady=30,command=lambda: button_add(1)).grid(row=3,column=0)
button2 = Button(app,fg="white",bg="#2B2422",text="2",padx=30,pady=30,command=lambda: button_add(2)).grid(row=3,column=1)
button3 = Button(app,fg="white",bg="#2B2422",text="3",padx=30,pady=30,command=lambda: button_add(3)).grid(row=3,column=2)
button4 = Button(app,fg="white",bg="#2B2422",text="4",padx=30,pady=30,command=lambda: button_add(4)).grid(row=2,column=0)
button5 = Button(app,fg="white",bg="#2B2422",text="5",padx=30,pady=30,command=lambda: button_add(5)).grid(row=2,column=1)
button6 = Button(app,fg="white",bg="#2B2422",text="6",padx=30,pady=30,command=lambda: button_add(6)).grid(row=2,column=2)
button7 = Button(app,fg="white",bg="#2B2422",text="7",padx=30,pady=30,command=lambda: button_add(7)).grid(row=1,column=0)
button8 = Button(app,fg="white",bg="#2B2422",text="8",padx=30,pady=30,command=lambda: button_add(8)).grid(row=1,column=1)
button9 = Button(app,fg="white",bg="#2B2422",text="9",padx=30,pady=30,command=lambda: button_add(9)).grid(row=1,column=2)
button0 = Button(app,fg="white",bg="#2B2422",text="0",padx=30,pady=30,command=lambda: button_add(0)).grid(row=4,column=0)

#Result
equal = Button(app,fg="white",bg="#A7A3A1",text="=",padx=30,pady=30,command=button_equal).grid(row=4,column=1)

#Operations
plus = Button(app,fg="white",bg="#CD6B20",text="+",padx=30,pady=30,command=button_plus).grid(row=1,column=4)
subtract = Button(app,fg="white",bg="#CD6B20",text="-",padx=30,pady=30,command=button_rest).grid(row=2,column=4)
multiply = Button(app,fg="white",bg="#CD6B20",text="x",padx=30,pady=30,command=button_multiply).grid(row=3,column=4)
divide = Button(app,fg="white",bg="#CD6B20",text="/",padx=30,pady=30,command=button_divide).grid(row=4,column=4)
exp = Button(app,fg="white",bg="#CD6B20",text="^",padx=30,pady=30,command=button_exp).grid(row=5,column=4)
clear = Button(app,fg="white",bg="#A7A3A1",foreground="white",text="C",padx=30,pady=30,command=delete).grid(row=4,column=2)


app.mainloop()
