print("Welcome to the show selector! V1.0 ACR GAMES LOCAL ENGINE 0.7")
import os
import vlc
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
def setup():
  Animatronic = PiGPIOFactory(host='192.168.1.110')
  Ch1 = LED(2,pin_factory=Animatronic)
  Ch2 = LED(3,pin_factory=Animatronic)
  Ch3 = LED(4,pin_factory=Animatronic)
  Ch4 = LED(5,pin_factory=Animatronic)
  Ch5 = LED(6,pin_factory=Animatronic)
  Ch6 = LED(7,pin_factory=Animatronic)
  Ch7 = LED(8,pin_factory=Animatronic)
  Ch8 = LED(9,pin_factory=Animatronic)
  Ch9 = LED(10,pin_factory=Animatronic)
  Ch10 = LED(11,pin_factory=Animatronic)
  Ch11 = LED(12,pin_factory=Animatronic)
  Ch12 = LED(12,pin_factory=Animatronic)
  Ch13 = LED(14,pin_factory=Animatronic)
  Ch14 = LED(15,pin_factory=Animatronic)
  Ch15 = LED(16,pin_factory=Animatronic)
  Ch16 = LED(17,pin_factory=Animatronic)
#setup()
Aval=os.listdir('./Music/Shows')
print(Aval)
selection=input("what song would you like?")
if not selection in Aval:
  print("Sorry, that song couldn't be found.")
else:
  ready=(Aval.index(selection))
  selection=(Aval[(ready)])
  print(selection)
  dir=("./Music/Shows/"+(selection)+"/")
