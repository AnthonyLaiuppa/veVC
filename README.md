#voiceEngine

A simple engine using a combination of libraries to pull information and
relay it to the user.

Im working on integrating it with a raspberry Pi that has a touch screen 
so I can create a display to go with the voice feature

Currently you ask ask it for the date, time and weather. You can also ask it a phrase with the the words 'today + like' and itll give
all three of those at once. In order to use the program launch Display.py as root, then click start jarvis and say jarvis. Any time
after that and he will vocalize a response. Im not sure why but you have to give him Jarvis the first time you click Start Jarvis. Its
a problem with the engine that vocalizes responses. 

#Dependencies 

-BeautifulSoup4

-Mechanize

-AudioPy

-SpeechRecognition

-Pyttsx

-Pytz

#Features to be added-
- [X] GUI for raspberryPi client side
- [ ] Camera code for live weather display
- [ ] Spur for ssh functionality on to communicate with the pi from the server


