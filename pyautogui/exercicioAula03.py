from time import sleep
import pyautogui as py



sleep(2)
busca = 'Pyautogui'


py.keyDown('Ctrl')
py.press('Tab')
sleep(2)
py.press('Tab')
sleep(2)
py.keyUp('Ctrl')


