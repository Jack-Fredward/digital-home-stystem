import tkinter as tk 
from tkinter import ttk
from commomsim import *
from kitchensim import *
from kitchen import *
from login import *
from diningRoom import *
from study import *
from breakfastNook import *
from laundryRoom import *
from laundryRoomSim import *
from bedroom import *
from halfBath import *
from bathroom import *
from masterBathroom import *
from livingRoom import *

LARGEFONT =("Verdana", 35) 
SMALLFONT =("calibre",10)

class DigitalHomeApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, db, dbCursor):

		# initializing the digital home
		self.db = db
		self.dbCursor = dbCursor
		self.kitchen=kitchen("kitchen", dbCursor)
		self.diningRoom=diningRoom("dining room",dbCursor)
		self.study = study("study",dbCursor)
		self.breakfastNook = breakfastNook("breakfast nook",dbCursor)
		self.laundryRoom = laundryRoom("laundry room", dbCursor)
		self.bedRoom2 = bedRoom("bedroom2", "2", dbCursor, 0)
		self.bedRoom3 = bedRoom("bedroom3", "3", dbCursor, 0)
		self.bedRoom4 = bedRoom("bedroom4", "4", dbCursor, 1)
		self.halfBathroom = halfBathroom("halfbathroom", dbCursor)
		self.bathroom2 = bathroom("bathroom2", "2", dbCursor, 0, 0, 0)
		self.bathroom3 = bathroom("bathroom3", "3", dbCursor, 0, 1, 0)
		self.bathroom4 = bathroom("bathroom4", "4", dbCursor, 1, 0, 1)
		self.masterBathroom = masterBathroom("masterbathroom", dbCursor)
		self.livingRoom = livingRoom("livingRoom", dbCursor)

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
		for F in (LoginPage, UpdatePassword, MainMenu, Kitchen, Oven, KitchenACHeat, Fridge, Stove, KitchenSink, PantrySink, Microwave, 
		Dishwasher, CoffeeMaker, Toaster, KitchenLights, GarbageDisposal, KitchenSmokeDetector, 
		DiningRoom, DiningRoomLights, DiningRoomACHeat,DiningRoomWindows, DiningRoomWetBarSink, 
		Study, StudyACHeat, StudyWindows, StudyDoors, StudyLights, 
		BreakfastNook, BreakfastNookACHeat, BreakfastNookLights, BreakfastNookWindows, 
		LaundryRoom, LaundryRoomLights, LaundryRoomACHeat, LaundryRoomDoors, LaundryRoomSink, Washer, Dryer, 
		BedRoom2, BedRoom2Lights, BedRoom2ACHeat, BedRoom2Windows, BedRoom2Doors, 
		BedRoom3, BedRoom3Lights, BedRoom3ACHeat, BedRoom3Windows, BedRoom3Doors, 
		BedRoom4, BedRoom4Lights, BedRoom4ACHeat, BedRoom4Windows, BedRoom4Doors, BedRoom4ExternalDoors,
		HalfBathroom, HalfBathroomLights, HalfBathroomACHeat, HalfBathroomDoors, HalfBathroomSink, HalfBathroomToilet,
		Bathroom2, Bathroom2Lights, Bathroom2ACHeat, Bathroom2Doors, Bathroom2Windows, Bathroom2Sink, Bathroom2Toilet, Bathroom2Shower,
		Bathroom3, Bathroom3Lights, Bathroom3ACHeat, Bathroom3Doors, Bathroom3Windows, Bathroom3Sink, Bathroom3Toilet, Bathroom3Bathtub,
		Bathroom4, Bathroom4Lights, Bathroom4ACHeat, Bathroom4Doors, Bathroom4Windows, Bathroom4Sink, Bathroom4Toilet, Bathroom4Shower, Bathroom4ExternalDoors,
		MasterBathroom, MasterBathroomLights, MasterBathroomACHeat, MasterBathroomDoors, MasterBathroomWindows, MasterBathroomHisSink, MasterBathroomHerSink, MasterBathroomHisToilet, 
		MasterBathroomHerToilet, MasterBathroomShower, MasterBathroomBathtub,
		LivingRoom, LivingRoomLights, LivingRoomACHeat, LivingRoomDoors, LivingRoomTelevision):

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		# self.show_frame(LoginPage)
		self.show_frame(MainMenu)

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 
		self.db.commit()


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
		passwordEntry = ttk.Entry(self, show="*", font = SMALLFONT)
		userNameEntry.grid(row=1,column = 2)
		passwordEntry.grid(row=2,column = 2)


		loginButton = ttk.Button(self, text = "Login", command = lambda : login(userNameEntry.get(),passwordEntry.get(),controller,MainMenu))
		loginButton.grid(row = 3, column =2)

		updatePasswordButton = ttk.Button(self, text = "Set/Update Password", command = lambda : controller.show_frame(UpdatePassword))
		updatePasswordButton.grid(row = 4, column =2)

class UpdatePassword(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text = "Update Password", font = LARGEFONT)
		mainLabel.grid(row=0, column = 4, padx = 10, pady=10)

		userNameLabel = ttk.Label(self, text = "First Name", font = SMALLFONT)
		passwordLabel = ttk.Label(self, text = "New Password", font = SMALLFONT)
		userNameLabel.grid(row=1,column=1)
		passwordLabel.grid(row=2,column=1)

		userNameEntry = ttk.Entry(self, font = SMALLFONT)
		passwordEntry = ttk.Entry(self, font = SMALLFONT)
		userNameEntry.grid(row=1,column = 2)
		passwordEntry.grid(row=2,column = 2)


		self.passwordUpdateLabel = ttk.Label(self, text ="", font = SMALLFONT)
		self.passwordUpdateLabel.grid(row=1,column=3)



		updateButton = ttk.Button(self, text = "Update", command = lambda : update_pw(self,userNameEntry.get(),passwordEntry.get(),controller,LoginPage))
		updateButton.grid(row = 3, column =2)

		backButton = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(LoginPage))
		backButton.grid(row = 4, column =2)

class MainMenu(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		
		# label of frame Layout 2 
		label = ttk.Label(self, text ="MainMenu", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 1, column = 1, padx = 10, pady = 10)

		diningRoomButton = ttk.Button(self, text ="Dining Room", command = lambda : controller.show_frame(DiningRoom))
		diningRoomButton.grid(row=1, column = 2, padx = 10, pady = 10)

		studyButton = ttk.Button(self, text = "Study", command = lambda : controller.show_frame(Study))
		studyButton.grid(row=2, column = 2, padx = 10, pady = 10)

		breakfastNookButton = ttk.Button(self, text ="Breakfast Nook", command = lambda : controller.show_frame(BreakfastNook)) 
		breakfastNookButton.grid(row = 2, column = 1, padx = 10, pady = 10)

		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 1, column = 3, padx = 10, pady = 10)

		bedroomButton2 = ttk.Button(self, text ="Bedroom 2", command = lambda : controller.show_frame(BedRoom2))
		bedroomButton2.grid(row=1, column = 4, padx = 10, pady = 10)

		bedroomButton3 = ttk.Button(self, text ="Bedroom 3", command = lambda : controller.show_frame(BedRoom3))
		bedroomButton3.grid(row=2, column = 4, padx = 10, pady = 10)

		bedroomButton4 = ttk.Button(self, text ="Bedroom 4", command = lambda : controller.show_frame(BedRoom4))
		bedroomButton4.grid(row=3, column = 4, padx = 10, pady = 10)

		halfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(HalfBathroom))
		halfBathroomButton.grid(row=1, column = 5, padx = 10, pady = 10)

		bathroomButton2 = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2))
		bathroomButton2.grid(row=2, column = 5, padx = 10, pady = 10)

		bathroomButton3 = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3))
		bathroomButton3.grid(row=3, column = 5, padx = 10, pady = 10)

		bathroomButton4 = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4))
		bathroomButton4.grid(row=4, column = 5, padx = 10, pady = 10)

		masterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom))
		masterBathroomButton.grid(row=5, column = 5, padx = 10, pady = 10)

		livingRoomButton = ttk.Button(self, text ="Living Room", command = lambda : controller.show_frame(LivingRoom))
		livingRoomButton.grid(row=1, column = 6, padx = 10, pady = 10)

		exitButton = ttk.Button(self, text = "Exit", command = lambda : exit(0))
		exitButton.grid(row = 5, column = 1)

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

		toasterButton = ttk.Button(self, text ="Toaster", command = lambda : controller.show_frame(Toaster)) 
		toasterButton.grid(row = 3, column = 2, padx = 10, pady = 10)

		lightsButton = ttk.Button(self, text ="Lights", command = lambda : controller.show_frame(KitchenLights)) 
		lightsButton.grid(row = 3, column = 2, padx = 10, pady = 10)

		garbageDisposalButton = ttk.Button(self, text ="Garbage Disposal", command = lambda : controller.show_frame(GarbageDisposal)) 
		garbageDisposalButton.grid(row = 3, column = 2, padx = 10, pady = 10)

		# smokeDetectorButton = ttk.Button(self, text ="Smoke Detector", command = lambda : controller.show_frame(kitchenSmokeDetector)) 
		# smokeDetectorButton.grid(row = 3, column = 3, padx = 10, pady = 10)

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
		tempButton = ttk.Button(self, text = "Go", command = lambda : simOvenTemp(controller.db,self,controller.kitchen,int(tempEntry.get())))
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

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.kitchen.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.kitchen.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.kitchen.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.kitchen.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.kitchen,int(tempEntry.get())))
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

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnFridge(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffFridge(self,controller.db))
		self.fridgeStateDisplayLabel = ttk.Label(self, text = "On")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.fridgeStateDisplayLabel.grid(row=1,column=3)

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.kitchen.openFridgeDoor(self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.kitchen.closeFridgeDoor(self,controller.db))
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
		burner1ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,0,controller.db))
		burner1ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,0,controller.db))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner1ButtonOn.grid(row=1,column=1)
		burner1ButtonOff.grid(row=1,column=2)
		self.burnerStateDisplayLabel[0].grid(row=1,column=3)



		burner1TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner1TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner1TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(controller.db,self,controller.kitchen,int(burner1TempEntry.get()),0))
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
		burner2ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,1,controller.db))
		burner2ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,1,controller.db))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner2ButtonOn.grid(row=1,column=5)
		burner2ButtonOff.grid(row=1,column=6)
		self.burnerStateDisplayLabel[1].grid(row=1,column=7)



		burner2TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner2TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner2TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(controller.db,self,controller.kitchen,int(burner2TempEntry.get()),1))
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
		burner3ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,2,controller.db))
		burner3ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,2,controller.db))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner3ButtonOn.grid(row=5,column=1)
		burner3ButtonOff.grid(row=5,column=2)
		self.burnerStateDisplayLabel[2].grid(row=5,column=3)



		burner3TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner3TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner3TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(controller.db, self,controller.kitchen,int(burner3TempEntry.get()),2))
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
		burner4ButtonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnStoveBurner(self,3,controller.db))
		burner4ButtonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffStoveBurner(self,3,controller.db))
		self.burnerStateDisplayLabel.append(ttk.Label(self, text = "Off"))

		burner4ButtonOn.grid(row=5,column=5)
		burner4ButtonOff.grid(row=5,column=6)
		self.burnerStateDisplayLabel[3].grid(row=5,column=7)



		burner4TempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		burner4TempEntry = ttk.Entry(self, font = SMALLFONT)
		burner4TempButton = ttk.Button(self, text = "Go", command = lambda : simStoveTemp(controller.db, self,controller.kitchen,int(burner4TempEntry.get()),3))
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

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffSink(self,controller.db))
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

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.setPantrySinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffPantrySink(self,controller.db))
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

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnMicrowave(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffMicrowave(self,controller.db))
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
		cookButton = ttk.Button(self, text = "Start", command = lambda : simMicrowave(controller.db,self, controller.kitchen, timeEntry.get(),powerSpinbox.get()))

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

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnDishwasher(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffDishwasher(self,controller.db))
		self.dishWasherStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.dishWasherStateDisplayLabel.grid(row=1,column=3)


		dishWasherDishEntryLabel = ttk.Label(self, text = "Number of dishes you are adding: ")
		dishWasherDishEntry = ttk.Entry(self, font = SMALLFONT)
		dishWasherDishEntryLabel.grid(row = 2,column=1)
		dishWasherDishEntry.grid(row=2, column = 2)

		self.dishWasherFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.dishWasherFlowLabel.grid(row=3, column =2)

		startButton = ttk.Button(self, text = "Start", command = lambda : simDishwasher(controller.kitchen, self, int(dishWasherDishEntry.get()),controller.db))
		startButton.grid(row=3, column=1)


		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class CoffeeMaker(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Coffee Maker", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnCoffeeMaker(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffCoffeeMaker(self,controller.db))
		self.coffeeMakerStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.coffeeMakerStateDisplayLabel.grid(row=1,column=3)

		self.cupSize = tk.IntVar()

		smallCup = ttk.Radiobutton(self, text = "Small Cup", variable = self.cupSize, value = 1)
		medCup = ttk.Radiobutton(self, text = "Medium Cup", variable = self.cupSize, value = 2)
		largeCup = ttk.Radiobutton(self, text = "Large Cup", variable=self.cupSize, value = 3)

		smallCup.grid(row = 2, column = 1)
		medCup.grid(row = 3, column = 1)
		largeCup.grid(row=4, column = 1)
		

		self.coffeeMakerTempLabel = ttk.Label(self, text = "Temp: 0 *F")
		self.coffeeMakerTempLabel.grid(row = 2, column = 2)
		
		self.coffeeMakerFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.coffeeMakerFlowLabel.grid(row=3, column =2)

		brewCoffeeButton = ttk.Button(self, text = "Brew Coffee", command = lambda : simCoffeeMaker(controller.db,self, controller.kitchen, self.cupSize.get()))
		brewCoffeeButton.grid(row = 4, column =2)




		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class Toaster(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Toaster", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)


		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnToaster(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffToaster(self,controller.db))
		self.toasterStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.toasterStateDisplayLabel.grid(row=1, column =3)

		powerSpinboxLabel = ttk.Label(self, text = "Toaster Power Level", font = SMALLFONT)
		powerSpinbox = tk.Spinbox(self, from_=1, to=10)
		powerSpinboxLabel.grid(row=2,column = 1)
		powerSpinbox.grid(row=2, column=2)

		
		toastButton = ttk.Button(self, text = "Toast", command = lambda : simToaster(controller.db,self, controller.kitchen,int(powerSpinbox.get())))

		toastButton.grid(row=4, column =2)


		self.toasterToastTimeDisplay = ttk.Label(self, text = "Time Remaining: 0")
		self.toasterToastTimeDisplay.grid(row=2, column = 4)



		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class KitchenLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Kitchen Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffLights(self,controller.db))
		self.kitchenLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.kitchenLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		kitchenLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		kitchenLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.kitchenLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.kitchenLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class GarbageDisposal(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Garbage Disposal", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.kitchen.turnOnGarbageDisposal(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.kitchen.turnOffGarbageDisposal(self,controller.db))
		self.garbageDisposalStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.garbageDisposalStateDisplayLabel.grid(row=1,column=3)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class KitchenSmokeDetector(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Smoke Detector", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.smokeDetectorStateLabel = ttk.Label(self, text = str(controller.kitchen.getSmokeState()))
		self.smokeDetectorStateLabel.grid(row=1,column=1)

		#to get back to the kitchen
		kitchenButton = ttk.Button(self, text ="Kitchen", command = lambda : controller.show_frame(Kitchen)) 
		kitchenButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class DiningRoom(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Dining Room", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(DiningRoomLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(DiningRoomACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(DiningRoomWindows))
		windowsButton.grid(row=2, column =3)

		wetBarSinkButton = ttk.Button(self, text = "Wet Bar Sink", command = lambda : controller.show_frame(DiningRoomWetBarSink))
		wetBarSinkButton.grid(row=2,column=4)

class DiningRoomLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Dining Room Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.diningRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.diningRoom.turnOffLights(self,controller.db))
		self.diningRoomLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.diningRoomLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		diningRoomLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		diningRoomLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.diningRoomLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.diningRoomLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the diningroom
		diningRoomButton = ttk.Button(self, text ="Dining Room", command = lambda : controller.show_frame(DiningRoom)) 
		diningRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class DiningRoomACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.diningRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.diningRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.diningRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.diningRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.diningRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Dining Room Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the diningRoom
		diningRoomButton = ttk.Button(self, text ="Dining Room", command = lambda : controller.show_frame(DiningRoom)) 
		diningRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class DiningRoomWindows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.diningRoom.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.diningRoom.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the diningRoom
		diningRoomButton = ttk.Button(self, text ="Dining Room", command = lambda : controller.show_frame(DiningRoom)) 
		diningRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class DiningRoomWetBarSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Wet Bar Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.diningRoom.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.diningRoom.turnOffSink(self,controller.db))
		self.diningRoomSinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.diningRoomSinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		diningRoomSinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		diningRoomSinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.diningRoomSinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.diningRoomSinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the diningRoom
		diningRoomButton = ttk.Button(self, text ="Dining Room", command = lambda : controller.show_frame(DiningRoom)) 
		diningRoomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class Study(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Study", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(StudyLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(StudyACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(StudyWindows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(StudyDoors))
		doorsButton.grid(row=2,column=4)

class StudyLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Study Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.study.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.study.turnOffLights(self,controller.db))
		self.studyLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.studyLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		studyLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		studyLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.studyLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.studyLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the study
		studyButton = ttk.Button(self, text ="Study", command = lambda : controller.show_frame(Study)) 
		studyButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class StudyACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.study.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.study.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.study.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.study.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.study,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Study Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the study
		studyButton = ttk.Button(self, text ="Study", command = lambda : controller.show_frame(Study)) 
		studyButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class StudyWindows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.study.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.study.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the study
		studyButton = ttk.Button(self, text ="Study", command = lambda : controller.show_frame(Study)) 
		studyButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class StudyDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.study.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.study.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the study
		studyButton = ttk.Button(self, text ="Study", command = lambda : controller.show_frame(Study)) 
		studyButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class BreakfastNook(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Breakfast Nook", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(BreakfastNookLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(BreakfastNookACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(BreakfastNookWindows))
		windowsButton.grid(row=2, column =3)

class BreakfastNookLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="BreakFast Nook Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.breakfastNook.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.breakfastNook.turnOffLights(self,controller.db))
		self.breakfastNookLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.breakfastNookLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		breakfastNookLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		breakfastNookLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.breakfastNookLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.breakfastNookLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the breakfastNook
		breakfastNookButton = ttk.Button(self, text ="Breakfast Nook", command = lambda : controller.show_frame(BreakfastNook)) 
		breakfastNookButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class BreakfastNookACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.breakfastNook.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.breakfastNook.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.breakfastNook.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.breakfastNook.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.breakfastNook,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Breakfast Nook Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the breakfastNook
		breakfastNookButton = ttk.Button(self, text ="Breakfast Nook", command = lambda : controller.show_frame(BreakfastNook)) 
		breakfastNookButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class BreakfastNookWindows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.breakfastNook.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.breakfastNook.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

		buttonOpen2 = ttk.Button(self, text = "Open", command = lambda : controller.breakfastNook.openWindow(1,self,controller.db))
		buttonClose2 = ttk.Button(self, text="Close",command = lambda : controller.breakfastNook.closeWindow(1,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen2.grid(row=2,column=1)
		buttonClose2.grid(row=2,column=2)
		self.windowStateDisplayLabel[1].grid(row=2,column=3) 

		#to get back to the breakfastNook
		breakfastNookButton = ttk.Button(self, text ="Breakfast Nook", command = lambda : controller.show_frame(BreakfastNook)) 
		breakfastNookButton.grid(row = 5, column = 1, padx = 10, pady = 10)


class LaundryRoom(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Laundry Room", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(LaundryRoomLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(LaundryRoomACHeat))
		aCHeatButton.grid(row=2, column =2)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(LaundryRoomDoors))
		doorsButton.grid(row=2, column =3)

		laundryRoomSinkButton = ttk.Button(self, text = "Sink", command = lambda : controller.show_frame(LaundryRoomSink))
		laundryRoomSinkButton.grid(row=2,column=4)

		washerButton = ttk.Button(self, text = "Washer", command = lambda : controller.show_frame(Washer))
		washerButton.grid(row=2,column=5)

		dryerButton = ttk.Button(self, text = "Dryer", command = lambda : controller.show_frame(Dryer))
		dryerButton.grid(row=2,column=6)

class LaundryRoomLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Laundry Room Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.laundryRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.laundryRoom.turnOffLights(self,controller.db))
		self.laundryRoomLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.laundryRoomLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		laundryRoomLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		laundryRoomLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.laundryRoomLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.laundryRoomLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LaundryRoomACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.laundryRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.laundryRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.laundryRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.laundryRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.laundryRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Laundry Room Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LaundryRoomDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.laundryRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.laundryRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3)

		buttonOpen2 = ttk.Button(self, text = "Open", command = lambda : controller.laundryRoom.openDoor(1,self,controller.db))
		buttonClose2 = ttk.Button(self, text="Close",command = lambda : controller.laundryRoom.closeDoor(1,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen2.grid(row=2,column=1)
		buttonClose2.grid(row=2,column=2)
		self.doorStateDisplayLabel[1].grid(row=2,column=3) 

		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LaundryRoomSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 4, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.laundryRoom.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.laundryRoom.turnOffSink(self,controller.db))
		self.laundryRoomSinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.laundryRoomSinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		laundryRoomSinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		laundryRoomSinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.laundryRoomSinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.laundryRoomSinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class Washer(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Washer", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 4, padx = 10, pady = 10)

		laodSizeLabel = ttk.Label(self, text = "Load Size", font = SMALLFONT)
		laodSizeLabel.grid(row=1,column=1)


		self.loadSize = tk.IntVar()

		smallLoad = ttk.Radiobutton(self, text = "Small Load", variable = self.loadSize, value = 1)
		medLoad = ttk.Radiobutton(self, text = "Medium Load", variable = self.loadSize, value = 2)
		largeLoad = ttk.Radiobutton(self, text = "Large Load", variable=self.loadSize, value = 3)

		smallLoad.grid(row = 2, column = 1)
		medLoad.grid(row = 3, column = 1)
		largeLoad.grid(row=4, column = 1)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		soilLevelLabel = ttk.Label(self, text = "Soil Level", font = SMALLFONT)
		soilLevelLabel.grid(row=1,column=3)

		self.soilLevel = tk.IntVar()

		lightSoil = ttk.Radiobutton(self, text = "Light", variable = self.soilLevel, value = 1)
		normalSoil = ttk.Radiobutton(self, text = "Normal", variable = self.soilLevel, value = 2)
		heavySoil = ttk.Radiobutton(self, text = "Heavy", variable=self.soilLevel, value = 3)

		lightSoil.grid(row = 2, column = 3)
		normalSoil.grid(row = 3, column = 3)
		heavySoil.grid(row=4, column = 3)


		washButton = ttk.Button(self, text = "Wash", command = lambda : simWasher(controller.laundryRoom, (self.loadSize.get()), int(self.tempSet.get()), int(self.soilLevel.get()), self, controller.db))
		washButton.grid(row=1,column = 4)


		self.washerStatusLabel = ttk.Label(self, text = "Off")
		self.washerStatusLabel.grid(row = 1, column = 5)

		self.timeLeftLabel = ttk.Label(self, text = "Time Left: ")
		self.timeLeftLabel.grid(row=2,column = 5)

		self.waterTempLabel = ttk.Label(self,text = "Water Temp(f): ")
		self.waterTempLabel.grid(row=3, column =5)
		
		self.flowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.flowLabel.grid(row=4, column = 5)







		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 10, column = 1, padx = 10, pady = 10)

class Dryer(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Dryer", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		#to get back to the laundryRoom
		laundryRoomButton = ttk.Button(self, text ="Laundry Room", command = lambda : controller.show_frame(LaundryRoom)) 
		laundryRoomButton.grid(row = 4, column = 1, padx = 10, pady = 10)


class BedRoom2(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Bedroom 2", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(BedRoom2Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(BedRoom2ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(BedRoom2Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(BedRoom2Doors))
		doorsButton.grid(row=2, column =4)

class BedRoom2Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Bedroom 2 Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.bedroom2LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bedroom2LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		bedroom2LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		bedroom2LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.bedroom2LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bedroom2LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the bedroom2
		bedroom2Button = ttk.Button(self, text ="Bedroom 2", command = lambda : controller.show_frame(BedRoom2))
		bedroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom2ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bedRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bedRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bedRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bedRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bedRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "BedRoom 2 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the bedroom2
		bedroom2Button = ttk.Button(self, text ="BedRoom 2", command = lambda : controller.show_frame(BedRoom2)) 
		bedroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom2Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the bedroom2
		bedroom2Button = ttk.Button(self, text ="BedRoom 2", command = lambda : controller.show_frame(BedRoom2)) 
		bedroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom2Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the bedroom2
		bedroom2Button = ttk.Button(self, text ="Bedroom 2", command = lambda : controller.show_frame(BedRoom2)) 
		bedroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)


class BedRoom3(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Bedroom 3", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(BedRoom3Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(BedRoom3ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(BedRoom3Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(BedRoom3Doors))
		doorsButton.grid(row=2, column =4)

class BedRoom3Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Bedroom 3 Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.BedRoom3LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BedRoom3LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		BedRoom3LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		BedRoom3LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.BedRoom3LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.BedRoom3LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the BedRoom3
		BedRoom3Button = ttk.Button(self, text ="BedRoom 3", command = lambda : controller.show_frame(BedRoom3))
		BedRoom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom3ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bedRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bedRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bedRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bedRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bedRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "BedRoom 3 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the BedRoom3
		BedRoom3Button = ttk.Button(self, text ="BedRoom 3", command = lambda : controller.show_frame(BedRoom3)) 
		BedRoom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom3Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the BedRoom3
		BedRoom3Button = ttk.Button(self, text ="BedRoom 3", command = lambda : controller.show_frame(BedRoom3)) 
		BedRoom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom3Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the BedRoom3
		BedRoom3Button = ttk.Button(self, text ="BedRoom 3", command = lambda : controller.show_frame(BedRoom3)) 
		BedRoom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)


class BedRoom4(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="BedRoom 4", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(BedRoom4Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(BedRoom4ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(BedRoom4Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(BedRoom4Doors))
		doorsButton.grid(row=2, column =4)

		doorsButton = ttk.Button(self, text = "External Doors", command = lambda : controller.show_frame(BedRoom4ExternalDoors))
		doorsButton.grid(row=2, column =5)

class BedRoom4Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="BedRoom 4 Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.BedRoom4LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BedRoom4LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		BedRoom4LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		BedRoom4LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.BedRoom4LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.BedRoom4LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the BedRoom4
		BedRoom4Button = ttk.Button(self, text ="BedRoom 4", command = lambda : controller.show_frame(BedRoom4))
		BedRoom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom4ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bedRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bedRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bedRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bedRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bedRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "BedRoom 4 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the BedRoom4
		BedRoom4Button = ttk.Button(self, text ="BedRoom 4", command = lambda : controller.show_frame(BedRoom4)) 
		BedRoom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom4Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the BedRoom4
		BedRoom4Button = ttk.Button(self, text ="BedRoom 4", command = lambda : controller.show_frame(BedRoom4)) 
		BedRoom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom4Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the BedRoom4
		BedRoom4Button = ttk.Button(self, text ="BedRoom 4", command = lambda : controller.show_frame(BedRoom4)) 
		BedRoom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class BedRoom4ExternalDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="External Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bedRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bedRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the BedRoom4
		BedRoom4Button = ttk.Button(self, text ="BedRoom 4", command = lambda : controller.show_frame(BedRoom4)) 
		BedRoom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)


class HalfBathroom(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Half Bathroom", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(HalfBathroomLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(HalfBathroomACHeat))
		aCHeatButton.grid(row=2, column =2)

		# windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(HalfBathroomWindows))
		# windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(HalfBathroomDoors))
		doorsButton.grid(row=2, column =4)

		halfBathroomSinkButton = ttk.Button(self, text ="Sink", command = lambda : controller.show_frame(HalfBathroomSink)) 
		halfBathroomSinkButton.grid(row = 2, column = 5) 

		halfBathroomToiletButton = ttk.Button(self, text ="Toilet", command = lambda : controller.show_frame(HalfBathroomToilet)) 
		halfBathroomToiletButton.grid(row = 2, column = 5) 

class HalfBathroomLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Half Bathroom Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.halfBathroomLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.halfBathroomLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		halfBathroomLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		halfBathroomLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.halfBathroomLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.halfBathroomLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the HalfBathroom
		HalfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(HalfBathroom))
		HalfBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class HalfBathroomACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.halfBathroom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.halfBathroom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.halfBathroom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.halfBathroom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.halfBathroom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Half Bathroom Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the HalfBathroom
		HalfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(HalfBathroom)) 
		HalfBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class HalfBathroomDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.halfBathroom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.halfBathroom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the HalfBathroom
		HalfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(HalfBathroom)) 
		HalfBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class HalfBathroomSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Half Bathroom Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.halfBathroom.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.halfBathroom.turnOffSink(self,controller.db))
		self.halfBathroomSinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.halfBathroomSinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		halfBathroomSinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		halfBathroomSinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.halfBathroomSinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.halfBathroomSinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the halfBathroom
		halfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(halfBathroom)) 
		halfBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class HalfBathroomToilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.halfBathroom.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.halfBathroom.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)

		#to get back to the HalfBathroom
		HalfBathroomButton = ttk.Button(self, text ="Half Bathroom", command = lambda : controller.show_frame(HalfBathroom)) 
		HalfBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)


class Bathroom2(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Bathroom 2", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(Bathroom2Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(Bathroom2ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(Bathroom2Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(Bathroom2Doors))
		doorsButton.grid(row=2, column =4)

		bathroom2SinkButton = ttk.Button(self, text ="Sink", command = lambda : controller.show_frame(Bathroom2Sink)) 
		bathroom2SinkButton.grid(row = 2, column = 5) 

		bathroom2ToiletButton = ttk.Button(self, text ="Toilet", command = lambda : controller.show_frame(Bathroom2Toilet)) 
		bathroom2ToiletButton.grid(row = 2, column = 6) 

		bathroom2ShowerButton = ttk.Button(self, text ="Shower", command = lambda : controller.show_frame(Bathroom2Shower)) 
		bathroom2ShowerButton.grid(row = 2, column = 7) 

class Bathroom2Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.bathroom2LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom2LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		bathroom2LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		bathroom2LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.bathroom2LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom2LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the Bathroom 2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2))
		Bathroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom2ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bathroom2.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bathroom2.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bathroom2.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bathroom2.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bathroom2,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Bathroom 2 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom2Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom2.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom2.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom2Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom2.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom2.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom2Sink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom2.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom2.turnOffSink(self,controller.db))
		self.bathroom2SinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom2SinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom2SinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom2SinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom2SinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom2SinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom2Toilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.bathroom2.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom2.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)

		#to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom2Shower(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Shower", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom2.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom2.turnOffSink(self,controller.db))
		self.bathroom2StateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom2StateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom2ShowerCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom2ShowerCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom2ShowerFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom2ShowerFlowValueDisplayLabel.grid(row=2,column = 3)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		#to get back to the Bathroom2
		Bathroom2Button = ttk.Button(self, text ="Bathroom 2", command = lambda : controller.show_frame(Bathroom2)) 
		Bathroom2Button.grid(row = 4, column = 1, padx = 10, pady = 10)


class Bathroom3(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Bathroom 3", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(Bathroom3Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(Bathroom3ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(Bathroom3Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(Bathroom3Doors))
		doorsButton.grid(row=2, column =4)

		bathroom3SinkButton = ttk.Button(self, text ="Sink", command = lambda : controller.show_frame(Bathroom3Sink)) 
		bathroom3SinkButton.grid(row = 2, column = 5) 

		bathroom3ToiletButton = ttk.Button(self, text ="Toilet", command = lambda : controller.show_frame(Bathroom3Toilet)) 
		bathroom3ToiletButton.grid(row = 2, column = 6) 

		bathroom3BathtubButton = ttk.Button(self, text ="Bathtub", command = lambda : controller.show_frame(Bathroom3Bathtub)) 
		bathroom3BathtubButton.grid(row = 2, column = 7) 

class Bathroom3Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bedRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bedRoom.turnOffLights(self,controller.db))
		self.bathroom3LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom3LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		bathroom3LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		bathroom3LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.bathroom3LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom3LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the Bathroom 3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3))
		Bathroom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom3ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bathroom3.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bathroom3.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bathroom3.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bathroom3.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bathroom3,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Bathroom 3 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom3Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom3.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom3.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the Bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom3Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom3.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom3.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom3Sink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom3.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom3.turnOffSink(self,controller.db))
		self.bathroom3SinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom3SinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom3SinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom3SinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom3SinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom3SinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom3Toilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.bathroom3.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom3.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)
	####### Need to be able to flush it ####

		#to get back to the Bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom3Bathtub(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Bathtub", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom3.setBathtubFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom3.turnOffBathtub(self,controller.db))
		self.bathroom3StateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom3StateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom3BathtubCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom3BathtubCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom3BathtubFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom3BathtubFlowValueDisplayLabel.grid(row=2,column = 3)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		#to get back to the bathroom3
		Bathroom3Button = ttk.Button(self, text ="Bathroom 3", command = lambda : controller.show_frame(Bathroom3)) 
		Bathroom3Button.grid(row = 4, column = 1, padx = 10, pady = 10)


class Bathroom4(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Bathroom 4", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(Bathroom4Lights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(Bathroom4ACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(Bathroom4Windows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(Bathroom4Doors))
		doorsButton.grid(row=2, column =4)

		doorsButton = ttk.Button(self, text = "External Doors", command = lambda : controller.show_frame(Bathroom4ExternalDoors))
		doorsButton.grid(row=2, column =5)

		bathroom4SinkButton = ttk.Button(self, text ="Sink", command = lambda : controller.show_frame(Bathroom4Sink)) 
		bathroom4SinkButton.grid(row = 2, column = 6) 

		bathroom4ToiletButton = ttk.Button(self, text ="Toilet", command = lambda : controller.show_frame(Bathroom4Toilet)) 
		bathroom4ToiletButton.grid(row = 2, column = 7) 

		bathroom4ShowerButton = ttk.Button(self, text ="Shower", command = lambda : controller.show_frame(Bathroom4Shower)) 
		bathroom4ShowerButton.grid(row = 2, column = 8) 

class Bathroom4Lights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text = "Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom.turnOffLights(self,controller.db))
		self.bathroom4LightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom4LightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		bathroom4LightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		bathroom4LightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.bathroom4LightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom4LightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the Bathroom 4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4))
		Bathroom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom4ACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.bathroom4.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.bathroom4.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.bathroom4.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.bathroom4.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.bathroom4,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Bathroom 4 Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the Bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom4Windows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom4.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom4.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the Bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom4Doors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom4.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom4.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the Bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom4ExternalDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="External Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.bathroom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.bathroom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the Bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 5, column = 1, padx = 10, pady = 10)

class Bathroom4Sink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Sink", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom4.setSinkFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom4.turnOffSink(self,controller.db))
		self.bathroom4SinkStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom4SinkStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom4SinkCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom4SinkCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom4SinkFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom4SinkFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom4Toilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.bathroom4.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom4.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)

	####### Need to be able to flush it ####

		#to get back to the Bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class Bathroom4Shower(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Shower", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom4.setShowerFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom4.turnOffShower(self,controller.db))
		self.bathroom4StateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.bathroom4StateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		bathroom4ShowerCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		bathroom4ShowerCurrFlowDisplayLabel.grid(row=2, column =2)

		self.bathroom4ShowerFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.bathroom4ShowerFlowValueDisplayLabel.grid(row=2,column = 3)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		#to get back to the bathroom4
		Bathroom4Button = ttk.Button(self, text ="Bathroom 4", command = lambda : controller.show_frame(Bathroom4)) 
		Bathroom4Button.grid(row = 4, column = 1, padx = 10, pady = 10)

class MasterBathroom(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Master Bathroom", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(MasterBathroomLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(MasterBathroomACHeat))
		aCHeatButton.grid(row=2, column =2)

		windowsButton = ttk.Button(self, text = "Windows", command = lambda : controller.show_frame(MasterBathroomWindows))
		windowsButton.grid(row=2, column =3)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(MasterBathroomDoors))
		doorsButton.grid(row=2, column =4)

		masterBathroomHerSinkButton = ttk.Button(self, text ="Her Sink", command = lambda : controller.show_frame(MasterBathroomHerSink)) 
		masterBathroomHerSinkButton.grid(row = 2, column = 5) 

		masterBathroomHisSinkButton = ttk.Button(self, text ="His Sink", command = lambda : controller.show_frame(MasterBathroomHisSink)) 
		masterBathroomHisSinkButton.grid(row = 3, column = 5)

		masterBathroomHerToiletButton = ttk.Button(self, text ="Her Toilet", command = lambda : controller.show_frame(MasterBathroomHerToilet)) 
		masterBathroomHerToiletButton.grid(row = 2, column = 6) 

		masterBathroomHisToiletButton = ttk.Button(self, text ="His Toilet", command = lambda : controller.show_frame(MasterBathroomHisToilet)) 
		masterBathroomHisToiletButton.grid(row = 3, column = 6)

		masterBathroomShowerButton = ttk.Button(self, text ="Shower", command = lambda : controller.show_frame(MasterBathroomShower)) 
		masterBathroomShowerButton.grid(row = 2, column = 7) 

		masterBathroomBathtubButton = ttk.Button(self, text ="Bathtub", command = lambda : controller.show_frame(MasterBathroomBathtub)) 
		masterBathroomBathtubButton.grid(row = 3, column = 7)

class MasterBathroomLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text = "Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.bathroom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.bathroom.turnOffLights(self,controller.db))
		self.masterBathroomLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.masterBathroomLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		masterBathroomLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		masterBathroomLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.masterBathroomLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.masterBathroomLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the Master Bathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom))
		MasterBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class MasterBathroomACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.masterBathroom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.masterBathroom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.masterBathroom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.masterBathroom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.masterBathroom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Master Bathroom Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the masterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class MasterBathroomWindows(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Windows", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.windowStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.masterBathroom.openWindow(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.masterBathroom.closeWindow(0,self,controller.db))
		self.windowStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.windowStateDisplayLabel[0].grid(row=1,column=3)

        #to get back to the masterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class MasterBathroomDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.masterBathroom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.masterBathroom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class MasterBathroomHerSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Bathroom2 Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.masterBathroom.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		masterBathroomToiletCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		masterBathroomToiletCurrFlowDisplayLabel.grid(row=2, column =2)

		self.masterBathroomToiletFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.masterBathroomToiletFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)	

class MasterBathroomHisSink(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Half Bathroom Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.masterBathroom.turnOnToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		masterBathroomToiletCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		masterBathroomToiletCurrFlowDisplayLabel.grid(row=2, column =2)

		self.masterBathroomToiletFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.masterBathroomToiletFlowValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class MasterBathroomHerToilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Her Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.masterBathroom.turnOnHerToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffHerToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class MasterBathroomHisToilet(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="His Toilet", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "Flush", command = lambda : controller.masterBathroom.turnOnHisToilet(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffHisToilet(self,controller.db))
		self.BathroomToiletStateDisplayLabel = ttk.Label(self, text = "Off")	

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.BathroomToiletStateDisplayLabel.grid(row=1,column=3)

		self.flushSize = tk.IntVar()

		smallFlush = ttk.Radiobutton(self, text = "Small Flush", variable = self.flushSize, value = 1)
		bigFlush = ttk.Radiobutton(self, text = "Big Flush", variable = self.flushSize, value = 3)
		
		smallFlush.grid(row = 2, column = 1)
		bigFlush.grid(row = 3, column = 1)
		
		self.toiletFlowLabel = ttk.Label(self, text = "Flow Rate: 0%")
		self.toiletFlowLabel.grid(row=3, column =2)


		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class MasterBathroomShower(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Shower", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.masterBathroom.setShowerFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffShower(self,controller.db))
		self.masterBathroomStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.masterBathroomStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		masterBathroomShowerCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		masterBathroomShowerCurrFlowDisplayLabel.grid(row=2, column =2)

		self.masterBathroomShowerFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.masterBathroomShowerFlowValueDisplayLabel.grid(row=2,column = 3)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class MasterBathroomBathtub(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Bathtub", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.masterBathroom.setBathtubFlow(self,flowScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.masterBathroom.turnOffBathtub(self,controller.db))
		self.masterBathroomStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.masterBathroomStateDisplayLabel.grid(row=1,column=3)

		flowScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		flowScale.grid(row=2,column=1, pady = 20)

		masterBathroomBathtubCurrFlowDisplayLabel = ttk.Label(self, text = "Flow Rate", font = SMALLFONT)
		masterBathroomBathtubCurrFlowDisplayLabel.grid(row=2, column =2)

		self.masterBathroomBathtubFlowValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.masterBathroomBathtubFlowValueDisplayLabel.grid(row=2,column = 3)

		tempSettingLabel = ttk.Label(self, text = "Temp Setting", font = SMALLFONT)
		tempSettingLabel.grid(row=1,column=2)

		self.tempSet = tk.IntVar()

		coldTemp = ttk.Radiobutton(self, text = "Cold", variable = self.tempSet, value = 1)
		warmTemp = ttk.Radiobutton(self, text = "Warm", variable = self.tempSet, value = 2)
		hotTemp = ttk.Radiobutton(self, text = "Hot", variable=self.tempSet, value = 3)

		coldTemp.grid(row = 2, column = 2)
		warmTemp.grid(row = 3, column = 2)
		hotTemp.grid(row=4, column = 2)

		#to get back to the MasterBathroom
		MasterBathroomButton = ttk.Button(self, text ="Master Bathroom", command = lambda : controller.show_frame(MasterBathroom)) 
		MasterBathroomButton.grid(row = 4, column = 1, padx = 10, pady = 10)

class LivingRoom(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Living Room", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show startframe
		#
		button1 = ttk.Button(self, text ="MainMenu", command = lambda : controller.show_frame(MainMenu))
		button1.grid(row=1,column=1)

		lightsButton = ttk.Button(self, text = "Lights", command = lambda : controller.show_frame(LivingRoomLights))
		lightsButton.grid(row=2, column =1)

		aCHeatButton = ttk.Button(self, text = "AC/Heat", command = lambda : controller.show_frame(LivingRoomACHeat))
		aCHeatButton.grid(row=2, column =2)

		doorsButton = ttk.Button(self, text = "Doors", command = lambda : controller.show_frame(LivingRoomDoors))
		doorsButton.grid(row=2,column=3)

		televisionButton = ttk.Button(self, text = "Television", command = lambda : controller.show_frame(LivingRoom))
		televisionButton.grid(row=2,column=4)

class LivingRoomLights(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Living Room Lights", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.livingRoom.setLightBrightness(self,brightScale.get(),controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.livingRoom.turnOffLights(self,controller.db))
		self.livingRoomLightsStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.livingRoomLightsStateDisplayLabel.grid(row=1,column=3)

		brightScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		brightScale.grid(row=2,column=1, pady = 20)

		livingRoomLightsCurrBrightDisplayLabel = ttk.Label(self, text = "Brightness", font = SMALLFONT)
		livingRoomLightsCurrBrightDisplayLabel.grid(row=2, column =2)

		self.livingRoomLightsBrightValueDisplayLabel = ttk.Label(self, text = "0%", font = SMALLFONT)
		self.livingRoomLightsBrightValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the livingRoom
		LivingRoomButton = ttk.Button(self, text ="Living Room", command = lambda : controller.show_frame(LivingRoom)) 
		LivingRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LivingRoomACHeat(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="AC/Heat", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOnAC = ttk.Button(self, text = "AC On", command = lambda : controller.livingRoom.turnOnAC(self,controller.db))
		buttonOnAC.grid(row=1,column=1)
		buttonOffAC = ttk.Button(self, text = "AC Off", command = lambda : controller.livingRoom.turnOffAC(self,controller.db))
		buttonOffAC.grid(row=1,column=2)

		buttonOnHeat = ttk.Button(self, text = "Heat On", command = lambda : controller.livingRoom.turnOnHeat(self,controller.db))
		buttonOnHeat.grid(row=2,column=1)
		buttonOffHeat = ttk.Button(self, text = "Heat Off", command = lambda : controller.livingRoom.turnOffHeat(self,controller.db))
		buttonOffHeat.grid(row=2,column=2)

		self.aCStateDisplayLabel = ttk.Label(self, text = "Off")
		self.aCStateDisplayLabel.grid(row=1,column=3, padx = 10)
		self.heatStateDisplayLabel = ttk.Label(self, text = "Off")
		self.heatStateDisplayLabel.grid(row=2,column=3, padx = 10)

		tempEntryLabel = ttk.Label(self, text = "Enter Desired Temp")
		tempEntry = ttk.Entry(self, font = SMALLFONT)
		tempButton = ttk.Button(self, text = "Go", command = lambda : commonSimACHeat(controller.db,self,controller.livingRoom,int(tempEntry.get())))
		self.tempDisplayLabel = ttk.Label(self, text = "70 *F")
		currTempLabel = ttk.Label(self,text = "Living Room Room Temp")


		tempEntryLabel.grid(row = 3, column = 1, padx = 10, pady = 10)
		tempEntry.grid(row = 3, column = 2)
		tempButton.grid(row= 3, column = 3)
		currTempLabel.grid(row=4,column=1)
		self.tempDisplayLabel.grid(row=4, column =2)

		#to get back to the livingRoom
		LivingRoomButton = ttk.Button(self, text ="Living Room", command = lambda : controller.show_frame(LivingRoom)) 
		LivingRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LivingRoomDoors(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = ttk.Label(self, text ="Doors", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		self.doorStateDisplayLabel = []

		buttonOpen = ttk.Button(self, text = "Open", command = lambda : controller.livingRoom.openDoor(0,self,controller.db))
		buttonClose = ttk.Button(self, text="Close",command = lambda : controller.livingRoom.closeDoor(0,self,controller.db))
		self.doorStateDisplayLabel.append(ttk.Label(self, text = "Closed"))

		buttonOpen.grid(row=1,column=1)
		buttonClose.grid(row=1,column=2)
		self.doorStateDisplayLabel[0].grid(row=1,column=3) 

		#to get back to the livingRoom
		LivingRoomButton = ttk.Button(self, text ="Living Room", command = lambda : controller.show_frame(LivingRoom)) 
		LivingRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

class LivingRoomTelevision(tk.Frame):
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent)

		mainLabel = ttk.Label(self, text ="Television", font = LARGEFONT) 
		mainLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

		buttonOn = ttk.Button(self, text = "On", command = lambda : controller.livingRoom.turnOnTelevision(self,controller.db))
		buttonOff = ttk.Button(self, text="Off",command = lambda : controller.livingRoom.turnOffTelevision(self,controller.db))
		self.livingRoomTelevisionStateDisplayLabel = ttk.Label(self, text = "Off")

		buttonOn.grid(row=1,column=1)
		buttonOff.grid(row=1,column=2)
		self.livingRoomTelevisionStateDisplayLabel.grid(row=1,column=3)

		# channelScale = tk.Scale(self, tickinterval = 10, length = 300,from_=100, to=0)
		# channelScale.grid(row=2,column=1, pady = 20)

		# livingRoomTelevisionCurrChannelDisplayLabel = ttk.Label(self, text = "Channel", font = SMALLFONT)
		# livingRoomTelevisionChannelDisplayLabel.grid(row=2, column =2)

		# self.livingRoomTelevisionChannelValueDisplayLabel = ttk.Label(self, text = "0", font = SMALLFONT)
		# self.livingRoomTelevisionChannelValueDisplayLabel.grid(row=2,column = 3)

		#to get back to the livingRoom
		LivingRoomButton = ttk.Button(self, text ="Living Room", command = lambda : controller.show_frame(LivingRoom)) 
		LivingRoomButton.grid(row = 5, column = 1, padx = 10, pady = 10)

# Driver Code 
def main():
	# Open database connection
	db = pymysql.connect("localhost","jp","Database","digital_home_database" )
	# db = pymysql.connect("localhost","root","Audrey1!seed","digitalhome" )
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	cursor.execute("DELETE FROM TempSensors")
	cursor.execute("DELETE FROM OpenCloseSensors")
	cursor.execute("DELETE FROM MotionSensors")
	cursor.execute("DELETE FROM LiquidFlowSensors")
	cursor.execute("DELETE FROM BrightnessSensor")
	cursor.execute("DELETE FROM Actuators")
	cursor.execute("DELETE FROM Devices")

	app = DigitalHomeApp(db,cursor) 
	app.mainloop() 

	db.commit()
	db.close()
main()
