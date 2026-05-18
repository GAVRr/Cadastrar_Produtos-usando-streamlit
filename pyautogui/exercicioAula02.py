import pyautogui
from time import sleep
import sys
#espera uma mensagem do usuario para iniciar o programa
resposta = pyautogui.prompt('Digite a palavra certa para iniciar o programa')

if resposta == 'picanha':
    print('Iniciando....')
    sleep(1)
else:
    print('Palavra errada! encerrando...')
    sys.exit()



# mostra um alerta para o usuário, iniciando o programa logo em seguida

#resposta = pyautogui.alert('Deseja iniciar a automação?')



#espera uma confirmação do usuário para iniciar o programa

#resposta = pyautogui.confirm('Deseja iniciar a automação?')

# if resposta == 'OK':
#     print("Iniciando a automação...")
#
# elif resposta == 'Cancel':
#     print("Operação cancelada pelo usuário!")
#     sys.exit()



pyautogui.PAUSE = 1

pyautogui.press('win')

pyautogui.write('chrome',interval=0.2)

pyautogui.press('enter')

perfil = pyautogui.moveTo(x=855, y=604, duration=1)

pyautogui.click(perfil)



# tela = pyautogui.locateCenterOnScreen('img_1.png', confidence=0.8)
#
# mover = pyautogui.moveTo(tela, duration=1)
#
# pyautogui.click(mover)

pyautogui.scroll(300)

pyautogui.write('pyautogui',interval=0.2)

pyautogui.press('enter')

link = pyautogui.locateOnScreen('img.png', confidence=0.8)

pyautogui.moveTo(link,duration=1)

pyautogui.click(link)

document = pyautogui.moveTo(x=87, y=258, duration=1)

pyautogui.click(document)
