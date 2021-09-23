from tkinter import *

# widgets = GUI elements: buttons, text boxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Title name")
# icon = PhotoImage('monkaS.png')
# window.iconphoto(True, icon)    #
window.config(background="#c5f1a2")

window.mainloop()   # places window on computer screen, listen for events
