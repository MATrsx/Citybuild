import Images
import tkinter as tk
import Calculations, footballEventAnimation

levelEnergy = [0,0,0,0]
colour = ["","","",""]
count = [0,0,0,0]
moveEnergy = [0,0,0,0]

class Upgrades():
    def setupFrames(frameCitybuild):
        global frameMenuBar, showMenu, frameMenuInformation, frameSlideValues, frameSelectedItem, lblDivide1, showAnyItem
        global lblRoadMenu, lblWaterMenu, lblElectricMenu, lblWasteMenu, lblEducationMenu, frameEnergyConsumption, \
        lblTransportMenu, lblPoliceMenu, lblFireDepMenu, lblHealthMenu, lblEntertainmentMenu, \
        lblShoppingMenu, lblIndicatorOpenMenu, lblIndicatorClosedMenu, showItem, showMenu, roadConditions, lblTrafficFlow, lblRoadCondition
        global lblSolar, lblWind, lblCoal, lblNuclear, lblRoadCity, lblRoadIntercity, lblMotorway, lblParking, lblParkingLot
        
        frameMenuBar = tk.Frame(frameCitybuild, width=5)
        frameMenuBar.grid(column=4, row=25, sticky = "nswe", columnspan=12)
        frameMenuBar.grid_rowconfigure(0, weight=1, minsize=55)
        frameMenuBar.grid_rowconfigure(1, weight=1, minsize=40)
        frameMenuBar.grid_columnconfigure((1,2,3,4,5,6,7,8,9,10,11), weight=1)

        lblRoadMenu, lblWaterMenu, lblElectricMenu, lblWasteMenu, lblEducationMenu, \
        lblTransportMenu, lblPoliceMenu, lblFireDepMenu, lblHealthMenu, lblEntertainmentMenu, \
        lblShoppingMenu, lblIndicatorOpenMenu, lblIndicatorClosedMenu = Images.createMenuBar(frameMenuBar)

        frameMenuInformation = tk.Frame(frameCitybuild, width=5, background="grey")

        frameEnergyConsumption = tk.Frame(frameMenuInformation, background="grey")
        frameOverview = tk.Frame(frameMenuBar, background="grey")
        
        frameSlideValues = tk.Frame(frameMenuInformation)
        frameSlideValues.grid(column=2, row=0, sticky = "nswe", columnspan=3, rowspan=8)
        frameMenuInformation.grid_columnconfigure(1, weight=1)
        frameSlideValues.grid_rowconfigure((2,5), minsize=50)
        
        showItem = False
        showAnyItem = True
        showMenu = False
        
        roadConditions = Images.createRoadConditions()
        lblRoadCondition = tk.Label(frameMenuInformation, anchor="n", compound="left")
        lblTrafficFlow = tk.Label(frameMenuInformation, anchor="n", compound="left")
        lblPollution = tk.Label(frameMenuInformation, anchor="n", compound="left")
        
        frameSelectedItem = tk.Frame(frameMenuBar, background="grey")
        lblSolar, lblWind, lblCoal, lblNuclear, lblSubstation = Images.createEnergyIcons(frameSelectedItem, 50, 50)
        lblRoadCity, lblRoadIntercity, lblMotorway, lblParking, lblParkingLot = Images.createRoadIcons(frameSelectedItem)
        lblDivide1 = tk.Label(frameSelectedItem, width=5, background="grey", foreground="grey")
        #Blitzer einbauen

        Calculations.setupValues(frameSlideValues)
        
        return lblIndicatorOpenMenu, lblIndicatorClosedMenu
  
    def statusMenu(event, roadcondition):
        global showMenu, showItem
        padX = 5
        
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
            lblRoadMenu.bind("<Button-1>", lambda event: Upgrades.optionRoad(event, frameSelectedItem, lblRoadMenu, roadcondition))
            lblWaterMenu.bind("<Button-1>")
            lblElectricMenu.bind("<Button-1>", lambda event: Upgrades.optionElectricity(event, frameSelectedItem, lblElectricMenu))
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
        global showMenu, showItem, showAnyItem, roadConditions, lblTrafficFlow, lblRoadCondition
        Upgrades.forgetAll() 
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
            lblRoadIntercity.grid(column=1,row=0, sticky="w", padx=(5,0)) 
            lblMotorway.grid(column=2,row=0, sticky="w", padx=(5,0)) 
            lblDivide1.grid(column=3,row=0, sticky="w", padx=(5,0))
            lblParking.grid(column=4,row=0, sticky="w", padx=(5,0))
            lblParkingLot.grid(column=5,row=0, sticky="w", padx=(5,0))
            
            lblRoadCity.bind("<Button-1>") 
            lblRoadCity.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblRoadCity.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            lblRoadIntercity.bind("<Button-1>")  
            lblRoadIntercity.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblRoadIntercity.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            lblMotorway.bind("<Button-1>")  
            lblMotorway.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblMotorway.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            lblParking.bind("<Button-1>") 
            lblParking.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblParking.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            lblParkingLot.bind("<Button-1>") 
            lblParkingLot.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblParkingLot.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            
            frameSlideValues.grid_forget()
            showItem = True
        elif showItem == True:
            showAnyItem = False
            lblRoadCity.grid_forget()
            lblRoadIntercity.grid_forget()
            lblMotorway.grid_forget()
            lblDivide1.grid_forget()
            lblParking.grid_forget()
            lblParkingLot.grid_forget()
            lblRoadCondition.grid_forget()
            lblTrafficFlow.grid_forget()
            frameSelectedItem.grid_forget()
            lblRoadMenu["background"] = "#F0F0F0"
            
            frameSlideValues.grid(column=2, row=0, sticky = "nswe", columnspan=3, rowspan=8)
            showItem = False
    
    def optionElectricity(event, frameSelectedItem, lblElectricMenu):
        global showMenu, showItem, showAnyItem
        #Windkraft, Atomkraft, Kohlekraft, Solarpark, 
        Upgrades.forgetAll()
        if showItem == False:
            frameEnergyConsumption.grid(column=0,row=2) 
            frameSelectedItem.grid(column=0,row=0, columnspan=10, sticky="w")
            lblElectricMenu["background"] = "#87CEFA"
            lblSolar.grid(column=0,row=0, sticky="w") 
            lblWind.grid(column=1,row=0, sticky="w", padx=(5,0)) 
            lblCoal.grid(column=2,row=0, sticky="w", padx=(5,0)) 
            lblNuclear.grid(column=3,row=0, sticky="w", padx=(5,0))

            lblSolar.bind("<Button-1>", Upgrades.buyEnergy) 
            lblSolar.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblSolar.bind('<Leave>', lambda e: e.widget.config(bg='grey'))

            lblWind.bind("<Button-1>", Upgrades.buyEnergy) 
            lblWind.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblWind.bind('<Leave>', lambda e: e.widget.config(bg='grey')) 

            lblCoal.bind("<Button-1>", Upgrades.buyEnergy)  
            lblCoal.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblCoal.bind('<Leave>', lambda e: e.widget.config(bg='grey'))

            lblNuclear.bind("<Button-1>", Upgrades.buyEnergy) 
            lblNuclear.bind('<Enter>', lambda e: e.widget.config(bg='yellow'))
            lblNuclear.bind('<Leave>', lambda e: e.widget.config(bg='grey'))
            
            frameSlideValues.grid_forget()
            showItem = True
            Upgrades.createEnergyOverview()
        elif showItem == True:
            showAnyItem  = False
            lblSolar.grid_forget()
            lblWind.grid_forget()
            lblCoal.grid_forget()
            lblNuclear.grid_forget()
            lblRoadCondition.grid_forget()
            lblTrafficFlow.grid_forget()
            frameSelectedItem.grid_forget()
            lblElectricMenu["background"] = "#F0F0F0"
            frameSlideValues.grid(column=2, row=0, sticky = "nswe", columnspan=3, rowspan=8)
            showItem = False
    
    def buyEnergy(event):
        global levelEnergy, canvas
        if event.widget == lblSolar:
            levelEnergy[0] += 1
            funderror = Calculations.calculateEnergyLevel("Solar")
            if levelEnergy[0] == 1:
                Upgrades.energyFlow1(canvas, 0, 0, 0)
                canvas.itemconfig(lineSolar, fill= "#50ED11")
                
        elif event.widget == lblWind:
            levelEnergy[1] += 1
            funderror = Calculations.calculateEnergyLevel("Wind")
            if levelEnergy[1] == 1:
                Upgrades.energyFlow2(canvas, 0, 0, 0)
                canvas.itemconfig(lineWind, fill= "#50ED11")
                
        elif event.widget == lblCoal:
            levelEnergy[2] += 1
            funderror = Calculations.calculateEnergyLevel("Coal")
            if levelEnergy[2] == 1:
                Upgrades.energyFlow3(canvas, 0, 0, 0)
                canvas.itemconfig(lineCoal, fill= "#50ED11")
                
        elif event.widget == lblNuclear:
            levelEnergy[3] += 1
            funderror = Calculations.calculateEnergyLevel("Nuclear")
            if levelEnergy[3] == 1:
                Upgrades.energyFlow4(canvas, 0, 0, 0)
                canvas.itemconfig(lineNuclear, fill= "#50ED11")
    
    def forgetAll():
        global count, moveEnergy1
        lblRoadCity.grid_forget()
        frameEnergyConsumption.grid_forget()
        lblRoadIntercity.grid_forget()
        lblMotorway.grid_forget()
        lblDivide1.grid_forget()
        lblParking.grid_forget()
        lblParkingLot.grid_forget()
        lblRoadCondition.grid_forget()
        lblTrafficFlow.grid_forget()
        frameSelectedItem.grid_forget()
        lblSolar.grid_forget()
        lblWind.grid_forget()
        lblCoal.grid_forget()
        lblNuclear.grid_forget()
        lblRoadCondition.grid_forget()
        lblTrafficFlow.grid_forget()
        lblRoadMenu["background"] = "#F0F0F0"
        lblElectricMenu["background"] = "#F0F0F0"
        for element in range (0, len(count)):
            if moveEnergy[element] != 0:
                canvas.after_cancel(moveEnergy[element])
            count[element] = 0
    
    def createEnergyOverview():
        global frameEnergyConsumption, levelEnergy, colour, count, canvas, lineSolar, lineWind, lineCoal, lineNuclear
        frameEnergyConsumption.grid(column=0,row=2)
        lblSolar, lblWind, lblCoal, lblNuclear, lblSubstation = Images.createEnergyIcons(frameSelectedItem, 100, 100)
        
        canvas = tk.Canvas(frameEnergyConsumption, width=500, height = 300, background="blue")
        canvas.grid(column=0,row=0)
        for level in range (0,len(levelEnergy)):
            if levelEnergy[level] == 0:
                colour[level] = "grey"
            else: 
                colour[level] = "#50ED11"

        lineSolar = canvas.create_line(65,185,210,235, fill=colour[0], width=5)
        lineWind = canvas.create_line(70,290,210,235, fill=colour[1], width=5)
        lineCoal = canvas.create_line(440,180,295,235, fill=colour[2], width=5)
        lineNuclear = canvas.create_line(440,290,295,235, fill=colour[3], width=5)
        
        if levelEnergy[0] != 0:
            Upgrades.energyFlow1(canvas, 0, 0, 0)
        if levelEnergy[1] != 0:
            Upgrades.energyFlow2(canvas, 0, 0, 0)
        if levelEnergy[2] != 0:
            Upgrades.energyFlow3(canvas, 0, 0, 0)
        if levelEnergy[3] != 0:
            Upgrades.energyFlow4(canvas, 0, 0, 0)
        
        SolarImage = canvas.create_image(50,150,image= lblSolar.image)
        WindImage = canvas.create_image(50,250,image= lblWind.image)
        CoalImage = canvas.create_image(450,150,image= lblCoal.image)
        NuclearImage = canvas.create_image(450,250,image= lblNuclear.image)
        SubstationImage = canvas.create_image(250,200,image= lblSubstation.image)
    
    def energyFlow1(canvas, Oval1, Oval2, Oval3):
        global count, moveEnergy
        count[0] += 1
        moveXSolar = (210-65) / 10
        moveYSolar = (230-180) / 10
        
        if count[0] == 1:
            Oval1 = canvas.create_oval(65,180,75,190, fill="yellow", width=3)
        if count[0] == 4:
            Oval2 = canvas.create_oval(65,180,75,190, fill="yellow", width=3)
        if count[0] == 7:
            Oval3 = canvas.create_oval(65,180,75,190, fill="yellow", width=3)


        if count[0] <= 10:   
            moveEnergy[0] = canvas.after(100, lambda: [canvas.move(Oval1, moveXSolar, moveYSolar), 
                                                       canvas.move(Oval2, moveXSolar, moveYSolar),
                                                       canvas.move(Oval3, moveXSolar, moveYSolar),
                                                       Upgrades.energyFlow1(canvas, Oval1, Oval2, Oval3)]) 
        if count[0] == 11:
            count[0] = 0
            canvas.move(Oval1, 210, 230)
            canvas.after(300, lambda: canvas.move(Oval2, 210, 230))
            canvas.after(600, lambda: canvas.move(Oval3, 210, 230))
            Upgrades.energyFlow1(canvas, Oval1, Oval2, Oval3)
            
    def energyFlow2(canvas, Oval1, Oval2, Oval3):
        global count, moveEnergy
        count[1] += 1
        moveXSolar = (210-70) / 10
        moveYSolar = (230-280) / 10
        
        if count[1] == 1:
            Oval1 = canvas.create_oval(70,280,80,290, fill="yellow", width=3)
        if count[1] == 4:
            Oval2 = canvas.create_oval(70,280,80,290, fill="yellow", width=3)
        if count[1] == 7:
            Oval3 = canvas.create_oval(70,280,80,290, fill="yellow", width=3)
        
        if count[1] <= 10:   
            moveEnergy[1] = canvas.after(100, lambda: [canvas.move(Oval1, moveXSolar, moveYSolar),
                                                       canvas.move(Oval2, moveXSolar, moveYSolar),
                                                       canvas.move(Oval3, moveXSolar, moveYSolar),
                                                       Upgrades.energyFlow2(canvas, Oval1, Oval2, Oval3)]) 
        if count[1] == 11:
            count[1] = 0
            canvas.move(Oval1, 210, 230)
            canvas.after(300, lambda: canvas.move(Oval2, 210, 230))
            canvas.after(600, lambda: canvas.move(Oval3, 210, 230))
            Upgrades.energyFlow2(canvas, Oval1, Oval2, Oval3)

    def energyFlow3(canvas, Oval1, Oval2, Oval3):
        global count, moveEnergy
        count[2] += 1
        moveXSolar = (285-420) / 10
        moveYSolar = (230-180) / 10
        
        if count[2] == 1:
            Oval1 = canvas.create_oval(420,180,430,190, fill="yellow", width=3)
        if count[2] == 4:
            Oval2 = canvas.create_oval(420,180,430,190, fill="yellow", width=3)
        if count[2] == 7:
            Oval3 = canvas.create_oval(420,180,430,190, fill="yellow", width=3)
        
        if count[2] <= 10:   
            moveEnergy[2] = canvas.after(100, lambda: [canvas.move(Oval1, moveXSolar, moveYSolar), 
                                                       canvas.move(Oval2, moveXSolar, moveYSolar), 
                                                       canvas.move(Oval3, moveXSolar, moveYSolar), 
                                                       Upgrades.energyFlow3(canvas, Oval1, Oval2, Oval3)]) 
        if count[2] == 11:
            count[2] = 0
            canvas.move(Oval1, 295, 230)
            canvas.after(300, lambda: canvas.move(Oval2, 210, 230))
            canvas.after(600, lambda: canvas.move(Oval3, 210, 230))
            Upgrades.energyFlow3(canvas, Oval1, Oval2, Oval3)

    def energyFlow4(canvas, Oval1, Oval2, Oval3):
        global count, moveEnergy
        count[3] += 1
        moveXSolar = (285-440) / 10
        moveYSolar = (230-290) / 10
        
        if count[3] == 1:
            Oval1 = canvas.create_oval(440,290,450,300, fill="yellow", width=3)
        if count[3] == 4:
            Oval2 = canvas.create_oval(440,290,450,300, fill="yellow", width=3)
        if count[3] == 7:
            Oval3 = canvas.create_oval(440,290,450,300, fill="yellow", width=3)
        
        if count[3] <= 10:   
            moveEnergy[3] = canvas.after(100, lambda: [canvas.move(Oval1, moveXSolar, moveYSolar), 
                                                       canvas.move(Oval2, moveXSolar, moveYSolar), 
                                                       canvas.move(Oval3, moveXSolar, moveYSolar), 
                                                       Upgrades.energyFlow4(canvas, Oval1, Oval2, Oval3)]) 
        if count[3] == 11:
            count[3] = 0
            canvas.move(Oval1, 295, 225)
            canvas.after(300, lambda: canvas.move(Oval2, 210, 230))
            canvas.after(600, lambda: canvas.move(Oval3, 210, 230))
            Upgrades.energyFlow4(canvas, Oval1, Oval2, Oval3)
    
    