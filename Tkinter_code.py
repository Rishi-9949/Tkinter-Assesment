 # Importing All Neccecary Libraries
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import json

# Naming my window as tk
window = tk.Tk()

# The Title of the window
window.title("Julie’s Party Hire")

# Addes an Icon as the windows logo
window.iconbitmap("jph.ico")

# Geometry of the window
window.geometry("700x700")

# Defining the Maximun and the minimun size of the window sto its locked and unchanged, (width,hieght)
window.minsize(700, 700)
window.maxsize(700, 700)

# giving the window a background colour
window.config(bg="#FFF1DC")

# Defining Constants
Max_num_of_items = 500
Min_num_of_items = 1

# Define the data structure to store items information
items_data = {}

# Create a line and draw it on the canvas
my_rect = tk.Canvas(window, width=800, height=20)
my_rect.pack()

# Shapping my line and filling it with colour
rect = my_rect.create_rectangle(800, 0, 0, 20, fill="#004AAD")
bottom_line = my_rect.create_rectangle(800, 20, 0, 17, fill="#000000")

# Displaying GUI Tittle in the tkinter window 
Jph = tk.Label(window, text=("Julie’s Party  \n Hire"), bg="#FAF4EF", font=("Garamond", 20))

# Locating the title in the window 
Jph.place(x=570, y=120)

#                            <----Labels and Entry Boxes---->
name_label = tk.Label(window, text="Full Name:", background="#FFD18B") # Name Label
name_label.pack(anchor="w") # Locating Name Label

name_entry = tk.Entry(window, border=1, relief="solid", fg="#929090") # Name Entry Box
name_entry.pack(anchor="w") # Locating Name Entry Box

receipt_num_label = tk.Label(window, text="Receipt Number:", background="#FFD18B") # Receipt Label
receipt_num_label.pack(anchor="w") # Locating Receipt Label 

receipt_entry = tk.Entry(window, border=1, relief="solid", fg="#929090") # Receipt Entry Box 
receipt_entry.pack(anchor="w") # Locating Receipt Entry Box 

item_label = tk.Label(window, text="Item Hired:", background="#FFD18B") # Item Label 
item_label.pack(anchor="w") # Locating Item Label

item_entry = tk.Entry(window, border=1, relief="solid", fg="#929090") # Item Entry Box
item_entry.pack(anchor="w") # Locating Item Entry Box

num_item_label = tk.Label(window, text="Number of items:", background="#FFD18B") # Label of Number of items Hired
num_item_label.pack(anchor="w") # Location for Number of items Hired 

num_item_entry = tk.Entry(window, border=1, relief="solid", fg="#929090") # Number of items Hired Entry Box
num_item_entry.pack(anchor="w") # Location for Number of items Hired Entry Box


#                <--------Inserting Temporary Text in Entry Boxes------>
name_entry.insert(0, "eg : David") # Inserting eg : David in name Entry Box
receipt_entry.insert(0, "eg : 1882839") # Inserting eg : 1882839 in receipt Entry Box
item_entry.insert(0, "eg : Plates") # Inserting eg : Plates in items Entry Box
num_item_entry.insert(0, "eg : 35") # Inserting eg : 35 in number of items hired Entry Box



#                       <---------- Def Functions------------->

# Clearing name entry box
def clear_name_entry(event):
    if name_entry.get().strip() == "eg : David":
        name_entry.delete(0, tk.END) # Empting everything in the Name Entry Box 
        name_entry.configure(fg="black")
        name_entry.bind("<Button-1>", clear_name_entry)

# Clearing Receipt Number entry box
def clear_receipt_entry(event):
    if receipt_entry.get().strip() == "eg : 1882839":
        receipt_entry.delete(0, tk.END) # Empting everything in the Receipt Entry Box 
        receipt_entry.configure(fg="black")
        receipt_entry.bind("<Button-1>", clear_receipt_entry)

# Clearing Items Hired entry box
def clear_item_entry(event):
    if item_entry.get().strip() == "eg : Plates":
        item_entry.delete(0, tk.END) # Empting everything in the Items Hired Entry Box 
        item_entry.configure(fg="black")
        item_entry.bind("<Button-1>", clear_item_entry)

# Clearing Number of items hired entry box
def clear_num_item_entry(event):
    if num_item_entry.get().strip() == "eg : 35":
        num_item_entry.delete(0, tk.END) # Empting everything in the Number of items hired Entry Box 
        num_item_entry.configure(fg="black")
        num_item_entry.bind("<Button-1>", clear_num_item_entry)

# Message Box/function for Exiting the application
def Exit():
    warning = messagebox.askquestion(
        "Exit Application",
        "Are you sure you want to exit the application?",
        icon="warning",
    )
    if warning == "yes":
        window.destroy()

# Set of comands when Submit Button is pressed
def submit_data():
    global name, receipt, item, num_item

    # Get input from the user
    name = name_entry.get().strip()
    receipt = receipt_entry.get().strip()
    item = item_entry.get().strip()
    num_item = num_item_entry.get().strip()

    # Check if any input fields are same as their temporary text
    if name_entry.get() == "eg : David":
        error_label.config(text="Please fill in all input field")
        return
    elif receipt_entry.get() == "eg : 1882839":
        error_label.config(text="Please fill in all input field")
        return
    elif item_entry.get() == "eg : Plates":
        error_label.config(text="Please fill in all input field")
        return
    elif num_item_entry.get() == "eg : 35":
        error_label.config(text="Please fill in all input field")
        return
    
    # Check if any input fields are empty
    if not all([name, receipt, item, num_item]):
        error_label.config(text="Please fill in all input fields")
        return

    # Validate the input
    try:
        receipt = int(receipt)
        num_item = int(num_item)
    except ValueError:
        error_label.config(
            text="Invalid Information!. (Enter Numbers only for Receipt Number and Number of Items Hired )"
        )
        return

    if num_item < Min_num_of_items or num_item > Max_num_of_items:
        error_label.config(
            text=f"Number of items hired must be between {Min_num_of_items} and {Max_num_of_items}"
        )
        return

    with open("data.json", "r") as file:
        customer_data = json.load(file)
        customer_data["Full Name:"].append(name)
        customer_data["Receipt Number:"].append(receipt)
        customer_data["Item hired:"].append(item)
        customer_data["Number of Items Hired:"].append(num_item)

    with open("data.json", "w") as file:
        json.dump(customer_data, file)

    # Clear the input fields
    name_entry.delete(0, tk.END) # Empting everything in the Name Entry Box 
    receipt_entry.delete(0, tk.END) # Empting everything in the Receipt Entry Box
    item_entry.delete(0, tk.END) # Empting everything in the Items Hired Entry Box 
    num_item_entry.delete(0, tk.END) # Empting everything in the Number of items hired Entry Box 


    # Update the display
    update_display()
    # Message Box to inform the user that the data has successfully submitted 
    messagebox.showinfo("Submitted", "Your data has successfully submitted.") 


# Set Display function
def update_display():
    with open("data.json", "r") as file:
        data = json.load(file)

    trv.delete(*trv.get_children())  # Clear the Treeview

    for i in range(len(data["Full Name:"])):
        trv.insert(
            "",
            "end",
            values=(
                i + 1,
                data["Full Name:"][i],
                data["Receipt Number:"][i],
                data["Item hired:"][i],
                data["Number of Items Hired:"][i],
            ),
        )


def update_data():
    selected_item = trv.focus()

    if not selected_item:
        error_label.config(text="Please select an item to update")
        return

    item_data = trv.item(selected_item)["values"]

    name_entry.delete(0, tk.END) # Empting everything in the Name Entry Box 
    receipt_entry.delete(0, tk.END) # Empting everything in the Receipt Entry Box 
    item_entry.delete(0, tk.END) # Empting everything in the Items Hired Entry Box 
    num_item_entry.delete(0, tk.END) # Empting everything in the Number of items hired Entry Box 

    # Categorizes data in the list heading
    name_entry.insert(0, item_data[1]) # Inserting all valid data in the Name Entry Box 
    receipt_entry.insert(0, item_data[2]) # Inserting all valid data in the Receipt Entry Box 
    item_entry.insert(0, item_data[3]) # Inserting all valid data in the Items Hired Entry Box 
    num_item_entry.insert(0, item_data[4])# Inserting all valid data in the Number of items hired Entry Box 

    # Get the index of the selected row
    index = trv.index(selected_item)
    # Open the JSON file
    with open("data.json", "r") as file:
        data = json.load(file)

    # Delete the corresponding data from the lists
    for key in data:
        data[key].pop(index)

    # Update the JSON file with the modified data
    with open("data.json", "w") as file:
        json.dump(data, file)

    # Delete the selected item from the Treeview
    trv.delete(selected_item)


def delete_row():
    selected_item = trv.focus()

    if not selected_item:
        error_label.config(text="Please select an item to delete")
        return

    warning = messagebox.askquestion(
        "Delete Rowe",
        "Are you sure you want to delete this row? \n"
        "(Once Deleted you won't be able to restore it)",
        icon="warning",
    )

    if warning == "yes":
        # Get the index of the selected row
        index = trv.index(selected_item)

        # Open the JSON file
        with open("data.json", "r") as file:
            data = json.load(file)

        # Delete the corresponding data from the lists
        for key in data:
            data[key].pop(index)

        # Update the JSON file with the modified data
        with open("data.json", "w") as file:
            json.dump(data, file)

        # Delete the selected item from the Treeview
        trv.delete(selected_item)

        # Update the display
        update_display()


clicked = name_entry.bind("<Button-1>", clear_name_entry)
clicked = receipt_entry.bind("<Button-1>", clear_receipt_entry)
clicked = item_entry.bind("<Button-1>", clear_item_entry)
clicked = num_item_entry.bind("<Button-1>", clear_num_item_entry)


#                      <-------Treeview Box -------->
# List Heading
trv = ttk.Treeview(window, columns=(1, 2, 3, 4, 5), show="headings", height=50)
trv.pack(anchor="w", ipadx=400)

# Input text in the heading
trv.heading(1, text="ID", anchor="center") # Treeview Heading of ID
trv.heading(2, text="Full Name", anchor="center") # Treeview Heading of Full Name
trv.heading(3, text="Receipt Number", anchor="center") # Treeview Heading of Receipt Number
trv.heading(4, text="Item Hired", anchor="center") # Treeview Heading of Item Hired
trv.heading(5, text="Number of Items Hired", anchor="center") # Treeview Heading of Number of Items Hired

trv.column("#1", anchor="w", width=40, stretch=True) # Labeling Treeview Heading in a column for ID
trv.column("#2", anchor="w", width=150, stretch=False) # Labeling Treeview Heading in a column for Name  
trv.column("#3", anchor="w", width=150, stretch=False) # Labeling Treeview Heading in a column for Receipt Number
trv.column("#4", anchor="w", width=150, stretch=False) # Labeling Treeview Heading in a column for Item Hired
trv.column("#5", anchor="w", width=150, stretch=False) # Labeling Treeview Heading in a column for Number of items hired 

# Reading the Data.json file which helps displaying the previous saved data
with open("data.json", "r") as file:
    data = json.load(file)

trv.delete(*trv.get_children())  # Clear the Treeview

for i in range(len(data["Full Name:"])):
    trv.insert(
        "",
        "end",
        values=(
            i + 1,
            data["Full Name:"][i],
            data["Receipt Number:"][i],
            data["Item hired:"][i],
            data["Number of Items Hired:"][i],
        ),
    )


#                                <---Buttons--->
# Submit
submit_button = tk.Button(window, text="Submit", bg="green", command=submit_data)
submit_button.place(x=160, y=158)

# Update
update_button = tk.Button(window, text="Update", bg="yellow", command=update_data)
update_button.place(x=250, y=158)

# Delete
delete_button = tk.Button(window, text="Delete Row", bg="orange", command=delete_row)
delete_button.place(x=630, y=350)

# Exit Program
exit_button = tk.Button(window, text="Exit Program", bg="red", command=Exit)
exit_button.place(x=630, y=400)

#                              <------Image------>
# Adding my Logo Image in my tkinter GUI
img = Image.open("Logo.jpg")
img = img.resize((100, 100))

# Create ImageTk objects
img_tk = ImageTk.PhotoImage(img)

# Create Label widget
img_label = tk.Label(window, image=img_tk)

# Place the Label widgets
img_label.place(x=595, y=23)


# Create a Frame for border in the image 
border_frame = tk.Frame(
    window,
    background="red",
    borderwidth=2,
    highlightbackground="red")
border_frame.place(x=160, y=130)

error_label = tk.Label(border_frame, text="There are no errors", fg="red") # Create the error label 
error_label.pack(padx=0, pady=0) # Locating the error label 



window.mainloop() # Lopping my window 