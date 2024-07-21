import pyautogui
import time
import keyboard

click_one = [(330, 585), (335, 585)] #bien pero no cierra correctamente
click_two = [(1202, 603), (1455, 755), (1102, 260)]
click_three = [(330, 504), (330, 660), 
               (916, 526), (918, 580), 
               (916, 635), (916, 700), 
               (916, 760), (916, 820), 
               (916, 881),
               (1190, 526), (1190, 580), 
               (1190, 635), (1190, 700), 
               (1190, 760), (1190, 820), 
               (1190, 881)]

def replay_mouse_clicks(clicks, delay=2):
    for x, y in clicks:
        time.sleep(delay)
        pyautogui.click(x, y)
        print(f"Clic en: {x}, {y}")
        time.sleep(delay)

if __name__ == "__main__":
    print("Reproduciendo clics con un retraso de 4 segundos entre cada uno.")
    replay_mouse_clicks(click_one)
    #replay_mouse_clicks(click_two)#No funciona normalmente desconosco
    replay_mouse_clicks(click_three)