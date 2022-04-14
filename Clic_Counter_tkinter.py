#Click counter :)
from tkinter import ttk
import tkinter

count = 0
def counter():
    global count
    count += 1
    label1.configure(text=f'Button was clicked {count} times :O')

window = tkinter.Tk()

window.title("My Clicker")

frm = ttk.Frame(window, padding=10)
frm.grid()
label = ttk.Label(frm, text="The Ultimate click counter machine").grid(column=0, row=0)



label1 = tkinter.Label(window)
label1.grid(column=0, row=1)

custom_button = ttk.Button(window, text="Click on me", command=counter)
custom_button.grid(column=1, row=0)

window.mainloop()