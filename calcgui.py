from tkinter import *
from tkinter import messagebox
import math
window = Tk()#Create window
window.title("Calculator")#Set title
#Text
lbl = Label(window, text="Enter your first number",font=("Georgia Bold", 20))
lb2 = Label(window, text="Enter your next number",font=("Georgia Bold", 20))
lbl.grid(column=0, row=0)
lb2.grid(column=0, row=1)
#Inputbox
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)
def add():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) + float(y)
  except:
    messagebox.showinfo("Calculator", "Enter a valid number!")
  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def minus():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) - float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def multiply():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) * float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def divide():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) / float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")
  
  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def flrdiv():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) // float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def modulo():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) % float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def exponent():
  x = txt.get()
  y = txt2.get()
  try:
   raw = float(x) ** float(y)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def factorial():
  x = txt.get()
  try:
   nx = int(x)
   raw = math.factorial(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def sqrt():
  x = txt.get()
  try:
   nx = int(x)
   raw = math.sqrt(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def absolute():
  x = txt.get()
  try:
   nx = int(x)
   raw = abs(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def sin():
  x = txt.get()
  try:
   nx = int(x)
   raw = math.sin(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def cos():
  x = txt.get()
  try:
   nx = int(x)
   raw = math.cos(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
def tan():
  x = txt.get()
  try:
   nx = int(x)
   raw = math.tan(nx)
  except:
   messagebox.showinfo("Calculator", "Enter a valid number!")

  ans = str(raw)
  msg = "Your answer is "
  messagebox.showinfo("Calculator", msg + ans)
#buttons
add = Button(window, text="Add",height=2,width=12,command=add)
add.grid(column=0, row=2)

subtract = Button(window, text="Subtract",height=2,width=12,command=minus)
subtract.grid(column=0, row=3)

multiply = Button(window, text="Multiply",height=2,width=12,command=multiply)
multiply.grid(column=1, row=2)

divide = Button(window, text="Divide",height=2,width=12,command=divide)
divide.grid(column=1, row=3)

flrdivide = Button(window, text="Floor Division",height=2,width=12,command=flrdiv)
flrdivide.grid(column=1, row=4)

modulo = Button(window, text="Modulo",height=2,width=12,command=modulo)
modulo.grid(column=0, row=4)

exponent = Button(window, text="Exponent",height=2,width=12,command=exponent)
exponent.grid(column=1, row=5)

fact = Button(window, text="Factorial",height=2,width=12,command=factorial)
fact.grid(column=0, row=5)

sqrt = Button(window, text="Square Root",height=2,width=12,command=sqrt)
sqrt.grid(column=1, row=6)

abso = Button(window, text="Absolute Value",height=2,width=12,command=absolute)
abso.grid(column=0, row=6)

sine = Button(window, text="Sine",height=2,width=12,command=sin)
sine.grid(column=1, row=7)

cosine = Button(window, text="Cosine",height=2,width=12,command=cos)
cosine.grid(column=0, row=7)

exitbtn = Button(window, text="Exit",height=2,width=12,command=exit)
exitbtn.grid(column=1, row=8)

tangent = Button(window, text="Tangent",height=2,width=12,command=tan)
tangent.grid(column=0, row=8)

window.resizable(0,0)
window.geometry('500x380')
window.mainloop()
