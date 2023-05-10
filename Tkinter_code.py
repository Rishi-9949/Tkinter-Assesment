import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import json


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

#giving the window an background colour 
window.config(bg="#FFF1DC")



# Defining Constants 
Max_num_of_items = 500
Min_num_of_items = 1

# Define the data structure to store items information
items_data = []

# Create a line and draw it on the canvas
my_rect = tk.Canvas(window, width=800, height=20)
my_rect.pack()


# Shapping my line and filling it with colour
rect = my_rect.create_rectangle(800, 0, 0, 20, fill="#004AAD")
bottom_line = my_rect.create_rectangle(800, 20, 0, 17, fill="#000000")

Jph = tk.Label(window, text=("""Julie’s Party 
Hire'"""), bg="#FAF4EF", font=("Garamond", 20))

Jph.place(x=570,y=120)




# Labels and Entry Boxes 
name_label = tk.Label(window, text="Full Name:", background="#FFD18B")
name_label.pack(anchor='w')
name_entry = tk.Entry(window, border = 1, relief='solid')
name_entry.pack(anchor='w')


receipt_num_label = tk.Label(window, text="Receipt Number:", background="#FFD18B")
receipt_num_label.pack(anchor='w')
receipt_entry = tk.Entry(window, border = 1, relief='solid')
receipt_entry.pack(anchor='w')


item_label = tk.Label(window, text="Item Hired:", background="#FFD18B")
item_label.pack(anchor='w')
item_entry = tk.Entry(window, border = 1, relief='solid')
item_entry.pack(anchor='w')



num_item_label = tk.Label(window, text="Number of items hired:", background="#FFD18B")
num_item_label.pack(anchor='w')
num_item_entry = tk.Entry(window, border = 1, relief='solid')
num_item_entry.pack(anchor='w')


# Define functions for adding, updating, and deleting camp information
def submit_data():
    global name, receipt, item, num_item

    # Get input from the user
    name = name_entry.get().strip()
    receipt = receipt_entry.get().strip()
    item = item_entry.get().strip()
    num_item = num_item_entry.get().strip()
    

    # Check if any input fields are empty
    if not all([name, receipt, item, num_item]):
        error_label.config(text="Please fill in all input fields")
        return

    # Validate the input
    try:
        receipt = int(receipt) 
        num_item = int(num_item)
    except ValueError:
        error_label.config(text="Please Enter Valid Information!!. (Only Numbers are valid )")
        return

    if num_item  < Min_num_of_items or num_item > Max_num_of_items:
        error_label.config(text=f"Number of items hired must be between {Min_num_of_items} and {Max_num_of_items}")
        return

    # Add the information to the data structure
    items_data.append([name, receipt, item, num_item])

    # Clear the input fields
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    num_item_entry.delete(0, tk.END)

    with open("data.json", "w") as file:
        customer_data = json.load(file)
        customer_data['Customer Name'].append(name)
        customer_data['Receipt'].append(receipt)
        customer_data['Item hired'].append(item)
        customer_data['Item hired amount'].append(num_item)

    with open('data.json', 'w') as file:
        json.dump(customer_data, file)




    # Update the display
    update_display()



#Set Display function

def update_display():
   
    listbox.delete(0, tk.END)
    print(items_data)


    for name, receipt, item, num_item in items_data:
        listbox.insert(
            tk.END,
            f"Full Name: {name}   Receipt Number: {receipt}    Item hired: {item}    Number of Items Hired: {num_item}"
            )



#Set Update function

def update_data():
    selected_item = listbox.curselection()


    for i in listbox.curselection():
        e = listbox.get(i).split(" ")

    if not selected_item:
        error_label.config("Please select an item to update")
        return
    
        
    userData = {
        "Name": e[1],
        "Receipt": int(e[8].replace("(","")),
        "Item hired": e[14],
        "Number of items hired": int(e[22].replace("(",""))
        }
    listbox.delete(0, tk.END)

    temp_list = []
    [temp_list.append(i) for i in userData.values()]

    for i in items_data:
        if temp_list == i:
            print(i)
            print("EEE")
            items_data.remove(i)

    print(items_data)
    print(userData)

    name_entry.insert(0, str(userData["Full Name"]))
    receipt_entry.insert(0, str(userData["Receipt Number"]))
    item_entry.insert(0, str(userData["Items hired"]))
    num_item_entry.insert(0, str(userData["Number of items hired"]))


#Set Delete function

def delete_row():
    selected_item = listbox.curselection()

    if not selected_item:
        error_label.config(text=f"Please selecte a row to delete")
        return
    index = selected_item[0]


    del items_data[index]
    return



# Create the listbox
listbox = tk.Listbox(window)
listbox.pack(anchor="w", ipadx=400)



#Buttons
#Submit
submit_button = tk.Button(window, text= "Submit", bg='green', command=submit_data)
submit_button.place(x=160,y=160)

#Update
update_button = tk.Button(window, text= "Update", bg='yellow', command=update_data)
update_button.pack(anchor='w')

#Delete 
delete_button = tk.Button(window, text= "Delete Row", bg='orange', command=delete_row)
delete_button.place(x=630,y=350)






def msg1():
    warning = messagebox.askquestion('Warning', 'Do you want to continue? (If you proceed to continue all data will be lost)')
    if warning == "yes":
        window.destroy()


#Exit Program 

exit_button = tk.Button(window, text="Exit Program", bg='red', command=msg1)
exit_button.pack(anchor='e')


img = Image.open("Logo.jpg")
img = img.resize((100, 100))


# Create ImageTk objects
img_tk = ImageTk.PhotoImage(img)

# Create Label widget
img_label = tk.Label(window, image=img_tk)

# Place the Label widgets
img_label.place(x=595,y=23)










# Create the error label
error_label = tk.Label(window, fg="red")
error_label.pack(anchor="w")

# Create a line and draw it on the canvas
my_rect_2 = tk.Canvas(window, width=700, height=600)
my_rect_2.place(x=0,y=450)

# Shapping my line and filling it with colour
rect_2 = my_rect_2.create_rectangle(800, 800, 0, 450, fill="#004AAD")
upper_line = my_rect_2.create_rectangle(700, 440, 0, 450, fill="black")


window.mainloop()