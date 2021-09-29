# scales

from tkinter import *

def submit():
    print("The temperature is", str(scale.get()), "degrees C")

window = Tk()

scale = Scale(window, from_=100,
              to=0,
              length=400,
              orient=VERTICAL,   #or HORIZONTAL
              font_=("Aerial", 20),
              tickinterval = 10,    #this adds numeric indicators for value
              showvalue= 0,
              troughcolor = '#69FAFF',
              fg="#ff1c00",
              bg = '#111111'
)
scale.pack()
button = Button(window, text="submit", command=submit)
button.pack()
# scale.set(100)
scale.set(((scale['from'] - scale['to'])/2)+scale['to'])


button = Button(window, text="submit", command=submit)

window.mainloop()