import random 
import datetime
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
from pathlib import Path

save1Local = []
save2Local = []
save3Local = []
lblSave1Local = 0
lblSave2Local = 0
lblSave3Local = 0
lblExplainLocal = 0
saveGamesLocal = []
btnStartLocal = 0
lblWelcomeLocal = 0
lblQueryLocal = 0
saveAble = True
startGame = False

cityName = "" 
balance = 0 
taxes = 10
residents = 10 
maxResidents = 50 
businesses = 1 
transportVehicles = 0 
education = 0 
entertainment = 100 
stage = 4 
daysPlayed = 1
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


def saveCountdown(btnSave):
    global saveAble
    btnSave.after(10000, saveTrue)

def saveTrue():
    global saveAble
    saveAble = True

def saveGame(entEntry, lblWelcome, cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, btnSave):
    """Save the current game"""
    global saveAble, startGame

    saveValues = [cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6]
    overwrite = False
    delLine = None  

    if balance == 0:
        #Save the city name and start the game
        cityName = entEntry.get()
        lblWelcome.grid_forget()
        entEntry.delete(0, tk.END)
        entEntry.grid_forget()  
        startGame = True 
    
    elif saveAble == True and balance > 0:
        saveAble = False
        saveCountdown(btnSave)
        
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
            
    return cityName

def loadGame(lblExplain, lblSave1, lblSave2, lblSave3, saveGames, returnValues, btnStart, lblWelcome, lblQuery):
    """Load an existing game file"""
    
    global save1, save2, save3, cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6
    
    global lblExplainLocal, lblSave1Local, lblSave2Local, lblSave3Local, saveGamesLocal, btnStartLocal, lblWelcomeLocal, lblQueryLocal, save1Local, save2Local, save3Local, GameLocal, startGame
    lblExplainLocal = lblExplain
    lblSave1Local = lblSave1
    lblSave2Local = lblSave2
    lblSave3Local = lblSave3
    saveGamesLocal = saveGames
    btnStartLocal = btnStart
    lblWelcomeLocal = lblWelcome
    lblQueryLocal = lblQuery
    
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
            save1Local = save1
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
            save2 = line.split(";")
            save2Local = save2
            lblSave2.bind("<Button-1>", load)
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
            save3 = line.split(";")
            save3Local = save3
            lblSave3.bind("<Button-1>", load)
        else:
            lblSave3["text"] = "SPEICHERSTAND 3: \nSpeicherstand nicht belegt!"
            lblSave3.grid(column=0, row=8, columnspan=3, sticky= tk.W)
    input.close()   
       
def load(event):
    """Load the requested savegame"""
    global save1Local, save2Local, save3Local, cityName, balance, taxes, residents, maxResidents, businesses, transportVehicles, education, entertainment, stage, upgradePrice, level, daysPlayed, p1, p2, p3, p4, p5, p6, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lblExplain, saveGames
    global lblExplainLocal, lblSave1Local, lblSave2Local, lblSave3Local, saveGamesLocal, startGame
    if event.widget == lblSave1Local:
        cityName = save1Local[0]  
        balance = save1Local[1] 
        taxes = save1Local[2] 
        residents = save1Local[3] 
        maxResidents = save1Local[4] 
        businesses = save1Local[5] 
        transportVehicles = save1Local[6] 
        education = save1Local[7] 
        entertainment = save1Local[8] 
        stage = save1Local[9] 
        upgradePrice = save1Local[10]
        level = save1Local[11] 
        daysPlayed = save1Local[12] 
        p1 = save1Local[13]
        p2 = save1Local[14]
        p3 = save1Local[15]
        p4 = save1Local[16]
        p5 = save1Local[17]
        p6 = save1Local[18]
        lvl1 = save1Local[19]
        lvl2 = save1Local[20]
        lvl3 = save1Local[21]
        lvl4 = save1Local[22]
        lvl5 = save1Local[23]
        lvl6 = save1Local[24]
    if event.widget == lblSave2Local:
        cityName = save2Local[0]  
        balance = save2Local[1] 
        taxes = save2Local[2] 
        residents = save2Local[3] 
        maxResidents = save2Local[4] 
        businesses = save2Local[5] 
        transportVehicles = save2Local[6] 
        education = save2Local[7] 
        entertainment = save2Local[8] 
        stage = save2Local[9] 
        upgradePrice = save2Local[10]
        level = save2Local[11] 
        daysPlayed = save2Local[12] 
        p1 = save2Local[13]
        p2 = save2Local[14]
        p3 = save2Local[15]
        p4 = save2Local[16]
        p5 = save2Local[17]
        p6 = save2Local[18]
        lvl1 = save2Local[19]
        lvl2 = save2Local[20]
        lvl3 = save2Local[21]
        lvl4 = save2Local[22]
        lvl5 = save2Local[23]
        lvl6 = save2Local[24]
    if event.widget == lblSave3Local:
        cityName = save3Local[0]  
        balance = save3Local[1] 
        taxes = save3Local[2] 
        residents = save3Local[3] 
        maxResidents = save3Local[4] 
        businesses = save3Local[5] 
        transportVehicles = save3Local[6] 
        education = save3Local[7] 
        entertainment = save3Local[8] 
        stage = save3Local[9] 
        upgradePrice = save3Local[10]
        level = save3Local[11] 
        daysPlayed = save3Local[12] 
        p1 = save3Local[13]
        p2 = save3Local[14]
        p3 = save3Local[15]
        p4 = save3Local[16]
        p5 = save3Local[17]
        p6 = save3Local[18]
        lvl1 = save3Local[19]
        lvl2 = save3Local[20]
        lvl3 = save3Local[21]
        lvl4 = save3Local[22]
        lvl5 = save3Local[23]
        lvl6 = save3Local[24]

    #Transform the values into the correct format
    upgradePrice = [int(p1), int(p2), int(p3), int(p4), int(p5), int(p6)]
    level = [int(lvl1), int(lvl2), int(lvl3), int(lvl4), int(lvl5), int(lvl6)]
    balance = float(balance)
    taxes = int(taxes)
    education = int(education)
    entertainment = int(entertainment)
    residents = int(residents)
    maxResidents = int(maxResidents)
    businesses = int(businesses)
    stage = int(stage)
    daysPlayed = daysPlayed.rstrip("\n")
    daysPlayed = int(daysPlayed) 
    
    startGame = True  
    
def endGame(window):
    """End the game"""
    window.destroy()
    
def newGame(btnClose,btnLoad, lblExplain, btnSave, btnStart, lblQuery, lblSave1, lblSave2, lblSave3, entEntry, lblWelcome):
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
    