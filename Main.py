import sys
from Drone import Drone
import time
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import threading

#here you should interact with the drone
sense = SenseHat()
drone = Drone("192.168.10.1",8889)
drone.connect()
#drone.takeOff()


#Display battery
def bat():
    sense.show_message(drone.battery())
    t = threading.Timer(1, bat)
    t.start()

bat()

MODE = False

def pushed_up(event):
    global MODE
    if event.action != ACTION_RELEASED:
        if MODE:
            drone.up(20)
        else:
            drone.forward(20)

def pushed_down(event):
    global MODE
    if event.action != ACTION_RELEASED:
        if MODE:
            drone.down(20)
        else:
            drone.back(20)

def pushed_left(event):
    global MODE
    if event.action != ACTION_RELEASED and not MODE:
        drone.left(20)
    if event.action == ACTION_PRESSED and MODE:
        drone.takeoff()

def pushed_right(event):
    global MODE
    if event.action != ACTION_RELEASED and not MODE:
        drone.right(20)
    if event.action == ACTION_PRESSED and MODE:
        drone.land()

def pushed_middle(event):
    global MODE
    if event.action == ACTION_PRESSED:
        MODE = not MODE

#&
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle

pause()
