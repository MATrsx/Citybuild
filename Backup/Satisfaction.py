import Images
import tkinter as tk

def calculateSatisfaction(stage, level):
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
        level[0]
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