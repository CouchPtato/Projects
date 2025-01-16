from tkinter import *
from random import randint

root = Tk()
root.geometry("500x300")
root.title("Tkinter Project")

# my_password = chr(randint(33, 126))

def Password():
    passwordEntry.delete(0, END)

    length = int(lengthEntry.get())
    pwd = ''

    for x in range(length):
        pwd += chr(randint(33,126))

    passwordEntry.insert(0, pwd)

def Copy():
    root.clipboard_clear()
    root.clipboard_append(passwordEntry.get())

# Handling placeholder
def on_click(event):
    if lengthEntry.get() == "Enter password length":
        lengthEntry.delete(0, END)
        lengthEntry.configure(fg="black")

lf  = LabelFrame(root, text="Password Generator", font=("Helvetica", 8))
lf.pack(pady=20)

lengthEntry = Entry(lf, font=("Helvetica", 18), fg="grey")
lengthEntry.pack(padx=20, pady=20)
lengthEntry.insert(0, "Enter password length")
lengthEntry.bind("<FocusIn>", on_click)

passwordEntry = Entry(lf, font=("Helvetica", 18), border=0, bg="systembuttonface")
passwordEntry.pack(padx=20, pady=20)

myFrame = Frame(root)
myFrame.pack()

button = Button(myFrame, text="Generate strong password", command=Password)
button.grid(row=0, column=0, padx=10)

copybutton = Button(myFrame, text="Copy to clipboard", command=Copy)
copybutton.grid(row=0, column=1, padx=10)

root.mainloop()