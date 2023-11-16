# Import the required libraries
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pathlib import Path

listFields = []
listImages = []
rotatedFields = []
activeLabel = ""
rotation = 0
menuOpened = False

ph = [] #keep photoimage instances separate
basePath = Path(__file__).parent
canvasLocal = ""
lblStreetsLocal = ""
lblHousesLocal = ""
lblMenuBarLocal = ""

def saveCanvas(canvas, lblStreets, lblHouses, lblMenuBar):
    global canvasLocal, lblHousesLocal, lblStreetsLocal, lblMenuBarLocal
    canvasLocal = canvas
    lblStreetsLocal = lblStreets
    lblHousesLocal = lblHouses
    lblMenuBarLocal = lblMenuBar
    
def getCanvas():
    global canvasLocal
    return canvasLocal

def getLabel():
    global lblHousesLocal, lblStreetsLocal, lblMenuBarLocal
    return lblStreetsLocal, lblHousesLocal, lblMenuBarLocal

# Define a function to draw the line between two points
def drawHouse(event):
    global listFields, ph
    x1=event.x
    y1=event.y
    canvas = getCanvas()

    foundField = False
    x1 = round(x1 / 50) * 50
    y1 = round(y1 / 50) * 50
    
    print(x1)
    print(y1)
    
    for x in listFields:
        if f"{x1} {y1}" in x:
            foundField = True         
            
    if foundField == False and x1 >= 50 and y1 >= 50 and x1 < 500 and y1 < 500:
        path = basePath / "Images" / "City" / "Haus.png"
        im = Image.open(path)
        houseSized = im.resize((50,50))
        ph.append(ImageTk.PhotoImage(houseSized))
        tag = str(x1) + " " + str(y1) + " " + "House"
        canvasImage = canvas.create_image(x1,y1,anchor="center",image=ph[len(ph)-1])
        listImages.append(tag)
        listFields.append(f"{x1} {y1}")
    else:
        canvas.create_rectangle(x1-25,y1-25,x1+25,y1+25, width=3, outline="red", tags= "Warn")
        canvas.after(250, lambda: canvas.delete("Warn"))

def drawStreet(event):
    global listFields, listImages, ph
    x1=event.x
    y1=event.y
    canvas = getCanvas()

    foundField = False
    x1 = round(x1 / 50) * 50
    y1 = round(y1 / 50) * 50
    
    print(x1)
    print(y1)
    
    for x in listFields:
        if f"{x1} {y1}" in x:
            foundField = True         
            
    if foundField == False and x1 >= 50 and y1 >= 50 and x1 < 500 and y1 < 500:
        path = basePath / "Images" / "City" / "StreetGerade.png"
        im = Image.open(path)
        houseSized = im.resize((50,32))
        ph.append(ImageTk.PhotoImage(houseSized))
        tag = str(x1) + " " + str(y1) + " " + "Street"
        canvas.create_image(x1,y1,anchor="center",image=ph[len(ph)-1], tags= "tag") 
        listImages.append(tag)
        listFields.append(f"{x1} {y1}")
        print(listImages)
    else:
        canvas.create_rectangle(x1-25,y1-25,x1+25,y1+25, width=3, outline="red", tags= "Warn")
        canvas.after(250, lambda: canvas.delete("Warn"))
        
def drawStreetCurved(event):
    global listFields, listImages, ph
    x1=event.x
    y1=event.y
    canvas = getCanvas()
    canvas.bind('<Button-2>', changeRotation)

    foundField = False
    
    streetDown = False
    streetLeft = False
    streetRight = False
    streetUp = False
    x1 = round(x1 / 50) * 50
    y1 = round(y1 / 50) * 50
    
    print(x1)
    print(y1)
    
    for x in listFields:
        if f"{x1} {y1}" in x:
            foundField = True 
        if f"{x1+50} {y1}" in x:
            streetRight = True
        if f"{x1} {y1+50}" in x:
            streetDown = True
        if f"{x1-50} {y1}" in x:
            streetLeft = True
        if f"{x1} {y1-50}" in x:
            streetUp = True
    print(foundField)
    
    if foundField == False and x1 >= 50 and y1 >= 50 and x1 < 500 and y1 < 500:
        path = basePath / "Images" / "City" / "StreetCurved.png"
        im = Image.open(path)
        houseSized = im.resize((50,50))
        if streetDown == True:
            houseSized = houseSized.rotate(90)
        if streetLeft == True:
            houseSized = houseSized.rotate(90)
        if streetUp == True:
            houseSized = curvedStreetRight()
        ph.append(ImageTk.PhotoImage(houseSized))
        tag = str(x1) + " " + str(y1) + " " + "StreetCurved"
        canvas.create_image(x1,y1,anchor="center",image=ph[len(ph)-1], tags= "tag") 
        listImages.append(tag)
        listFields.append(f"{x1} {y1}")
        print(listFields)
    else:
        canvas.create_rectangle(x1-25,y1-25,x1+25,y1+25, width=3, outline="red", tags= "Warn")
        canvas.after(250, lambda: canvas.delete("Warn"))

def curvedStreetRight():
    path = basePath / "Images" / "City" / "StreetCurvedRight.png"
    im = Image.open(path)
    houseSized = im.resize((50,50))
    return houseSized

def openMenu(event):
    global menuOpened
    
    lblStreets, lblHouses, lblMenuBar = getLabel()
    if menuOpened == False:
        lblHouses.grid(column=6, row=25)
        lblStreets.grid(column=5, row=25)
        lblHouses.bind('<Button-1>', buildHouse)
        lblStreets.bind('<Button-1>', buildStreet)
        lblMenuBar["text"] = "Menüleiste\n einklappen"
        lblMenuBar.grid(column=8, row=25)
        menuOpened = True
    elif menuOpened == True:
        lblHouses.grid_forget()
        lblStreets.grid_forget()
        lblHouses.bind('<Button-1>', buildHouse)
        lblStreets.bind('<Button-1>', buildStreet)
        lblMenuBar["text"] = "Menüleiste\n ausklappen"
        menuOpened = False
        
def buildHouse(event):
    global activeLabel
    canvas = getCanvas()
    
    if activeLabel == "Street":
        canvas.unbind('<Button-1>', drawStreet)
    canvas.bind('<Button-1>', drawHouse)
    
def buildStreet(event):
    global activeLabel
    canvas = getCanvas()
    
    if activeLabel == "House":
        canvas.unbind('<Button-1>', drawHouse)
    canvas.bind('<Button-1>', drawStreetCurved)
    canvas.bind('<Button-3>', drawStreet)
    #canvas.bind('<Button-2>', drawStreet)
    
def changeRotation(event):
    global foundField, listFields, ph, rotatedFields, rotation
    x1 = event.x
    y1 = event.y
    canvas = getCanvas()
    
    x1 = round(x1 / 50) * 50
    y1 = round(y1 / 50) * 50
    foundField = False
    type = ""
    sizeX = 50
    sizeY = 50
    
    count = 0
    for x in listFields:
        if f"{x1} {y1}" in x:
            foundField = True
            a, b, type = listImages[count].split(" ")
            print(type)
        count += 1
    
    tag = str(x1) + " " + str(y1) + " " + type
        
    if foundField == True and type != "House":
        rotation += 90
        print(rotation)
        loadPictures(x1, y1, type)
        if type == "StreetCurved":
            path = basePath / "Images" / "City" / "StreetCurved.png"
        elif type == "Street":
            path = basePath / "Images" / "City" / "StreetGerade.png"
            if rotation%180 == 0:
                sizeX = 50
                sizeY = 32
            else:
                sizeX = 32
                sizeY = 50
        im = Image.open(path)
        houseSized = im.resize((sizeX,sizeY))
        houseSized = houseSized.rotate(rotation)
        ph.append(ImageTk.PhotoImage(houseSized))
        listImages.append(tag)
        canvasImage = canvas.create_image(x1,y1,anchor="center",image=ph[len(ph)-1])
        print(listImages)

def loadPictures(x1, y1, type):
    global ph, listImages
    for pic in range (0, len(listImages)):
        print(pic)
        if f"{x1} {y1} {type}" == listImages[pic]:
            ph.remove(ph[pic])
            listImages.remove(f"{x1} {y1} {type}")
            print(ph)
            break

def createCanvas(window):
    # Create an instance of tkinter frame or window
    listFields = []
    listImages = []
    rotatedFields = []
    activeLabel = ""
    rotation = 0

    ph = [] #keep photoimage instances separate
    basePath = Path(__file__).parent
    
    lblMenuBar = tk.Label(text= "Menüleiste\n ausklappen")
    lblMenuBar.grid(column=8, row=25)

    lblStreets = tk.Label(text= "Straßenbau")
    lblHouses = tk.Label(text= "Hausbau")

    # Create a canvas widget
    canvas = tk.Canvas(window, height=510, width=510)
    canvas.create_rectangle(10,10,500,500, width=5, outline="red")
    saveCanvas(canvas, lblStreets, lblHouses, lblMenuBar)
    canvas.grid(row=3, column=5, rowspan=20, columnspan=50)

def createMenuBar():
    lblMenuBar = tk.Label(text= "Menüleiste\n ausklappen")
    lblMenuBar.grid(column=8, row=25)
    lblMenuBar.bind('<Button-1>', openMenu)