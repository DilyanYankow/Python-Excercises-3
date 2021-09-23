from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()
photo = PhotoImage(file='monke.png')
label = Label(window,
              text='Wake up, its time 4 school',
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief =SUNKEN,   #SUNKEN/RAISED/...
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=5,y=5)
window.mainloop()
