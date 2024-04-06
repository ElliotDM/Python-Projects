import tkinter as tk
from tkinter import ttk, END
from tkinter import messagebox


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('RGB Converter')

        self.label = ttk.Label(self, text='Insert RGB color')
        self.red_255 = ttk.Entry(self)
        self.green_255 = ttk.Entry(self)
        self.blue_255 = ttk.Entry(self)
        self.button = ttk.Button(self, text='Ok')
        self.label1 = ttk.Label(self, text='Result')
        self.red_1 = ttk.Entry(self)
        self.green_1 = ttk.Entry(self)
        self.blue_1 = ttk.Entry(self)

        self.label.grid(row=0, column=0)
        self.red_255.grid(row=1, column=0, padx=5)
        self.green_255.grid(row=1, column=1, padx=5)
        self.blue_255.grid(row=1, column=2, padx=5)
        self.button.grid(row=1, column=3, padx=5)
        self.label1.grid(row=2)
        self.red_1.grid(row=3, column=0, padx=5, pady=5)
        self.green_1.grid(row=3, column=1, padx=5, pady=5)
        self.blue_1.grid(row=3, column=2, padx=5, pady=5)

        self.button['command'] = self.convert

    def convert(self) -> None:
        try:
            red = int(self.red_255.get())
            green = int(self.green_255.get())
            blue = int(self.blue_255.get())

            assert (0 <= red <= 255)
            assert (0 <= green <= 255)
            assert (0 <= blue <= 255)

            self.red_1.delete(0, END)
            self.green_1.delete(0, END)
            self.blue_1.delete(0, END)
        except Exception:
            messagebox.showinfo(
                message="Choose a color between 0 and 255", title="Warning")
            return

        red = red / 255
        green = green / 255
        blue = blue / 255

        self.red_1.insert(0, f'{red:.3f}')
        self.green_1.insert(0, f'{green:.3f}')
        self.blue_1.insert(0, f'{blue:.3f}')


if __name__ == "__main__":
    app = Window()
    app.mainloop()
