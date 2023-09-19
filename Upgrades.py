import Images
import tkinter as tk
import Calculations

class Upgrades():
    def setupFrames(frameCitybuild):
        global frameMenuBar, showMenu, frameMenuInformation, frameSlideValues
        global lblRoadMenu, lblWaterMenu, lblElectricMenu, lblWasteMenu, lblEducationMenu, \
        lblTransportMenu, lblPoliceMenu, lblFireDepMenu, lblHealthMenu, lblEntertainmentMenu, \
        lblShoppingMenu, lblIndicatorOpenMenu, lblIndicatorClosedMenu, showItem, showMenu, roadConditions, lblTrafficFlow, lblRoadCondition
        
        frameMenuBar = tk.Frame(frameCitybuild, width=5)
        frameMenuBar.grid(column=4, row=25, sticky = "nswe", columnspan=12)
        frameMenuBar.grid_rowconfigure(0, weight=1, minsize=55)
        frameMenuBar.grid_rowconfigure(1, weight=1, minsize=40)
        frameMenuBar.grid_columnconfigure((1,2,3,4,5,6,7,8,9,10,11), weight=1)

        lblRoadMenu, lblWaterMenu, lblElectricMenu, lblWasteMenu, lblEducationMenu, \
        lblTransportMenu, lblPoliceMenu, lblFireDepMenu, lblHealthMenu, lblEntertainmentMenu, \
        lblShoppingMenu, lblIndicatorOpenMenu, lblIndicatorClosedMenu = Images.createMenuBar(frameMenuBar)

        frameMenuInformation = tk.Frame(frameCitybuild, width=5, background="grey")

        frameSlideValues = tk.Frame(frameMenuInformation)
        frameSlideValues.grid(column=2, row=0, sticky = "nswe", columnspan=3, rowspan=8)
        frameMenuInformation.grid_columnconfigure(1, weight=1)
        frameSlideValues.grid_rowconfigure((2,5), minsize=50)
        
        showItem = False
        showMenu = False
        
        roadConditions = Images.createRoadConditions()
        lblRoadCondition = tk.Label(frameMenuInformation, anchor="n", compound="left")
        lblTrafficFlow = tk.Label(frameMenuInformation, anchor="n", compound="left")
        lblPollution = tk.Label(frameMenuInformation, anchor="n", compound="left")
        
        Calculations.setupValues(frameSlideValues)
        
        return lblIndicatorOpenMenu, lblIndicatorClosedMenu
  
    def statusMenu(event, roadcondition):
        global showMenu, showItem
        padX = 5
        
        frameSelectedItem = tk.Frame(frameMenuBar, background="grey")
        
        if showMenu == False:
            frameMenuInformation.grid(column=4, row=5, sticky = "nswe", columnspan=7, rowspan=8)
            lblRoadMenu.grid(column=0,row=1, padx=padX)
            lblWaterMenu.grid(column=1,row=1, padx=padX)
            lblElectricMenu.grid(column=2,row=1, padx=padX)
            lblWasteMenu.grid(column=3,row=1, padx=padX)
            lblEducationMenu.grid(column=4,row=1, padx=padX)
            lblTransportMenu.grid(column=5,row=1, padx=padX)
            lblPoliceMenu.grid(column=6,row=1, padx=padX)
            lblFireDepMenu.grid(column=7,row=1, padx=padX)
            lblHealthMenu.grid(column=8,row=1, padx=padX)
            lblEntertainmentMenu.grid(column=9,row=1, padx=padX)
            lblShoppingMenu.grid(column=10,row=1, padx=padX)
            lblRoadMenu.bind("<Button-1>", lambda y: Upgrades.optionRoad(event, frameSelectedItem, lblRoadMenu, roadcondition))
            lblWaterMenu.bind("<Button-1>")
            lblElectricMenu.bind("<Button-1>", lambda y: Upgrades.optionElectricity(event, frameSelectedItem, lblElectricMenu))
            lblWasteMenu.bind("<Button-1>")
            lblEducationMenu.bind("<Button-1>")
            lblTransportMenu.bind("<Button-1>")
            lblPoliceMenu.bind("<Button-1>")
            lblFireDepMenu.bind("<Button-1>")
            lblHealthMenu.bind("<Button-1>")
            lblEntertainmentMenu.bind("<Button-1>")
            lblShoppingMenu.bind("<Button-1>")
            lblIndicatorClosedMenu.grid_forget()
            lblIndicatorOpenMenu.grid(column=12, row=1)
            showMenu = True
        elif showMenu == True:
            frameMenuInformation.grid_forget()
            lblRoadMenu.grid_forget()
            lblWaterMenu.grid_forget()
            lblElectricMenu.grid_forget()
            lblWasteMenu.grid_forget()
            lblEducationMenu.grid_forget()
            lblTransportMenu.grid_forget()
            lblPoliceMenu.grid_forget()
            lblFireDepMenu.grid_forget()
            lblHealthMenu.grid_forget()
            lblEntertainmentMenu.grid_forget()
            lblShoppingMenu.grid_forget()
            lblIndicatorClosedMenu.grid(column=12, row=1)
            lblIndicatorOpenMenu.grid_forget()
            if showItem == True:
                frameSelectedItem.grid_forget()
                showItem = False
            showMenu = False
    
    def optionRoad(event, frameSelectedItem, lblRoadMenu, roadcondition):
        global showMenu, showItem, roadConditions, lblTrafficFlow, lblRoadCondition
        lblRoadCity, lblRoadIntercity, lblMotorway, lblParking, lblParkingLot = Images.createRoadIcons(frameSelectedItem)
        lblDivide1 = tk.Label(frameSelectedItem, width=5, background="grey", foreground="grey")
        #Blitzer einbauen
        
        if showItem == False: 
            if roadcondition >= 67:
                lblRoadCondition["image"] = roadConditions[0]
            elif roadcondition >= 33:
                lblRoadCondition["image"] = roadConditions[1]
            else:
                lblRoadCondition["image"] = roadConditions[2]
                
            lblRoadCondition["text"] = f"{roadcondition}% Straßenzustand"
            lblRoadCondition.grid(column=0,row=0)
            lblTrafficFlow["text"] = f"{roadcondition}% Verkehrsfluss"
            lblTrafficFlow.grid(column=0,row=1)
            frameSelectedItem.grid(column=0,row=0, columnspan=10, sticky="w")
            lblRoadMenu["background"] = "#87CEFA"
            lblRoadCity.grid(column=0,row=0, sticky="w") 
            lblRoadIntercity.grid(column=1,row=0, sticky="w", padx=5) 
            lblMotorway.grid(column=2,row=0, sticky="w", padx=5) 
            lblDivide1.grid(column=3,row=0, sticky="w", padx=5)
            lblParking.grid(column=4,row=0, sticky="w", padx=5)
            lblParkingLot.grid(column=5,row=0, sticky="w", padx=5)
            lblRoadCity.bind("<Button-1>") 
            lblRoadIntercity.bind("<Button-1>")  
            lblMotorway.bind("<Button-1>")  
            lblParking.bind("<Button-1>") 
            lblParkingLot.bind("<Button-1>") 
            showItem = True
        elif showItem == True:
            frameSelectedItem.grid_forget()
            lblRoadCity.destroy()
            lblRoadIntercity.destroy()
            lblMotorway.destroy()
            lblDivide1.destroy()
            lblParking.destroy()
            lblParkingLot.destroy()
            lblRoadCondition.grid_forget()
            lblTrafficFlow.grid_forget()
            lblRoadMenu["background"] = "#F0F0F0"
            showItem = False
    
    def optionElectricity(event, frameSelectedItem, lblElectricMenu):
        global showMenu, showItem
        #Windkraft, Atomkraft, Kohlekraft, Solarpark, 
        lblSolar, lblWind, lblCoal, lblNuclear = Images.createEnergyIcons(frameSelectedItem)
        if showItem == False: 
            frameSelectedItem.grid(column=0,row=0, columnspan=10, sticky="w")
            lblElectricMenu["background"] = "#87CEFA"
            lblSolar.grid(column=0,row=0, sticky="w") 
            lblWind.grid(column=1,row=0, sticky="w", padx=5) 
            lblCoal.grid(column=2,row=0, sticky="w", padx=5) 
            lblNuclear.grid(column=3,row=0, sticky="w", padx=5)
            lblSolar.bind("<Button-1>") 
            lblWind.bind("<Button-1>")  
            lblCoal.bind("<Button-1>")  
            lblNuclear.bind("<Button-1>") 
            showItem = True
        elif showItem == True:
            frameSelectedItem.grid_forget()
            lblRoadCondition.grid_forget()
            lblTrafficFlow.grid_forget()
            lblElectricMenu["background"] = "#F0F0F0"
            showItem = False
    