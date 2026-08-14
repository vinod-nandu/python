import tkinter as tk

# ---------------------------------------
# Function to handle button clicks
# ---------------------------------------
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


# ---------------------------------------
# Function to clear the display
# ---------------------------------------
def clear():
    display.delete(0, tk.END)


# ---------------------------------------
# Function to calculate the result
# ---------------------------------------
def calculate():
    try:
        expression = display.get()

        # eval() evaluates the mathematical expression
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ---------------------------------------
# Create the main window
# ---------------------------------------
window = tk.Tk()

window.title("Python Calculator")
window.geometry("400x550")
window.resizable(False, False)

# Configure grid weights for proper sizing
for i in range(6):
    window.grid_rowconfigure(i, weight=1, minsize=80)
for i in range(4):
    window.grid_columnconfigure(i, weight=1, minsize=90)


# ---------------------------------------
# Create display box
# ---------------------------------------
display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)


# ---------------------------------------
# Calculator buttons
# ---------------------------------------

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
]


# ---------------------------------------
# Create number/operator buttons
# ---------------------------------------
for text, row, column in buttons:

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda value=text: button_click(value)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ---------------------------------------
# Clear button
# ---------------------------------------
clear_button = tk.Button(
    window,
    text="C",
    font=("Arial", 18),
    width=5,
    height=2,
    command=clear
)

clear_button.grid(
    row=5,
    column=0,
    padx=5,
    pady=5
)


# ---------------------------------------
# Equal button
# ---------------------------------------
equal_button = tk.Button(
    window,
    text="=",
    font=("Arial", 18),
    width=16,
    height=2,
    command=calculate
)

equal_button.grid(
    row=5,
    column=1,
    columnspan=3,
    padx=5,
    pady=5
)


# ---------------------------------------
# Start the GUI application
# ---------------------------------------
window.mainloop()