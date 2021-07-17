from tkinter import *
from tkinter import messagebox
#Use metres and kilograms!
window = Tk()#Create window
window.title("BMI Calculator")#Set title

lbl = Label(window, text="Enter your weight",font=("Georgia Bold", 20))#Label 1
lb2 = Label(window, text="Enter your height",font=("Georgia Bold", 20))#Label 2
lbl.grid(column=0, row=0)#Place label
lb2.grid(column=0, row=1)#Place label

txt = Entry(window,width=10)#input
txt.grid(column=1, row=0)#place input
txt2 = Entry(window,width=10)#input
txt2.grid(column=1, row=1)#place input
def clicked():
 a =  txt.get()#get int
 b =  txt2.get()#get int
 try:
  weight = float(a)#convert to float
  height = float(b)#convert to float
  heightsq = height * height#get height squared
  raw = weight / heightsq#get raw bmi
  ans = str(round(raw, 1))#round it and convert it to string
 except:
  messagebox.showinfo("BMI Calculator", "Enter a valid weight and height!")
 msg = "Your BMI is "#message to you
 messagebox.showinfo("BMI Calculator", msg + ans)#Create a messagebox that shows you your bmi

btn = Button(window, text="Try it",command=clicked)
btn.grid(column=1, row=2)
window.geometry('600x200')
window.mainloop()
