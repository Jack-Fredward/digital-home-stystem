import tkinter



# Let's create the Tkinter window.
window = tkinter.Tk()
window.title("My Kitchen")

#set window size
window.geometry("400x250")


#set window color
window.configure(bg='pink')




# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

#button 1
btn1 = tkinter.Button(top_frame, text = "Oven", fg = "red").place(x=250, y=50)
 #'fg or foreground' is for coloring the contents (buttons)
#button 2
btn2 = tkinter.Button(top_frame, text = "Fridge", fg = "purple").place(x=45, y=100)

#button 3
btn3 = tkinter.Button(top_frame, text = "Toaster", fg = "orange").place(x=45, y=50) #'fg or foreground' is for coloring the contents (buttons)

#button 4
btn4 = tkinter.Button(top_frame, text = "AC", fg = "blue").place(x=250, y=100)

#button 5
btn5 = tkinter.Button(top_frame, text = "Microwave", fg = "purple").place(x=145, y=50)

#button 6
btn6 = tkinter.Button(top_frame, text = "Lights", fg = "yellow").place(x=145, y=100)

#button 7
btn7 = tkinter.Button(top_frame, text = "Coffee", fg = "brown").place(x=145, y=150)

#button 8
btn8 = tkinter.Button(top_frame, text = "Stove", fg = "grey").place(x=45, y=150)

#button 9
btn9 = tkinter.Button(top_frame, text = "dishwasher", fg = "red").place(x=250, y=150)

#logout button
btn5 = tkinter.Button(top_frame, text = "Logout", fg = "green").place(x=250, y=200)


window.mainloop()
