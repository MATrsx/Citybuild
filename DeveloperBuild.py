"""Spielidee: Der Spieler ist der Bürgermeister einer kleinen Stadt. In seiner Position verwaltet er die Stadt,
zieht neue Bewohner und Unternehmen an und sorgt dafür dass ihre Bedürfnisse gedeckt sind. Dafür baut er neue Wohn- und
Gewerbegebiete sowie andere Infrastruktur wie Polizei, Parks etc. um die Bewohner bei Laune zu halten."""
import random 
import datetime
import time, threading
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
from pathlib import Path
import Update, Images, GameStartStop, TimeControls, Satisfaction, Calculations, test, LiveFootball, TestFile
from Upgrades import Upgrades

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
incomeTime = TimeControls.incomeTimeLocal
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
matchday = 6
educatedpeople = 0
basePath = Path(__file__).parent
blockInput = False
blinking = False
pause = False
daysNoEnergy = 0 
daysNoWater = 0
LoopID = 0
start = False
showMatch = False
timechanged = False
roadcondition = 100

def GameLoop():
    global incomeTime, gameEnd, pause, blockInput, satisfaction, LoopID, start
    blockInput = False
    if start == False:
        start = True
        checkTime()
            
    if gameEnd == False and pause == False:
        if TimeControls.currentHour == 0:
            Calculate()
            if matchday == 6:
                lblStadium = Images.getStadium()
                lblStadium.bind("<Button-1>", liveFootballMatch)
                Images.blinkStadium()
            if matchday == 5:
                lblStadium = Images.getStadium()
                lblStadium.unbind("<Button-1>") 
            LoopID = frameCitybuild.after(incomeTime, GameLoop)
        else:
            frameCitybuild.after(100, GameLoop)
                  
def checkTime():
    frameCitybuild.after(100, timeChanged)

def timeChanged():
    global incomeTime, LoopID, timechanged
    if TimeControls.incomeTimeLocal != incomeTime:
        incomeTime = TimeControls.incomeTimeLocal
        frameCitybuild.after_cancel(LoopID)
        timechanged = True
    if TimeControls.currentHour == 0 and timechanged == True:
        timechanged = False
        GameLoop()
    checkTime()
    
def Calculate():
    global balance, residents, maxResidents, taxes, crimeRate, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, daysNoEnergy, daysNoWater, \
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, showValues, frist, eventNow, parkCost, unterhaltung, Bildung, blinking, satisfaction, \
    lblDate, lblEvent, level, lblFactories, lblOffices, lblResidents, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, lblPolice, lblFire, lblMedical, lblQuery, lblMoneyAdd, frameSatisfaction, frameCitybuild, btnUpgrades, lblValues, upgradePrice, \
    lblStreets, lblWater, incomeTime, lblVehicles, lblEnergy, lblSchools, lblStadium, clicked, events, lblresidentsLeave, lblnewResidents, lblEventChoice1, lblEventChoice2, lblEventChoice3, lblEnergyStatus, \
    lblWaterStatus, lblWeatherStatus, lblPersonStatus, lblMoneyStatus, lblSatisfactionStatus, blinkRed, resetProgress, btnCityInformation, pad1, pad2, pad3, pad4, pad5, lblConstructing, lblDamagedHouse, frameWeather, lblExplain, \
    lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2, roadcondition    
    
    
    balance, residents, maxResidents, taxes, crimeRate, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, daysNoEnergy, daysNoWater, \
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, showValues, frist, eventNow, parkCost, unterhaltung, Bildung, blinking, satisfaction, \
    lblDate, lblEvent, level, lblFactories, lblOffices, lblResidents, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, lblPolice, lblFire, lblMedical, lblQuery, lblMoneyAdd, frameSatisfaction, frameCitybuild, btnUpgrades, lblValues, upgradePrice, \
    lblStreets, lblWater, incomeTime, lblVehicles, lblEnergy, lblSchools, lblStadium, clicked, events, lblresidentsLeave, lblnewResidents, lblEventChoice1, lblEventChoice2, lblEventChoice3, lblEnergyStatus, \
    lblWaterStatus, lblWeatherStatus, lblPersonStatus, lblMoneyStatus, lblSatisfactionStatus,blinkRed, resetProgress, btnCityInformation, pad1, pad2, pad3, pad4, pad5, lblConstructing, lblDamagedHouse, frameWeather, lblExplain,\
    lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2, roadcondition \
    = Calculations.Calculate(
    balance, residents, maxResidents, taxes, crimeRate, businesses, daysPlayed, education, entertainment, matchday, educatedpeople, daysNoEnergy, daysNoWater, \
    stage, gameEnd, listBuildings, transportVehicles, leaveCity, joinCity, showUpgrades, showValues, frist, eventNow, parkCost, unterhaltung, Bildung, blinking, satisfaction, \
    lblDate, lblEvent, level, lblFactories, lblOffices, lblResidents, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, lblPolice, lblFire, lblMedical, lblQuery, lblMoneyAdd, frameSatisfaction, frameCitybuild, btnUpgrades, lblValues, upgradePrice, \
    lblStreets, lblWater, incomeTime, lblVehicles, lblEnergy, lblSchools, lblStadium, clicked, events, lblresidentsLeave, lblnewResidents, lblEventChoice1, lblEventChoice2, lblEventChoice3, lblEnergyStatus, \
    lblWaterStatus, lblWeatherStatus, lblPersonStatus, lblMoneyStatus, lblSatisfactionStatus, blinkRed, resetProgress, btnCityInformation, pad1, pad2, pad3, pad4, pad5, lblConstructing, lblDamagedHouse, frameWeather, lblExplain,
    lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2, roadcondition)
    
    blinkRed()

def events():
    global gameEnd, stage, taxes, listBuildings, balance, parkCost, frist, eventNow, pause

    #Display event notification
    if eventNow == False and gameEnd == False:
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
    
    #Display the level up notification
    elif gameEnd == True:
        lblEventChoice1.grid_forget()
        lblEventChoice1.grid_forget()
        lblEvent["text"] = f"Du bist nun auf Stufe {stage}, dabei hast du folgende Perks erhalten: \n"\
        f"   - Steuererhöhung: Der Steuersatz erhöht sich um von {taxes} auf \n"\
        f"   - Infrastruktur: Du hast folgende Kategorien freigeschaltet: {listBuildings[stage-1]} \n"\
        f"   - Interaktion: Du kannst nun durch zufällige Events mit deinen Bewohnern interagieren"  
        lblEvent.grid(column=0,row=11, columnspan=4)
        gameEnd = False
        lblExplain.grid_forget()
        
        pause = True
        frameCitybuild.after(incomeTime, GameLoop)

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
            showValues = True
            Update.UpdateCityInfLabel(showValues, btnUpgrades, stage, lblValues, residents, maxResidents, balance, taxes, businesses, listBuildings, unterhaltung, incomeTime, lblDamagedHouse, 
                                  lblresidentsLeave, leaveCity, joinCity, lblConstructing, lblnewResidents, lblStreets, lblWater, lblEnergy, lblVehicles, lblSchools, lblStadium, showUpgrades, lblExplain)
            showValues = False
    
        lblEventChoice1.grid_forget()
        lblEventChoice2.grid_forget()

        #Re-enter the game loop
        GameLoop()
    else:
        lblEventChoice3["text"] = "Nicht genug Gutahaben vorhanden, \num den Wunsch der Einwohner zu erfüllen!"
        lblEventChoice3.grid(column=0, row= 15, columnspan=2, sticky= tk.W)
     
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
    GameLoop()

def buyUpgrades():
    """Switch between showing/hiding the Upgrades-Tab"""
    global level, balance, upgradePrice, showUpgrades, showValues, stage
    
    rowAdd = 0
    if showValues == False:
        rowAdd = 2
        lblStreets.grid_forget()
        lblWater.grid_forget()
        lblEnergy.grid_forget()
        lblVehicles.grid_forget()
        lblSchools.grid_forget()
        lblStadium.grid_forget()
        lblExplain.grid_forget()
    
    #Display the upgrades screen
    if showUpgrades == True:
        lblStreets["text"] = f"[Level: {level[0]}] Straßen ausbauen \n(+ Verkehrsfluss und Zufriedenheit) \n(- {upgradePrice[0]}$)"
        lblStreets.grid(column=3, row=5+rowAdd, columnspan=2, sticky = tk.W)
        lblStreets.bind("<Button-1>", clicked)
        
        lblWater["text"] = f"[Level: {level[1]}] Wasserrohre bauen \n(+ Wasserversorgung und Zufriedenheit) \n(- {upgradePrice[1]}$)"
        lblWater.grid(column=3, row=6+rowAdd, columnspan=2, sticky = tk.W)
        lblWater.bind("<Button-1>", clicked)
        
        lblEnergy["text"] = f"[Level: {level[2]}] Stromleitungen verlegen \n(+ Energieversorgung und Zufriedenheit) \n(- {upgradePrice[2]}$)"
        lblEnergy.grid(column=3, row=7+rowAdd, columnspan=2, sticky = tk.W)
        lblEnergy.bind("<Button-1>", clicked)
        
        if stage >= 2:
            lblVehicles["text"] = f"[Level: {level[3]}] Neuen Bus kaufen \n(+ Wartezeit und Zufriedenheit) \n(- {upgradePrice[3]}$)"
            lblVehicles.grid(column=3, row=8+rowAdd, columnspan=2, sticky = tk.W)
            lblVehicles.bind("<Button-1>", clicked)
            lblTransport["text"] = f" {transportVehicles} ÖPNV Fahrzeuge"
        
        if stage >= 3:
            lblSchools["text"] = f"[Level: {level[4]}] Bildungsmittel kaufen \n(+ Bildung und Zufriedenheit) \n(- {upgradePrice[4]}$)"
            lblSchools.grid(column=3, row=9+rowAdd, columnspan=2, sticky = tk.W)
            lblSchools.bind("<Button-1>", clicked)
            lblEducation["text"] = f" {education}% Bildung"
            
        if stage >= 4:
            lblStadium["text"] = f"[Level: {level[5]}] Stadion erweitern \n(+ Sitzplätze und Einnahmen) \n(- {upgradePrice[5]}$)"
            lblStadium.grid(column=3, row=10+rowAdd, columnspan=2, sticky = tk.W)
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
        lblExplain.grid_forget()
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
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
    
    #Upgrade costs for the water-upgrade
    elif event.widget == lblWater:
        if balance >= upgradePrice[1]:
            lblExplain.grid_forget()
            level[1] = level[1] + 1
            balance = balance - upgradePrice[1]
            upgradePrice[1] = upgradePrice[1] + (upgradePrice[1] / 2)
            upgradePrice[1] = int(upgradePrice[1])
        else:
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
    
    #Upgrade costs for the energy-upgrade
    elif event.widget == lblEnergy:
        if balance >= upgradePrice[2]:
            lblExplain.grid_forget()
            level[2] = level[2] + 1
            balance = balance - upgradePrice[2]
            upgradePrice[2] = upgradePrice[2] + (upgradePrice[2] / 2)
            upgradePrice[2] = int(upgradePrice[2])
        else:
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
            
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
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
    
    #Upgrade costs for the education-upgrade
    elif event.widget == lblSchools:
        if balance >= upgradePrice[4]:
            lblExplain.grid_forget()
            level[4] = level[4] + 1
            balance = balance - upgradePrice[4]
            upgradePrice[4] = upgradePrice[4] + (upgradePrice[4] / 2)
            upgradePrice[4] = int(upgradePrice[4])
        else:
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
    
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
            lblExplain["text"] = f"Nicht genug Guthaben, \num diese Transaktion durchzuführen!"
            lblExplain.grid(column=3, row=14, columnspan=2, sticky = tk.W)
            Images.insufficientFunds(lblMoneyStatus, 0)
    showUpgrades = True
    
    lblExplain.after(5000, lambda: lblExplain.grid_forget())
    
    #Update the values in the cityInformation Label, if it is opened 
    if showValues == False:
        showValues = True
        Update.UpdateCityInfLabel(showValues, btnUpgrades, stage, lblValues, residents, maxResidents, balance, taxes, businesses, listBuildings, unterhaltung, incomeTime, lblDamagedHouse, 
                                  lblresidentsLeave, leaveCity, joinCity, lblConstructing, lblnewResidents, lblStreets, lblWater, lblEnergy, lblVehicles, lblSchools, lblStadium, showUpgrades, lblExplain)
        showValues = False
        
    Update.UpdateStatusBar(lblPersonStatus, lblWaterStatus, lblEnergyStatus, lblMoneyStatus, residents, balance, businesses, level, pad1, pad2, pad3, pad4)   
    buyUpgrades()

def resetProgress(b1,b2,b3,b4,b5,b6,b7,b8):
    """Reset the progress for each level-up"""
    global gameEnd, balance, taxes, residents, maxResidents, businesses, stage, level, upgradePrice, transportVehicles, education, entertainment, Bildung, educatedpeople, unterhaltung, blockInput

    lblEvent["text"] = "Herzlichen Glückwunsch, du bist eine Stufe aufgestiegen! \nDu kannst deinen Fortschritt zurücksetzen um neue Kategorien freizuschalten!"
    lblEvent.grid(column=0,row=11, columnspan=4)
    gameEnd = True
    TimeControls.pauseGame()
    
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
    blockInput = True
    lblStreets.unbind("<Button-1>", b1)
    lblWater.unbind("<Button-1>", b2)
    lblEnergy.unbind("<Button-1>", b3)    
    lblVehicles.unbind("<Button-1>", b4)
    lblSchools.unbind("<Button-1>", b5)
    lblStadium.unbind("<Button-1>", b6)
    btnUpgrades.unbind("<Button-1>", b7)
    btnCityInformation.unbind("<Button-1>", b8)
    Images.blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput)
    frameCitybuild.after(5000, events)

def values():
    """Switch between showing and hiding the cityInformationLabel"""
    global showValues, showUpgrades, residents, businesses, balance, taxes, incomeTime, stage, listBuildings
    print(showUpgrades)

    if showValues == True:
        btnUpgrades.grid_forget()
        btnUpgrades.grid(column=3, row=6, sticky = tk.W)
        if showUpgrades == False:
            lblStreets.grid_forget()
            lblVehicles.grid_forget()
            lblWater.grid_forget()
            lblEnergy.grid_forget()
            lblSchools.grid_forget()
            lblStadium.grid_forget()
            lblExplain.grid_forget()
            lblStreets.grid(column=3, row=7, sticky = tk.W)
            lblWater.grid(column=3, row=8, sticky = tk.W)
            lblEnergy.grid(column=3, row=9, sticky = tk.W)  
            if stage >= 2: 
                lblVehicles.grid(column=3, row=10, sticky = tk.W)
            if stage >=3:
                lblSchools.grid(column=3, row=11, sticky = tk.W)
            if stage >= 4:
                lblStadium.grid(column=3, row=12, sticky = tk.W)
        if stage >= 2:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/1000)} Sekunden \n"\
            f"Entwicklungsstufe: {stage} von 5 \n"\
            f"  Steuersatz: {taxes}$ pro Einwohner | {taxes*3}$ pro Unternehmen \n"\
            f"  Neues Gebäude: {listBuildings[stage]}"
        else:
            lblValues["text"] = f"Dies sind die aktuellen Statistiken: \nEinwohnerzahl: {residents} / {maxResidents} \n"\
            f"Guthaben: {balance}$ \nEinkommen: {((residents * taxes + businesses * (1.5 *taxes)) + unterhaltung)}$ pro {int(incomeTime/1000)} Sekunden \n"\
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
        lblStreets.grid_forget()
        lblVehicles.grid_forget()
        lblWater.grid_forget()
        lblEnergy.grid_forget()
        lblSchools.grid_forget()
        lblStadium.grid_forget()
        if showUpgrades == False:
            lblStreets.grid(column=3, row=5, sticky = tk.W)
            lblWater.grid(column=3, row=6, sticky = tk.W)
            lblEnergy.grid(column=3, row=7, sticky = tk.W)  
            if stage >= 2: 
                lblVehicles.grid(column=3, row=8, sticky = tk.W)
            if stage >=3:
                lblSchools.grid(column=3, row=9, sticky = tk.W)
            if stage >= 4:
                lblStadium.grid(column=3, row=10, sticky = tk.W)
        lblValues.grid_forget()
        lblDamagedHouse.grid_forget()
        lblresidentsLeave.grid_forget()
        lblConstructing.grid_forget()
        lblnewResidents.grid_forget()
        btnUpgrades.grid(column=3, row=4, sticky = tk.W)
        showValues = True

lblLightning = 0 
lblWaterdrop = 0
lblPerson = 0
lblMoney = 0
lblPlay = 0
lblPause = 0
lblFF2x = 0
lblFF3x = 0
loadID = 0
lblFactory = 0 
lblOffice = 0
lblPoliceStation = 0
lblFireDepartment = 0 
lblHospital = 0
lblStadiumLvl1 = 0
lblStadiumLvl2 = 0 
lblStadiumLvl3_1 = 0 
lblStadiumLvl3_2 = 0
lblStadiumLvl4_1 = 0 
lblStadiumLvl4_2 = 0
lblRoadMenu = 0 
lblWaterMenu = 0 
lblElectricMenu = 0 
lblWasteMenu = 0 
lblEducationMenu = 0 
lblTransportMenu = 0 
lblPoliceMenu = 0 
lblFireDepMenu = 0 
lblHealthMenu = 0 
lblEntertainmentMenu = 0 
lblShoppingMenu = 0
lblIndicatorOpenMenu = 0
lblIndicatorClosedMenu = 0

def Game():
    """Add the widets to the canvas at the start of the game"""
    global cityName, residents, businesses, lblLightning, lblWaterdrop, lblPerson, lblMoney, entEntry, lblWelcome, cityName, balance, taxes, residents, maxResidents, businesses, gameEnd
    global transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, btnSave, incomeTime, pause
    global lblPlay, lblPause, lblFF2x, lblFF3x, loadID, lblPoliceStation, lblFireDepartment, lblHospital, lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2
    global lblRoadMenu, lblWaterMenu, lblElectricMenu, lblWasteMenu, lblEducationMenu, lblTransportMenu, lblPoliceMenu, lblFireDepMenu, lblHealthMenu, lblEntertainmentMenu, lblShoppingMenu, lblIndicatorOpenMenu, lblIndicatorClosedMenu
    global lblFactory, lblOffice
    gameEnd = False 

    if GameStartStop.startGame == True:
        balance = GameStartStop.balance
        taxes = GameStartStop.taxes
        residents = GameStartStop.residents
        maxResidents = GameStartStop.maxResidents 
        businesses = GameStartStop.businesses 
        transportVehicles = GameStartStop.transportVehicles 
        education = GameStartStop.education
        entertainment = GameStartStop.entertainment
        stage = GameStartStop.stage
        upgradePrice = GameStartStop.upgradePrice
        level = GameStartStop.level 
        daysPlayed = GameStartStop.daysPlayed
        p1 = GameStartStop.p1
        p2 = GameStartStop.p2
        p3 = GameStartStop.p3
        p4 = GameStartStop.p4
        p5 = GameStartStop.p5
        p6 = GameStartStop.p6
        lvl1 = GameStartStop.lvl1
        lvl2 = GameStartStop.lvl2
        lvl3 = GameStartStop.lvl3
        lvl4 = GameStartStop.lvl4
        lvl5 = GameStartStop.lvl5
        lvl6 = GameStartStop.lvl6
        
        GameStartStop.startGame = False
        if loadID != 0:
            frameCitybuild.after_cancel(loadID)
        
        #Delete the Savelabels from the canvas
        lblSave1.grid_forget()
        lblSave2.grid_forget()
        lblSave3.grid_forget()
        btnStart.grid_forget()
        lblWelcome.grid_forget()
        lblQuery.grid_forget() 
        lblGame["text"] = ""
        lblWelcome = tk.ttk.Label(frameCitybuild, text= f"Deine Stadt: {cityName}")
        lblWelcome.grid_forget()
        lblWelcome.grid(column=0, row=3, columnspan=2)
        lblGame.grid(column=0, row=4, rowspan=2)
        lblMoneyAdd.grid(column=3, row=2, sticky= "nw", padx= 25)
        btnLoad.grid(column=0, row=2)
        btnClose.grid(column=2, row=2, sticky = tk.W)
        btnSave.grid(column=1, row=2)
        btnCityInformation.grid(column=3,row=3, sticky = tk.W)
        btnUpgrades.grid(column=3, row=4, sticky = tk.NW)

        #Create Canvas for the Game
        #test.createCanvas(frameCitybuild)
        
        #Add Images to the canvas
        lblLightning, lblWaterdrop, lblPerson, lblMoney = Images.createImages(frameCitybuild, lblResidents, lblFactories, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, frameEnergy, frameWater, framePerson, frameMoney, frameTime)
        lblPoliceStation, lblFireDepartment, lblHospital = Images.createPoliceFireMedical(frameCitybuild, lblPolice, lblFire, lblMedical, switchDepartments)
        lblPlay, lblPause, lblFF1x, lblFF2x, lblFF3x = Images.createTimeControls(frameTime)
        lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2 = Images.createStadiums(frameCitybuild, lblEntertainment)
        
        lblIndicatorOpenMenu, lblIndicatorClosedMenu = Upgrades.setupFrames(frameCitybuild)
        
        lblIndicatorClosedMenu.grid(column=12,row=1, sticky="e")
        lblIndicatorOpenMenu.bind("<Button-1>", lambda y: Upgrades.statusMenu(EventType, roadcondition))
        lblIndicatorClosedMenu.bind("<Button-1>", lambda x: Upgrades.statusMenu(EventType, roadcondition))
        
        lblFactory, lblOffice = Images.createFactory(frameCitybuild, lblFactories, switchBusiness)
        RBBusinesses.grid(column=0,row=6)
        
        frameCitybuild.rowconfigure(12, minsize=60)
        RadioButtons.grid(column=0, row=13)
        
        #Add timespeedmanipulation buttons to the canvas (pause, 1x, 2x, 5x Speed)
        TimeControls.initButtons(lblPlay, lblPause, lblFF1x, lblFF2x, lblFF3x)    
        
        #Enter the game-loop
        GameLoop()

def switchBusiness(event):
    global activeBusiness
    if event.widget == lblFactory:
        activeBusiness.set("Office")
        lblFactory.grid_forget()
        lblFactories.grid_forget()
        
        RbFactory["state"] = DISABLED
        RbOffice["state"] = ACTIVE
        
        lblOffice.grid(column=0,row=5)
        lblOffices.grid(column=1,row=5, sticky="w")
    elif event.widget == lblOffice:
        activeBusiness.set("Factory")
        lblOffice.grid_forget()
        lblOffices.grid_forget()
        
        RbFactory["state"] = ACTIVE
        RbOffice["state"] = DISABLED
        
        lblFactory.grid(column=0,row=5)
        lblFactories.grid(column=1,row=5, sticky="w")
    
def saveGame():
    global entEntry, lblWelcome, cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, btnSave
    cityName = GameStartStop.saveGame(entEntry, lblWelcome, cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, btnSave)
    if balance == 0:
        Game()

def loadGame():
    global cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, loadID
    GameStartStop.loadGame(lblExplain, lblSave1, lblSave2, lblSave3, saveGames, False, btnStart, lblWelcome, lblQuery)
    if GameStartStop.startGame == True:
        Game()
    elif GameStartStop.startGame == False:
        print("RESTART")
        loadID = frameCitybuild.after(1000, loadGame)
    
def endGame():
    GameStartStop.endGame(window)
    
def newGame():
    global btnClose, btnLoad, lblExplain, btnSave, btnStart, lblQuery, lblSave1, lblSave2, lblSave3, entEntry, lblWelcome, cityName
    GameStartStop.newGame(btnClose, btnLoad, lblExplain, btnSave, btnStart, lblQuery, lblSave1, lblSave2, lblSave3, entEntry, lblWelcome, window)
    btnSave["command"] = lambda: [TestFile.progressbar().start_progressbar(window), TestFile.action_timer().action_timer_thread(saveGame)]
    
def blinkRed():
    global blockInput, blinking, residents, businesses, level  
    Update.saveBlinking(residents, businesses, level)
    
    if Images.blinking == False and residents + businesses * 2 + level[5] * 5 > level[1] * 15 or residents + businesses * 2 + level[5] * 5 > level[2] * 15 and Images.blinking == False:   
        Images.blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput)

def switchDepartments(event):
    global currentlyShownStation, Rb1, Rb2, Rb3
    if event.widget == lblPoliceStation:
       currentlyShownStation.set("Fire")
       lblPoliceStation.grid_forget() 
       lblPolice.grid_forget()
       Rb1["state"] = DISABLED
       Rb2["state"] = ACTIVE
       
       lblFire.grid(column=1, row=12)
       lblFireDepartment.grid(column=0, row=12, sticky="w", columnspan=2)
       
    elif event.widget == lblFireDepartment:
       currentlyShownStation.set("Medical")
       lblFire.grid_forget()
       lblFireDepartment.grid_forget()
       Rb2["state"] = DISABLED
       Rb3["state"] = ACTIVE
       
       lblMedical.grid(column=1, row=12)
       lblHospital.grid(column=0, row=12, sticky="w", columnspan=2)
       
    elif event.widget == lblHospital:
       currentlyShownStation.set("Police")
       lblMedical.grid_forget()
       lblHospital.grid_forget()
       Rb3["state"] = DISABLED
       Rb1["state"] = ACTIVE
       
       lblPolice.grid(column=1, row=12)
       lblPoliceStation.grid(column=0, row=12, sticky="w", columnspan=2)

def liveFootballMatch(event):
    global showMatch, pause

    if showMatch == False:
        showMatch = True
        frameCitybuild.grid_forget()
        LiveFootball.showFootballArena(window)
        btnStopFootball.grid(column=15, row=5)
        pause = True
        TimeControls.pauseGame()
    elif showMatch == True:
        btnStopFootball.grid_forget()
        LiveFootball.hideArena()
        showMatch = False
        frameCitybuild.grid(column=0,row=0)
        pause = False
        TimeControls.normalSpeed(12000)

pad1 = (50 - len(str(residents))) / 2 + 10
pad4 = (50 - len(str(balance))) / 2 + 10
pad5 = (50 - len(str(satisfaction))) / 2 + 10

window = tk.Tk()
window.title("Builtopia")
window.resizable(width=False, height=False)

frameCitybuild = tk.Frame(window)
frameCitybuild.grid(column=0, row=0, sticky = "nswe", columnspan=30, rowspan=30)

frameTime = tk.Frame(frameCitybuild)
frameTime.grid(column=0, row=25, sticky = "n", columnspan=3, rowspan=2, pady=10)

frameWeather = tk.Frame(frameCitybuild)
frameWeather.grid(column=5, row=0, sticky = "nswe", rowspan=2)
lblWeatherStatus = ttk.Label(frameWeather, text= "")

frameSatisfaction = tk.Frame(frameCitybuild)
frameSatisfaction.grid(column=4, row=0, sticky = "nswe", rowspan=2)
lblSatisfactionStatus = ttk.Label(frameSatisfaction, text= "")
lblSatisfactionStatus.grid(column=4, row=1, sticky = "nswe", padx=pad5)

frameMoney = tk.Frame(frameCitybuild)
frameMoney.grid(column=3, row=0, sticky = "nswe", rowspan=2)
lblMoneyStatus = ttk.Label(frameMoney, text= "", anchor= "center")
lblMoneyStatus.grid(column=3, row=1, sticky = "nswe", padx=pad4)

frameEnergy = tk.Frame(frameCitybuild)
frameEnergy.grid(column=2, row=0, sticky = "nswe", rowspan=2)
lblEnergyStatus = ttk.Label(frameEnergy, text= "", anchor= "center")
pad3 = (50 - len(lblEnergyStatus["text"])) / 2 + 10
lblEnergyStatus.grid(column=2, row=1, sticky = "nswe", padx=pad3)

frameWater = tk.Frame(frameCitybuild)
frameWater.grid(column=1, row=0, sticky = "nswe", rowspan=2)
lblWaterStatus = ttk.Label(frameWater, text= "")
pad2 = (50 - len(lblWaterStatus["text"])) / 2 + 10
lblWaterStatus.grid(column=1, row=1, sticky = "nswe", padx=pad2)

framePerson = tk.Frame(frameCitybuild)
framePerson.grid(column=0, row=0, sticky = "nswe", rowspan=2)
lblPersonStatus = ttk.Label(framePerson, text= "")
lblPersonStatus.grid(column=0, row=1, sticky = "nswe", padx=pad1)

lblQuery = ttk.Label(frameCitybuild, text = "Herzlich Willkommen beim Spiel Builtopia")
lblQuery.grid(column=0,row=0,columnspan=4)

lblSave1 = ttk.Label(frameCitybuild, text = "")

lblSave2 = ttk.Label(frameCitybuild, text = "")

lblSave3 = ttk.Label(frameCitybuild, text = "")

lblEvent = ttk.Label(frameCitybuild, text = " ")

lblValues = ttk.Label(frameCitybuild, text= "")

lblEmpty = tk.Label(frameCitybuild, text = "")
frameCitybuild.columnconfigure(5, minsize=400)
lblEmpty.grid(column=5, row=0)

lblWelcome = ttk.Label(frameCitybuild, text="Willkommen in Builtopia \nBitte gib den Namen deiner neuen Stadt ein: ")

lblExplain = ttk.Label(frameCitybuild, text="Das Spielprinzip ist einfach. Du bist der Bürgermeister deiner eigenen Stadt. \n"
                            "Deine Stadt ist zunächst kaum bewohnt und unattraktiv für große Unternehmen, \n"
                            "sobald dein level aber hoch genug ist, kannst du deine Stadt von neu aufbauen \n"
                            "um so neue Gebäude freizuschalten")
lblExplain.grid(column=0, row=2, columnspan=4)

lblDate = ttk.Label(frameTime, text=" ", anchor="center")

lblGame = ttk.Label(frameCitybuild, text = " ")

lblMoneyAdd = ttk.Label(frameCitybuild, text= " ", foreground = "green")

activeBusiness = tk.StringVar(window, "Factory")
lblResidents = ttk.Label(frameCitybuild, text= f" {residents} Einwohner")
lblFactories = ttk.Label(frameCitybuild, text= f" {businesses} Fabriken")
RBBusinesses = tk.Frame(frameCitybuild)
RbFactory = ttk.Radiobutton(RBBusinesses, text='', variable=activeBusiness, value='Factory', state=ACTIVE)
RbOffice = ttk.Radiobutton(RBBusinesses, text='', variable=activeBusiness, value='Office', state=DISABLED)
lblOffices = ttk.Label(frameCitybuild, text= "")
lblTransport = ttk.Label(frameCitybuild, text= "")
lblSchools = ttk.Label(frameCitybuild, text= "")
lblEducation = ttk.Label(frameCitybuild, text= "")
lblEntertainment = ttk.Label(frameCitybuild, text= "")
lblShopping = ttk.Label(frameCitybuild, text= "")
lblGarbage = ttk.Label(frameCitybuild, text= "")
RbFactory.grid(column=0,row=0, sticky="n")
RbOffice.grid(column=1,row=0, sticky="n")

currentlyShownStation = tk.StringVar(window, "Police")
RadioButtons = tk.Frame(frameCitybuild)
lblPolice = ttk.Label(frameCitybuild, text= "")
Rb1 = ttk.Radiobutton(RadioButtons, text='', variable=currentlyShownStation, value='Police', state=ACTIVE)
lblFire = ttk.Label(frameCitybuild, text= "")
Rb2 = ttk.Radiobutton(RadioButtons, text='', variable=currentlyShownStation, value='Fire', state=DISABLED)
lblMedical = ttk.Label(frameCitybuild, text= "")
Rb3 = ttk.Radiobutton(RadioButtons, text='', variable=currentlyShownStation, value='Medical', state=DISABLED)
Rb1.grid(column=0,row=0, sticky="n")
Rb2.grid(column=1,row=0, sticky="n")
Rb3.grid(column=2,row=0, sticky="n")

lblresidentsLeave = ttk.Label(frameCitybuild, text= "")
lblnewResidents = ttk.Label(frameCitybuild, text= "")

lblUpgrades = ttk.Label(frameCitybuild, text= "")

lblStreets = ttk.Label(frameCitybuild, text= "")                      
lblEnergy = ttk.Label(frameCitybuild, text= "")
lblWater = ttk.Label(frameCitybuild, text= "")
lblVehicles = ttk.Label(frameCitybuild, text= "")
lblSchools = ttk.Label(frameCitybuild, text= "")
lblStadium = ttk.Label(frameCitybuild, text= "")

lblEventChoice1 = ttk.Label(frameCitybuild, text= "")
lblEventChoice2 = ttk.Label(frameCitybuild, text= "")
lblEventChoice3 = ttk.Label(frameCitybuild, text= "")

entEntry = ttk.Entry(frameCitybuild)

btnSave = ttk.Button(master=frameCitybuild, text="Speichern", command= saveGame)

btnStart = ttk.Button(master=frameCitybuild, text="Neues Spiel", command=newGame)
btnStart.grid(column=0, row=1)

btnLoad = ttk.Button(master=frameCitybuild, text="Spiel laden", command=loadGame)
btnLoad.grid(column=1, row=1)

btnClose = ttk.Button(master=frameCitybuild, text="Beenden", command=endGame)
btnClose.grid(column=2, row=1)

btnStopFootball = ttk.Button(master=window, text="Zurück zu deiner Stadt", command= lambda: liveFootballMatch(EventType))

btnUpgrades = ttk.Button(master=frameCitybuild, text="Upgrades", command=buyUpgrades)

btnCityInformation = ttk.Button(master=frameCitybuild, text="Zeige Werte", command=values)

lblConstructing = Images.constructHouse(frameCitybuild)
lblDamagedHouse = Images.brokenHouse(frameCitybuild)

window.mainloop()

#TO-DO
#   Kaufhaus / Shopping einbauen
#   Tag-Nacht-Zyklus
#   Wetter und Temperatur 
#   Müllverarbeitung
#   Bewohner auf verschiedenen stages haben verschiedene Bedürfnisse:
#       - Stage 1: Kleines Haus
#           - Strom, Wasser, Müll
#       - Stage 2: 
#
#   Landwirtschaft
#   Abwasser
#   Feuerwehr, Polizei, Krankenhaus
#   Straßen in Menübar einbauen
#       - Straßenzustand
#       - Straßenauslastung
#   Einnahmen und Ausgaben-Ansicht (Kosten für Energie, Wasser, ÖPNV, ...)
#   Mehr Investitionsmöglichkeiten -> Energie aufteilen in Solarenergie, Kohle etc. mit verschiedenen Vor- und Nachteilen
#   Buseinnahmen abhängig von Einwohnerzahl 
#   Hafen und Flughafen
#---Calculate Funktion auslagern