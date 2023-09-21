import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from pathlib import Path
import Images, footballEventAnimation
import random

target = False
currentFieldLocal = 5
currentBallX = 510
currentBallY = 340
ph = []
shots = [1,2,3]
fieldParts = [
    (23,63,98,613), 
    (98,63,206,613),
    (206,63,310,613),
    (310,63,417,613),
    (417,63,509,613),
    (509,63,605,613),
    (605,63,709,613),
    (709,63,816,613),
    (816,63,924,613),
    (924,63,997,613)
    ]
listEnemies = [
    ("Alisson Wunderland", "AWL"),
    ("All the Smallings", "ATS"),
    ("Backstreet Moyes.", "BSM"),
    ("The Big Lewandowski", "TBL"),
    ("Blink-1 Eto'o.", "BEO"),
    ("Call of Guti", "COG")
]

EnemyTeamName = "Global Eleite"
YourTeamName = "City Kickers"


frameOverlayLocal = 0
frameOverlayEventLocal = 0
lblYourTeamLocal = 0
lblEnemyTeamLocal = 0
lblYourScoreLocal = 0
lblEnemyScoreLocal = 0
lblTimeLocal = 0
lblGoalLocal = 0
canvasLocal = 0

playing = True
minutesPlayed = 0
secondsPlayed = 0
count = 0
numberOfFouls = 0

posessionPercent = []

def showOverlay(canvas, window, Ball):
    global frameOverlayLocal,lblYourTeamLocal,lblEnemyTeamLocal,lblYourScoreLocal,lblEnemyScoreLocal,lblTimeLocal,lblGoalLocal,frameOverlayEventLocal
    frameOverlayLocal = frameOverlay = tk.Frame(window)
    frameOverlayEventLocal = frameOverlayEvent = tk.Frame(window)
    lblYourTeamLocal = lblYourTeam = tk.Label(frameOverlay, text = "Your TEAM")
    lblEnemyTeamLocal = lblEnemyTeam = tk.Label(frameOverlay, text = "Enemy TEAM")
    lblYourScoreLocal = lblYourScore = tk.Label(frameOverlay, text = f"{0}")
    lblEnemyScoreLocal = lblEnemyScore = tk.Label(frameOverlay, text = "0")
    lblTimeLocal = lblTime = tk.Label(frameOverlay, text = "Time")
    lblScoreDivider = tk.Label(frameOverlay, text = " - ")
    lblGoalLocal = tk.Label(window, text = "GOAL")  
    frameOverlay.grid(column=0, row=0, sticky = "nswe", columnspan=5, rowspan=2)
    lblYourTeam.grid(column=0,row=0)
    lblEnemyTeam.grid(column=4,row=0)
    lblYourScore.grid(column=1,row=0)
    lblEnemyScore.grid(column=3,row=0)
    lblScoreDivider.grid(column=2,row=0)
    lblTime.grid(column=0,row=1, columnspan=5, sticky= "nswe")
    countTime(3000, window, canvas, Ball)

def showFootballArena(window):
    global ph, canvasLocal
    
    canvas = tk.Canvas(window, height=790, width=1030)
    canvasLocal = canvas
    canvas.create_rectangle(10,10,1010,670, width=5, outline="red")
    canvas.grid(row=2, column=0, rowspan=10, columnspan=10)

    ph = Images.createFootballField(ph)
    Feld = canvas.create_image(510,340,anchor="center",image=ph[len(ph)-2])
    Ball = canvas.create_image(510,340,anchor="center",image=ph[len(ph)-1])
    
    #footballEventAnimation.showAnimation(canvas, window, 65, 38)
    
    showOverlay(canvas, window, Ball)
    footballGame(window, canvas, Ball, 0, 0)

def hideArena():
    global frameOverlayLocal, lblGoalLocal, canvasLocal, playing, count
    playing = False
    count = 11
    canvasLocal.delete("all")
    frameOverlayLocal.destroy()
    lblGoalLocal.destroy()

def footballGame(window, canvas, Ball, moveX, moveY):
    global target, currentFieldLocal, currentBallX, currentBallY, target, playing, posessionPercent
    
    previousPossession = None
    
    #Wer hat Ballbesitz?
    posession = random.randint(0,1)
    posessionPercent.append(posession)
    PosessionYourTeam, PosessionEnemyTeam = calculatePosession(window)
    
    print(currentBallX)
    if posession == 1 and currentBallX == 510 and currentBallY == 340:
        currentFieldLocal = 5
        print("FOUND")
        target = False
    elif posession == 0 and currentBallX == 510 and currentBallY == 340:
        currentFieldLocal = 4
    
    
    
    #Chance für einen Zweikampf
    if previousPossession != posession:
        zweikampf = random.randint(0,1)
        
        #Chance für ein Foul
        foul = random.randint(1,10)
        if foul == 5 and zweikampf == 1 \
            and currentBallX != 510 and currentBallY != 340 \
            and minutesPlayed < 42 or minutesPlayed > 47 and minutesPlayed < 87:
            foulPlay(window, Ball)
            
    previousPossession = posession
    
    if playing == True:
        moveX, moveY = calculateMove(window, posession, zweikampf, canvas, Ball)

        canvas.after(1000, lambda: moveBall(window, canvas, Ball, moveX, moveY))

def foulPlay(window, Ball):
    global width, height, minutesPlayed, canvasLocal, playing, numberOfFouls
    print("FOUL!")
    
    numberOfFouls += 1
    playing = False
    width = 350
    height= 75

    canvasEvent = tk.Canvas(window, height=75, width=350, background="white")
    canvasEvent.grid(column=4,row=8, columnspan=2, sticky="w")

    currentMinute = minutesPlayed + 1 
    
    window.after(0, lambda: canvasLocal.create_text(500,125, text= "FOUL", tags = "FOUL", font= ("Arial", 50)))
    window.after(2000, lambda: canvasLocal.delete("FOUL"))

    canvasCurrentMinute = canvasEvent.create_text(100,33, text=f"{currentMinute}")
    frames = footballEventAnimation.loadAnimation(canvasEvent, 65, 38, "trillerpfeife.gif")
    footballEventAnimation.showAnimation(canvasEvent, frames)      
    canvasEvent.after(6500, lambda: canvasEvent.delete("all"))
    canvasEvent.after(6500, lambda: canvasEvent.grid_forget())
    resumeAfter(0, 7, window, canvasLocal, Ball)
    return 1
    
def resumeAfter(startPause, endPause, window, canvas, Ball):
    global playing, minutesPlayed
    playing = False
    startPause += 1
    if startPause <= endPause:
        window.after(1000, lambda: resumeAfter(startPause, endPause, window, canvas, Ball)) 
    else:
        playing = True
        minutesPlayed += 1
        countTime(3000, window, canvas, Ball)
        footballGame(window, canvas, Ball, 0,0)

def calculatePosession(window):
    global posessionPercent
    posessionYou = 0
    for number in range (0, len(posessionPercent)):
        if posessionPercent[number] == 0:
            posessionYou += 1
    
    PosessionYourTeam = posessionYou / len(posessionPercent) * 100
    PosessionEnemyTeam = (len(posessionPercent) - posessionYou) / len(posessionPercent) * 100
    PosessionYourTeam = round(PosessionYourTeam, 2)
    PosessionEnemyTeam = round(PosessionEnemyTeam, 2)
    print(PosessionYourTeam, PosessionEnemyTeam)
    
    if minutesPlayed == 25 or minutesPlayed == 75 and playing == True:
        playing = False
        showPosession(PosessionYourTeam, PosessionEnemyTeam, window)
    elif minutesPlayed != 25 and minutesPlayed != 75:
        playing = True
        
    return PosessionYourTeam, PosessionEnemyTeam

def showPosession(PosessionYourTeam, PosessionEnemyTeam, window):
    global frameOverlayEventLocal,frameOverlayLocal, YourTeamName, EnemyTeamName
    
    width = 350
    height= 75

    canvasEvent = tk.Canvas(window, height=height, width=width)
    
    canvasPossessionYou = canvasEvent.create_text(65,33,text=f"{PosessionYourTeam} \n{YourTeamName}", justify=tk.LEFT, font= ("Arial", 16))
    canvasPossessionEnemy = canvasEvent.create_text(285,33,text=f"{PosessionEnemyTeam} \n{EnemyTeamName}", justify=tk.RIGHT, font= ("Arial", 16))
    canvasEvent.grid(column=4,row=8, columnspan=2, sticky="w")
    style = ttk.Style()
    style.theme_use('clam')
    TROUGH_COLOR = 'blue'
    BAR_COLOR = 'green'
    style.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, 
                    bordercolor=BAR_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR, 
                    darkcolor=BAR_COLOR)
    prgBarPosession = ttk.Progressbar(
        canvasEvent,
        style= "bar.Horizontal.TProgressbar",
        orient="horizontal",
        length=200,
        mode="determinate",
        value= int(PosessionYourTeam),
        )
    
    bar = canvasEvent.create_window(width/2 - 100, 10, anchor=tk.NW, window=prgBarPosession)
    
    frameOverlayEventLocal.grid(column=4,row=8, padx=100)
    frameOverlayEventLocal.after(5000, lambda: canvasEvent.grid_forget())

def updateScore(side):
    if side == "right":
        lblYourScoreLocal["text"] = int(lblYourScoreLocal["text"]) + 1
        lblYourScoreLocal.grid(column=1,row=0)
    elif side == "left":
        lblEnemyScoreLocal["text"] = int(lblEnemyScoreLocal["text"]) + 1
        lblEnemyScoreLocal.grid(column=3,row=0)

def countTime(gameTime, window, canvas, Ball):
    global playing, minutesPlayed, secondsPlayed
    seconds = gameTime / 60
    seconds = int(seconds)
    if minutesPlayed != 45 or minutesPlayed != 90 and playing == True:
        window.after(seconds, lambda: addSeconds(gameTime, window, canvas, Ball))   
    if minutesPlayed == 45 and playing == True:
        playing = False
        pause(0, window, canvas, Ball)
    if minutesPlayed == 90 and playing == True:
        playing = False

def pause(pauselenght, window, canvas, Ball):
    global playing, minutesPlayed, currentBallX, currentBallY
    pauselenght += 1
    currentBallX = 510
    currentBallY = 340
    reset(canvas, Ball)
    if pauselenght <= 9:
        window.after(1000, lambda: pause(pauselenght, window, canvas, Ball)) 
    else:
        playing = True
        minutesPlayed += 1
        countTime(3000, window, canvas, Ball)
        footballGame(window, canvas, Ball, 0,0)

def addSeconds(gameTime, window, canvas, Ball):
    global minutesPlayed, secondsPlayed, playing
    secondsPlayed += 1
    if secondsPlayed == 60:
        secondsPlayed = 0
        minutesPlayed += 1
    if minutesPlayed < 10:
        minutesPlayed = f"0{minutesPlayed}"
    if secondsPlayed < 10:
        secondsPlayed = f"0{secondsPlayed}"
    if playing == True:
        lblTimeLocal["text"] = f"{minutesPlayed}:{secondsPlayed}"
        lblTimeLocal.grid(column=0,row=1, columnspan=5, sticky= "nswe")
    minutesPlayed = int(minutesPlayed)
    secondsPlayed = int(secondsPlayed)
    countTime(gameTime, window, canvas, Ball)

def shotTaken(shot, window, canvas, Ball, moveX, moveY):
    if shot >= 5 and shot < 8:
        print("GOAL")
        lblGoalLocal["text"] = "GOAL"
        #lblGoalLocal.grid(column=0,row=15)
        if currentFieldLocal == 1:
            canvas.after(2000, lambda: updateScore("left"))
        elif currentFieldLocal == 8:
            canvas.after(2000, lambda: updateScore("right"))
        goalORMiss = "GOAL"
    else:
        lblGoalLocal["text"] = "MISS"
        #lblGoalLocal.grid(column=0,row=15)
        print("MISS")
        goalORMiss = "MISS"
    window.after(2000, lambda: canvas.create_text(500,125, text= goalORMiss, tags = "GOAL", font= ("Arial", 50)))
    window.after(4000, lambda: canvas.delete("GOAL"))

def calculateMove(window, posession, zweikampf, canvas, Ball):
    global currentBallX, currentBallY, currentFieldLocal, shots
    shot = random.randint(1,10)
    
    if currentFieldLocal == 8 and posession == 0:
        if shot < 5:
            moveXTarget = random.randint(940,980)
            moveYTarget = random.randint(50,310)
        elif shot >= 5 and shot < 8:
            moveXTarget = random.randint(940,970)
            moveYTarget = random.randint(325,335)
        elif shot >= 8:
            moveXTarget = random.randint(940,980)
            moveYTarget = random.randint(360,590)
            
        moveX = (moveXTarget - currentBallX) / 10 
        moveY = (moveYTarget - currentBallY) / 10 
        shotTaken(shot, window, canvas, Ball, moveX, moveY)
    elif currentFieldLocal == 1 and posession == 1:
        if shot < 5:
            moveXTarget = random.randint(40,80)
            moveYTarget = random.randint(50,310)
        elif shot >= 5 and shot < 8:
            moveXTarget = random.randint(50,80)
            moveYTarget = random.randint(325,335)
        elif shot >= 8:
            moveXTarget = random.randint(40,80)
            moveYTarget = random.randint(360,590)
            
        moveX = (moveXTarget - currentBallX) / 10
        moveY = (moveYTarget - currentBallY) / 10
        shotTaken(shot, window, canvas, Ball, moveX, moveY)
    elif posession == 1: 
        moveXTarget = random.randint(20 + fieldParts[currentFieldLocal-1][0], fieldParts[currentFieldLocal-1][2] - 20)
        moveYTarget = random.randint(20 + fieldParts[currentFieldLocal-1][1], fieldParts[currentFieldLocal-1][3] - 20)
        moveX = (moveXTarget - currentBallX) / 10
        moveY = (moveYTarget - currentBallY) / 10
    else:
        moveXTarget = random.randint(20 + fieldParts[currentFieldLocal+1][0], fieldParts[currentFieldLocal+1][2] - 20)
        moveYTarget = random.randint(20 + fieldParts[currentFieldLocal+1][1], fieldParts[currentFieldLocal+1][3] - 20)
        moveX = (moveXTarget - currentBallX) / 10
        moveY = (moveYTarget - currentBallY) / 10
    return moveX, moveY

def moveBall(window, canvas, Ball, moveX, moveY):
    global target, currentBallX, currentBallY, currentFieldLocal, count, target, canvasLocal
    count += 1
        
    if count <= 9 and playing == True:
        canvas.move(Ball, moveX, moveY)
        currentBallX += moveX
        currentBallY += moveY
        checkCurrentField(canvas, Ball)
        canvas.after(100, lambda: moveBall(window, canvas, Ball, moveX, moveY))
    elif playing == False:
        reset(canvas, Ball)
        footballGame(window, canvas, Ball, 0, 0)    
    
    
    if count == 10:
        count = 0
        if currentFieldLocal == 0 or currentFieldLocal == 9:
            currentBallX = 510
            currentBallY = 340
            canvas.after(1000, lambda: reset(canvas, Ball))
        footballGame(window, canvas, Ball, 0, 0)
    elif count == 11:
        canvasLocal.destroy()
    
def checkCurrentField(canvas, Ball):
    global fieldParts, currentFieldLocal, currentBallX, currentBallY, target
    
    currentCoords = canvas.coords(Ball)
    
    for x in range (0, len(fieldParts)):
        if currentCoords[0] >= fieldParts[x][0] and currentCoords[0] <= fieldParts[x][2] \
                and currentCoords[1] >= fieldParts[x][1] and currentCoords[1] <= fieldParts[x][3]:
            position = x   
            x0 = fieldParts[position][0]
            y0 = fieldParts[position][1]
            x1 = fieldParts[position][2]
            y1 = fieldParts[position][3]  
            canvas.create_rectangle(x0,y0,x1,y1, width=4, outline="red", tags = "FieldLocal")
            break
    
    if currentFieldLocal != position:
        canvas.delete("FieldLocal")  
        currentFieldLocal = position    
            
        x0 = fieldParts[position][0]
        y0 = fieldParts[position][1]
        x1 = fieldParts[position][2]
        y1 = fieldParts[position][3]
        currentField = canvas.create_rectangle(x0,y0,x1,y1, width=4, outline="red", tags = "FieldLocal")

def reset(canvas, Ball):
    global currentBallX, currentBallY, currentFieldLocal
    currentFieldLocal = 5
    canvas.delete("FieldLocal") 
    currentBallX = 510
    currentBallY = 340
    canvas.coords(Ball, currentBallX, currentBallY) 
