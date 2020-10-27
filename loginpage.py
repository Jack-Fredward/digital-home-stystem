

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("Login")

#set window size
window.geometry("250x150")


#set window color
window.configure(bg='light blue')


# You will create two text labels namely 'admin' and 'password' and and two input labels for them

tkinter.Label(window, text = "Admin").grid(row = 0) #'admin' is placed on position 00 (row - 0 and column - 0)

# 'Entry' class is used to display the input-field for 'admin' text label
tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

tkinter.Label(window, text = "Password").grid(row = 1) #'password' is placed on position 10 (row - 1 and column - 0)

tkinter.Entry(window).grid(row = 1, column = 1) #second input-field is placed on position 11 (row - 1 and column - 1)

# 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)                 

#login button
btn5 = tkinter.Button(text = "Login", fg = "green").place(x=100, y=80)



window.mainloop()