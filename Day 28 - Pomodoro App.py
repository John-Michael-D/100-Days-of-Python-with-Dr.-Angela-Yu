from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SOUND_EFFECT = AudioSegment.from_mp3("digital-ding-bell-notification-tone-352772.mp3")
# ---------------------------- TIMER RESET ------------------------------- #
timer = None
reps = 1
def resetReps():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    label1["text"] = "Timer"
    label1.place(x=50, y=-45)
    reps -= reps
    reps += 1
    label2["text"] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60
    if reps % 8 == 0 and reps != 1:
        reps += 1
        label1["text"] = "Long Break"
        label1.place(x=5, y=-45)
        countDown(longBreakSec)
    elif reps % 2 == 0 and reps != 1:
        reps += 1
        label1["text"] = "Short Break"
        label1.place(x=5, y=-45)
        countDown(shortBreakSec)
    else:
        reps += 1
        label1["text"] = "Work"
        label1.place(x=60, y=-45)
        countDown(workSec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    global timer
    countMin = math.floor(count/60)
    countSec = count % 60
    if countSec >= 10 and count > 0:
        canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
        timer = window.after(1000, countDown, count - 1)
    elif countSec <= 9 and count > 0:
        canvas.itemconfig(timerText, text=f"{countMin}:0{countSec}")
        timer = window.after(1000, countDown, count - 1)
    if count == 0:
        canvas.itemconfig(timerText, text="00:00")
        label1["text"] = "Timer"
        label1.place(x=50, y=-45)
        if count == 0 and label1["text"] == "Timer":
            play(SOUND_EFFECT)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time Management")
window.config(padx=100,pady=50,bg=PINK)
window.minsize(width=400,height=325)
window.maxsize(width=400,height=325)

canvas = Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomatoImg)
timerText = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()

label1 = Label(text="Timer",fg=YELLOW,bg=PINK,font=(FONT_NAME,24))
label1.place(x=50,y=-45)
label2 = Label(text="✓" * ((reps - 1) // 2), fg=YELLOW, bg=PINK, font=(FONT_NAME, 24))
label2.place(x=-90, y=240)

button1 = Button(text="Start",highlightthickness=0, command=startTimer)
button1.place(x=-50,y=200)
button2 = Button(text="Reset",highlightthickness=0, command=resetReps)
button2.place(x=190,y=200)

window.mainloop()