from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        birth_date = datetime.strptime(dob_entry.get(), "%d/%m/%Y")
        today = datetime.today()
        
        # Calculate age in years
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        textbox.delete(1.0, END)
        textbox.insert(END, f"You are {age} years old!")
    except ValueError:
        textbox.delete(1.0, END)
        textbox.insert(END, "Invalid date format! Use DD/MM/YYYY")

# Main Window setup
root = Tk()
root.title("Age Calculator")
root.geometry("600x450") 

frame = Frame(master=root, height=250, width=360, bg="#d0efff")
frame.place(x=120, y=50)

# Labels
label_dob = Label(frame, text="Date of Birth", bg="#3895D3", fg="white", width=12)

# Entries
dob_entry = Entry(frame)

# Button and Textbox
btn = Button(frame, text="Calculate Age", command=calculate_age, bg="#FF5733", fg="white")
textbox = Text(master=frame, height=3, width=40)

# Placing Widgets
label_dob.place(x=20, y=50)
dob_entry.place(x=150, y=50)

btn.place(x=130, y=120)
textbox.place(x=20, y=170)

root.mainloop()
