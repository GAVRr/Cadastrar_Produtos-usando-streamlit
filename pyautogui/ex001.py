import pyautogui
from time import sleep

pyautogui.PAUSE = 0.3


pyautogui.press('win')
sleep(1)
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')

pyautogui.moveTo(x=893, y=612 , duration= 1)
pyautogui.click(x=893, y=612)
sleep(1)

pyautogui.write('https://www.hashtagtreinamentos.com/')
pyautogui.press('enter')
pyautogui.moveTo(x=609, y=130, duration= 1 )

pyautogui.click(x=609, y=130)
posicao_cursor = pyautogui.locateCenterOnScreen('python_automacao.png',confidence=0.8)
pyautogui.click(posicao_cursor )

#pyautogui.click(x=853, y=288)