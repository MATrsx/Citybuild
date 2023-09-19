import tkinter.ttk as ttk
import tkinter as tk
import datetime, Calculations


pauseLocal = False
incomeTimeLocal = 12000
start = False
lblDateLocal = ""
tomorrowLocal = ""
currentHour = 0
daysPlayedLocal = 0
nowLocal = ""
lblMoneyAddLocal = ""
stop = False
lblPlayLocal = 0
lblPauseLocal = 0
lblFF1xLocal = 0
lblFF2xLocal = 0
lblFF3xLocal = 0

def addIngameDays(daysPlayed, lblDate, lblMoneyAdd):
    global lblDateLocal, tomorrowLocal, daysPlayedLocal, nowLocal, start, lblMoneyAddLocal, stop
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=daysPlayed)
    now = now.strftime("%d %B %Y")
    tomorrow = tomorrow.strftime("%d %B %Y")
    lblDateLocal = lblDate
    tomorrowLocal = tomorrow
    daysPlayedLocal = daysPlayed
    nowLocal = now
    lblMoneyAddLocal = lblMoneyAdd
    
    if start == False:
        start = True
        lblDateLocal["text"] = f"00:00 | {nowLocal}"
        lblDateLocal.grid(column=2, row=0, sticky= tk.NW)
        countTime(incomeTimeLocal, lblDate)     
    return daysPlayed

def countTime(incomeTime, lblDate):
    hour = incomeTime / 24
    hour = int(hour)
    if pauseLocal == False:
        lblDate.after(hour, addHour)   

def addHour():
    global lblDateLocal, tomorrowLocal, currentHour, daysPlayedLocal, nowLocal, tomorrowLocal, lblMoneyAddLocal
    currentHour += 1
    #Calculate Funktion direkt hier in Time Controls einbauen?
    if currentHour == 12:
        lblMoneyAddLocal.grid_forget()
    if currentHour == 24:
        currentHour = 0
        addIngameDays(daysPlayedLocal, lblDateLocal, lblMoneyAddLocal)
        lblMoneyAddLocal.grid(column=3,row=2, sticky= "nw", padx= 25)
        daysPlayedLocal += 1
        nowLocal = tomorrowLocal
    lblDateLocal["text"] = f"{currentHour}:00 | {nowLocal}"
    lblDateLocal.grid(column=2, row=0, sticky= tk.NW, pady= 10)
    countTime(incomeTimeLocal, lblDateLocal)

def getCurrentMonth(daysPlayed):
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=daysPlayed)
    month = tomorrow.strftime("%m")
    return int(month)

def initButtons(lblPlay, lblPause, lblFF1x, lblFF2x, lblFF3x):
    global lblPlayLocal, lblPauseLocal, lblFF1xLocal, lblFF2xLocal, lblFF3xLocal
    lblPlayLocal = lblPlay
    lblPauseLocal = lblPause
    lblFF1xLocal = lblFF1x
    lblFF2xLocal = lblFF2x
    lblFF3xLocal = lblFF3x
    lblPlay.bind("<Button-1>", changeSpeed)
    lblPause.bind("<Button-1>", changeSpeed)
    lblFF1x.bind("<Button-1>", changeSpeed)
    lblFF2x.bind("<Button-1>", changeSpeed)
    lblFF3x.bind("<Button-1>", changeSpeed)

def changeSpeed(event):
    global incomeTimeLocal
    if event.widget == lblPlayLocal:
        lblPlayLocal.grid_forget()
        lblPauseLocal.grid(column=0, row=0, padx=5)
        pauseGame()
    elif event.widget == lblPauseLocal:
        lblPauseLocal.grid_forget()
        lblPlayLocal.grid(column=0, row=0, padx=10)
        
        normalSpeed(incomeTimeLocal)
    elif event.widget == lblFF1xLocal:
        
        lblFF1xLocal.grid_forget()
        lblFF2xLocal.grid(column=3, row=0, padx=10)
        
        if pauseLocal == False:
            fastForward2x(incomeTimeLocal)
    elif event.widget == lblFF2xLocal:
        lblFF2xLocal.grid_forget()
        lblFF3xLocal.grid(column=3, row=0, padx=10)
        
        if pauseLocal == False:
            fastForward5x(incomeTimeLocal)
    elif event.widget == lblFF3xLocal:
        lblFF3xLocal.grid_forget()
        lblFF1xLocal.grid(column=3, row=0, padx=10)
        
        if pauseLocal == False:
            normalSpeed(incomeTimeLocal)

def getIncomeTime():
    return incomeTimeLocal

def normalSpeed(incomeTime):
    global pauseLocal, incomeTimeLocal, incomeTimeLocal, lblDateLocal, stop
    incomeTime = 12000
    incomeTime = int(incomeTime)
    pauseLocal = False
    incomeTimeLocal = incomeTime
    if stop == True:
        stop = False
        countTime(incomeTimeLocal, lblDateLocal)

def pauseGame():
    global pauseLocal, stop
    pauseLocal = True
    stop = True

def fastForward2x(incomeTime):
    global pauseLocal, incomeTimeLocal, incomeTimeLocal, lblDateLocal, stop
    incomeTime = 6000
    incomeTime = int(incomeTime)
    pauseLocal = False
    incomeTimeLocal = incomeTime
    if stop == True:
        stop = False
        countTime(incomeTimeLocal, lblDateLocal)
    
def fastForward5x(incomeTime):
    global pauseLocal, incomeTimeLocal, incomeTimeLocal, lblDateLocal, stop
    incomeTime = 2400
    incomeTime = int(incomeTime)
    pauseLocal = False
    incomeTimeLocal = incomeTime
    if stop == True:
        stop = False
        countTime(incomeTimeLocal, lblDateLocal)

def checkStatus():
    return pauseLocal, incomeTimeLocal

def markActiveButton():
    print()
    #Den aktiven Button hervorheben