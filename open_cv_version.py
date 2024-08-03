import cv2
import numpy as np
import pyautogui
import time
import os

def capture_screenshoot(region=None):
    screenshoot = pyautogui.screenshot(region=region)
    screenshoot = cv2.cvtColor(np.array(screenshoot), cv2.COLOR_BGR2RGB)
    return screenshoot

def find_template_on_screen(template_path, threshold=0.8):
    template = cv2.imread(template_path, 0)
    #print(template.shape)
    weight, height = template.shape[::-1]#invertir ambos shapes desde imagen
    #print(w, h)
    
    
    screen_shoot = capture_screenshoot()
    #screenshoot = pyautogui.screenshot(region=region)
    #screenshoot = cv2.cvtColor(np.array(screenshoot), cv2.COLOR_BGR2RGB)
    screen_gray = cv2.cvtColor(screen_shoot, cv2.COLOR_BGR2GRAY)
    print(screen_gray)
    
    #encontrar mediante la plantilla el elemento en la pantalla
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    print(res.shape)
    loc = np.where(res >= threshold)
    print(loc)
    
    
    

def click_on_screen(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

if __name__ == "__main__":
    for root, dirs, files in os.walk('./resources_example'):
        #print(root, dirs, file)
        for file in files:
            coords = find_template_on_screen(os.path.join(root, file))