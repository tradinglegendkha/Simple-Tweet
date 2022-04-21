from tkinter import *
import twitterAPI as ta

#example of a window, widgets are the elements
window = Tk() #instantiate an instance of a window

window.geometry("500x700")
window.title("Simple Tweet")
iconE = PhotoImage(file="Icon.png") #route to the icon photo
window.iconphoto(True, iconE)
window.config(background = "#152238")

frame = Frame(window, bg="#262526", bd=2)
frame.place(x=0, y=0)
Label(frame, text=ta.tweets, width=70, height=6, bg="#1c1b1c", fg="#c4c3be").pack(side=TOP)


#window.update()
window.mainloop() #place window on computer screen, listen for events

