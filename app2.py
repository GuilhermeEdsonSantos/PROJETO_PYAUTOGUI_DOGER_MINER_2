# Como usar a função click

# Meu código inicial para o desafio 

'''
import pyautogui

pyautogui.click(x=305,y=406,interval=1,button='right',duration=2)
pyautogui.click(x=384,y=365,clicks=1,interval=1,duration=2)
pyautogui.click(x=595,y=365,clicks=1,button='left',interval=1,duration=2)'
'''

# Meu código para o desafio melhorado
import pyautogui
import time

# Pequena pausa antes do início para evitar cliques acidentais
time.sleep(2)

# Coordenadas organizadas para facilitar a leitura
pos_1 = (305, 406)
pos_2 = (384, 365)
pos_3 = (595, 365)

# Clique com o botão direito
pyautogui.click(x=pos_1[0], y=pos_1[1], interval=1, button='right', duration=2)
time.sleep(1)  # Pequena pausa para garantir a resposta do sistema

# Primeiro clique esquerdo
pyautogui.click(x=pos_2[0], y=pos_2[1], clicks=1, interval=1, duration=2)
time.sleep(1)

# Segundo clique esquerdo
pyautogui.click(x=pos_3[0], y=pos_3[1], clicks=1, button='left', interval=1, duration=2)


