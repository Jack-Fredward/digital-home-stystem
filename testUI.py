import tkinter as tk 
from tkinter import ttk
from commomsim import *
from kitchensim import *
from kitchen import *
from login import *

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
		for F in (LoginPage, MainMenu, Kitchen, Oven, KitchenACHeat, Fridge, Stove, KitchenSink, PantrySink, Microwave, Dishwasher, CoffeeMaker): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(LoginPage) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 


class LoginPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text = "LoginPage", font = LARGEFONT)
		mainLabel.grid(row=0, column = 4, padx = 10, pady=10)

		userNameLabel = ttk.Label(self, text = "First Name", font = SMALLFONT)
		passwordLabel = ttk.Label(self, text = "Password", font = SMALLFONT)
		userNameLabel.grid(row=1,column=1)
		passwordLabel.grid(row=2,column=1)

		userNameEntry = ttk.Entry(self, font = SMALLFONT)
		passwordEntry = ttk.Entry(self, font = SMALLFONT)
		userNameEntry.grid(row=1,column = 2)
		passwordEntry.grid(row=2,column = 2)

		loginButton = ttk.Button(self, text = "Login", command = lambda : login(userNameEntry.get(),passwordEntry.get(),controller,MainMenu))
		loginButton.grid(row = 3, column =2)





# first window frame startpage 

class MainMenu(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		
		# label of frame Layout 2 
		label = ttk.Label(self, text ="MainMenu", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
	
		# putting the button in its place by 
		# using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

		## button to show frame 2 with text layout2 
		# button2 = ttk.Button(self, text ="Page 2", command = lambda : controller.show_frame(Oven)) 
	
		# putting the button in its place by 
		# using grid 
		# button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

		


# second window frame page1 
class Kitchen(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Kitchen", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu)) 
	
		# putting the button in its place 
		# by using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

		# button to show frame 2 with text 
		# layout2 
		button2 = ttk.Button(self, text ="Oven", command = lambda : controller.show_frame(Oven)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(KitchenACHeat))
		aCHeatButton.grid(row=2, column =2)

		
		fridgeButton = ttk.Button(self, text ="Fridge", command = lambda : controller.show_frame(Fridge)) 
		fridgeButton.grid(row = 2, column = 3, padx = 10, pady = 10) 

	
		stoveButton = ttk.Button(self, text ="Stove", command = lambda : controller.show_frame(Stove)) 
		stoveButton.grid(row = 2, column = 4, padx = 10, pady = 10) 

		kitchenSinkButton = ttk.Button(self, text ="Sink", command = lambda : controller.show_frame(KitchenSink)) 
		kitchenSinkButton.grid(row = 2, column = 5, padx = 10, pady = 10) 

		pantrySinkButton = ttk.Button(self, text ="Pantry Sink", command = lambda : controller.show_frame(PantrySink)) 
		pantrySinkButton.grid(row = 2, column = 6, padx = 10, pady = 10)

		microwaveButton = ttk.Button(self, text ="Microwave", command = lambda : controller.show_frame(Microwave)) 
		microwaveButton.grid(row = 2, column = 7, padx = 10, pady = 10)

		dishwasherButton = ttk.Button(self, text ="Dishwasher", command = lambda : controller.show_frame(Dishwasher)) 
		dishwasherButton.grid(row = 2, column = 8, padx = 10, pady = 10)

		coffeeMakerButton = ttk.Button(self, text ="Coffee Maker", command = lambda : controller.show_frame(CoffeeMaker)) 
		coffeeMakerButton.grid(row = 3, column = 1, padx = 10, pady = 10)


# def showEntry(text):
# 	print(text)

class Oven(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		# self.temp=tk.StringVar()
		mainLabel = ttk.Label(self, text ="Oven", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)
	
		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnOven(self))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffOven(self))
		self.ovenStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.ovenStateDisplayLabel.grid(row=1,column=3)



		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : simOvenTemp(self,controller.kitchen,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "0 *F")
		currTempLabel = ttk.Label(self,text = "Oven Temp")
		#THIS IS HOW TO DO THE UI MAKE THE BUTTONS ATTRIBUTESD PASS TO OTHER PLACES UPDATE IN THE OTHER PLACES AND BOOM WORKING UPDATING UI
		tempEntryLabel.grid(row = 2, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 2, column = 2)
		tempButton.grid(row= 2, column = 3)
		currTempLabel.grid(row=3,column=1)
		self.tempDisplayLabel.grid(row=3, column =2)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 4, column = 1, padx = 10, pady = 10) 


class KitchenACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.kitchen.turnOnAC(self))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.kitchen.turnOffAC(self))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.kitchen.turnOnHeat(self))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.kitchen.turnOffHeat(self))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(self,controller.kitchen,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Kitchen Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10) 

class Fridge(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Fridge", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnFridge(self))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffFridge(self))
		self.fridgeStateDisplayLabel = ttk.Label(self, text = "On")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.fridgeStateDisplayLabel.grid(row=1,column=3)

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.kitchen.openFridgeDoor(self))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.kitchen.closeFridgeDoor(self))
		self.fridgeDoorStateDisplayLabel = ttk.Label(self, text = "Closed")

		buttonOpen.grid(row=2,column=1)
		buttonClose.grid(row=2,column=2)
		self.fridgeDoorStateDisplayLabel.grid(row=2,column=3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10) 

class Stove(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Stove", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.burnerStateDisplayLabel=[]
		self.burnerTempDisplayLabel=[]

		#BURNER 1
		burner1ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,0))
		burner1ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,0))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner1ButtonOn.grid(row=1,column=1)
		burner1ButtonOff.grid(row=1,column=2)
		self.burnerStateDisplayLabel[0].grid(row=1,column=3)



		burner1TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner1TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner1TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(self,controller.kitchen,int(burner1TempEntry.get()),0))
		self.burnerTempDisplayLabel.append(ttk.Label(self, text = "0 *F"))
		burner1CurrTempLabel = ttk.Label(self,text = "Burner 1")
		burner1TempEntryLabel.grid(row = 2, column = 1, padx = 10, pady = 10)
		burner1TempEntry.grid(row = 2, column = 2)
		burner1TempButton.grid(row= 2, column = 3)
		burner1CurrTempLabel.grid(row=3,column=1)
		self.burnerTempDisplayLabel[0].grid(row=3, column =2)

		#to get back to the kitchen
		# kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		# kitchenButton.grid(row = 4, column = 1, padx = 10, pady = 10) 


		#BURNER 2
		burner2ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,1))
		burner2ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,1))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner2ButtonOn.grid(row=1,column=5)
		burner2ButtonOff.grid(row=1,column=6)
		self.burnerStateDisplayLabel[1].grid(row=1,column=7)



		burner2TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner2TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner2TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(self,controller.kitchen,int(burner2TempEntry.get()),1))
		self.burnerTempDisplayLabel.append(ttk.Label(self, text = "0 *F"))
		burner2CurrTempLabel = ttk.Label(self,text = "Burner 2")
		burner2TempEntryLabel.grid(row = 2, column = 5, padx = 10, pady = 10)
		burner2TempEntry.grid(row = 2, column = 7)
		burner2TempButton.grid(row= 2, column = 8)
		burner2CurrTempLabel.grid(row=3,column=5)
		self.burnerTempDisplayLabel[1].grid(row=3, column =7)

		#to get back to the kitchen
		# kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		# kitchenButton.grid(row = 8, column = 1, padx = 10, pady = 10) 

		#BURNER 3
		burner3ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,2))
		burner3ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,2))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner3ButtonOn.grid(row=5,column=1)
		burner3ButtonOff.grid(row=5,column=2)
		self.burnerStateDisplayLabel[2].grid(row=5,column=3)



		burner3TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner3TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner3TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(self,controller.kitchen,int(burner3TempEntry.get()),2))
		self.burnerTempDisplayLabel.append(ttk.Label(self, text = "0 *F"))
		burner3CurrTempLabel = ttk.Label(self,text = "Burner 3")
		burner3TempEntryLabel.grid(row = 6, column = 1, padx = 10, pady = 10)
		burner3TempEntry.grid(row = 6, column = 2)
		burner3TempButton.grid(row= 6, column = 3)
		burner3CurrTempLabel.grid(row=7,column=1)
		self.burnerTempDisplayLabel[2].grid(row=7, column =2)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 9, column = 1, padx = 10, pady = 10) 

		#BURNER 4
		burner4ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,3))
		burner4ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,3))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner4ButtonOn.grid(row=5,column=5)
		burner4ButtonOff.grid(row=5,column=6)
		self.burnerStateDisplayLabel[3].grid(row=5,column=7)



		burner4TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner4TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner4TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(self,controller.kitchen,int(burner4TempEntry.get()),3))
		self.burnerTempDisplayLabel.append(ttk.Label(self, text = "0 *F"))
		burner4CurrTempLabel = ttk.Label(self,text = "Burner 4")
		burner4TempEntryLabel.grid(row = 6, column = 5, padx = 10, pady = 10)
		burner4TempEntry.grid(row = 6, column = 7)
		burner4TempButton.grid(row= 6, column = 8)
		burner4CurrTempLabel.grid(row=7,column=5)
		self.burnerTempDisplayLabel[3].grid(row=7, column =7)
		
class KitchenSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Kitchen Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.setSinkFlow(self,flowScale.get()))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffSink(self))
		self.kitchenSinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.kitchenSinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		kitchenSinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		kitchenSinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.kitchenSinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.kitchenSinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 4, column = 1, padx = 10, pady = 10) 

class PantrySink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Pantry Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.setPantrySinkFlow(self,flowScale.get()))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffPantrySink(self))
		self.pantrySinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.pantrySinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		pantrySinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		pantrySinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.pantrySinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.pantrySinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10) 

class Microwave(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Microwave", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnMicrowave(self))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffMicrowave(self))
		self.microwaveStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.microwaveStateDisplayLabel.grid(row=1,column=3)


		powerSpinboxLabel = ttk.Label(self, text = "Power Level", font = SMALLFONT)
		powerSpinbox = tk.Spinbox(self, from_=1, to=10)
		powerSpinboxLabel.grid(row=2,column = 1)
		powerSpinbox.grid(row=2, column=2)

		timeEntryLabel = ttk.Label(self, text = "Cook Time(s)", font = SMALLFONT)
		timeEntry = ttk.Entry(self, font = SMALLFONT)
		cookButton = ttk.Button(self, text = "Start", command = lambda : simMicrowave(self, controller.kitchen, timeEntry.get(),powerSpinbox.get()))

		timeEntryLabel.grid(row = 3, column=1)
		timeEntry.grid(row=3, column = 2)
		cookButton.grid(row=4, column =2)


		self.microwaveCookTimeDisplay = ttk.Label(self, text = "Time Remaining: 0")
		self.microwaveCookTimeDisplay.grid(row=2, column = 4)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class Dishwasher(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Dishwasher", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class CoffeeMaker(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Coffee Maker", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnCoffeeMaker(self))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffCoffeeMaker(self))
		self.coffeeMakerStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.coffeeMakerStateDisplayLabel.grid(row=1,column=3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)



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
