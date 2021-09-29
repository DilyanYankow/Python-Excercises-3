# scales

from tkinter import *

def submit():
    food =[]
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "apple")
listbox.insert(2, "banana")
listbox.insert(3, "pineapple")
listbox.insert(4, "orange")
listbox.insert(5, "fat steak")

entryBox = Entry(window)
entryBox.pack()

listbox.config(height=listbox.size())
addButton = Button(window, text="add", command=add)
addButton.pack()


submitBtn= Button(window, text="submit", command=submit)
submitBtn.pack()

delButton = Button(window, text="delete", command=delete)
delButton.pack()

window.mainloop()
