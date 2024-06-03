from tkinter import *

def leftClickButton(event):
    height = txtBoxHight.get()
    weight = txtBoxWight.get()
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

labelWel = Label(mainwindows,text="Welcome to Program BMI",anchor="center",bg ="#b39ddb",fg="#e0f7fa")
labelWel.grid(row=0,column=1)
#-----------ปุ่มส่วนสูง-----------------------
labelheight = Label(mainwindows,text='ส่วนสูง(cm.) ')
labelheight.grid(row=1,column=0)
txtBoxHight = Entry(mainwindows)
txtBoxHight.grid(row=1,column=1)
#-------------ปุ่มน้ำหนัก-----------------------
labelweight = Label(mainwindows,text='น้ำหนัก(Kg.) ')
labelweight.grid(row=2,column=0)
txtBoxWight = Entry(mainwindows)
txtBoxWight.grid(row=2,column=1)
#--------------ปุ่มคำนวณ----------------------
calculateButton = Button(mainwindows,text="คำนวณ")
calculateButton.grid(row=3)
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=3,column=0)
#---------------แสดงผล-------------------------
labelTotal = Label(mainwindows,text =" ")
labelTotal.grid(row=3,column=1)
#---------------------------------------
labelResult = Label(mainwindows,text=" ")
labelResult.grid(row=4,column=1)
#-------------------------------------
mainwindows.mainloop()