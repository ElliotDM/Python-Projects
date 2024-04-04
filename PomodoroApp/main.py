import time
import datetime
import threading
from tkinter import *

countdown = "25:00"
work = True
rest = False
iterations = 0


def change_color(color: str):
    frame.config(bg=color)
    label.config(bg=color)


def update_label():
    global countdown
    label.config(text=countdown)
    root.after(1000, update_label)


def pomodoro():
    global countdown
    global work
    global rest
    global iterations
    total_seconds = 0

    start.config(state=DISABLED)

    # TODO: fix pomodoro iterations
    # iterations = 4
    if iterations >= 2:
        total_seconds = 0.5 * 60
        work = True
        iterations = 0
    elif work:
        total_seconds = 0.25 * 60
        work = False
        rest = True
    elif rest and iterations < 2:
        total_seconds = 0.25 * 60
        work = True
        rest = False
        iterations += 1

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        countdown = str(timer)[2:]
        time.sleep(1)
        total_seconds -= 1
    
    if iterations >= 2:
        countdown = "15:00"
        change_color("#00A2E8")
    elif work:
        countdown = "25:00"
        change_color("#D61616") 
    elif rest:
        countdown = "05:00"
        change_color("#16BE16") 

    start.config(state=NORMAL)


def start_pomodoro():
    x = threading.Thread(target=pomodoro)
    x.start()
    update_label()


root = Tk()
root.title("Pomodoro")
root.geometry("420x300")
root.resizable(0,0)

frame = Frame(root, 
              width=400,
              height=180)
frame.config() 

# TODO: fix label size
label = Label(root, text=countdown)
label.config(fg="#FFFFFF",
             bg="#D61616",
             font=("Segoe UI Black",50))

start = Button(root, 
               text="START",
               font=("Segoe UI",16),
               command=start_pomodoro)

frame.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
label.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
start.grid(row=1,column=1, columnspan=2, padx=10, pady=10)

root.mainloop()

