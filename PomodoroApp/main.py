import time
import datetime
import threading
from tkinter import *
from tkinter import messagebox

NUM_ITERATIONS = 4
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

    if iterations >= NUM_ITERATIONS:
        total_seconds = 15 * 60
        work = True
        iterations = 0
    elif work:
        total_seconds = 25 * 60
        work = False
        rest = True
        iterations += 1
    elif rest and iterations < NUM_ITERATIONS:
        total_seconds = 5 * 60
        work = True
        rest = False

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        countdown = str(timer)[2:]
        time.sleep(1)
        total_seconds -= 1
    
    if iterations >= NUM_ITERATIONS:
        countdown = "15:00"
        change_color("#00A2E8")
        messagebox.showinfo(message="Take a long rest", title="Pomodoro")
    elif work:
        countdown = "25:00"
        change_color("#D61616") 
        messagebox.showinfo(message="Continue working", title="Pomodoro")
    elif rest and iterations < NUM_ITERATIONS:
        countdown = "05:00"
        change_color("#16BE16")
        messagebox.showinfo(message="Take a rest", title="Pomodoro")

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

label = Label(frame, text=countdown)
label.config(fg="#FFFFFF",
             bg="#D61616",
             font=("Segoe UI Black",50))

start = Button(root, 
               text="START",
               font=("Segoe UI",16),
               command=start_pomodoro)

# TODO: add pause button

frame.pack(expand=True, fill=BOTH, padx=20, pady=10)
label.pack(expand=True, fill=BOTH)
start.pack(padx=20, pady=10)

root.mainloop()

