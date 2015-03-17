#! usr/bin/python

import speech_recognition as sr 
import pyaudio
from voiceCommands import *


def main(source):
    audio=r.listen(source)
    test=None
    test=str(r.recognize(audio))
    switch(test)

if __name__ == "__main__":
    r=sr.Recognizer() 
    r.energy_threshold=800
    r.pause_threshold=0.3
    r.quiet_duration=0.3
    with sr.Microphone() as source:
        while 1:
            try:
                main(source)
            except LookupError:
                print("No sound detected")