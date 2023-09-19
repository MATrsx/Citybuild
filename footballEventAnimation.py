from PIL import ImageTk, Image, ImageSequence
from pathlib import Path
import tkinter as tk
import time


thumbnail = []
count = 0
canvasID = 0

def getImages(canvas, x1, y1, image):
    global thumbnail, canvasID, count 
    
    thumbnail = []
    canvasID = 0
    count = 0
    
    basePath = Path(__file__).parent
    path = basePath / "Images" / "Football" / image
    
    with Image.open(path) as gif:
        index = 0
        frames = []
        image = ImageTk.PhotoImage(gif)
        thumbnail.append(image)
        canvasID = canvas.create_image(x1, y1, image= thumbnail)
        while True:
            try:
                gif.seek(index)
                gif.resize((50,50))
                frame = ImageTk.PhotoImage(gif)
                frames.append(frame)
            except EOFError:
                break
                
            index += 1
            
        return frames

def playGif(canvas, window, frames):
    global count
    
    if count < len(frames) - 1:
        window.after(75, nextFrame, canvas, window, frames)
        
def nextFrame(canvas, window, frames):
    global count, canvasID
    
    canvas.itemconfig(
        canvasID,
        image = frames[count]
    )
    
    count += 1
    playGif(canvas, window, frames)

def loadAnimation(canvas, x1, y1, image):
    frames = getImages(canvas, x1, y1, image)
    return frames

def showAnimation(canvas, window, frames):
    global count
    count = 0
    playGif(canvas, window, frames)

def removeFromCanvas(canvas):
    global thumbnail, canvasID
    
    thumbnail = []
    canvasID = 0
    canvas.delete(canvasID)

def resizeGif(frames):
    # Output (max) size
    size = 50, 50

    # Open source
    im = Image.open(Path(__file__).parent / "Images" / "Football" / "REDCard.gif")

    # Get sequence iterator
    frames = ImageSequence.Iterator(im)

    # Wrap on-the-fly thumbnail generator
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

    # Save output
    om = next(frames) # Handle first frame separately
    om.info = im.info # Copy sequence info
    om.save(Path(__file__).parent / "Images" / "Football" / "Output.gif", save_all=True, append_images=list(frames))
