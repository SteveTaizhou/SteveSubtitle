from tkinter import *
from tkinter import messagebox
from tkinter import font

def backone():
    global where
    where -= 1
    text.set(textlist[where])
    if where == 0:
        prevbutton["state"] = "disabled"
    if where == len(textlist) - 2:
        nextbutton["state"] = "normal"

def nextone():
    global where
    where += 1
    text.set(textlist[where])
    if where == 1:
        prevbutton["state"] = "normal"
    if where == len(textlist) - 1:
        nextbutton["state"] = "disabled"

def add():
    global where
    where += 1
    textlist.insert(where,"")
    text.set("")
    if len(textlist) == 2:
        deletebutton["state"] = "normal"
        prevbutton["state"] = "normal"

def delete():
    global where
    a = textlist.pop(where)
    messagebox.showinfo("Deleted subtitle",a)
    where -= 1
    text.set(textlist[where])
    if len(textlist) == 1:
        deletebutton["state"] = "disabled"
        prevbutton["state"] = "disabled"
        nextbutton["state"] = "disabled"

def refresh():
    global where
    textlist[where] = text.get()
    messagebox.showinfo("Message","Saved")

def disableall():
    nextbutton["state"] = "disabled"
    deletebutton["state"] = "disabled"
    prevbutton["state"] = "disabled"

win = Tk()
win.title("SteveSubtitle")

where = int(0)
text = StringVar()
textlist = [""]

buttonfont = font.Font(family = "Microsoft YaHei UI",size = 14)
textfont = font.Font(family = "Microsoft YaHei UI",size = 20)

prevbutton = Button(win,text = "Prev",font = buttonfont,command = backone)
prevbutton.grid(row = 1,column = 1)
textentry = Entry(win,textvariable = text,font = textfont,width = 80)
textentry.grid(row = 1,column = 2)
nextbutton = Button(win,text = "Next",font = buttonfont,command = nextone)
nextbutton.grid(row = 1,column = 3)
addbutton = Button(win,text = "Add",font = buttonfont,command = add)
addbutton.grid(row = 2,column = 1)
deletebutton = Button(win,text = "Del",font = buttonfont,command = delete)
deletebutton.grid(row = 2,column = 2)
refreshbutton = Button(win,text = "Save",font = buttonfont,command = refresh)
refreshbutton.grid(row = 2,column = 3)

disableall()

win.lift()
win.attributes("-topmost", True)

win.mainloop()
