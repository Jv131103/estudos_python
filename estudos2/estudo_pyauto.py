import time

import pyautogui

time.sleep(5)  # tempo para você abrir o navegador

pyautogui.write("https://google.com", interval=0.5)
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("Python automation", interval=0.5)
pyautogui.press("enter")
