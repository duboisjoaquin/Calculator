from tkinter import *


root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row = 1, columnspan = 8, sticky = W+E)

#string position index
i = 0

def get_number(n):
    global i 
    display.insert(i, n)
    i+=1

def get_operation(o):
    global i
    operation_len = len(o)
    display.insert(i, o)
    i+=operation_len

def clean_display():
    display.delete(0, END)

def undo():
    display_state = display.get()

    if len(display_state):
        display_new_state = display_state[:-1]
        clean_display()
        display.insert(0, display_new_state)
    else:
        clean_display()

def calculate():

    display_state = display.get()

    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clean_display()
        display.insert(0,result)
    except:
        clean_display()
        display.insert(0,"error")

#Num Buttons 
Button(root, text="1", command=lambda:get_number(1)).grid(row=3, column = 1, sticky = W+E)
Button(root, text="2", command=lambda:get_number(2)).grid(row=3, column = 3, sticky = W+E)
Button(root, text="3", command=lambda:get_number(3)).grid(row=3, column = 5, sticky = W+E)

Button(root, text="4", command=lambda:get_number(4)).grid(row=4, column = 1, sticky = W+E)
Button(root, text="5", command=lambda:get_number(5)).grid(row=4, column = 3, sticky = W+E)
Button(root, text="6", command=lambda:get_number(6)).grid(row=4, column = 5, sticky = W+E)

Button(root, text="7", command=lambda:get_number(7)).grid(row=5, column = 1, sticky = W+E)
Button(root, text="8", command=lambda:get_number(8)).grid(row=5, column = 3, sticky = W+E)
Button(root, text="9", command=lambda:get_number(9)).grid(row=5, column = 5, sticky = W+E)

Button(root, text="0", command=lambda:get_number(0)).grid(row=6, column = 1,columnspan = 5, sticky = W+E)

#Operations Buttons 

Button(root, text="AC", command=lambda:clean_display()).grid(row=2, column = 1, sticky = W+E, columnspan = 3)
Button(root, text="⇠", command=lambda: undo()).grid(row=2, column = 9, sticky = W+E, columnspan = 3)

Button(root, text="%", command=lambda:get_operation("%")).grid(row=2, column = 5, sticky = W+E)
Button(root, text="÷", command=lambda:get_operation("/")).grid(row=2, column = 7, sticky = W+E)
Button(root, text="X", command=lambda:get_operation("*")).grid(row=3, column = 7, sticky = W+E)
Button(root, text="+", command=lambda:get_operation("+")).grid(row=4, column = 7, sticky = W+E)
Button(root, text="-", command=lambda:get_operation("-")).grid(row=5, column = 7, sticky = W+E)

Button(root, text="=", command=lambda: calculate()).grid(row=6, column = 9, sticky = W+E, columnspan = 3)

Button(root, text=".", command=lambda:get_operation(".")).grid(row=6, column = 7, sticky = W+E)

Button(root, text="(", command=lambda:get_operation("(")).grid(row=3, column = 9, sticky = W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=3, column = 10, sticky = W+E)

Button(root, text="^", command=lambda:get_operation("**")).grid(row=4, column = 9, sticky = W+E, columnspan = 3)
Button(root, text="√", command=lambda:get_operation("**(1/")).grid(row=5, column = 9, sticky = W+E, columnspan = 3)






root.mainloop()

