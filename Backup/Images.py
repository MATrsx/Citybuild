from PIL import ImageTk, Image
from pathlib import Path
import tkinter as tk

basePath = Path(__file__).parent

def createImages(window, lblResidents, lblBusinesses, lblTransport, lblEducation, lblEntertainment, frameEnergy, frameWater, framePerson, frameMoney):
    """Create and add the images to the canvas"""
    global lblWater, lblLightning, lblPerson, lblMoney
    
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
    lblLightning = tk.Label(frameEnergy, image = lightningP, anchor= "center")
    lblLightning.image = lightningP
    lblLightning.grid(column=2,row=0, padx=10)
    
    imageWater = Image.open(basePath / "Images" / "droplet.png")
    waterSized = imageWater.resize((50,50))
    waterP = ImageTk.PhotoImage(waterSized)
    lblWaterdrop = tk.Label(frameWater, image = waterP, anchor= "center")
    lblWaterdrop.image = waterP
    lblWaterdrop.grid(column=1,row=0, padx=10)
    
    imagePerson = Image.open(basePath / "Images" / "person.png")
    personSized = imagePerson .resize((50,50))
    personP = ImageTk.PhotoImage(personSized)
    lblPerson = tk.Label(framePerson, image = personP, anchor= "center")
    lblPerson.image = personP
    lblPerson.grid(column=0,row=0, padx=10)
    
    imageMoney = Image.open(basePath / "Images" / "dollar.png")
    moneySized = imageMoney.resize((50,50))
    moneyP = ImageTk.PhotoImage(moneySized)
    lblMoney = tk.Label(frameMoney, image = moneyP, anchor= "center")
    lblMoney.image = moneyP
    lblMoney.grid(column=3,row=0, padx=10)
    
    return lblLightning, lblWaterdrop, lblPerson, lblMoney 

def brokenHouse(window):
    imageResidentsLeave = Image.open(basePath / "Images" / "derelict_house_building.png")
    residentsLeaveSized = imageResidentsLeave.resize((25,25))
    residentsLeave = ImageTk.PhotoImage(residentsLeaveSized)
    lblDamagedHouse = tk.Label(window, image = residentsLeave)
    lblDamagedHouse.image = residentsLeave
    
    return lblDamagedHouse

def constructHouse(window):
    imageNewHouse = Image.open(basePath / "Images" / "building_construction.png")
    newHouseSized = imageNewHouse.resize((25,25))
    newHouse = ImageTk.PhotoImage(newHouseSized)
    lblConstructing = tk.Label(window, image = newHouse)
    lblConstructing.image = newHouse
    
    return lblConstructing

def satisfactionSmiley(frameSatisfaction):
    #80 - 100% satisfaction
    imageGrinning = Image.open(basePath / "Images" / "Satisfaction" / "grinning.png")
    GrinningSized = imageGrinning.resize((50,50))
    Grinning = ImageTk.PhotoImage(GrinningSized)
    lblGrinning = tk.Label(frameSatisfaction, image = Grinning)
    lblGrinning.image = Grinning

    #60 - 80% satisfaction
    imageSmiling = Image.open(basePath / "Images" / "Satisfaction" / "smiling.png")
    SmilingSized = imageSmiling.resize((50,50))
    Smiling = ImageTk.PhotoImage(SmilingSized)
    lblSmiling = tk.Label(frameSatisfaction, image = Smiling)
    lblSmiling.image = Smiling
    
    #40 - 60% satisfaction
    imageNeutral = Image.open(basePath / "Images" / "Satisfaction" / "neutral.png")
    NeutralSized = imageNeutral.resize((50,50))
    Neutral = ImageTk.PhotoImage(NeutralSized)
    lblNeutral = tk.Label(frameSatisfaction, image = Neutral)
    lblNeutral.image = Neutral
    
    #20 - 40% satisfaction
    imageFrowning = Image.open(basePath / "Images" / "Satisfaction" / "frowning.png")
    FrowningSized = imageFrowning.resize((50,50))
    Frowning = ImageTk.PhotoImage(FrowningSized)
    lblFrowning = tk.Label(frameSatisfaction, image = Frowning)
    lblFrowning.image = Frowning
    
    #0 - 20% satisfaction
    imageRage = Image.open(basePath / "Images" / "Satisfaction" / "rage.png")
    RageSized = imageRage.resize((50,50))
    Rage = ImageTk.PhotoImage(RageSized)
    lblRage = tk.Label(frameSatisfaction, image = Rage)
    lblRage.image = Rage
    
    return lblGrinning, lblSmiling, lblNeutral, lblFrowning, lblRage


def blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput):
    print("BLRED")
    if blockInput == False:
        Widget = ""
        if residents + businesses * 2 + level[5] * 5 > level[1] * 15:  
            lblWaterdrop["bg"] = 'red'
            frameWater["bg"] = 'red'
            lblWaterStatus["background"] = 'red'
            if "lblWater" not in Widget:
                Widget += " lblWater"
        if residents + businesses * 2 + level[5] * 5 > level[2] * 15:  
            lblLightning["bg"] = 'red'
            frameEnergy["bg"] = 'red'
            lblEnergyStatus["background"] = 'red'
            if "lblEnergy" not in Widget:
                Widget += " lblEnergy"
        elif residents + businesses * 2 + level[5] * 5 < level[2] * 15:
            Widget = Widget.replace(" lblEnergy", "")
        elif residents + businesses * 2 + level[5] * 5 < level[1] * 15:
            Widget = Widget.replace(" Water", "")
        if Widget != "":
            lblLightning.after(1000, lambda : bgWhite(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, Widget, blockInput))

def bgWhite(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, Widget, blockInput):
    print("BLWHITE")
    if  "lblWater" in Widget:
        lblWaterdrop["bg"] = '#F0F0F0'
        frameWater["bg"] = '#F0F0F0'
        lblWaterStatus["background"] = '#F0F0F0'
    if "lblEnergy" in Widget:
        lblLightning["bg"] = '#F0F0F0'
        frameEnergy["bg"] = '#F0F0F0'
        lblEnergyStatus["background"] = '#F0F0F0'
    lblLightning.after(1000, lambda : blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput))

def insufficientFunds(lblMoneyStatus, count):
    if count < 8:
        lblMoneyStatus["foreground"] = 'red'
        lblMoneyStatus["font"] = ('Segoe UI', 9)
        count += 1
        lblMoneyStatus.after(350, lambda: fontMoney(lblMoneyStatus, count))
    
def fontMoney(lblMoneyStatus, count):
    if count < 8:
        lblMoneyStatus["foreground"] = ''
        lblMoneyStatus["font"] = ('Segoe UI', 9)
        count += 1
        lblMoneyStatus.after(350, lambda: insufficientFunds(lblMoneyStatus, count))


