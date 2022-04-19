from tkinter import *

#example of a window, widgets are the elements
window = Tk() #instantiate an instance of a window
window.geometry("500x800")
window.title("Simple Tweet")

iconE = PhotoImage(file="Icon.png") #route to the icon photo
window.iconphoto(True, iconE)

window.config(background = "#152238")

window.mainloop() #place window on computer screen, listen for events

