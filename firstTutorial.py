from tkinter import * 

#The Tk() instance creates a window and sets up everything
root = Tk()

#Creating the lable widget
my_label = Label(root, text="Hello World!")

#Packing the lable on the screen
my_label.pack()



#This is a continuous loop to track what the user is doing 
root.mainloop()
