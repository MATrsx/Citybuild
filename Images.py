from PIL import ImageTk, Image
from pathlib import Path
import tkinter as tk
import Update, TimeControls
import threading

basePath = Path(__file__).parent

lblHouseLocal = None
lblStadiumLocal = None
blinking = False

def createImages(frameCitybuild, lblResidents, lblBusinesses, lblTransport, lblEducation, lblEntertainment, lblShopping, lblGarbage, frameEnergy, frameWater, framePerson, frameMoney, frameTime):
    """Create and add the images to the canvas"""
    global lblWater, lblLightning, lblPerson, lblMoney, lblStadiumLocal
    
    imageHouse = Image.open(basePath / "Images" / "house.png")
    houseSized = imageHouse.resize((50,50))
    house = ImageTk.PhotoImage(houseSized)
    lblHouse = tk.Label(frameCitybuild, image = house)
    lblHouse.image = house
    lblHouse.grid(column=0,row=4)
    lblResidents.grid(column=1,row=4, sticky= tk.W)
    
    #Factory
    
    imageTransport = Image.open(basePath / "Images" / "trainStation2.png")
    transportSized = imageTransport.resize((100,50))
    transport = ImageTk.PhotoImage(transportSized)
    lblStation = tk.Label(frameCitybuild, image = transport)
    lblStation.image = transport
    lblStation.grid(column=0,row=7)
    lblTransport.grid(column=1, row=7, sticky= tk.W)
    
    imageEducation = Image.open(basePath / "Images" / "school.png")
    educationSized = imageEducation.resize((100,50))
    educationP = ImageTk.PhotoImage(educationSized)
    lblSchool = tk.Label(frameCitybuild, image = educationP)
    lblSchool.image = educationP
    lblSchool.grid(column=0,row=8)
    lblEducation.grid(column=1, row=8, sticky= tk.W)
    
    #lblStadium
    
    imageShopping = Image.open(basePath / "Images" / "department_store.png")
    shoppingSized = imageShopping.resize((50,50))
    shoppingP = ImageTk.PhotoImage(shoppingSized)
    lblStore = tk.Label(frameCitybuild, image = shoppingP)
    lblStore.image = shoppingP
    lblStore.grid(column=0,row=10)
    lblShopping.grid(column=1, row=10, sticky= tk.W)
    
    imageGarbage = Image.open(basePath / "Images" / "waste_incineration.png")
    garbageSized = imageGarbage.resize((100,80))
    garbageP = ImageTk.PhotoImage(garbageSized)
    lblIncineration = tk.Label(frameCitybuild, image = garbageP)
    lblIncineration.image = garbageP
    lblIncineration.grid(column=0,row=11, sticky="n")
    lblGarbage.grid(column=1, row=11, sticky= tk.W)
    
    imageCalendar = Image.open(basePath / "Images" / "calendar.png")
    calendarSized = imageCalendar.resize((35,35))
    calendarP = ImageTk.PhotoImage(calendarSized)
    lblCalendar = tk.Label(frameTime, image = calendarP)
    lblCalendar.image = calendarP
    lblCalendar.grid(column=1,row=0)
    
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

def createFactory(frameCitybuild, lblFactories, switchBusiness):
    imageFactory = Image.open(basePath / "Images" / "factory.png")
    factorySized = imageFactory.resize((100,80))
    factory = ImageTk.PhotoImage(factorySized)
    lblFactory = tk.Label(frameCitybuild, image = factory)
    lblFactory.image = factory
    lblFactory.grid(column=0,row=5)
    lblFactories.grid(column=1,row=5, sticky= tk.W)
    lblFactory.bind("<Button-1>", switchBusiness)
    
    imageOffice = Image.open(basePath / "Images" / "office.png")
    officeSized = imageOffice.resize((100,80))
    office = ImageTk.PhotoImage(officeSized)
    lblOffice = tk.Label(frameCitybuild, image = office)
    lblOffice.image = office
    lblOffice.bind("<Button-1>", switchBusiness)
    
    return lblFactory, lblOffice

def createStadiums(frameCitybuild, lblEntertainment):
    global lblStadiumLocal
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" / "stadiumLevel1.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl1 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl1.image = entertainmentP
    lblStadiumLvl1.grid(column=0,row=8)
    lblEntertainment.grid(column=1, row=8, sticky= tk.W)
    
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" / "stadiumLevel2.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl2 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl2.image = entertainmentP
    
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" /  "stadiumLevel3.1.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl3_1 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl3_1.image = entertainmentP
    
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" /  "stadiumLevel3.2.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl3_2 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl3_2.image = entertainmentP
    
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" /  "stadiumLevel4.1.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl4_1 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl4_1.image = entertainmentP
    
    imageEntertainment = Image.open(basePath / "Images" / "Football" / "Stadium" /  "stadiumLevel4.2.png")
    entertainmentSized = imageEntertainment.resize((100,80))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblStadiumLvl4_2 = tk.Label(frameCitybuild, image = entertainmentP)
    lblStadiumLvl4_2.image = entertainmentP
    
    
    lblStadiumLocal = lblStadiumLvl1
    
    return lblStadiumLvl1, lblStadiumLvl2, lblStadiumLvl3_1, lblStadiumLvl3_2, lblStadiumLvl4_1, lblStadiumLvl4_2

def getStadium():
    return lblStadiumLocal

def createPoliceFireMedical(frameCitybuild, lblPolice, lblFire, lblMedical, switchDepartments):
    imagePolice = Image.open(basePath / "Images" / "policeStation.png")
    policeSized = imagePolice.resize((100,60))
    policeP = ImageTk.PhotoImage(policeSized)
    lblPoliceStation = tk.Label(frameCitybuild, image = policeP, anchor="s")
    lblPoliceStation.image = policeP
    lblPoliceStation.grid(column=0,row=12, sticky="nswe")
    lblPolice.grid(column=1, row=12, padx=10)
    lblPoliceStation.bind("<Button-1>", switchDepartments)
    
    imageFire = Image.open(basePath / "Images" / "fireDepartment.png")
    fireSized = imageFire.resize((100,50))
    fireP = ImageTk.PhotoImage(fireSized)
    lblFireDepartment = tk.Label(frameCitybuild, image = fireP, anchor="s")
    lblFireDepartment.image = fireP
    lblFireDepartment.bind("<Button-1>", switchDepartments)
    
    imageMedical = Image.open(basePath / "Images" / "hospital.png")
    medicalSized = imageMedical.resize((100,50))
    medicalP = ImageTk.PhotoImage(medicalSized)
    lblHospital = tk.Label(frameCitybuild, image = medicalP, anchor="s")
    lblHospital.image = medicalP
    lblHospital.bind("<Button-1>", switchDepartments)
    
    return lblPoliceStation, lblFireDepartment, lblHospital

def createMenuBar(frameMenuBar):
    
    xSize = 30
    ySize = 30
    
    imageRoad = Image.open(basePath / "Images" / "MenuBar" / "road.png")
    roadSized = imageRoad.resize((xSize,ySize))
    roadP = ImageTk.PhotoImage(roadSized)
    lblRoad = tk.Label(frameMenuBar, image = roadP, anchor= "center")
    lblRoad.image = roadP
    
    imageWater = Image.open(basePath / "Images" / "MenuBar" / "water.png")
    waterSized = imageWater.resize((xSize,ySize))
    waterP = ImageTk.PhotoImage(waterSized)
    lblWater = tk.Label(frameMenuBar, image = waterP, anchor= "center")
    lblWater.image = waterP
    
    imageElectric = Image.open(basePath / "Images" / "MenuBar" / "lightning.png")
    electricSized = imageElectric.resize((xSize,ySize))
    electricP = ImageTk.PhotoImage(electricSized)
    lblElectric = tk.Label(frameMenuBar, image = electricP, anchor= "center")
    lblElectric.image = electricP
    
    imageWaste = Image.open(basePath / "Images" / "MenuBar" / "garbage.png")
    wasteSized = imageWaste.resize((xSize,ySize))
    wasteP = ImageTk.PhotoImage(wasteSized)
    lblWaste = tk.Label(frameMenuBar, image = wasteP, anchor= "center")
    lblWaste.image = wasteP
    
    imageEducation = Image.open(basePath / "Images" / "MenuBar" / "education.png")
    educationSized = imageEducation.resize((xSize+5,ySize+5))
    educationP = ImageTk.PhotoImage(educationSized)
    lblEducation = tk.Label(frameMenuBar, image = educationP, anchor= "center")
    lblEducation.image = educationP
    
    imageTransport = Image.open(basePath / "Images" / "MenuBar" / "publicTransport.png")
    transportSized = imageTransport.resize((xSize+5,ySize+5))
    transportP = ImageTk.PhotoImage(transportSized)
    lblTransport = tk.Label(frameMenuBar, image = transportP, anchor= "center")
    lblTransport.image = transportP
    
    imagePolice = Image.open(basePath / "Images" / "MenuBar" / "police.png")
    policeSized = imagePolice.resize((xSize,ySize))
    policeP = ImageTk.PhotoImage(policeSized)
    lblPolice = tk.Label(frameMenuBar, image = policeP, anchor= "center")
    lblPolice.image = policeP
    
    imageFireDep = Image.open(basePath / "Images" / "MenuBar" / "firefighter.png")
    fireDepSized = imageFireDep.resize((xSize+5,ySize+5))
    fireDepP = ImageTk.PhotoImage(fireDepSized)
    lblFireDep = tk.Label(frameMenuBar, image = fireDepP, anchor= "center")
    lblFireDep.image = fireDepP

    imageHealth = Image.open(basePath / "Images" / "MenuBar" / "health.png")
    healthSized = imageHealth.resize((xSize,ySize))
    healthP = ImageTk.PhotoImage(healthSized)
    lblHealth = tk.Label(frameMenuBar, image = healthP, anchor= "center")
    lblHealth.image = healthP
    
    imageEntertainment = Image.open(basePath / "Images" / "MenuBar" / "entertainment.png")
    entertainmentSized = imageEntertainment.resize((xSize,ySize))
    entertainmentP = ImageTk.PhotoImage(entertainmentSized)
    lblEntertainment = tk.Label(frameMenuBar, image = entertainmentP, anchor= "center")
    lblEntertainment.image = entertainmentP

    imageShopping = Image.open(basePath / "Images" / "MenuBar" / "shopping.png")
    shoppingSized = imageShopping.resize((xSize,ySize))
    shoppingP = ImageTk.PhotoImage(shoppingSized)
    lblShopping = tk.Label(frameMenuBar, image = shoppingP, anchor= "center")
    lblShopping.image = shoppingP 
    
    imageIndicatorOpen = Image.open(basePath / "Images" / "MenuBar" / "indicatorOpen.png")
    indicatorOpenSized = imageIndicatorOpen.resize((xSize,ySize))
    indicatorOpenP = ImageTk.PhotoImage(indicatorOpenSized)
    lblIndicatorOpen = tk.Label(frameMenuBar, image = indicatorOpenP, anchor= "center")
    lblIndicatorOpen.image = indicatorOpenP 
    
    imageIndicatorClosed = Image.open(basePath / "Images" / "MenuBar" / "indicatorClosed.png")
    indicatorClosedSized = imageIndicatorClosed.resize((xSize,ySize))
    indicatorClosedP = ImageTk.PhotoImage(indicatorClosedSized)
    lblIndicatorClosed = tk.Label(frameMenuBar, image = indicatorClosedP, anchor= "center")
    lblIndicatorClosed.image = indicatorClosedP 

    return lblRoad, lblWater, lblElectric, lblWaste, lblEducation, lblTransport, lblPolice, lblFireDep, lblHealth, lblEntertainment, lblShopping, lblIndicatorOpen, lblIndicatorClosed

def createRoadIcons(frameSelectedItem):

    xSize = 50
    ySize = 50

    imageRoadCity = Image.open(basePath / "Images" / "MenuBar" / "MenuStreets" / "streetCity.png")
    roadCitySized = imageRoadCity.resize((xSize,ySize))
    roadCityP = ImageTk.PhotoImage(roadCitySized)
    lblRoadCity = tk.Label(frameSelectedItem, image = roadCityP, anchor= "center", background="grey")
    lblRoadCity.image = roadCityP
    
    imageRoadIntercity = Image.open(basePath / "Images" / "MenuBar" / "MenuStreets" / "streetIntercity.png")
    roadIntercitySized = imageRoadIntercity.resize((xSize,ySize))
    roadIntercityP = ImageTk.PhotoImage(roadIntercitySized)
    lblRoadIntercity = tk.Label(frameSelectedItem, image = roadIntercityP, anchor= "center", background="grey")
    lblRoadIntercity.image = roadIntercityP
    
    imageMotorway = Image.open(basePath / "Images" / "MenuBar" / "MenuStreets" / "motorway.png")
    motorwaySized = imageMotorway.resize((xSize,ySize))
    motorwayP = ImageTk.PhotoImage(motorwaySized)
    lblMotorway = tk.Label(frameSelectedItem, image = motorwayP, anchor= "center", background="grey")
    lblMotorway.image = motorwayP
    
    imageParking = Image.open(basePath / "Images" / "MenuBar" / "MenuStreets" / "parking.png")
    parkingSized = imageParking.resize((xSize,ySize))
    parkingP = ImageTk.PhotoImage(parkingSized)
    lblParking = tk.Label(frameSelectedItem, image = parkingP, anchor= "center", background="grey")
    lblParking.image = parkingP
    
    imageParkingLot = Image.open(basePath / "Images" / "MenuBar" / "MenuStreets" / "parkingLot.png")
    parkingLotSized = imageParkingLot.resize((xSize,ySize))
    parkingLotP = ImageTk.PhotoImage(parkingLotSized)
    lblParkingLot = tk.Label(frameSelectedItem, image = parkingLotP, anchor= "center", background="grey")
    lblParkingLot.image = parkingLotP
    
    return lblRoadCity, lblRoadIntercity, lblMotorway, lblParking, lblParkingLot

def createTimeControls(frameTime):
    imagePlay = Image.open(basePath / "Images" / "Time" /  "play.png")
    PlaySized = imagePlay.resize((30,30))
    Play = ImageTk.PhotoImage(PlaySized)
    lblPlay = tk.Label(frameTime, image = Play, anchor= "center")
    lblPlay.image = Play
    lblPlay.grid(column=0,row=0, padx=10)
    
    imagePause = Image.open(basePath / "Images" / "Time" /  "pause.png")
    PauseSized = imagePause.resize((35,35))
    Pause = ImageTk.PhotoImage(PauseSized)
    lblPause = tk.Label(frameTime, image = Pause, anchor= "center")
    lblPause.image = Pause

    imageFF1x = Image.open(basePath / "Images" / "Time" /  "FastForward(1x).png")
    FF1xSized = imageFF1x.resize((25,25))
    FF1x = ImageTk.PhotoImage(FF1xSized)
    lblFF1x = tk.Label(frameTime, image = FF1x, anchor= "center")
    lblFF1x.image = FF1x
    lblFF1x.grid(column=3, row=0, padx=10)

    imageFF2x = Image.open(basePath / "Images" / "Time" /  "FastForward(2x).png")
    FF2xSized = imageFF2x.resize((25,25))
    FF2x = ImageTk.PhotoImage(FF2xSized)
    lblFF2x = tk.Label(frameTime, image = FF2x, anchor= "center")
    lblFF2x.image = FF2x
    
    imageFF3x = Image.open(basePath / "Images" / "Time" /  "FastForward(3x).png")
    FF3xSized = imageFF3x.resize((25,25))
    FF3x = ImageTk.PhotoImage(FF3xSized)
    lblFF3x = tk.Label(frameTime, image = FF3x, anchor= "center")
    lblFF3x.image = FF3x
    
    return lblPlay, lblPause, lblFF1x, lblFF2x, lblFF3x

def createFootballField(ph):
    path = basePath / "Images" / "Football" / "Field.png"
    im = Image.open(path)
    imSized = im.resize((978,638))
    ph.append(ImageTk.PhotoImage(imSized))
    
    path = basePath / "Images" / "Football" / "Ball.png"
    im = Image.open(path)
    imSized = im.resize((35,35))
    ph.append(ImageTk.PhotoImage(imSized))
    
    return ph

def getImages(frameCitybuild):
    imageHouse = Image.open(basePath / "Images" / "house.png")
    houseSized = imageHouse.resize((25,25))
    house = ImageTk.PhotoImage(houseSized)
    lblHouse = tk.Label(frameCitybuild, image = house)
    lblHouse.image = house
    lblHouse.grid(column=0,row=4)
    lblHouseLocal = lblHouse
    
    return lblHouseLocal

def brokenHouse(frameCitybuild):
    imageResidentsLeave = Image.open(basePath / "Images" / "derelict_house_building.png")
    residentsLeaveSized = imageResidentsLeave.resize((25,25))
    residentsLeave = ImageTk.PhotoImage(residentsLeaveSized)
    lblDamagedHouse = tk.Label(frameCitybuild, image = residentsLeave)
    lblDamagedHouse.image = residentsLeave
    
    return lblDamagedHouse

def constructHouse(frameCitybuild):
    imageNewHouse = Image.open(basePath / "Images" / "building_construction.png")
    newHouseSized = imageNewHouse.resize((25,25))
    newHouse = ImageTk.PhotoImage(newHouseSized)
    lblConstructing = tk.Label(frameCitybuild, image = newHouse)
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

def weatherIcon(frameWeather):
    #80 - 100% satisfaction
    imageSunny = Image.open(basePath / "Images" / "Weather" / "sunny.png")
    SunnySized = imageSunny.resize((50,50))
    Sunny = ImageTk.PhotoImage(SunnySized)
    lblSunny = tk.Label(frameWeather, image = Sunny)
    lblSunny.image = Sunny

    #60 - 80% satisfaction
    imageCloudy = Image.open(basePath / "Images" / "Weather" / "barely_sunny.png")
    CloudySized = imageCloudy.resize((50,50))
    Cloudy = ImageTk.PhotoImage(CloudySized)
    lblCloudy = tk.Label(frameWeather, image = Cloudy)
    lblCloudy.image = Cloudy
    
    #40 - 60% satisfaction
    imageRainy = Image.open(basePath / "Images" / "Weather" / "rain_cloud.png")
    RainySized = imageRainy.resize((50,50))
    Rainy = ImageTk.PhotoImage(RainySized)
    lblRainy = tk.Label(frameWeather, image = Rainy)
    lblRainy.image = Rainy
    
    #20 - 40% satisfaction
    imageThunder = Image.open(basePath / "Images" / "Weather" / "thunder_cloud_and_rain.png")
    ThunderSized = imageThunder.resize((50,50))
    Thunder = ImageTk.PhotoImage(ThunderSized)
    lblThunder = tk.Label(frameWeather, image = Thunder)
    lblThunder.image = Thunder
    
    #0 - 20% satisfaction
    imageSnow = Image.open(basePath / "Images" / "Weather" / "snow_cloud.png")
    SnowSized = imageSnow.resize((50,50))
    Snow = ImageTk.PhotoImage(SnowSized)
    lblSnow = tk.Label(frameWeather, image = Snow)
    lblSnow.image = Snow
    
    lblTemperature = tk.Label(text = "")
    
    return lblSunny, lblCloudy, lblRainy, lblThunder, lblSnow, lblTemperature

def blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput):
    #print("BLRED")
    global blinking
    
    residents, businesses, level = Update.loadBlinking()
    
    if blockInput == False:
        Widget = ""
        if residents + businesses * 2 + level[5] * 5 > level[1] * 15:  
            lblWaterdrop["bg"] = 'red'
            frameWater["bg"] = 'red'
            lblWaterStatus["background"] = 'red'
            blinking = True
            if "lblWater" not in Widget:
                Widget += " lblWater"     
        if residents + businesses * 2 + level[5] * 5 > level[2] * 15:  
            lblLightning["bg"] = 'red'
            frameEnergy["bg"] = 'red'
            lblEnergyStatus["background"] = 'red'
            blinking = True
            if "lblEnergy" not in Widget:
                Widget += " lblEnergy"
        if residents + businesses * 2 + level[5] * 5 < level[2] * 15:
            Widget = Widget.replace(" lblEnergy", "")
            blinking = False   
        if residents + businesses * 2 + level[5] * 5 < level[1] * 15:
            Widget = Widget.replace(" Water", "")
            blinking = False
        if Widget != "":
            lblLightning.after(1000, lambda : bgWhite(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, Widget, blockInput))

def bgWhite(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, Widget, blockInput):
    #print("BLWHITE")
    global blinking
    
    if  "lblWater" in Widget:
        lblWaterdrop["bg"] = '#F0F0F0'
        frameWater["bg"] = '#F0F0F0'
        lblWaterStatus["background"] = '#F0F0F0'
    if "lblEnergy" in Widget:
        lblLightning["bg"] = '#F0F0F0'
        frameEnergy["bg"] = '#F0F0F0'
        lblEnergyStatus["background"] = '#F0F0F0'
    lblLightning.after(1000, lambda : blinkRed(residents, businesses, level, lblWaterdrop, frameWater, lblWaterStatus, frameEnergy, lblLightning, lblEnergyStatus, lblPerson, lblMoney, blockInput))

def blinkStadium():
    global count
    lblStadiumLocal["bg"] = '#00EE00'
    if TimeControls.currentHour == 23:
        lblStadiumLocal["bg"] = '#F0F0F0'
    else:
        lblStadiumLocal.after(100, blinkStadium)
    
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


