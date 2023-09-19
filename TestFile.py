from tkinter import *
from tkinter import ttk
import time
import threading

window = Tk()
window.title("Progressbar")

### Window size
window_width = 300
window_height = 50

### Screen dimension, center point and positioning of the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/4 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


### Klasse 'progressbar'
class progressbar():
  def start_progressbar(self):
    ### Erstellung des Ladefensters
    global loadingWindow
    loadingWindow = Toplevel(window)

    ### Position und Kosmetik
    loadingWindow.geometry(f'{300}x{95}+{center_x}+{center_y}')
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

  def check_process(self):
    z = proc.is_alive()
    while z is True:
      z = proc.is_alive()
    self.close_progressbar()

  def check_process_thread(self):
    threading.Thread(target=self.check_process).start()

### Klasse 'action_timer'
class action_timer():
  def action_timer_command(self):
    time.sleep(5)

  def action_timer_thread(self):
    global proc
    proc = threading.Thread(target=self.action_timer_command)
    proc.start()


progressbar_btn = Button(window, text="Prozess starten", bg='white', command=lambda: [progressbar().start_progressbar(), action_timer().action_timer_thread(), progressbar().check_process_thread()])
progressbar_btn.pack()

window.mainloop()