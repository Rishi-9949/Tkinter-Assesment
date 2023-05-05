import tkinter as tk

window = tk.Tk()


# The Title of the window 
window.title("Julie’s Party Hire")

# Addes an Icon as the windows logo
window.iconbitmap("jph.ico")

# Geometry of the window
window.geometry("800x800")

# Defining the Maximun and the minimun size of the window sto its locked and unchanged, (width,hieght)
window.minsize(800, 800)
window.minsize(800, 800)

#giving the window an background colour 
window.config(bg="#F9F9E0")



# Defining Constants 
Max_num_of_items = 500
Min_num_of_items = 1

# Define the data structure to store items information
items_data = []


# Labels and Entry Boxes 
name_label = tk.Label(window, text="Full Name:", background="#FFD18B")
name_label.pack(anchor='w')
name_entry = tk.Entry(window, border = 2)
name_entry.pack(anchor='w')


receipt_num_label = tk.Label(window, text="Receipt Number:", background="#FFD18B")
receipt_num_label.pack(anchor='w')
reciept_entry = tk.Entry(window, border = 2)
reciept_entry.pack(anchor='w')


item_label = tk.Label(window, text="Item Hired:", background="#FFD18B")
item_label.pack(anchor='w')
item_entry = tk.Entry(window, border = 2)
item_entry.pack(anchor='w')


num_item_label = tk.Label(window, text="Number of items hired:", background="#FFD18B")
num_item_label.pack(anchor='w')
new_item_entry = tk.Entry(window, border = 2)
new_item_entry.pack(anchor='w')





















window.mainloop()