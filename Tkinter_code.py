import ttkbootstrap as ttkb

window = ttkb.Window()


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
















window.mainloop()