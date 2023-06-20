from tkinter import *

def doNothing():
    print("ok ok I won't ...")    
    
root = Tk()

menu = Menu(root)
root.config(menu=menu) # parameter menu = variable menu

subMenu = Menu(menu)
# drop-down functionaility -> cascading in tkinter
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now Project...", command=doNothing)
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_separator() 
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()