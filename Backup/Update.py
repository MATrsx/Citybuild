import tkinter as tk
import TimeControls

def UpdateStatusBar(lblPersonStatus, lblWaterStatus, lblEnergyStatus, lblMoneyStatus, residents, balance, businesses, level, pad1, pad2, pad3, pad4):
    lblEnergyStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[2] * 15}"
    lblWaterStatus["text"] = f"{residents + businesses * 2 + level[5] * 5} / {level[1] * 15}"
    lblPersonStatus["text"] = f"{residents}"
    lblMoneyStatus["text"] = f"{balance}$"
    lblPersonStatus.grid(column=0, row=1, sticky = "nswe", padx=pad1)
    lblWaterStatus.grid(column=1, row=1, sticky = "nswe", padx=pad2)
    lblEnergyStatus.grid(column=2, row=1, sticky = "nswe", padx=pad3)
    lblMoneyStatus.grid(column=3, row=1, sticky = "nswe", padx=pad4)  
    
def UpdateCityInfLabel(showValues, btnUpgrades, stage, lblValues, residents, maxResidents, balance, taxes, businesses, listBuildings, unterhaltung,
                       incomeTime, lblDamagedHouse, lblresidentsLeave, leaveCity, joinCity, lblConstructing, lblnewResidents):
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
        