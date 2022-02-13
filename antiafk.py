import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

# screen resolution
# set the width and height to your resolution
class screen:  
    #width = 3440
    #width = 2560
    #height = 1440
    width = 2560
    height = 1440

# variables
flag = "pulled"
counter = 1
idletimer = 0

# function to cast fishing rod ingame
def castFishingRod(count):
    print(strftime("%H:%M:%S", gmtime()), f"Casting fishing rod. Counter: {count}")

    # Cast fishing rod ingame
    pyautogui.keyDown('e')
    time.sleep( random.uniform( 0.25, 0.55 ))
    pyautogui.keyUp('e')
    time.sleep( random.uniform(4.5, 6.5)) 

# template images
# if needed, create your own template images
template = cv2.imread("resources/template.png", 0)
poplavok = cv2.imread("resources/poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "Starting the bot in 5 seconds.")
time.sleep(5)

while(1):
    idletimer = idletimer + 1
    if flag == "pulled":
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1
        
    # screenshot creation
    image = pyautogui.screenshot(region=(screen.width/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # search pattern on screen for exclamation point
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where( template_coordinates >= 0.7)

    # Based on the search results, either E is pressed or nothing happens and the cycle repeats
    if len(loc[0]) > 0 and flag == "thrown":
        print(strftime("%H:%M:%S", gmtime()), "Found a fish.")
        idletimer = 0
        time.sleep(random.uniform(0.25, 1.0))

        # Caught fish, press e ingame to reel it in
        pyautogui.keyDown('e')
        time.sleep( random.uniform( 0.25, 0.55 ))
        pyautogui.keyUp('e')

        flag = "pulled"

        # Waiting 8.5-10 minutes to recast.
        waittime = round(random.uniform(500, 600))
        print(f"Waiting {waittime} seconds to recast.")
        time.sleep(waittime)
        flag = "pulled"

    # search pattern on screen for buoy
    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1

    print(strftime("%H:%M:%S", gmtime()), f"Waiting for a fish. Idle timer: {idletimer}. Recast at 500.")
    
    if idletimer == 500:
        print(f"Idle timer reached 500. Recasting now.")
        idletimer = 0

        # Recast
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1