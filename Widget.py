from tkinter import *

# Function to calculate the product
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text="Product = " + str(result))

# Create window
window = Tk()
window.title("Product Calculator")
window.geometry("300x200")

# Labels and Entry boxes
Label(window, text="Enter First Number:").pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text="Enter Second Number:").pack()
entry2 = Entry(window)
entry2.pack()

# Button
Button(window, text="Multiply", command=multiply).pack(pady=10)

# Result Label
result_label = Label(window, text="Product = ")
result_label.pack()

# Run the program
window.mainloop()