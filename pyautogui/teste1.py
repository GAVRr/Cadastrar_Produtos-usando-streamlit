from time import sleep
import pyautogui

pyautogui.PAUSE = 0.3
#pegar posições do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#funções do mouse
sleep(5)
pyautogui.moveTo(x = 575 , y = 124 , duration= 1)
pyautogui.click(x=886, y=248 )
pyautogui.scroll(-200)


#funções do teclado
pyautogui.write('Hello world')
pyautogui.hotkey('ctrl' , 'c')
pyautogui.press('enter')

