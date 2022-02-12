import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

# screen resolution
# set the weight and height to your resolution
class screen:   
    weight = 2560
    height = 1440

flag = "pulled"

# template images
# if needed, create your own template images
template = cv2.imread("template.png", 0)
poplavok = cv2.imread("poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "starting a bot")
time.sleep(5)

while(1):
    if flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod [1]")
        pyautogui.keyDown('e')
        time.sleep( random.uniform( 0.25, 0.55 ))
        pyautogui.keyUp('e')
        flag = "thrown"
        time.sleep( random.uniform(4.5, 6.5))        
        
    # screenshot creation
    image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # search pattern on screen
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where( template_coordinates >= 0.7)

    # Based on the search results, either E is pressed or nothing happens and the cycle repeats
    if len(loc[0]) > 0:
        if flag == "thrown":  
            print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
            time.sleep(random.uniform(0.25, 1.0))
            pyautogui.keyDown('e')
            time.sleep( random.uniform( 0.25, 0.55 ))
            pyautogui.keyUp('e')
            flag = "pulled"
            time.sleep(random.uniform(5.5, 7.5))

    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod [2]")
        pyautogui.keyDown('e')
        time.sleep( random.uniform( 0.25, 0.55 ))
        pyautogui.keyUp('e')
        flag = "thrown"
        time.sleep( random.uniform(4.5, 6.5))

    print(strftime("%H:%M:%S", gmtime()), "Not time yet!")