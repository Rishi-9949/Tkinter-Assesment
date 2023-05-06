import tkinter as tk
from PIL import ImageTk, Image, ImageOps

window = tk.Tk()


# The Title of the window 
window.title("Julie’s Party Hire")

# Addes an Icon as the windows logo
window.iconbitmap("jph.ico")

# Geometry of the window
window.geometry("700x700")

# Defining the Maximun and the minimun size of the window sto its locked and unchanged, (width,hieght)
window.minsize(700, 700)

#giving the window an background colour 
window.config(bg="#F9F9E0")



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

img = Image.open("Logo.jpg")
img = img.resize((100, 100))


# Create ImageTk objects
img_tk = ImageTk.PhotoImage(img)

# Create Label widget
img_label = tk.Label(window, image=img_tk)

# Place the Label widgets
img_label.place(x=595,y=23)

# Labels and Entry Boxes 
name_label = tk.Label(window, text="Full Name:", background="#FFD18B")
name_label.pack(anchor='w')
name_entry = tk.Entry(window, border = 1, relief='solid')
name_entry.pack(anchor='w')


receipt_num_label = tk.Label(window, text="Receipt Number:", background="#FFD18B")
receipt_num_label.pack(anchor='w')
reciept_entry = tk.Entry(window, border = 1, relief='solid')
reciept_entry.pack(anchor='w')


item_label = tk.Label(window, text="Item Hired:", background="#FFD18B")
item_label.pack(anchor='w')
item_entry = tk.Entry(window, border = 1, relief='solid')
item_entry.pack(anchor='w')



num_item_label = tk.Label(window, text="Number of items hired:", background="#FFD18B")
num_item_label.pack(anchor='w')
new_item_entry = tk.Entry(window, border = 1, relief='solid')
new_item_entry.pack(anchor='w')





















window.mainloop()