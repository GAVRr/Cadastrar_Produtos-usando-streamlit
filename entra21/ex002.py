import pyautogui
from time import sleep

from django.utils.duration import duration_string

pyautogui.PAUSE = 0.3
pyautogui.moveTo(x=1179, y=1057, duration=1)
sleep(1)

pyautogui.click(x=1179, y=1057)

sleep(1)

circulo = pyautogui.locateCenterOnScreen('img.png', grayscale= True , confidence= 0.8)

pyautogui.moveTo(circulo.x , circulo.y , 0.5)

alvo = pyautogui.locateCenterOnScreen('img_1.png', grayscale= True , confidence= 0.8)

pyautogui.dragTo(alvo.x , alvo.y , duration= 1)
sleep(0.5)

texto = pyautogui.locateCenterOnScreen('img_2.png', grayscale= True , confidence= 0.8 )

sleep(0.5)
pyautogui.doubleClick(texto)

pyautogui.write('Pronto!!!')

pyautogui.moveRel(xOffset= 200 , yOffset= 100)

pyautogui.click()