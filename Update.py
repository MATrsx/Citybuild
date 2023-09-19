import tkinter as tk
import TimeControls
from PIL import Image, ImageTk
import datetime

residentsLoc = None
businessesLoc = None
levelLoc = None

def UpdateStatusBar(lblPersonStatus, lblWaterStatus, lblEnergyStatus, lblMoneyStatus, residents, balance, businesses, level, pad1, pad2, pad3, pad4):
    lblEnergyStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[2] * 15}"
    lblWaterStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[1] * 15}"
    lblPersonStatus["text"] = f"{residents}"
    lblMoneyStatus["text"] = f"{balance}$"
    lblPersonStatus.grid(column=0, row=1, sticky = "nswe", padx=pad1)
    lblWaterStatus.grid(column=1, row=1, sticky = "nswe", padx=pad2)
    lblEnergyStatus.grid(column=2, row=1, sticky = "nswe", padx=pad3)
    
def UpdateCityInfLabel(showValues, btnUpgrades, stage, lblValues, residents, maxResidents, balance, taxes, businesses, listBuildings, unterhaltung,
                       incomeTime, lblDamagedHouse, lblresidentsLeave, leaveCity, joinCity, lblConstructing, lblnewResidents, lblStreets, lblWater,
                       lblEnergy, lblVehicles, lblSchools, lblStadium, showUpgrades, lblExplain):
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
        
        #Display how many residents join and leave the city
        lblDamagedHouse.grid(column=2,row=4, sticky= tk.NW)
        lblresidentsLeave["text"] = f"- {leaveCity}"
        lblresidentsLeave.grid(column=2, row=4, sticky= tk.N)
        
        lblConstructing.grid(column=2,row=4, sticky= tk.SW)
        lblnewResidents["text"] = f"+ {joinCity}"
        lblnewResidents.grid(column=2, row=4, sticky= tk.S)

def updateWeatherForecast(listForecastLabel, basePath, listForecast, ph, listTemperatureLabel, listTemperature):
        path = basePath / "Images" / "Weather"
        daysPlayed = TimeControls.daysPlayedLocal
        now = datetime.datetime.now()
        
        for x in range (1,7):
            print(x)
            if listForecast[x] == 1:
                im = Image.open(path / "sunny.png")
            elif listForecast[x] == 2:
                im = Image.open(path / "barely_sunny.png")
            elif listForecast[x] == 3:
                im = Image.open(path / "rain_cloud.png")
            elif listForecast[x] == 4:
                im = Image.open(path / "thunder_cloud_and_rain.png")
            elif listForecast[x] == 5:
                im = Image.open(path / "snow_cloud.png")
            im = im.resize((25,25))
            ph.append(ImageTk.PhotoImage(im))
            tomorrow = now + datetime.timedelta(days=daysPlayed)
            weekday = tomorrow.strftime("%a")
            listForecastLabel[x]["image"] = ph[len(ph)-1]   
            printday = tomorrow.strftime("%d.%m")
            listForecastLabel[x]["text"] =  f"{weekday} \n{printday}" + " "
            listForecastLabel[x]["compound"] = 'right'
            listForecastLabel[x]["anchor"] = 'w'
            listTemperatureLabel[x]["text"] = f"{listTemperature[x]}°"
            listForecastLabel[x].image = ph[len(ph)-1]
            listForecastLabel[x].grid(column=5, row=x+2)
            listTemperatureLabel[x].grid(column=6, row=x+2, sticky="nswe")
            daysPlayed += 1

def UpdateUpgradesLabel():
    print()
    
def saveBlinking(residents, businesses, level):
    global residentsLoc, businessesLoc, levelLoc
    residentsLoc =  residents
    businessesLoc = businesses 
    levelLoc = level

def loadBlinking():
    global residentsLoc, businessesLoc, levelLoc
    return residentsLoc, businessesLoc, levelLoc   