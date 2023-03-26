from tkinter import *
from time import sleep

app = Tk()
app.title("Simple Calculator")

e = Entry(app, width=33, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipadx=10,ipady=10)

# Calculator's Functions
def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_Clear():
	e.delete(0, END)

def button_Add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + int(second_number))
	if math == "subtraction":
		e.insert(0, f_num - int(second_number))
	if math == "multiplication":
		e.insert(0, f_num * int(second_number))
	if math == "division":
		e.insert(0, f_num / int(second_number))

# Operators


def button_Subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_Multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_Divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)


# Define Buttons

button_1 = Button(app, borderwidth=10, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(app, borderwidth=10, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(app, borderwidth=10, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(app, borderwidth=10, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(app, borderwidth=10, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(app, borderwidth=10, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(app, borderwidth=10, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(app, borderwidth=10, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(app, borderwidth=10, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(app, borderwidth=10, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(app,borderwidth=10,  text="+", padx=39, pady=20, command=button_Add)
button_subtract = Button(app,borderwidth=10,  text="-", padx=41, pady=20, command=button_Subtract)
button_multiply = Button(app,borderwidth=10,  text="*", padx=40, pady=20, command=button_Multiply)
button_divide = Button(app,borderwidth=10,  text="÷", padx=41, pady=20, command=button_Divide)

button_equal = Button(app, borderwidth=10, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(app, borderwidth=10, text="Clear", padx=79, pady=20, command=button_Clear)




# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1,columnspan=2,sticky="nsew")

button_add.grid(row=5, column=0,sticky="se")
button_equal.grid(row=5, column=1,columnspan=2,sticky="nsew")

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

app.mainloop()