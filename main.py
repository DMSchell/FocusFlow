import tkinter as tk

import notes
import clocks
import timers
import spotify
import upload
import todo
import ai
import dateAndTime

# notes.py
def makeNote():
    notes.instantiateWindow(window, tk)
#clocks.py
def makeClock():
    clocks.instantiateWindow(window, tk)
def makeTimer():
    timers.instantiateWindow(window, tk)
#spotify.py
def makeSpotify():
    spotify.instantiateWindow(window, tk)
#upload.py
def beginSearch():
    upload.findFileToUpload(upload_Label, window, tk)
#todo.py
def makeToDo():
    todo.instantiateWindow(window, tk)
#ai.py
def makeAi():
    ai.instantiateWindow(window, tk)
#calender.py
def makeDateAndTime():
    dateAndTime.instantiateWindow(window, tk)

window = tk.Tk()
window.title("FocusFlow")

frame = tk.Frame(window)
frame.pack(pady=20)

label = tk.Label(frame, text="Set Up Your Widgets!")
label.pack(pady=20)

#layer 1
note_button = tk.Button(frame, text="Make a note!", command=makeNote)
note_button.pack(side=tk.LEFT, padx=5)

spotify_button = tk.Button(frame, text="Spotify player", command=makeSpotify)
spotify_button.pack(side=tk.LEFT, padx=5)

toDo_button = tk.Button(frame, text="To-Do list", command=makeToDo)
toDo_button.pack(side=tk.LEFT, padx=5)

aibutton = tk.Button(frame, text="AI response", command=makeAi)
aibutton.pack(side=tk.LEFT, padx=5)

#layer 2
frame2 = tk.Frame(window)
frame2.pack(pady=20)

time_button = tk.Button(frame2, text="Show time", command=makeClock)
time_button.pack(side=tk.LEFT, padx=5)

timer_button = tk.Button(frame2, text="Show timer", command=makeTimer)
timer_button.pack(side=tk.LEFT, padx=5)

date_button = tk.Button(frame2, text="Show calendar", command=makeDateAndTime)
date_button.pack(side=tk.LEFT, padx=5)

# uploading
upload_Label = tk.Label(window, text="No file selected")
upload_Label.pack(pady=10)

upload_button = tk.Button(window, text="Upload New Widget", command=beginSearch)
upload_button.pack(pady=5)

# extensions
frame3 = tk.Frame(window)
frame3.pack(pady=20)

upload.checkForExtensions(frame3, window, "extensions")


window.mainloop()