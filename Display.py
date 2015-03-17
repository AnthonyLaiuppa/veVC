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
    return

def aboutMe():
    webbrowser.open("README.md")
    return

def stopJarvis():
    pass

app = Tk()
app.title("Jarvis")
app.geometry('450x300+200+200')

menubar=Menu(app)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Start Jarvis", command=startJarvis)
filemenu.add_command(label="Live Weather Feed", command=stopJarvis)
filemenu.add_command(label="Quit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=aboutMe)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)
button1=Button(app, text="Start Jarvis", width =20, command= startJarvis)
button1.pack(side='top', padx=15, pady=15)
button2=Button(app, text="Live Weather Feed", width=20, command=stopJarvis)
button2.pack(side='bottom', padx=15, pady=15)
app.mainloop()
