from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('PIZZA Selection')

Toppings = [
    ('Pepperoni','Pepperoni'),
    ('Cheese','Cheese'),
    ('Mushroom','Mushroom'),
    ('Onion','Onion')
]

Pizza = StringVar()
Pizza.set('Pepperoni')

for text, picks in Toppings:
    Radiobutton(root, text=text, variable=Pizza, value=picks).pack(anchor=W)

def clicked(value):
    mylabel = Label(root, text=value).pack()

Button(root, text='Click', command=lambda: clicked(Pizza.get())).pack()

# frame = LabelFrame(root, text='This is my frame...', padx=5, pady=5)
# frame.pack(padx=10,pady=10)




root.mainloop()