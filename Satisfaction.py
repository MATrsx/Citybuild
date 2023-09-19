import Images
import tkinter as tk
import re

def calculateSatisfaction(satisfaction, stage, level, residents, businesses, daysNoEnergy, daysNoWater, frameSatisfaction, taxes):
    """Calculate how satisfied the residents are right now:
        Depending on 
        - Water and Energy Supply
        - Road condition
        - Enough workload/ businesses
            Stage 2:
                - Enough buses (shorter time to wait for a bus)
                - Event outcomes
            Stage 3:
                - High education
    """
    
    if stage >= 1:
        if residents + businesses * 2 + level[5] * 5 > level[1] * 15:
            daysNoWater += 1
            
            if daysNoWater >= 3:
                satisfaction -= 1
        else:
            daysNoWater = 0
            satisfaction += 0.5
        if residents + businesses * 2 + level[5] * 5 > level[2] * 15:
            daysNoEnergy += 1
            
            if daysNoEnergy >= 5:
                satisfaction -= 1
        else: 
            daysNoEnergy = 0
            satisfaction += 0.5
            
    #Calculate satsifaction based on taxes
    satisfaction = round(satisfaction + ((taxes - 10) * 0.1) * -1 , 1)
        
    #Strip the digits if the digit equals 0 (e.g 100.0 -> 100)
    if re.search(".0\Z", str(satisfaction)) != None:
        satisfaction = re.sub('.0\Z', "", str(satisfaction))
        satisfaction = int(satisfaction)
    else:
        satisfaction = float(satisfaction)
    
    if satisfaction > 100:
        satisfaction = 100
    if satisfaction < 0:
        satisfaction = 0
     
    displayIndicatorImage(satisfaction, frameSatisfaction)
    return daysNoEnergy, daysNoWater, satisfaction
        
    #Bus wait time
    
    #Ein bus braucht 100ms von einer 'Siedlung' zur nächsten (1 Siedlung -> 10 Einwohner)
    
def removeFromCanvas(lblGrinning, lblSmiling, lblNeutral, lblFrowning, lblRage):
    lblGrinning.grid_forget()
    lblSmiling.grid_forget()
    lblNeutral.grid_forget()
    lblFrowning.grid_forget()
    lblRage.grid_forget()
    
def displayIndicatorImage(satisfaction, frameSatisfaction):
    lblGrinning, lblSmiling, lblNeutral, lblFrowning, lblRage = Images.satisfactionSmiley(frameSatisfaction)
    
    removeFromCanvas(lblGrinning, lblSmiling, lblNeutral, lblFrowning, lblRage)
    if satisfaction >= 80 and satisfaction <= 100:
        lblGrinning.grid(column=4,row=0, padx=10)
        
    elif satisfaction >= 60 and satisfaction < 80:
        lblSmiling.grid(column=4,row=0, padx=10)
        
    elif satisfaction >= 40 and satisfaction < 60:
        lblNeutral.grid(column=4,row=0, padx=10)
        
    elif satisfaction >= 20 and satisfaction < 40:
        lblFrowning.grid(column=4,row=0, padx=10)

    elif satisfaction >= 0 and satisfaction < 20:
        lblRage.grid(column=4,row=0, padx=10)