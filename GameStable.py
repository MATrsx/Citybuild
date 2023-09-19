"""Spielidee: Der Spieler ist der Bürgermeister einer kleinen Stadt. In seiner Position verwaltet er die Stadt,
zieht neue Bewohner und Unternehmen an und sorgt dafür dass ihre Bedürfnisse gedeckt sind. Dafür baut er neue Wohn- und
Gewerbegebiete sowie andere Infrastruktur wie Polizei, Parks etc. um die Bewohner bei Laune zu halten."""
import random 
import datetime
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
from pathlib import Path

"""Gamevariables"""
cityName = ""
balance = 0
taxes = 10
crimeRate = 0
residents = 10
maxResidents = 50
leaveCity = 0
joinCity = 0
businesses = 1
transportVehicles = 0
education = 0
entertainment = 100
stage = 1
satisfaction = 100
p1 = 10
p2 = 25
p3 = 50
p4 = 100
p5 = 250
p6 = 500
upgradePrice = [p1, p2, p3, p4, p5, p6]
lvl1 = 0
lvl2 = 0
lvl3 = 0
lvl4 = 0
lvl5 = 0
lvl6 = 0
level = [lvl1, lvl2, lvl3, lvl4, lvl5, lvl6]

"""Variables"""
incomeTime = 5000
showValues = True
showUpgrades = True
daysPlayed = 0
gameEnd = False
listBuildings = ["Einwohner", "Unternehmen", "ÖPNV", "Bildung", "Unterhaltung", ""]
savegames = 0
saveGames = [0,0,0,0]
frist = 0
eventNow = False
parkCost = (residents * taxes + businesses * (1.5 *taxes)) * 5 
unterhaltung = 0
Bildung = level[4] / residents * 100
matchday = 7
educatedpeople = 0
basePath = Path(__file__).parent

def addValues():
    global incomeTime, gameEnd, unterhaltung
    lblMoneyAdd.grid_forget()
    unterhaltung = 0
    
    if gameEnd == False:
        lblMoneyAdd.after(incomeTime, Calculate)

def calcSatisfaction():
    """Calculate all values needed for the game"""
    global residents, maxResidents, level, leaveCity, stage, satisfaction
    
    if residents >= maxResidents and stage == 1:
        satisfaction = 100
    elif residents >= maxResidents and stage == 2:
        satisfaction = 100
        
def Calculate():
    """Calculate all values needed for the game"""
    global balance, residents, maxResidents, taxes, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, \
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, gameEnd, frist, eventNow, parkCost, unterhaltung, Bildung
    lvlBonus = None
    
    #Increase the day counter    
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=daysPlayed)
    now = now.strftime("%d.%m.%y")
    tomorrow = tomorrow.strftime("%d.%m.%y")
    lblDate["text"] = f"Datum: {tomorrow}"
    lblDate.grid(column=0, row=18, sticky= tk.NW)
    now = tomorrow
    daysPlayed += 1
    matchday -= 1
    
    if eventNow == False:
        lblEvent.grid_forget()

    #Add new residents and businesses
    if residents <= 25:
        rN = random.randint(0,3)
        ctzLeave = 0
        lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
        lvlBonus = int(lvlBonus)


    elif residents > 25 and residents <= 100:
        rN = random.randint(0,8) 
        ctzLeave = random.randint(0,1)
        lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
        lvlBonus = int(lvlBonus)
        
        #chance for a business to move to the city
        if random.randint(0, 100-education) == 10:
            businesses += 1
    elif residents > 100 and residents <= 1000:
        rN = random.randint(0,23)
        ctzLeave = random.randint(0,4)
        lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
        lvlBonus = int(lvlBonus)
        
        #chance for a business to move to the city
        if random.randint(0, 100-education) == 10:
            businesses += 1
    elif residents > 1000 and residents <= 10000:
        rN = random.randint(0,54)
        ctzLeave = random.randint(0,9)
        lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
        lvlBonus = int(lvlBonus)
        
        #chance for a business to move to the city
        if random.randint(0, 100-education) == 10:
            businesses += 1
    elif residents > 10000:
        rN = random.randint(0,73)
        ctzLeave = random.randint(0,16)
        lvlBonus = ((level[0]*10 + level[1]*20 + level[2]*30 + level[3]*40 + level[4]*50)  / 150)
        lvlBonus = int(lvlBonus)
        
        #chance for a business to move to the city
        if random.randint(0, 100-education) == 8:
            businesses += 1
    
    #Educationsystem
    educatedpeople = educatedpeople + level[4]
    Bildung = educatedpeople / residents * 100
    Bildung = int(Bildung)
    if Bildung > 100:
        Bildung = 100
    education = Bildung
    
    leaveCity = ctzLeave
    joinCity = rN + lvlBonus
    residents = residents + joinCity - leaveCity
    
    #Every seven days add entertainment income (Stadium Level * number of seats)
    if daysPlayed %7 == 0:
        unterhaltung = entertainment * (level[5] + 1)
    
    #Display each `Building` currently available
    lblBusinesses["text"] = f" {businesses} Unternehmen"
    lblResidents["text"] = f" {residents} Einwohner"
    if stage >= 2:
        lblTransport["text"] = f" {transportVehicles} ÖPNV Fahrzeuge"
    if stage >= 3:
        lblEducation["text"] = f" {education}% Bildung"
    if stage >= 4:
        lblEntertainment["text"] = f" {entertainment} Sitzplätze"
        if matchday >= 1:
            lblQuery["text"] = f" {matchday} Tage bis zum nächsten Spiel \n "
        else:
            lblQuery["text"] = f" Ticketeinnahmen am heutigen Spieltag: {unterhaltung}$ \n "
            matchday = 7
        lblQuery.grid(column=0, row=9, columnspan=2, padx= 15, sticky= tk.NW)
    
    #Add the income to your Total balance and display the income
    balance = balance + ((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)
    lblMoneyAdd["text"] = f"+ {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$"
    lblMoneyAdd.grid(column=4,row=3)
    
    #Update the values in the cityInformation Label, if it is opened
    if showValues == False:
        btnUpgrades.grid_forget()
        btnUpgrades.grid(column=3, row=6, sticky = tk.W)
        if stage >= 2:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5 \n"\
            f"  Steuersatz: {taxes} pro Einwohner | {taxes*1.5} pro Unternehmen \n"\
            f"  Neues Gebäude: {listBuildings[stage]}"
        else:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5" 
        
        #Display how many residents join and leave the city
        lblDamagedHouse.grid(column=2,row=4, sticky= tk.NW)
        lblresidentsLeave["text"] = f" - {leaveCity}"
        lblresidentsLeave.grid(column=2, row=4, sticky= tk.N)
        
        lblConstructing.grid(column=2,row=4, sticky= tk.SW)
        lblnewResidents["text"] = f" + {joinCity}"
        lblnewResidents.grid(column=2, row=4, sticky= tk.S)
        lblValues.grid(column=3,row=4, rowspan=2, columnspan=2, sticky= tk.W)
    
    #Update the values in the upgrades Label, if it is opened
    if showUpgrades == False:
        lblStreets["text"] = f"[Level: {level[0]}] Straßen ausbauen \n(+ Verkehrsfluss und Zufriedenheit) \n(- {upgradePrice[0]}$)"
        lblWater["text"] = f"[Level: {level[1]}] Wasserrohre bauen \n(+ Wasserversorgung und Zufriedenheit) \n(- {upgradePrice[1]}$)"
        lblEnergy["text"] = f"[Level: {level[2]}] Stromleitungen verlegen \n(+ Energieversorgung und Zufriedenheit) \n(- {upgradePrice[2]}$)"       
        lblVehicles["text"] = f"[Level: {level[3]}] Neuen Bus kaufen \n(+ Wartezeit und Zufriedenheit) \n(- {upgradePrice[3]}$)"  
        lblSchools["text"] = f"[Level: {level[4]}] Bildungsmittel kaufen \n(+ Bildung und Zufriedenheit) \n(- {upgradePrice[4]}$)"
        lblStadium["text"] = f"[Level: {level[5]}] Stadion erweitern \n(+ Sitzplätze und Einnahmen) \n(- {upgradePrice[5]}$)"
        if stage >= 2:
            lblVehicles.grid(column=3, row=10, columnspan=2, sticky = tk.W) 
            lblVehicles.bind("<Button-1>", clicked)
            lblStreets.bind("<Button-1>", clicked)
            lblWater.bind("<Button-1>", clicked)
            lblEnergy.bind("<Button-1>", clicked)
        if stage >= 3:
            lblSchools.grid(column=3, row=11, columnspan=2, sticky = tk.W) 
            lblSchools.bind("<Button-1>", clicked)
        if stage >= 4:
            lblStadium.grid(column=3, row=12, columnspan=2, sticky = tk.W)
            lblStadium.bind("<Button-1>", clicked)
            
    #Random chance for a event
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
    
    lblEnergyStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[1] * 15}"
    lblWaterStatus.grid(column=1, row=1, sticky = "nswe")
    lblWaterStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[2] * 15}"
    lblEnergyStatus.grid(column=2, row=1, sticky = "nswe")
    lblPersonStatus["text"] = f"{residents}"
    lblPersonStatus.grid(column=0, row=1, sticky = "nswe")
        
    
    #Reset the game if residents are at the limit
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
    
    #Game-Loop
    if gameEnd == False:
        lblMoneyAdd.after(incomeTime, addValues)

def events():
    global gameEnd, stage, taxes, listBuildings, balance, parkCost, frist, eventNow
    
    #Display the level up notification
    if gameEnd == True:
        lblEvent["text"] = f"Du bist nun auf Stufe {stage}, dabei hast du folgende Perks erhalten: \n"\
        f"   - Steuererhöhung: Der Steuersatz erhöht sich um von {taxes} auf \n"\
        f"   - Infrastruktur: Du hast folgende Kategorien freigeschaltet: {listBuildings[stage-1]} \n"\
        f"   - Interaktion: Du kannst nun durch zufällige Events mit deinen Bewohnern interagieren"  
        lblEvent.grid(column=0,row=11, columnspan=4)
        gameEnd = False
        lblExplain.grid_forget()
        
        lblMoneyAdd.after(incomeTime, Calculate)

    #Display event notification
    else:
        eventNow = True
        lblEvent["text"] = f"{3 - frist} Tage um eine Entscheidung zu treffen: \n"\
        "Deine Bewohner wünschen sich einen neuen Park in ihrer Nähe, \num nach einem langen Arbeitstag entspannen zu können und dort Sport zu treiben: "
        lblEventChoice1["text"] = f"[1] ZUSTIMMEN -> Einen neuen Park in der Nähe des Wohngebietes bauen \n [- {parkCost}] [+ Zufriedenheit]"
        lblEventChoice2["text"] = f"[2] ABLEHNEN -> Keinen neuen Park bauen [- Zufriedenheit]"
        lblEvent.grid(column=0, row=13, columnspan=4, sticky= tk.W)
        lblEventChoice1.grid(column=0, row=15, columnspan=4, sticky= tk.W)
        lblEventChoice2.grid(column=0, row=16, columnspan=4, sticky= tk.W)
        lblEventChoice1.bind("<Button-1>", eventCh1)
        lblEventChoice2.bind("<Button-1>", eventCh2)
        frist += 1

def eventCh1(event):
    """Choice 1 for the event notification"""
    global balance, residents, parkCost, satisfaction, eventNow, frist, showValues
    
    #Calculate changing values
    newResidents = residents * 0.05
    newResidents = int(newResidents)
    newSatisfaction = satisfaction * 0.08
    
    if newSatisfaction + satisfaction <= 100:
        satisfaction = newSatisfaction + satisfaction   
    else:
        newSatisfaction = newSatisfaction - (satisfaction - 100)
    
    if balance >= parkCost:
        balance = balance - parkCost 
        lblEvent["text"] = "Hurra, der Wunsch wurde erfüllt. Die Einwohner danken dir \n"\
            "und fühlen sich in ihrer Wahl des Bürgermeisters bestätigt!\n"\
            f"Folgende Werte haben sich durch deine Entscheidung verbessert: \n"\
            f"Zufriedenheit: +{newSatisfaction}% \n"\
            f"Einwohner: +{newResidents}"
        eventNow = False
        frist = 5
        
        #Update the values in the cityInformation Label, if it is opened 
        if showValues == False:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5 \n"\
            f"  Steuersatz: {taxes}$ pro Einwohner | {taxes*1.5}$ pro Unternehmen \n"\
            f"  Neues Gebäude: {listBuildings[stage]}"
            lblValues.grid(column=3,row=4, rowspan=2, columnspan=2, sticky= tk.W)
        
        lblEventChoice1.grid_forget()
        lblEventChoice2.grid_forget()

        #Re-enter the game loop
        addValues()
    else:
        lblEventChoice3["text"] = "Nicht genug Gutahaben vorhanden, um den Wunsch der Einwohner zu erfüllen!"
        lblEventChoice3.grid(column=0, row= 15, columnspan=4, sticky= tk.W)
    
    
def eventCh2(event):
    """Choice 2 for the event notification"""
    global residents, satisfaction, eventNow, frist

    #Calculate changing values
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
    eventNow = False
    frist = 5

    #Re-enter the game loop
    addValues()

def buyUpgrades():
    """Switch between showing/hiding the Upgrades-Tab"""
    global level, balance, upgradePrice, showUpgrades, showValues, stage
    
    #Display the upgrades screen
    if showUpgrades == True:
        lblStreets["text"] = f"[Level: {level[0]}] Straßen ausbauen \n(+ Verkehrsfluss und Zufriedenheit) \n(- {upgradePrice[0]}$)"
        lblStreets.grid(column=3, row=7, columnspan=2, sticky = tk.W)
        lblStreets.bind("<Button-1>", clicked)
        
        lblWater["text"] = f"[Level: {level[1]}] Wasserrohre bauen \n(+ Wasserversorgung und Zufriedenheit) \n(- {upgradePrice[1]}$)"
        lblWater.grid(column=3, row=8, columnspan=2, sticky = tk.W)
        lblWater.bind("<Button-1>", clicked)
        
        lblEnergy["text"] = f"[Level: {level[2]}] Stromleitungen verlegen \n(+ Energieversorgung und Zufriedenheit) \n(- {upgradePrice[2]}$)"
        lblEnergy.grid(column=3, row=9, columnspan=2, sticky = tk.W)
        lblEnergy.bind("<Button-1>", clicked)
        
        if stage >= 2:
            lblVehicles["text"] = f"[Level: {level[3]}] Neuen Bus kaufen \n(+ Wartezeit und Zufriedenheit) \n(- {upgradePrice[3]}$)"
            lblVehicles.grid(column=3, row=10, columnspan=2, sticky = tk.W)
            lblVehicles.bind("<Button-1>", clicked)
            lblTransport["text"] = f" {transportVehicles} ÖPNV Fahrzeuge"
        
        if stage >= 3:
            lblSchools["text"] = f"[Level: {level[4]}] Bildungsmittel kaufen \n(+ Bildung und Zufriedenheit) \n(- {upgradePrice[4]}$)"
            lblSchools.grid(column=3, row=11, columnspan=2, sticky = tk.W)
            lblSchools.bind("<Button-1>", clicked)
            lblEducation["text"] = f" {education}% Bildung"
            
        if stage >= 4:
            lblStadium["text"] = f"[Level: {level[5]}] Stadion erweitern \n(+ Sitzplätze und Einnahmen) \n(- {upgradePrice[5]}$)"
            lblStadium.grid(column=3, row=12, columnspan=2, sticky = tk.W)
            lblStadium.bind("<Button-1>", clicked)
            lblEntertainment["text"] = f" {entertainment} Sitzplätze"
        
        showUpgrades = False

    #Hide the upgrade screen
    elif showUpgrades == False:
        lblStreets.grid_forget()
        lblVehicles.grid_forget()
        lblWater.grid_forget()
        lblEnergy.grid_forget()
        lblSchools.grid_forget()
        lblStadium.grid_forget()
        showUpgrades = True

def clicked(event):
    """Calculate the costs for each upgrade"""
    global balance, stage, showValues, showUpgrades, transportVehicles, entertainment
    
    #Upgrade costs for the streets-upgrade
    if event.widget == lblStreets:
        if balance >= upgradePrice[0]:
            lblExplain.grid_forget()
            level[0] = level[0] + 1
            balance = balance - upgradePrice[0]
            upgradePrice[0] = upgradePrice[0] + (upgradePrice[0] / 2)
            upgradePrice[0] = int(upgradePrice[0])
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
    
    #Upgrade costs for the water-upgrade
    elif event.widget == lblWater:
        if balance >= upgradePrice[1]:
            lblExplain.grid_forget()
            level[1] = level[1] + 1
            balance = balance - upgradePrice[1]
            upgradePrice[1] = upgradePrice[1] + (upgradePrice[1] / 2)
            upgradePrice[1] = int(upgradePrice[1])
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
    
    #Upgrade costs for the energy-upgrade
    elif event.widget == lblEnergy:
        if balance >= upgradePrice[2]:
            lblExplain.grid_forget()
            level[2] = level[2] + 1
            balance = balance - upgradePrice[2]
            upgradePrice[2] = upgradePrice[2] + (upgradePrice[2] / 2)
            upgradePrice[2] = int(upgradePrice[2])
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            
    #Upgrade costs for the vehicles-upgrade
    elif event.widget == lblVehicles:
        if balance >= upgradePrice[3]:
            lblExplain.grid_forget()
            level[3] = level[3] + 1
            balance = balance - upgradePrice[3]
            upgradePrice[3] = upgradePrice[3] + (upgradePrice[3] / 2)
            upgradePrice[3] = int(upgradePrice[3])
            transportVehicles = level[3]
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
    
    #Upgrade costs for the education-upgrade
    elif event.widget == lblSchools:
        if balance >= upgradePrice[4]:
            lblExplain.grid_forget()
            level[4] = level[4] + 1
            balance = balance - upgradePrice[4]
            upgradePrice[4] = upgradePrice[4] + (upgradePrice[4] / 2)
            upgradePrice[4] = int(upgradePrice[4])
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
    
    #Upgrade costs for the entertainment-upgrade
    elif event.widget == lblStadium:
        if balance >= upgradePrice[5]:
            lblExplain.grid_forget()
            level[5] = level[5] + 1
            balance = balance - upgradePrice[5]
            upgradePrice[5] = upgradePrice[5] + (upgradePrice[5] / 2)
            upgradePrice[5] = int(upgradePrice[5])
            entertainment = entertainment + (entertainment * 0.35)
            entertainment = int(entertainment)
        else:
            lblExplain["text"] = f"Du hast nicht genug Guthaben um diese Transaktion durchzuführen"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
    showUpgrades = True
    
    #Update the values in the cityInformation Label, if it is opened 
    if showValues == False:
        if stage >= 2:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5 \n"\
            f"  Steuersatz: {taxes}$ pro Einwohner | {taxes*3}$ pro Unternehmen \n"\
            f"  Neues Gebäude: {listBuildings[stage]}"
        else:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5"
            
        lblValues.grid(column=3,row=4, rowspan=2, columnspan=2)
    buyUpgrades()

def saveGame():
    """Save the current game"""
    global cityName, savegames

    saveValues = [cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6]
    overwrite = False
    delLine = None

    #Save current game if there are less than 3 Games already saved
    with open("Savegames.txt", "r") as input:
        numLines = input.readlines()
    input.close()

    with open("Savegames.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if line starts with substring 'cityName' then don't write it in temp file
                if not line.strip("\n").startswith(cityName):
                    output.write(line)
        output.close()
    input.close()
    # replace file with original name
    os.replace('temp.txt', 'Savegames.txt') 

    if len(numLines) < 3 and balance > 0:
        with open ("Savegames.txt", "a") as svg:
            svg.write(f"{saveValues[0]};{saveValues[1]};{saveValues[2]};{saveValues[3]};{saveValues[4]};{saveValues[5]};{saveValues[6]};{saveValues[7]};{saveValues[8]};{saveValues[9]};{saveValues[10]};{saveValues[11]};"\
                    f"{saveValues[12]};{saveValues[13]};{saveValues[14]};{saveValues[15]};{saveValues[16]};{saveValues[17]};{saveValues[18]};{saveValues[19]};{saveValues[20]};{saveValues[21]};{saveValues[22]};{saveValues[23]};{saveValues[24]};;\n")
        svg.close()
    
    #Save the city name and start the game
    if balance == 0:
        cityName = entEntry.get()
        lblWelcome.grid_forget()
        Game()
        entEntry.delete(0, tk.END)
        entEntry.grid_forget()

def loadGame():
    """Load an existing game file"""
    global saveGames, save1, save2, save3

    lblExplain.grid_forget()
    a = 0

    #Open the file with the savegames
    with open("Savegames.txt", "r") as input:

        #Savegame 1
        line = input.readline()
        saveGames[a] = line 
        if line != "":
            cityList = line.split(";")   
            lblSave1["text"] = f"\nSPEICHERSTAND 1: \nStadtname: {cityList[0]} [Guthaben: {cityList[1]}] [Spieltage: {cityList[12]}]\n"
            lblSave1.grid(column=0, row=6, columnspan=3, sticky= tk.W)
            save1 = line.split(";")
            lblSave1.bind("<Button-1>", load)
            a += 1
        else:
            lblSave1["text"] = "SPEICHERSTAND 1: \nSpeicherstand nicht belegt!\n"
            lblSave1.grid(column=0, row=6, columnspan=3, sticky= tk.W)

        #Savegame 2
        line = input.readline()
        saveGames[a] = line 
        if line != "":
            cityList = line.split(";")   
            lblSave2["text"] = f"SPEICHERSTAND 2: \nStadtname: {cityList[0]} [Guthaben: {cityList[1]}] [Spieltage: {cityList[12]}]\n"
            lblSave2.grid(column=0, row=7, columnspan=3, sticky= tk.W)
            lblSave2.bind("<Button-1>", load)
            save2 = line.split(";")
            a += 1
        else:
            lblSave2["text"] = "SPEICHERSTAND 2: \nSpeicherstand nicht belegt!\n"
            lblSave2.grid(column=0, row=7, columnspan=3, sticky= tk.W)

        #Savegame 3
        line = input.readline()
        saveGames[a] = line 
        if line != "":
            cityList = line.split(";")   
            lblSave3["text"] = f"SPEICHERSTAND 3: \nStadtname: {cityList[0]} [Guthaben: {cityList[1]}] [Spieltage: {cityList[12]}]"
            lblSave3.grid(column=0, row=8, columnspan=3, sticky= tk.W)
            lblSave3.bind("<Button-1>", load)
            save3 = line.split(";")
        else:
            lblSave3["text"] = "SPEICHERSTAND 3: \nSpeicherstand nicht belegt!"
            lblSave3.grid(column=0, row=8, columnspan=3, sticky= tk.W)
        
def load(event):
    """Load the requested savegame"""
    global cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, unterhaltung
    if event.widget == lblSave1:
        cityName = save1[0]  
        balance = save1[1] 
        taxes = save1[2] 
        residents = save1[3] 
        maxResidents = save1[4] 
        businesses = save1[5] 
        transportVehicles = save1[6] 
        education = save1[7] 
        entertainment = save1[8] 
        stage = save1[9] 
        upgradePrice = save1[10]
        level = save1[11] 
        daysPlayed = save1[12] 
        p1 = save1[13]
        p2 = save1[14]
        p3 = save1[15]
        p4 = save1[16]
        p5 = save1[17]
        p6 = save1[18]
        lvl1 = save1[19]
        lvl2 = save1[20]
        lvl3 = save1[21]
        lvl4 = save1[22]
        lvl5 = save1[23]
        lvl6 = save1[24]
    if event.widget == lblSave2:
        cityName = save2[0]  
        balance = save2[1] 
        taxes = save2[2] 
        residents = save2[3] 
        maxResidents = save2[4] 
        businesses = save2[5] 
        transportVehicles = save2[6] 
        education = save2[7] 
        entertainment = save2[8] 
        stage = save2[9] 
        upgradePrice = save2[10]
        level = save2[11] 
        daysPlayed = save2[12] 
        p1 = save2[13]
        p2 = save2[14]
        p3 = save2[15]
        p4 = save2[16]
        p5 = save2[17]
        p6 = save2[18]
        lvl1 = save2[19]
        lvl2 = save2[20]
        lvl3 = save2[21]
        lvl4 = save2[22]
        lvl5 = save2[23]
        lvl6 = save2[24]
    if event.widget == lblSave3:
        cityName = save3[0]  
        balance = save3[1] 
        taxes = save3[2] 
        residents = save3[3] 
        maxResidents = save3[4] 
        businesses = save3[5] 
        transportVehicles = save3[6] 
        education = save3[7] 
        entertainment = save3[8] 
        stage = save3[9] 
        upgradePrice = save3[10]
        level = save3[11] 
        daysPlayed = save3[12] 
        p1 = save3[13]
        p2 = save3[14]
        p3 = save3[15]
        p4 = save3[16]
        p5 = save3[17]
        p6 = save3[18]
        lvl1 = save3[19]
        lvl2 = save3[20]
        lvl3 = save3[21]
        lvl4 = save3[22]
        lvl5 = save3[23]
        lvl6 = save3[24]

    #Transform the values into the correct format
    upgradePrice = [int(p1), int(p2), int(p3), int(p4), int(p5), int(p6)]
    level = [int(lvl1), int(lvl2), int(lvl3), int(lvl4), int(lvl5), int(lvl6)]
    balance = float(balance)
    taxes = int(taxes)
    unterhaltung = int(unterhaltung)
    education = int(education)
    entertainment = int(entertainment)
    residents = int(residents)
    maxResidents = int(maxResidents)
    businesses = int(businesses)
    stage = int(stage)
    daysPlayed = daysPlayed.rstrip("\n")
    daysPlayed = int(daysPlayed)
    
    #Delete the Savelabels from the canvas
    lblSave1.grid_forget()
    lblSave2.grid_forget()
    lblSave3.grid_forget()
    btnStart.grid_forget()
    lblWelcome.grid_forget()
    lblQuery.grid_forget()
    Game()

"""
import GameStartStop
def saveGame():
    GameStartStop.saveGame(entEntry, lblWelcome, Game(), cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6)
    
def loadGame():
    global cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, unterhaltung
    cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6 = GameStartStop.loadGame(lblExplain, lblSave1, lblSave2, lblSave3, saveGames)
    Game()

def newGame():
    GameStartStop.newGame(btnClose,btnLoad, lblExplain, btnSave, btnStart, lblQuery, lblSave1, lblSave2, lblSave3, entEntry, lblWelcome)
    
def endGame():
    GameStartStop.endGame(window)
"""
    
def endGame():
    """End the game"""
    window.destroy()

def resetProgress(b1,b2,b3,b4,b5,b6,b7,b8):
    """Reset the progress for each level-up"""
    global gameEnd, balance, taxes, residents, maxResidents, businesses, stage, level, upgradePrice, transportVehicles, education, entertainment, Bildung, educatedpeople, unterhaltung

    lblEvent["text"] = "Herzlichen Glückwunsch, du bist eine Stufe aufgestiegen! \nDu kannst deinen Fortschritt zurücksetzen um neue Kategorien freizuschalten!"
    lblEvent.grid(column=0,row=11, columnspan=4)
    gameEnd = True
    
    upgradePrice = [10,25,50,100,250,500]
    level = [0,0,0,0,0,0]
    stage = stage + 1
    balance = 0
    balance = float(balance)
    taxes = 25
    residents = 10
    maxResidents = maxResidents + (maxResidents / 2)
    if stage == 5:
        maxResidents = 1000000000
    maxResidents = int(maxResidents)
    businesses = 1
    transportVehicles = 0
    education = 0
    Bildung = 0
    educatedpeople = 0
    entertainment = 100
    unterhaltung = 0
    
    #Block input
    lblStreets.unbind("<Button-1>", b1)
    lblWater.unbind("<Button-1>", b2)
    lblEnergy.unbind("<Button-1>", b3)    
    lblVehicles.unbind("<Button-1>", b4)
    lblSchools.unbind("<Button-1>", b5)
    lblSchools.unbind("<Button-1>", b6)
    btnUpgrades.unbind("<Button-1>", b7)
    btnCityInformation.unbind("<Button-1>", b8)
    lblEvent.after(5000, events)

def newGame():
    """Create a new game"""
    btnClose.grid_forget()
    btnLoad.grid_forget()
    lblExplain.grid_forget()
    btnSave.grid(column=1,row=3)
    btnStart.grid_forget()
    lblQuery.grid_forget()
    lblSave1.grid_forget()
    lblSave2.grid_forget()
    lblSave3.grid_forget()

    entEntry.bind('<Return>', lambda event=None: btnSave.invoke())
    lblWelcome.grid(column=0, row=2)
    entEntry.grid(column=0, row=3)

def values():
    """Switch between showing and hiding the cityInformationLabel"""
    global showValues, showUpgrades, residents, businesses, balance, taxes, incomeTime, stage, listBuildings

    if showValues == True:
        btnUpgrades.grid_forget()
        btnUpgrades.grid(column=3, row=6, sticky = tk.W)
        if stage >= 2:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5 \n"\
            f"  Steuersatz: {taxes}$ pro Einwohner | {taxes*3}$ pro Unternehmen \n"\
            f"  Neues Gebäude: {listBuildings[stage]}"
        else:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/500)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5"
        lblValues.grid(column=3,row=4, rowspan=2, columnspan=2, sticky= tk.W)
        
        lblDamagedHouse.grid(column=2,row=4, sticky= tk.NW)
        lblresidentsLeave["text"] = f"- {leaveCity}"
        lblresidentsLeave.grid(column=2, row=4, sticky= tk.N)
        
        lblConstructing.grid(column=2,row=4, sticky= tk.SW)
        lblnewResidents["text"] = f"+ {joinCity}"
        lblnewResidents.grid(column=2, row=4, sticky= tk.S)
        showValues = False
    elif showValues == False:
        btnUpgrades.grid_forget()
        btnUpgrades.grid(column=3, row=4, sticky = tk.W)
        lblValues.grid_forget()
        lblDamagedHouse.grid_forget()
        lblresidentsLeave.grid_forget()
        lblConstructing.grid_forget()
        lblnewResidents.grid_forget()
        showValues = True

def Game():
    """Add the widets to the canvas at the start of the game"""
    global cityName, residents, businesses
    gameEnd = False 

    lblGame["text"] = ""
    lblWelcome = tk.ttk.Label(text= f"Deine Stadt: {cityName}")
    lblWelcome.grid_forget()
    lblWelcome.grid(column=0, row=3, columnspan=2)
    lblGame.grid(column=0, row=4, rowspan=2)
    lblMoneyAdd.grid(column=4, row=3)
    btnLoad.grid(column=0, row=2)
    btnClose.grid(column=2, row=2, sticky = tk.W)
    btnSave.grid(column=1, row=2)
    btnCityInformation.grid(column=3,row=3, sticky = tk.W)
    btnUpgrades.grid(column=3, row=4, sticky = tk.NW)
    
    #Add Images to the canvas
    createImages()
    
    #Enter the game-loop
    Calculate()

def createImages():
    """Create and add the images to the canvas"""
    imageHouse = Image.open(basePath / "Images" / "house.png")
    houseSized = imageHouse.resize((50,50))
    house = ImageTk.PhotoImage(houseSized)
    lblHouse = tk.Label(window, image = house)
    lblHouse.image = house
    lblHouse.grid(column=0,row=4)
    lblResidents.grid(column=1,row=4, sticky= tk.W)
    
    imageFactory = Image.open(basePath / "Images" / "factory.png")
    factorySized = imageFactory.resize((50,50))
    factory = ImageTk.PhotoImage(factorySized)
    lblFactory = tk.Label(window, image = factory)
    lblFactory.image = factory
    lblFactory.grid(column=0,row=5)
    lblBusinesses.grid(column=1,row=5, sticky= tk.W)
    
    imageTransport = Image.open(basePath / "Images" / "station.png")
    transportSized = imageTransport.resize((50,50))
    transport = ImageTk.PhotoImage(transportSized)
    lblStation = tk.Label(window, image = transport)
    lblStation.image = transport
    lblStation.grid(column=0,row=6)
    lblTransport.grid(column=1, row=6, sticky= tk.W)
    
    imageEducation = Image.open(basePath / "Images" / "school.png")
    educationSized = imageEducation.resize((50,50))
    educationP = ImageTk.PhotoImage(educationSized)
    lblSchool = tk.Label(window, image = educationP)
    lblSchool.image = educationP
    lblSchool.grid(column=0,row=7)
    lblEducation.grid(column=1, row=7, sticky= tk.W)
    
    imageEntertainment = Image.open(basePath / "Images" / "stadium.png")
    entertainmentSized = imageEntertainment.resize((50,50))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadium = tk.Label(window, image = entertainmentP)
    lblStadium.image = entertainmentP
    lblStadium.grid(column=0,row=8)
    lblEntertainment.grid(column=1, row=8, sticky= tk.W)
    
    imageCalendar = Image.open(basePath / "Images" / "calendar.png")
    calendarSized = imageCalendar.resize((50,50))
    calendarP = ImageTk.PhotoImage(calendarSized)
    lblCalendar = tk.Label(window, image = calendarP)
    lblCalendar.image = calendarP
    lblCalendar.grid(column=0,row=17)
    
    imageLightning = Image.open(basePath / "Images" / "zap.png")
    lightningSized = imageLightning.resize((50,50))
    lightningP = ImageTk.PhotoImage(lightningSized)
    lblLightning = tk.Label(frameEnergy, image = lightningP)
    lblLightning.image = lightningP
    lblLightning.grid(column=8,row=0)
    
    imageWater = Image.open(basePath / "Images" / "droplet.png")
    waterSized = imageWater.resize((50,50))
    waterP = ImageTk.PhotoImage(waterSized)
    lblWater = tk.Label(frameWater, image = waterP)
    lblWater.image = waterP
    lblWater.grid(column=7,row=0)
    
    imagePerson = Image.open(basePath / "Images" / "person.png")
    personSized = imagePerson .resize((50,50))
    personP = ImageTk.PhotoImage(personSized)
    lblPerson = tk.Label(framePerson, image = personP)
    lblPerson.image = personP
    lblPerson.grid(column=7,row=0)
    
    imageMoney = Image.open(basePath / "Images" / "dollar.png")
    moneySized = imageMoney.resize((50,50))
    moneyP = ImageTk.PhotoImage(moneySized)
    lblMoney = tk.Label(frameMoney, image = moneyP)
    lblMoney.image = moneyP
    lblMoney.grid(column=9,row=0)
    
    

window = tk.Tk()
window.title("Builtopia")
window.resizable(width=False, height=False)

frameMoney = tk.Frame(window)
frameMoney.grid(column=3, row=0, sticky = "nswe", rowspan=2)
lblMoneyStatus = ttk.Label(frameMoney, text= "", anchor= "ne")
lblMoneyStatus.grid(column=3, row=1, sticky = "nswe")

frameEnergy = tk.Frame(window)
frameEnergy.grid(column=2, row=0, sticky = "nswe", rowspan=2)
lblEnergyStatus = ttk.Label(frameEnergy, text= "", anchor= "ne")
lblEnergyStatus.grid(column=2, row=1, sticky = "nswe")

frameWater = tk.Frame(window)
frameWater.grid(column=1, row=0, sticky = "nswe", rowspan=2)
lblWaterStatus = ttk.Label(frameWater, text= "")
lblWaterStatus.grid(column=1, row=1, sticky = "nswe")

framePerson = tk.Frame(window)
framePerson.grid(column=0, row=0, sticky = "nswe", rowspan=2)
lblPersonStatus = ttk.Label(framePerson, text= "")
lblPersonStatus.grid(column=0, row=1, sticky = "nswe")

lblQuery = ttk.Label(text = "Herzlich Willkommen beim Spiel Builtopia")
lblQuery.grid(column=0,row=0,columnspan=4)

lblSave1 = ttk.Label(text = "")

lblSave2 = ttk.Label(text = "")

lblSave3 = ttk.Label(text = "")

lblEvent = ttk.Label(text = " ")

lblValues = ttk.Label(text= "")

lblWelcome = ttk.Label(text="Willkommen in Builtopia \nBitte gib den Namen deiner neuen Stadt ein: ")

lblExplain = ttk.Label(text="Das Spielprinzip ist einfach. Du bist der Bürgermeister deiner eigenen Stadt. \n"
                            "Deine Stadt ist zunächst kaum bewohnt und unattraktiv für große Unternehmen, \n"
                            "sobald dein level aber hoch genug ist, kannst du deine Stadt von neu aufbauen \n"
                            "um so neue Gebäude freizuschalten")
lblExplain.grid(column=0, row=2, columnspan=4)

lblDate = ttk.Label(text=" ")

lblGame = ttk.Label(text = " ")

lblMoneyAdd = ttk.Label(text= " ")

lblResidents = ttk.Label(text= f" {residents} Einwohner")

lblBusinesses = ttk.Label(text= f" {businesses} Unternehmen")

lblEntertainment = ttk.Label(text= "")

lblEducation = ttk.Label(text= "")

lblTransport = ttk.Label(text= "")

lblSchools = ttk.Label(text= "")

lblresidentsLeave = ttk.Label(text= "")

lblnewResidents = ttk.Label(text= "")

lblUpgrades = ttk.Label(text= "")

lblStreets = ttk.Label(text= "")
                       
lblEnergy = ttk.Label(text= "")

lblWater = ttk.Label(text= "")

lblVehicles = ttk.Label(text= "")

lblSchools = ttk.Label(text= "")

lblStadium = ttk.Label(text= "")

lblEventChoice1 = ttk.Label(text= "")
lblEventChoice2 = ttk.Label(text= "")
lblEventChoice3 = ttk.Label(text= "")

entEntry = ttk.Entry()

btnSave = ttk.Button(master=window, text="Speichern", command=saveGame)

btnStart = ttk.Button(master=window, text="Neues Spiel", command=newGame)
btnStart.grid(column=0, row=1)

btnLoad = ttk.Button(master=window, text="Spiel laden", command=loadGame)
btnLoad.grid(column=1, row=1)

btnClose = ttk.Button(master=window, text="Beenden", command=endGame)
btnClose.grid(column=2, row=1)

btnUpgrades = ttk.Button(master=window, text="Upgrades", command=buyUpgrades)

btnCityInformation = ttk.Button(master=window, text="Zeige Werte", command=values)

imageResidentsLeave = Image.open(basePath / "Images" / "derelict_house_building.png")
residentsLeaveSized = imageResidentsLeave.resize((25,25))
residentsLeave = ImageTk.PhotoImage(residentsLeaveSized)
lblDamagedHouse = tk.Label(window, image = residentsLeave)
lblDamagedHouse.image = residentsLeave

imageNewHouse = Image.open(basePath / "Images" / "building_construction.png")
newHouseSized = imageNewHouse .resize((25,25))
newHouse = ImageTk.PhotoImage(newHouseSized)
lblConstructing = tk.Label(window, image = newHouse)
lblConstructing.image = newHouse

window.mainloop()