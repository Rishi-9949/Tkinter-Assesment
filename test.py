from tkinter import *

master = Tk()
nameentryframe = Frame(master, background = 'BLACK', borderwidth = 1, relief = SUNKEN)
nameentry = Entry(nameentryframe)
nameentryframe.pack()
nameentry.pack()

master.mainloop()