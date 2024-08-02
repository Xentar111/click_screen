import cv2
import numpy as np
import pyautogui
import time
import os

def capture_screenshoot(region=None):
    screenshoot = pyautogui.screenshot(region=region)
    screenshoot = cv2.cvtColor(np.array(screenshoot), cv2.COLOR_BGR2RGB)
    return screenshoot

def click_on_screen(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

if __name__ == "__main__":
    for root, dirs, file in os.walk('./resources_example'):
        #print(root, dirs, file)