import random 
import datetime
import tkinter as tk
import tkinter.ttk as ttk
import Satisfaction, Images, Update, TimeControls, Weather
start = False
criminalResidents = 0
injuredResidents = []
lvl2 = 0
lvl3_1 = 0
lvl3_2 = 0
lvl4_1 = 0
lvl4_2 = 0

def Calculate(balance, residents, maxResidents, taxes, crimerate, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, daysNoEnergy, daysNoWater, 
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, showValues, frist, eventNow, parkCost, unterhaltung, Bildung, blinking, satisfaction, 
    lblDate, lblEvent, level, lblFactories, lblOffices, lblResidents, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, lblPolice, lblFire, lblMedical, lblQuery, lblMoneyAdd, frameSatisfaction, frameCitybuild, btnUpgrades, lblValues, upgradePrice, 
    lblStreets, lblWater, incomeTime, lblVehicles, lblEnergy, lblSchools, lblStadium, clicked, events, lblresidentsLeave, lblnewResidents, lblEventChoice1, lblEventChoice2, lblEventChoice3, lblEnergyStatus, 
    lblWaterStatus, lblWeatherStatus, lblPersonStatus, lblMoneyStatus, lblSatisfactionStatus,blinkRed, resetProgress, btnCityInformation, pad1, pad2, pad3, pad4, pad5, lblConstructing, lblDamagedHouse, frameWeather, lblExplain,
    lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2, roadcondition):
    """Calculate all values needed for the game"""
    lvlBonus = None
    global start, criminalResidents, injuredResidents, lvl2, lvl3_1, lvl3_2, lvl4_1, lvl4_2
    
    #Remove event after finishing
    if eventNow == False:
        lblEvent.grid_forget()

    #Add new residents and businesses
    cumWeights = []
    probabilityJoin = []
    probabilityLeave = []
    max = int(residents/4)
    maxLeave = int(residents/6)
    for resident in range (1, max):
        cumWeights.append(resident*2)
        probabilityJoin.append(max - resident)
        if residents >= 100 or satisfaction <= 20:
            probabilityLeave.append(maxLeave - resident)
                    
    rN = random.choices(probabilityJoin, weights=cumWeights, k=1) 
    print(cumWeights)
    print(probabilityJoin)
    print(probabilityLeave)
    rN = int(rN[0] * satisfaction / 100)
    print(rN)
    if residents >= 100 or satisfaction <= 20:
        ctzLeave = random.choices(probabilityLeave, weights=cumWeights, k=1) 
        ctzLeave = ctzLeave[0] * -1
    else:
        ctzLeave = 0
    lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
    lvlBonus = int(lvlBonus)
      
    #Join/Leave Residents
    leaveCity = ctzLeave + int(random.randint(0, ctzLeave*(taxes-10)))
    if leaveCity < 0:
        leaveCity = 0
    joinCity = rN + lvlBonus + int(random.randint(0, rN*(taxes-10)))
    residents = residents + joinCity - leaveCity
    if residents < 0:
        residents = 0
    
    #Calculate department store revenue
    storeRevenue = 0
    customersDaily = residents/2 + random.randint(int((-1*(residents/4))), int((residents/4)))
    for customer in range (int(customersDaily)):
        moneyPerCustomer = random.randint(1,100) * 0.17
        storeRevenue += moneyPerCustomer 
    storeRevenue = int(storeRevenue)
    
    #Berechnen der Kriminalitätsrate
    crimerate = 0
    for einwohner in range (residents-criminalResidents):
        if random.randint(1,20) == 5:
            criminalResidents += 1
        elif random.randint(1,20) > 15:
            criminalResidents - 0.5
    crimerate = round(criminalResidents/residents * 100, 1)
    
    #Berechne die Bettenkapazität
    capacity = 100
    for einwohner in range (residents-len(injuredResidents)):
        if random.randint(1,20) == 5:
            injuredResidents.append(random.randint(1,5))
    
    x = 0
    for einwohner in range (len(injuredResidents) - 1):
        injuredResidents[x] -= 1
        if injuredResidents[x] == 0:
            del injuredResidents[x]
            x -= 1
        x += 1
            
    capacity = capacity - len(injuredResidents)
    
    #Display each `Building` currently available
    lblFactories["text"] = f" {businesses} Fabriken"
    lblOffices["text"] = f" {businesses} Bürogebäude"
    lblResidents["text"] = f" {residents} Einwohner"
    if stage >= 2:
        lblTransport["text"] = f" {transportVehicles} ÖPNV Fahrzeuge"
    if stage >= 3:
        lblEducation["text"] = f" {education}% Bildung"
    if stage >= 4:
        lblEntertainment["text"] = f" {entertainment} Sitzplätze"
        if matchday >= 2:
            unterhaltung = 0
            lblQuery["text"] = f" {matchday} Tage bis zum nächsten Spiel \n "
        elif matchday == 1:
            lblQuery["text"] = f" {matchday} Tag bis zum nächsten Spiel \n "
        else:
            unterhaltung = entertainment * (level[5] + 1)
            lblQuery["text"] = f" Ticketeinnahmen am heutigen Spieltag: {unterhaltung}$ \n "
            matchday = 7
        lblQuery.grid(column=0, row=9, columnspan=3, padx= 15, sticky= tk.NW)
    if stage >= 4:
        lblShopping["text"] = f"{storeRevenue}$ Einnahmen \n \n{int(customersDaily)} Kunden"
        lblGarbage["text"] = f"8 Tonnen Müll"
        lblPolice["text"] = f"{crimerate}% Kriminalität"
        lblFire["text"] = f"3/5 Löscheinsätze"
        lblMedical["text"] = f"{capacity}% Bettenkapazität"

    #Display the Stadium
    if level[5] == 11 and lvl2 == False:
        lvl2 = True
        lblStadiumLvl2.grid(column=0,row=8)
    if level[5] == 16 and lvl2 == True:
        lvl2 = False
        lvl3_1 = True
        lblStadiumLvl3_1.grid(column=0,row=8)
    if level[5] == 21 and lvl3_1 == True:
        lvl3_1 = False
        lvl3_2 = True
        lblStadiumLvl3_2.grid(column=0,row=8)
    if level[5] == 24 and lvl3_2 == True:
        lvl3_2 = False
        lvl4_1 = True
        lblStadiumLvl4_1.grid(column=0,row=8)
    if level[5] == 27 and lvl4_1 == True:
        lvl4_1 = False
        lvl4_2 = True
        lblStadiumLvl4_2.grid(column=0,row=8)
    
    #Add the income to your total balance and display the income
    taxesResidents, taxesBusinesses = getCurrentTaxes()
    balance = balance + ((residents * taxesResidents + businesses * taxesBusinesses) + unterhaltung)
    lblMoneyAdd["text"] = f"+ {((residents * taxesResidents + businesses * taxesBusinesses) + unterhaltung)}$"
    
    #Chance for a business to move to the city
    chance = int(100 - education + ((taxesBusinesses - 19) * - 0.49))
    if random.randint(0, chance) == 0:
        businesses += 1
    
    #Increase the day counter  
    if start == False:  
        start = True
        lblMoneyAdd.grid(column=3,row=2, sticky= "nw", padx= 25)
        daysPlayed = TimeControls.addIngameDays(daysPlayed, lblDate, lblMoneyAdd)
    matchday -= 1
        
    #Calculate residents satisfaction
    daysNoEnergy, daysNoWater, satisfaction = Satisfaction.calculateSatisfaction(satisfaction, stage, level, residents, businesses, daysNoEnergy, daysNoWater, frameSatisfaction, taxesResidents)
    
    #Get current weather conditions
    Weather.displayCurrentWeather(daysPlayed, frameWeather, frameCitybuild, lblWeatherStatus)
    
    #Educationsystem
    if educatedpeople <= residents:
        educatedpeople = educatedpeople + level[4] * 2 # (* 5 als Platzhalter)
        Bildung = educatedpeople / residents * 100
        Bildung = int(Bildung)
        if Bildung > 100:
            Bildung = 100
            educatedpeople = residents
        education = Bildung
    
    #Update the values in the cityInformation Label, if it is opened
    if showValues == False:
        showValues = True
        print(showUpgrades)
        Update.UpdateCityInfLabel(showValues, btnUpgrades, stage, lblValues, residents, maxResidents, balance, taxes, businesses, listBuildings, unterhaltung, incomeTime, lblDamagedHouse, 
                                  lblresidentsLeave, leaveCity, joinCity, lblConstructing, lblnewResidents, lblStreets, lblWater, lblEnergy, lblVehicles, lblSchools, lblStadium, showUpgrades, lblExplain)
        showValues = False

    #Update the values in the upgrades Label, if it is opened
    if showUpgrades == False:
        lblStreets["text"] = f"[Level: {level[0]}] Straßen ausbauen \n(+ Verkehrsfluss und Zufriedenheit) \n(- {upgradePrice[0]}$)" 
        lblWater["text"] = f"[Level: {level[1]}] Wasserrohre bauen \n(+ Wasserversorgung und Zufriedenheit) \n(- {upgradePrice[1]}$)"
        lblEnergy["text"] = f"[Level: {level[2]}] Stromleitungen verlegen \n(+ Energieversorgung und Zufriedenheit) \n(- {upgradePrice[2]}$)"       
        lblVehicles["text"] = f"[Level: {level[3]}] Neuen Bus kaufen \n(+ Wartezeit und Zufriedenheit) \n(- {upgradePrice[3]}$)"  
        lblSchools["text"] = f"[Level: {level[4]}] Bildungsmittel kaufen \n(+ Bildung und Zufriedenheit) \n(- {upgradePrice[4]}$)"
        lblStadium["text"] = f"[Level: {level[5]}] Stadion erweitern \n(+ Sitzplätze und Einnahmen) \n(- {upgradePrice[5]}$)"
        if stage >= 2:
            lblVehicles.grid(column=3, row=8, columnspan=2, sticky = tk.W) 
            lblVehicles.bind("<Button-1>", clicked)
            lblStreets.bind("<Button-1>", clicked)
            lblWater.bind("<Button-1>", clicked)
            lblEnergy.bind("<Button-1>", clicked)
        if stage >= 3:
            lblSchools.grid(column=3, row=9, columnspan=2, sticky = tk.W) 
            lblSchools.bind("<Button-1>", clicked)
        if stage >= 4:
            lblStadium.grid(column=3, row=10, columnspan=2, sticky = tk.W)
            lblStadium.bind("<Button-1>", clicked)
    
    #Calculate road condition
    if TimeControls.daysPlayedLocal %10 == 0:
        roadcondition = roadcondition-1
    print(roadcondition)
    
    #Calculate traffic flow
    
    
    #Random chance for a event
    """
    if stage >= 2:
        rdmnEvent = random.randint(1, 20)
        if rdmnEvent == 1 and eventNow == False:
            parkCost = (residents * taxes + businesses * (1.5 *taxes)) * 5 
            lblEvent.after(0, events)
        elif frist < 4 and eventNow == True:
            lblEvent.after(0, events)
        elif frist == 4 and eventNow == True:
            newSatisfaction = satisfaction * 0.08
            lostResidents = residents * 0.03
            
            lostResidents = int(lostResidents)
            
            lblEvent["text"] = "Oh nein, der Wunsch der Bürger wurde nicht erfüllt! \n"\
                "Die Bürger fühlen sich von dir im Stich gelassen!\n"\
                f"Folgende Werte haben sich durch deine Entscheidung verschlechtert: \n"\
                f"Zufriedenheit: -{newSatisfaction}% \n"\
                f"Einwohner: -{lostResidents}"
            lblEventChoice1.grid_forget()  
            lblEventChoice2.grid_forget()
            frist += 1
        elif frist == 5:
            lblEvent.grid_forget()
            lblEventChoice1.grid_forget()
            lblEventChoice2.grid_forget()
            lblEventChoice3.grid_forget()
            frist = 0
            eventNow = False
    """
    lblEnergyStatus["text"] = f"{residents + businesses * 3 + level[5] * 5} / {level[2] * 15}"
    lblWaterStatus["text"] = f"{residents + businesses * 2 + level[5] * 3} / {level[1] * 15}"
    lblPersonStatus["text"] = f"{residents}"
    lblMoneyStatus["text"] = f"{balance}$"
    lblSatisfactionStatus["text"] = f"{satisfaction}%"
    lblPersonStatus.grid(column=0, row=1, sticky = "nswe", padx=pad1)
    lblWaterStatus.grid(column=1, row=1, sticky = "nswe", padx=pad2)
    lblEnergyStatus.grid(column=2, row=1, sticky = "nswe", padx=pad3)
    lblMoneyStatus.grid(column=3, row=1, sticky = "nswe", padx=pad4)    
    lblSatisfactionStatus.grid(column=4, row=1, sticky = "nswe", padx=pad5) 
    
    #Reset the game if residents are at the limit
    """
    if residents >= maxResidents:
        resetProgress(lblStreets.bind("<Button-1>", clicked),
                      lblWater.bind("<Button-1>", clicked),
                      lblEnergy.bind("<Button-1>", clicked),
                      lblVehicles.bind("<Button-1>", clicked),
                      lblSchools.bind("<Button-1>", clicked),
                      lblStadium.bind("<Button-1>", clicked),
                      btnUpgrades.bind("<Button-1>", clicked),
                      btnCityInformation.bind("<Button-1>", clicked)
                      )
    """    

    return balance, residents, maxResidents, taxes, crimerate, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, daysNoEnergy, daysNoWater, \
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, showValues, frist, eventNow, parkCost, unterhaltung, Bildung, blinking, satisfaction, \
    lblDate, lblEvent, level, lblFactories, lblOffices, lblResidents, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, lblPolice, lblFire, lblMedical, lblQuery, lblMoneyAdd, frameSatisfaction, frameCitybuild, btnUpgrades, lblValues, upgradePrice, \
    lblStreets, lblWater, incomeTime, lblVehicles, lblEnergy, lblSchools, lblStadium, clicked, events, lblresidentsLeave, lblnewResidents, lblEventChoice1, lblEventChoice2, lblEventChoice3, lblEnergyStatus, \
    lblWaterStatus, lblWeatherStatus, lblPersonStatus, lblMoneyStatus, lblSatisfactionStatus,blinkRed, resetProgress, btnCityInformation, pad1, pad2, pad3, pad4, pad5, lblConstructing, lblDamagedHouse, frameWeather, lblExplain, \
    lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2, roadcondition







taxProgressResidents = 0
taxSliderResidents = 0
taxProgressBusiness = 0
taxSliderBusiness = 0
lblTaxValue = 0
lblTaxValueBusiness = 0
def setupValues(frameSlideValues): 
    global taxProgressResidents, taxSliderResidents, lblTaxValue, lblTaxValueBusiness, taxSliderBusiness, taxProgressBusiness
    
    #Slider for residents taxes
    taxVar = tk.IntVar(frameSlideValues, value=10)  
    lblTaxResidents = tk.Label(frameSlideValues, text="Lohnsteuer (Einwohner)") 
    taxProgressResidents = ttk.Progressbar(
        frameSlideValues,
        orient="horizontal",
        mode="determinate",
        value=10,
        maximum=20)
    taxSliderResidents = tk.Scale(
        frameSlideValues, 
        variable=taxVar, 
        orient="horizontal", 
        from_=0, to=20,
        showvalue=0,
        command=changeTax)
    lblTaxResidents.grid(column=0, row=0)
    lblTaxValue = tk.Label(frameSlideValues, text=f"{taxSliderResidents.get()}%")
    taxProgressResidents.grid(column=0,row=1, sticky="n")
    taxSliderResidents.grid(column=0,row=2, sticky="n")
    lblTaxValue.grid(column=1,row=1, sticky="w")
    
    #Slider for Business taxes
    taxVarBusiness = tk.IntVar(frameSlideValues, value=19)   
    lblTaxBusiness = tk.Label(frameSlideValues, text="Umsatzsteuer (Gewerbe)") 
    taxProgressBusiness = ttk.Progressbar(
        frameSlideValues,
        orient="horizontal",
        mode="determinate",
        value=19,
        maximum=30)
    taxSliderBusiness = tk.Scale(
        frameSlideValues, 
        variable=taxVarBusiness, 
        orient="horizontal", 
        from_=0, to=30,
        showvalue=0,
        command=changeTax)
    lblTaxBusiness.grid(column=0, row=3)
    lblTaxValueBusiness = tk.Label(frameSlideValues, text=f"{taxSliderBusiness.get()}%")
    taxProgressBusiness.grid(column=0,row=4, sticky="n")
    taxSliderBusiness.grid(column=0,row=5, sticky="n")
    lblTaxValueBusiness.grid(column=1,row=4, sticky="w")

def changeTax(value):
    global taxProgressResidents, taxSliderResidents, lblTaxValue, lblTaxValueBusiness, taxProgressBusiness, taxSliderBusiness
    
    taxProgressResidents["value"] = taxSliderResidents.get()
    lblTaxValue["text"] = str(taxSliderResidents.get()) + "%"
    lblTaxValue.grid(column=1,row=1, sticky="w")
    taxProgressBusiness["value"] = taxSliderBusiness.get()
    lblTaxValueBusiness["text"] = str(taxSliderBusiness.get()) + "%"
    lblTaxValueBusiness.grid(column=1,row=4, sticky="w")
        
def getCurrentTaxes():
    global taxSliderResidents, taxSliderBusiness
    taxes = taxSliderResidents.get()
    taxesBusinesses = taxSliderBusiness.get()
    return taxes, taxesBusinesses
    
