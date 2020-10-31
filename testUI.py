import tkinter as tk 
from tkinter import ttk
from kitchensim import *
from kitchen import *

LARGEFONT =("Verdana", 35) 
SMALLFONT =("calibre",10)

class DigitalHomeApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, dbCursor):

		# initializing the digital home
		self.dbCursor = dbCursor
		self.kitchen=kitchen("kitchen", dbCursor)
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, "Digital Home") 
		
		# creating a container 
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, Page1, Page2): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(StartPage) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 

# first window frame startpage 

class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		
		# label of frame Layout 2 
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Page 1", command = lambda : controller.show_frame(Page1)) 
	
		# putting the button in its place by 
		# using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

		## button to show frame 2 with text layout2 
		button2 = ttk.Button(self, text ="Page 2", command = lambda : controller.show_frame(Page2)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

		


# second window frame page1 
class Page1(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Kitchen", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage)) 
	
		# putting the button in its place 
		# by using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

		# button to show frame 2 with text 
		# layout2 
		button2 = ttk.Button(self, text ="Oven", command = lambda : controller.show_frame(Page2)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 


def showEntry(text):
	print(text)

# third window frame page2 
class Page2(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		# self.temp=tk.StringVar()
		mainLabel = ttk.Label(self, text ="Oven", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)
	

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : simOvenTemp(self,controller.kitchen,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "0 *F")
		#THIS IS HOW TO DO THE UI MAKE THE BUTTONS ATTRIBUTESD PASS TO OTHER PLACES UPDATE IN THE OTHER PLACES AND BOOM WORKING UPDATING UI

		tempEntryLabel.grid(row = 1, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 1, column = 2)
		tempButton.grid(row= 1, column = 3)
		self.tempDisplayLabel.grid(row=1, column =4)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Page1)) 
		kitchenButton.grid(row = 2, column = 1, padx = 10, pady = 10) 



# Driver Code 
def main():
	# Open database connection
	db = pymysql.connect("localhost","jp","Database","digital_home_database" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	cursor.execute("DELETE FROM TempSensors")
	cursor.execute("DELETE FROM OpenCloseSensors")
	cursor.execute("DELETE FROM MotionSensors")
	cursor.execute("DELETE FROM LiquidFlowSensors")
	cursor.execute("DELETE FROM BrightnessSensor")
	cursor.execute("DELETE FROM Actuators")
	cursor.execute("DELETE FROM Devices")

	app = DigitalHomeApp(cursor) 
	app.mainloop() 

	db.commit()
	db.close()
main()
