from tkinter import *

# https://github.com/thom-jp/tkinter_pack_simulator




'''
class BuckysButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print("Wow, this actually worked!")
    
root = Tk()

b = BuckysButtons(root)

root.mainloop()
'''


'''
root = Tk()

def leftClick(event):
    print("Left click")

def middleClick(event):
    print("Middle click")

def rightClick(event):
    print("Right click")

frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
'''


'''
root = Tk()

def printName(): 
    print("printName")
    
button = Button(root, text="Print my name", command=printName)
button.pack()
    
def printName1(event):
    print("Hello, my name is Chan!")
    
button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName1)
button_1.pack()


def printName2(event):
    print("Hello 2 again!")

button_2 = Button(root, text="Print Hello 2")
button_2.bind("<Button-1>", printName2)
button_2.pack()

root.mainloop()
'''



'''
root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
# user entering input
entry_1 = Entry(root)
entry_2 = Entry(root)

# sticky=E (places it to the East, right-align)
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=W)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
# take up two columns
c.grid(columnspan=2)

root.mainloop()
'''



'''
root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
# grow in X axis
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()
'''


'''
root = Tk()

# create a invisible container and it is going into the main window(root)
topFrame = Frame(root)
# display somewhere
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
'''



'''
# basic window. minimize, maximize, exit.
root = Tk() 
# text on the screen (creating a widget)
theLabel = Label(root, text='This is too easy')
# pack the widget in order (displaying a widget)
theLabel.pack()
# gotta infinitely loop it otherwise it's gonna display and disappear in a sec
root.mainloop()
'''

