import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

print(strftime("%H:%M:%S", gmtime()), "Starting the bot in 5 seconds.")
time.sleep(5)

screenWidth, screenHeight= pyautogui.size()
# Development: get current mouse position
pyautogui.position()

print(strftime("%H:%M:%S", gmtime()), "Opening pet inventory (ALT + P).")
pyautogui.keyDown('alt')
pyautogui.keyDown('p')
pyautogui.keyUp('p')
pyautogui.keyUp('alt')

# Sleep random amount of time
time.sleep(random.uniform(2.0, 3.0))

# ClRepair Button offset
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