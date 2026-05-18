# import pyautogui as py
# from time import sleep
#
# sleep(2)
#
# py.moveTo(x=830, y=250, duration=1)
# py.press('space')
#
# sleep(1)
#
# while True:
#     # TODO: entrar no em chrome://dino
#
#     x, y = py.position()
#     color = py.pixel(x, y)
#     print(color)
#     if color != (32, 33, 36):
#         py.press('space')
#
import pyautogui as py
from time import sleep

sleep(3)  # tempo pra abrir o Bloco de Notas

# 1. Digita o título
py.typewrite('Meu Primeiro Robo', interval=0.05)
py.press('enter')
py.press('enter')

# 2. Digita uma lista
itens = ['Acorda', 'Escova os dentes', 'Toma cafe', 'Vai pra escola']
for item in itens:
    py.typewrite(f'- {item}', interval=0.08)
    py.press('enter')

py.press('enter')
# # 3. Digita uma frase e seleciona tudo
py.typewrite('Criado por: Gabriel', interval=0.08)
py.press('enter')
py.press('enter')
py.hotkey('ctrl', 'a')



sleep(1)

# # 4. Copia e cola
py.hotkey('ctrl', 'c')
py.press('end')  # vai pro final
py.press('enter')
py.press('enter')
py.hotkey('ctrl', 'v')  # cola de novo

# import pyautogui as py
# from time import sleep
#
# mensagem = 'ogobor o mob mu uos ue'
# correta = mensagem[::-1]
#
# sleep(2)
# py.typewrite(correta, interval=0.08)
