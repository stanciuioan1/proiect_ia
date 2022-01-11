# Import module
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "800x800" )
  
# Change the label text
def add_new_term():
    print(clicked.get()+"(x) * (" + coef_real.get()+ " +  "+coef_imaginar.get() +" * i)\n")
    coef_real.delete(0,100)
    coef_imaginar.delete(0,100)

def finish_ecuation():
    print("am terminat")

# Dropdown menu options
options = [
    "sin",
    "cos",
    "tg",
    "ctg",
    "poly"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "poly" )
  
# Create Dropdown menu


LA = Label(root, text="(")
LA.grid(row=0, column=0)

coef_real = Entry(root)
coef_real.grid(row=0, column=1)

LA = Label(root, text=" + ")
LA.grid(row=0, column=2)

coef_imaginar = Entry(root)
coef_imaginar.grid(row=0, column=3)

LA2 = Label(root, text=" i) * ")
LA2.grid(row=0, column=4)

drop = OptionMenu( root , clicked , *options )
drop.grid(row=0, column=5)

LA2 = Label(root, text=" * x")
LA2.grid(row=0, column=6)
# Create button, it will change label text
button_add_term = Button( root , text = " + " , command = add_new_term).grid(row=0, column=8)
button_finish_ecuation = Button( root , text = " = " , command = finish_ecuation).grid(row=1, column=8)
# Create Label
label = Label( root , text = " " )
label.grid(row=2, column=2)
  
# Execute tkinter
root.mainloop()

