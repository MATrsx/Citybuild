import random
import TimeControls, Images, Update
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
import datetime, locale

basePath = Path(__file__).parent
temperature = 20
listForecast = []
listForecastLabel = []
listTemperature = []
frameCitybuildLocal = 0
ph = []
showForecast = False
start = False
tomorrow = 0
pad = (50 - len(str(temperature))) / 2 + 10


lblForecastPos1 = 0
lblForecastPos2 = 0
lblForecastPos3 = 0
lblForecastPos4 = 0
lblForecastPos5 = 0
lblForecastPos6 = 0
lblForecastPos7 = 0
lblTemperaturePos1 = 0
lblTemperaturePos2 = 0 
lblTemperaturePos3 = 0 
lblTemperaturePos4 = 0
lblTemperaturePos5 = 0
lblTemperaturePos6 = 0
lblTemperaturePos7 = 0
frameForecast = 0
lblTemperature = 0
listForecastLabel = []
listTemperatureLabel = []

def initLabels(frameCitybuild):
    global lblForecastPos1, lblForecastPos2, lblForecastPos3, lblForecastPos4, lblForecastPos5, lblForecastPos6, lblForecastPos7, frameForecast, listForecastLabel, lblTemperature
    global lblTemperaturePos1, lblTemperaturePos2, lblTemperaturePos3, lblTemperaturePos4, lblTemperaturePos5, lblTemperaturePos6, lblTemperaturePos7, listTemperatureLabel
    frameForecast = tk.Frame(frameCitybuild)

    lblForecastPos1 = tk.Label(frameForecast)
    lblForecastPos2 = tk.Label(frameForecast)
    lblForecastPos3 = tk.Label(frameForecast)
    lblForecastPos4 = tk.Label(frameForecast)
    lblForecastPos5 = tk.Label(frameForecast)
    lblForecastPos6 = tk.Label(frameForecast)
    lblForecastPos7 = tk.Label(frameForecast)
    lblTemperaturePos1 = tk.Label(frameForecast)
    lblTemperaturePos2 = tk.Label(frameForecast)
    lblTemperaturePos3 = tk.Label(frameForecast)
    lblTemperaturePos4 = tk.Label(frameForecast)
    lblTemperaturePos5 = tk.Label(frameForecast)
    lblTemperaturePos6 = tk.Label(frameForecast)
    lblTemperaturePos7 = tk.Label(frameForecast)
    lblTemperature = tk.Label(frameForecast)
    listForecastLabel = [lblForecastPos1, lblForecastPos2, lblForecastPos3, lblForecastPos4, 
                        lblForecastPos5, lblForecastPos6, lblForecastPos7]
    listTemperatureLabel = [lblTemperaturePos1, lblTemperaturePos2, lblTemperaturePos3, lblTemperaturePos4, 
                            lblTemperaturePos5, lblTemperaturePos6, lblTemperaturePos7]

def removeFromCanvas(lblSunny, lblCloudy, lblRainy, lblThunder, lblSnow):
    lblSunny.grid_forget()
    lblCloudy.grid_forget()
    lblRainy.grid_forget()
    lblThunder.grid_forget()
    lblSnow.grid_forget()
    
def calculateTemperature(weather):
    global temperature, listTemperature
    if weather == 1:
        temperature = temperature + random.randint(1, 3)
    elif weather == 2:
        temperature = temperature + random.randint(-2, 2)
    elif weather == 3:
        temperature = temperature + random.randint(-2, 0)
    elif weather == 4:
        temperature = temperature + random.randint(-5, -2)
    elif weather == 5:
        temperature = temperature + random.randint(-2, 0)
    listTemperature.append(temperature)

def displayCurrentWeather(daysPlayed, frameWeather, frameCitybuild, lblWeatherStatus):
    global listForecast, frameCitybuildLocal, showForecast, listForecastLabel, tomorrow, start, listTemperature, pad, listTemperatureLabel, listTemperature
    month = TimeControls.getCurrentMonth(daysPlayed)
    lblSunny, lblCloudy, lblRainy, lblThunder, lblSnow, lblTemperature = Images.weatherIcon(frameWeather)
    Options = [lblSunny, lblCloudy, lblRainy, lblThunder, lblSnow]
    frameCitybuildLocal = frameCitybuild
    
    weather, activeLabel = weatherForecast(frameCitybuild, month, Options)
    lblWeatherStatus["text"] = f"{listTemperature[0]}°"
    lblWeatherStatus.grid(column=5, row=1, sticky = "nswe", padx=pad)
    if start == False:
        start = True
        initLabels(frameCitybuild)
    
    
    if showForecast == True and listForecastLabel[0] != "":
        ph.clear()
        tomorrow = Update.updateWeatherForecast(listForecastLabel, basePath, listForecast, ph, listTemperatureLabel, listTemperature)
    
    if activeLabel != "":
        removeFromCanvas(lblSunny, lblCloudy, lblRainy, lblThunder, lblSnow)    
    if weather == 1:
        lblSunny.grid(column=5,row=0, padx=10)
        lblSunny.bind("<Button-1>", displayWeatherForecast)
    elif weather == 2:
        lblCloudy.grid(column=5,row=0, padx=10)
        lblCloudy.bind("<Button-1>", displayWeatherForecast)
    elif weather == 3:
        lblRainy.grid(column=5,row=0, padx=10)
        lblRainy.bind("<Button-1>", displayWeatherForecast)
    elif weather == 4:
        lblThunder.grid(column=5,row=0, padx=10)
        lblThunder.bind("<Button-1>", displayWeatherForecast)
    elif weather == 5:
        lblSnow.grid(column=5,row=0, padx=10)
        lblSunny.bind("<Button-1>", displayWeatherForecast)

def weatherForecast(frameCitybuild, month, Options):
    global listForecast, listTemperature, temperature
    activeLabel = ""
    
    if len(listForecast) == 0:
        for x in range (8):
            if month >= 12 or month <= 2:
                if temperature >= 20:
                    weather = random.choice((1,2,3,5))
                else:
                    weather = random.randint(1, 5)
            else:
                if temperature >= 20:
                    weather = random.choice((1,2,3))
                else:
                    weather = random.randint(1, 4)
                
            for x in range (0, len(Options)):
                if Options[x].grid_info() != False:
                    activeLabel = Options[x]
                    break
                
            Fifty50 = random.randint(1, 2)
            if Fifty50 == 1:
                listForecast.append(weather)
                calculateTemperature(weather)
            elif Fifty50 == 2:
                listForecast.append(weather)
                calculateTemperature(weather)
                if weather != 5 and len(listForecast) <= 6:
                    x += 1
                    listForecast.append(weather)
                    calculateTemperature(weather)
                
    else:
        for x in range(1, 8):
            listForecast[x-1] = listForecast[x]
            listTemperature[x-1] = listTemperature[x]
        del listForecast[7]
        del listTemperature[7]
        if month >= 12 or month <= 2:
            if temperature >= 20:
                weather = random.choice((1,2,3,5))
            else:
                weather = random.randint(1, 5)
        else:
            if temperature >= 20:
                weather = random.choice((1,2,3))
            else:
                weather = random.randint(1, 4)
        listForecast.append(weather)
        calculateTemperature(weather)
    
    return listForecast[0], activeLabel

def displayWeatherForecast(event):
    global listForecast, frameCitybuildLocal, ph, showForecast, start, listForecastLabel, tomorrow, listTemperatureLabel, listTemperature
    
    daysPlayed = TimeControls.daysPlayedLocal
    now = datetime.datetime.now()
    
    if showForecast == False:
        path = basePath / "Images" / "Weather"
        frameForecast.grid(column=5, row=2, sticky = "nswe", rowspan=5)
        for x in range (1, 7):
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
        showForecast = True
            
    elif showForecast == True:
        lblForecastPos1.grid_forget()
        lblForecastPos2.grid_forget()
        lblForecastPos3.grid_forget()
        lblForecastPos4.grid_forget()
        lblForecastPos5.grid_forget()
        lblForecastPos6.grid_forget()
        lblForecastPos7.grid_forget()
        frameForecast.grid_forget()
        showForecast = False

