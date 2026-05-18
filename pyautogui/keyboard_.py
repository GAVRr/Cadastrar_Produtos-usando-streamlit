# import keyboard
# import pyautogui
# import time

''''Diferente de funções que esperam você apertar e soltar uma tecla, 
a is_pressed() verifica o estado atual da tecla no exato momento
 em que o código passa por aquela linha. Ela retorna um valor booleano:
True: Se a tecla estiver pressionada.
False: Se a tecla não estiver pressionada.'''''

# print("Automação iniciada. Segure 'q' para parar.")
#
# while True:
#     if keyboard.is_pressed('q'):
#         print("Interrupção detectada! Saindo...")
#         break
#
#     # Simula um clique
#     pyautogui.click()
#     time.sleep(0.1)

# -------------------------------------------------------------
'''Ela é uma função de callback. Isso significa que você diz ao Python: "Toda vez que a tecla X for apertada,
 pare o que estiver fazendo e execute esta função específica".'''

# import keyboard
#
# def minha_funcao(evento):
#     print(f"A tecla {evento.name} foi pressionada!")
#
# # Configura o gatilho
# keyboard.on_press_key("a", minha_funcao)
#
# # Mantém o programa rodando para ouvir o teclado
# keyboard.wait("esc")

# -------------------------------------------------------------
'''Supressão de Teclas (suppress)
Você pode impedir que o Windows ou o aplicativo que você está usando receba o comando da tecla.
 Por exemplo, você pode "sequestrar" a tecla de volume para fazer outra coisa:'''

import keyboard

#
#keyboard.add_hotkey('windows', lambda: print('Menu iniciar bloqueado!'), suppress=True)
#
#
#keyboard.wait('esc')

#---------------------------------------------------------------------------------------
'''Se a sua função precisar de parâmetros, você pode passá-los diretamente na add_hotkey:'''

# import keyboard
# def saudar(nome):
#    print(f"Olá, {nome}!")
# #
# keyboard.add_hotkey('windows', lambda: print('Menu iniciar bloqueado!'), suppress=True)
# keyboard.add_hotkey('windows+z', saudar, args=['Mundo'])
# #
# keyboard.wait('esc')