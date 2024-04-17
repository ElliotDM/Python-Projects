import tkinter as tk


class ToDo(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("ToDo")
        self.geometry("300x500")
        self.resizable(1,0)

        self.task_var = tk.StringVar()
        self.dict = {}

        self.label = tk.Label(self,
                              text="ToDo",
                              font=("Segoe UI",18))
        
        self.frame = tk.Frame(self,
                              bg="#30C9E4")
        
        self.entry = tk.Entry(self,
                              textvariable=self.task_var,
                              font=("Segoe UI",14))
        
        self.add_btn = tk.Button(self,
                                 text="Add task",
                                 font=("Segoe UI",14),
                                 command=self.add_task)
        
        self.del_btn = tk.Button(self,
                                 text="Delete task",
                                 font=("Segoe UI",14),
                                 command=self.delete_task)
        
        self.label.pack()
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10)
        self.add_btn.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)
        self.del_btn.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)

    def add_task(self):
        if self.task_var.get() in self.dict:
            self.task_var.set("")
            return

        self.task_frame = tk.Frame(self.frame,
                                   bg="#FFFFFF")
        
        self.task_label = tk.Label(self.task_frame,
                                   text=self.task_var.get(), 
                                   bg="#FFFFFF",
                                   font=("Segoe UI",18))
        
        self.dict[self.task_var.get()] = self.task_frame
        self.task_var.set("")
    
        self.task_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.task_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.del_btn.pack(side=tk.LEFT, padx=10, pady=10)

    def delete_task(self):
        if self.task_var.get() not in self.dict:
            self.task_var.set("")
            return
        
        this_frame = self.dict.pop(self.task_var.get())
        this_frame.destroy()
        self.task_var.set("")


if __name__ == '__main__':
    app = ToDo()
    app.mainloop()
  