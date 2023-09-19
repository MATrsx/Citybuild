from tkinter import *
from tkinter import ttk
import time
import threading

proc = 0
### Klasse 'progressbar'
class progressbar():
  def start_progressbar(self, window):
    ### Erstellung des Ladefensters
    global loadingWindow
    loadingWindow = Toplevel(window)

    ### Position und Kosmetik
    loadingWindow.geometry(f'{300}x{95}+{10}+{10}')
    loadingWindow.overrideredirect(True)
    loadingWindow.lift()
    loadingWindow_frame = Frame(loadingWindow, highlightbackground="black", highlightthickness=2, bg='white')
    loadingWindow_frame.pack()

    ### Ladeanimation
    pb = ttk.Progressbar(loadingWindow_frame, orient='horizontal', mode='indeterminate', length=280)
    pb.pack(padx=10, pady=10)
    loadingWindow_lbl = Label(loadingWindow_frame, text="Prozess gestartet.\nBitte warten ...", font=("Arial", 15), bg='white')
    loadingWindow_lbl.pack()

    ### Start progressbar
    threading.Thread(target=pb.start()).start()

  def close_progressbar(self):
    loadingWindow.destroy()

### Klasse 'action_timer'
class action_timer():
  def action_timer_command(self, saveGame):
      saveGame()
      time.sleep(0.25)
      progressbar().close_progressbar()
    
  def action_timer_thread(self, saveGame):
    global proc
    proc = threading.Thread(target=lambda: self.action_timer_command(saveGame))
    proc.start()