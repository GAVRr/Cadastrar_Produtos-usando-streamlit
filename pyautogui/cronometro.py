import pyautogui as py
from time import sleep, time
sleep(3)
# =============================================
# PASSO 1 — Abre o navegador e vai ao site
# =============================================
py.press('win')       # seleciona a barra de endereço
sleep(0.5)
py.typewrite('bloco de notas', interval=0.08)
py.press('enter')
sleep(3)                     # espera o site carregar

# =============================================
# PASSO 2 — Clica no campo e começa a digitar
# =============================================

frase = 'o rato roeu a roupa do rei de roma'

inicio = time()              # começa o cronômetro

py.typewrite(frase, interval=0.08)   # digita a frase

fim = time()                 # para o cronômetro

# =============================================
# PASSO 3 — Mostra o resultado no terminal
# =============================================
tempo = fim - inicio
print(f'Frase digitada: "{frase}"')
print(f'Tempo total: {tempo:.2f} segundos')
print(f'Velocidade: {len(frase) / tempo:.1f} caracteres por segundo')