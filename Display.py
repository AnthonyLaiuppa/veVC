from Tkinter import *
from voiceEngine import *
import threading
import subprocess
import webbrowser
from multiprocessing import process

def startJarvis():
    t=threading.Thread(target=main())
    t.daemon=True
    t.start()

def aboutMe():
    t=threading.Thread(target=webbrowser.open("README.md"))
    t.daemon=True
    t.start()

def stopJarvis():
    pass

app = Tk()
app.title("Jarvis")
app.geometry('450x300+200+200')

menubar=Menu(app)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Start Jarvis", command=startJarvis)
filemenu.add_command(label="Stop Jarvis", command=stopJarvis)
filemenu.add_command(label="Quit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=aboutMe)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)

app.mainloop()
