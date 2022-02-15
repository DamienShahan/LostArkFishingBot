import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

# screen resolution
screenWidth, screenHeight= pyautogui.size()

# Backup hardcoded width and height
#screenWidth = 2560
#screenHeight = 1440

# Variables
flag = "pulled"
counter = 1
idletimer = 0

# Function to cast fishing rod ingame
def castFishingRod(count):
    print(strftime("%H:%M:%S", gmtime()), f"Casting fishing rod. Counter: {count}")

    # Cast fishing rod ingame
    pyautogui.keyDown('e')
    time.sleep( random.uniform( 0.25, 0.55 ))
    pyautogui.keyUp('e')
    time.sleep( random.uniform(4.5, 6.5))

# Function with all steps to repair the fishing rod through the pet inventory
def repairFishingRod(screenWidth, screenHeight):
    # Open pet inventory
    print(strftime("%H:%M:%S", gmtime()), "Opening pet inventory (ALT + P).")
    pyautogui.keyDown('alt')
    pyautogui.keyDown('p')
    pyautogui.keyUp('p')
    pyautogui.keyUp('alt')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Small repair button offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on Pet Function: remote repair.")
    xOffset = 0.674
    yOffset = 0.641
    moveToX1 = round(screenWidth * xOffset)
    moveToY1 = round(screenHeight * yOffset)
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair All offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on Repair All button.")
    xOffset = 0.384
    yOffset = 0.688
    moveToX2 = round(screenWidth * xOffset)
    moveToY2 = round(screenHeight * yOffset)
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair OK offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on OK button.")
    xOffset = 0.457
    yOffset = 0.578
    moveToX3 = round(screenWidth * xOffset)
    moveToY3 = round(screenHeight * yOffset)
    pyautogui.click(x=moveToX3, y=moveToY3, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX3, y=moveToY3, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(4.0, 5.0))

    # Press ESC
    print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing repair window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Press ESC
    print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing pet window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

# template images
# if needed, create your own template images
template = cv2.imread(f"resources/{screenHeight}/template.png", 0)
poplavok = cv2.imread(f"resources/{screenHeight}/poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "Starting the bot in 5 seconds. Automatic repair every 50 casts.")
time.sleep(5)

while(1):
    idletimer = idletimer + 1
    if flag == "pulled":
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1
        
    # screenshot creation
    image = pyautogui.screenshot(region=(screenWidth/2 - 100, screenHeight/2 - 150, 200, 200))
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
        time.sleep(random.uniform(5.5, 7.5))

    # Repair if modulo 50 and either found a fish, or fully idle
    if counter % 50 == 0 and (idletimer == 500 or flag == "pulled"):
        print(strftime("%H:%M:%S", gmtime()), f"Counter: {counter}. Repairing now. flag: {flag}")
        repairFishingRod(screenWidth, screenHeight)
        counter = counter + 1

    # search pattern on screen for buoy
    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1

    print(strftime("%H:%M:%S", gmtime()), f"Waiting for a fish. Idle timer: {idletimer}. Recast at 500. flag: {flag}")

    if idletimer == 500:
        print(f"Idle timer reached 500. Recasting now.")
        idletimer = 0

        # Recast
        castFishingRod(counter)
        flag = "thrown"
        counter = counter + 1