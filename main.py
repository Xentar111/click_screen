import pyautogui
import time
import keyboard

click_one = [(330, 585), (335, 585)] #bien pero no cierra correctamente
click_two = [(1202, 603)]#, (1455, 755), (1102, 260)]

click_three = [(330, 660), 
               (916, 526), (918, 580), 
               (916, 635), (916, 700), 
               (916, 760), (916, 820), 
               (916, 881),
               (1190, 526), (1190, 580), 
               (1190, 635), (1190, 700), 
               (1190, 760), (1190, 820), 
               (1190, 881)]

click_fourth = [(918, 630), (1179, 630),
                (918, 686), (1179, 686),
                (918, 744), (1179, 744),
                (918, 802), (1179, 802),
                (918, 862), (1179, 862),
                (1440, 361)]

click_five = [(330, 504)]

click_six = [(1378, 440),
             (1378, 440),
             (1251, 849),]

click_seven = [(914, 588)]

click_eight = [(1521, 850)]

click_nine = [(317, 966)]

click_ten = [(505, 555),
             (619, 555),
             (739, 555),
             (866, 555),
             (1000, 555),
             (1106, 555),
             (1242, 555),
             (1362, 555)]#15pixel 8columns, 120pixel 3 row
def replay_mouse_clicks(clicks, delay=1):
    for x, y in clicks:
        pyautogui.moveTo(x, y)
        time.sleep(delay)
        pyautogui.doubleClick(x, y)
        #pyautogui.click(x, y)
        print(f"Clic en: {x}, {y}")
        time.sleep(delay)

def moveto_mouse_clicks(delay=2):
    #for x, y in clicks:
    #    pyautogui.moveTo(x, y, duration=2)
    #    time.sleep(delay)
    #    pyautogui.doubleClick(x, y)
    #    #pyautogui.click(x, y)
    #    print(f"Clic en: {x}, {y}")
    #    time.sleep(delay)
    pyautogui.moveTo(590, 868)
    pyautogui.mouseDown()
    pyautogui.dragTo(684, 513, duration=2)
    pyautogui.mouseUp()
    time.sleep(delay)
    pyautogui.doubleClick(684, 513)
    pyautogui.doubleClick(684, 513)
    pyautogui.doubleClick(684, 513)
    time.sleep(delay)
    

def smooth_scroll_down(amount, steps=10, delay=0.1):
    step_amount = amount // steps
    for _ in range(steps):
        pyautogui.scroll(step_amount)
        time.sleep(delay)

if __name__ == "__main__":
    #for x, y in click_ten:
        #replay_mouse_clicks(clicks=[(x, y)], delay=4)
        #hago scroll y veo de sumarle +3 donde baje
        print("Reproduciendo clics con un retraso de 4 segundos entre cada uno.")
        #replay_mouse_clicks(click_one)
        replay_mouse_clicks(click_two)
        #moveto_mouse_clicks()#No funciona normalmente desconozco
        replay_mouse_clicks(click_three)
        smooth_scroll_down(-500, steps=20, delay=0.05)
        replay_mouse_clicks(click_fourth)
        replay_mouse_clicks(click_five)
        time.sleep(10)
        
        replay_mouse_clicks(click_six)
        replay_mouse_clicks(click_six)
        time.sleep(5)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        time.sleep(4)
        replay_mouse_clicks(click_eight)
        time.sleep(4)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_seven)
        replay_mouse_clicks(click_one)
        #time.sleep(4)
        #replay_mouse_clicks(click_nine)
