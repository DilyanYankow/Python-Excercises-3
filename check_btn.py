from tkinter import *

def display():
    if (x.get() == True):
        print("you agree")
    else:
        print("You dont agree")



window = Tk()
x = BooleanVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial", 20),
                           fg="#00ff00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00ff00",
                           padx=25,
                           pady=20,
                           # compound='left'
                           )

check_button.pack()
window.mainloop()
