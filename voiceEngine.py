#! usr/bin/python
import pytz, time
import speech_recognition as sr 
import pyaudio
import threading
import subprocess
from multiprocessing import process
from voiceCommands import *


def engine(source, r):
    audio=r.listen(source)
    test=None
    test=str(r.recognize(audio))
    switch(test)


def main():
    r=sr.Recognizer()
    r.energy_threshold=800
    r.pause_threshold=0.3
    r.quiet_duration=0.3
    with sr.Microphone() as source:
        try:
             t=threading.Thread(target=engine(source,r))
             t.daemon=True 
             #engine(source,r)
             t.start()
        except LookupError:
            print("No voice detected")

if __name__ == "__main__":main()
