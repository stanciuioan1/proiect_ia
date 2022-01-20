# Import module
from tkinter import *
import math
from tokenize import Double 
# Create object
root = Tk()
  
# Adjust size
root.geometry( "1200x600" )

ecuation=[]
ecuation_label = Entry(root, width=200)
ecuation_label.grid(row=2, column = 10)
text_ecuation = " "

def get_value_in_point(ecuation,x):
    result_real = 0
    result_imag = 0
    for i in ecuation:
        if(i[0]== "sin"):
            result_real = result_real + i[1] * math.sin(x)
            result_imag = result_imag + i[2] * math.sin(x)
        if(i[0]== "cos"):
            result_real = result_real + i[1] * math.cos(x)
            result_imag = result_imag + i[2] * math.cos(x)
        if(i[0]== "tg"):
            result_real = result_real + i[1] * math.tan(x)
            result_imag = result_imag + i[2] * math.tan(x)
        if(i[0]== "ctg"):
            result_real = result_real + i[1] * 1/math.tan(x)
            result_imag = result_imag + i[2] * 1/math.tan(x)
        if(i[0]== "poly"):
            result_real = result_real + i[1] * x ** Double(i[3])
            result_imag = result_imag + i[2] * x ** Double(i[3])

    return result_real, result_imag


def get_roots(ecuation):
    #this is the place to calculate roots
    roots=[1,2,3]
    return roots

# Change the label text
def add_new_term():
    global text_ecuation
    if(clicked.get()=="poly"):
        print("(x ^ "+power.get()+") * (" + coef_real.get()+ " +  "+coef_imaginar.get() +" * i)\n")
        ecuation.append((clicked.get(), coef_real.get(), coef_imaginar.get(), power.get()))
        text_ecuation = text_ecuation + "(x ^ "+power.get()+") * (" + coef_real.get()+ " +  "+coef_imaginar.get() +" * i)" + " + "
    else:
        print(clicked.get()+"(x) * (" + coef_real.get()+ " +  "+coef_imaginar.get() +" * i)\n")
        ecuation.append((clicked.get(), coef_real.get(), coef_imaginar.get()))
        text_ecuation = text_ecuation + clicked.get()+"(x) * (" + coef_real.get()+ " +  "+coef_imaginar.get() +" * i)" + " + "
    coef_real.delete(0,100)
    coef_imaginar.delete(0,100)
    power.delete(0,100)
    ecuation_label.delete(0,1000)
    ecuation_label.insert(0,text_ecuation)


def finish_ecuation():
    global text_ecuation
    print("am terminat")
    text_ecuation =  text_ecuation + "0 = 0"
    ecuation_label.delete(0,1000)
    ecuation_label.insert(0,text_ecuation)
    print(ecuation)

    roots = get_roots(ecuation)
    roots_label = Entry(root, width=50)
    roots_label.grid(row=5, column = 0)
    text="Roots are: "
    for i in roots:
        text = text + str(i)+", "
    roots_label.insert(0, text)



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

LA_power = Label(root, text="(only for poly) ^ ")
LA_power.grid(row=0, column=7)

power = Entry(root)
power.grid(row=0, column=8)
# Create button, it will change label text
button_add_term = Button( root , text = " + " , command = add_new_term).grid(row=0, column=9)
button_finish_ecuation = Button( root , text = " = " , command = finish_ecuation).grid(row=1, column=9)
# Create Label


  
# Execute tkinter
root.mainloop()

