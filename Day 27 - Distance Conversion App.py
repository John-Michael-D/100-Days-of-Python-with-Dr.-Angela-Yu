from tkinter import *

def buttonClicked1():
    n = float(input1.get())
    result = n * 1.609344
    label4["text"] = f"{result:.2f}"

def buttonClicked2():
    n = float(input2.get())
    result = n / 1.609344
    label7["text"] = f"{result:.2f}"

window = Tk()
window.title("Miles to Kilometers and Kilometers to Miles Converter")
window.minsize(width=500, height=300)
window.maxsize(width=500, height=300)

label1 = Label(text="Miles",font=("Arial",12))
label1.place(x=150,y=55)
label2 = Label(text="is equal to",font=("Arial",12))
label2.place(x=200,y=55)
label3 = Label(text="Kilometers",font=("Arial",12))
label3.place(x=350,y=55)
label4 = Label(text="0",font=("Arial",12))
label4.place(x=300,y=55)

label5 = Label(text="Kilometers",font=("Arial",12))
label5.place(x=140,y=150)
label6 = Label(text="is equal to",font=("Arial",12))
label6.place(x=225,y=150)
label7 = Label(text="0",font=("Arial",12))
label7.place(x=325,y=150)
label8 = Label(text="Miles",font=("Arial",12))
label8.place(x=375,y=150)

button1 = Button(text="Calculate!",command=buttonClicked1)
button1.place(x=200,y=90)
button2 = Button(text="Calculate!",command=buttonClicked2)
button2.place(x=200,y=185)


input1 = Entry(width=10)
input1.insert(END,string="0")
input1.place(x=50,y=55)
input2 = Entry(width=10)
input2.insert(END,string="0")
input2.place(x=50,y=150)

window.mainloop()