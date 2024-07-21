import pyautogui
import time

print("Presiona Ctrl+C para detener el script.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posición del mouse: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript terminado.")