from tkinter import *
from tkinter import messagebox      #import messagebox library

def click():
    # messagebox.showinfo(title="this is an info message box", message="You are a person")
    # messagebox.showwarning(title="this is an info warning", message="You have a virus!")
    # messagebox.showerror(title="this is an error", message="something went wrong 404")
    # messagebox.askokcancel()
    # messagebox.askyesno()     #returns true or false boolean
    answer= messagebox.askquestion(title="this is an info question box", message="Do you want to do that thing")
    # askquestion returns a string of yes or no
    print(answer)
    if messagebox.askokcancel(title="ask ok cancel", message="To be or not to be"):
        print("To be")
    else:
        print("not to be")
    answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you want to code?",
                                       icon='warning')  # true false or none #icon=INFO ERROR WARNNIG
    if answer == True:
        print("nice")
    elif answer == False:
        print("Why did you open this program for programming then?")
    else:
        print("You dodged the question successfully...")

window = Tk()
button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()   # places window on computer screen, listen for events