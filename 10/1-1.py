from tkinter import *

# gui Graphical user interface
 
window = Tk()

label = Label(window, text='I am a label')

# label.pack()
label.place(x=15, y=10)

entry = Entry(width=30)
entry . place(x=90, y=10)


window.mainloop()