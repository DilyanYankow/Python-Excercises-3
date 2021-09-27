# radio buttons

from tkinter import *

food = ["pizza","hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    else:
        print("You ordered a hotdog:")

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index],   #adds text to radio buttons
                            variable=x,         #groups radio buttons if they share the same variable
                            value=index,        #assigns each radio button a different value
                            padx = 25,          #adds padding on x axis
                            font=("impact", 50),
                            indicatoron = 0,    #eliminate circle indicators
                            width=375,          #width of radio buttons
                            command=order       #set command of radio buttons to function
                            )
    radiobutton.pack(anchor=W)

window.mainloop()