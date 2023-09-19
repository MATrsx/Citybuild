import tkinter.ttk as ttk
import tkinter as tk

pauseLocal = False
incomeTimeLocal = 10000

def initButtons(window, incomeTime, pause):
    btnNormalSpeed = ttk.Button(master=window, text="1x", command= lambda: normalSpeed(incomeTime, pause))
    btnPauseGame = ttk.Button(master=window, text="Pause", command= lambda: pauseGame(pause))
    btnFastForward2x = ttk.Button(master=window, text="2x", command= lambda: fastForward2x(incomeTime, pause))
    btnFastForward5x = ttk.Button(master=window, text="5x", command= lambda: fastForward5x(incomeTime, pause))
    btnNormalSpeed.grid(column=1, row=25, sticky = tk.NW)
    btnPauseGame.grid(column=0, row=25, sticky = tk.NW)
    btnFastForward2x.grid(column=2, row=25, sticky = tk.NW)
    btnFastForward5x.grid(column=3, row=25, sticky = tk.NW)

def normalSpeed(incomeTime, pause):
    global pauseLocal, incomeTimeLocal
    incomeTime = 10000
    incomeTime = int(incomeTime)
    pause = False
    pauseLocal = pause
    incomeTimeLocal = incomeTime

def pauseGame(pause):
    global pauseLocal
    pause = True
    pauseLocal = True

def fastForward2x(incomeTime, pause):
    global pauseLocal, incomeTimeLocal
    incomeTime = 5000
    incomeTime = int(incomeTime)
    pause = False
    pauseLocal = pause
    incomeTimeLocal = incomeTime
    
def fastForward5x(incomeTime, pause):
    global pauseLocal, incomeTimeLocal
    incomeTime = 2000
    incomeTime = int(incomeTime)
    pause = False
    pauseLocal = pause
    incomeTimeLocal = incomeTime

def checkStatus():
    print(pauseLocal)
    print(incomeTimeLocal)
    return pauseLocal, incomeTimeLocal

def markActiveButton():
    print()
    #Den aktiven Button hervorheben