from tkinter import *

task_list = []

root = Tk()
root.title("ToDo")
root.geometry("300x500")
root.resizable(1,0)

task_var = StringVar()

label = Label(root, 
              text="ToDo", 
              font=("Segoe UI",18))

frame = Frame(root, 
              bg="#30C9E4")

entry = Entry(root,
              textvariable=task_var,
              font=("Segoe UI",14))

def submit_task():
    task_frame = Frame(frame,
                       bg="#FFFFFF")
    
    task_label = Label(task_frame,
                       text=task_var.get(), 
                       bg="#FFFFFF",
                       font=("Segoe UI",18))
    
    del_btn = Button(task_frame,
                     text="✓",
                     command=delete_task)
    
    task_frame.pack(fill=BOTH, padx=10, pady=10)
    task_label.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)
    del_btn.pack(side=LEFT, padx=10, pady=10)

    task_list.append(task_frame)
    task_var.set("")


# TODO: fix button bug
def delete_task():
    task_list[0].destroy()

sub_btn = Button(root,
                text="+",
                font=("Segoe UI",14),
                command=submit_task)

label.pack()
frame.pack(expand=True, fill=BOTH, padx=10, pady=10)
entry.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)
sub_btn.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
