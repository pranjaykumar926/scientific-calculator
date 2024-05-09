import tkinter as tk
import math

def calculate():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear():
    entry.delete(0, 'end')
    result.set("")

def button_click(value):
    entry.insert('end', value)

def scientific_function(func):
    try:
        expression = entry.get()
        result.set(func(float(expression)))
    except Exception as e:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create entry widget for input
entry = tk.Entry(root, width=40, font=('Helvetica', 14))
entry.grid(row=0, column=0, columnspan=5)

# Create buttons for digits and operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
    ('sqrt', 5, 4), ('log', 6, 0), ('exp', 6, 1), ('(', 6, 2), (')', 6, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Helvetica', 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=column)

# Create button for clearing the input
clear_button = tk.Button(root, text="C", width=5, height=2, font=('Helvetica', 14), command=clear)
clear_button.grid(row=7, column=0, columnspan=2)

# Create button for calculating the result
equal_button = tk.Button(root, text="=", width=5, height=2, font=('Helvetica', 14), command=calculate)
equal_button.grid(row=7, column=2, columnspan=3)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, width=40, font=('Helvetica', 14))
result_label.grid(row=8, column=0, columnspan=5)

# Scientific functions
scientific_functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log10,
    'exp': math.exp,
    '^': lambda x: x**2
}

def find_button_position(func):
    for i, (text, row, column) in enumerate(buttons):
        if text == func:
            return row, column

for func in scientific_functions:
    row, column = find_button_position(func)
    button = tk.Button(root, text=func, width=5, height=2, font=('Helvetica', 14), command=lambda f=func: scientific_function(scientific_functions[f]))
    button.grid(row=row, column=column)

# Start the main event loop
root.mainloop()
