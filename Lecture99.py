from tkinter import *

def leftClickButton(event):
    height = txtBoxHight.get()
    weight = txtBoxWegiht.get()
    BMI = int(weight) / (int(height)/100)** 2
    labelTotal.configure(text=BMI)
    if BMI <= 18.5 :
       labelResult.configure(text="ผอมเกินไป")
    elif BMI < 23.0:
       labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI < 25.0:
       labelResult.configure(text="น้ำหนักเกิน")
    elif BMI < 30.0:
       labelResult.configure(text="อ้วน")
    else:
       labelResult.configure(text="อ้วนมาก")

mainwindows = Tk()
lebelheight = Label(mainwindows,text='ส่วนสูง(cm.)')
lebelheight.grid(row=0,column=0)
txtBoxHight = Entry(mainwindows)

txtBoxHight.grid(row=0,column=1)
lebelweight = Label(mainwindows,text='น้ำหนัก(kg.)')
lebelweight.grid(row=1,column=0)

txtBoxWegiht = Entry(mainwindows)
txtBoxWegiht.grid(row=1,column=1)
calculateButton = Button(mainwindows,text='คำนวณ')
calculateButton.grid(row=2)

calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelTotal = Label(mainwindows,text =" ")
labelTotal.grid(row=2,column=1)

labelResult = Label(mainwindows,text=" ")
labelResult.grid(row=3,column=1)

mainwindows.mainloop()