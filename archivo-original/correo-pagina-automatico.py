import os
try:
    import webbrowser
except:
    os.system("pip install webbrowser") # Si no se puede importar webbrowser, se instala con pip

import time
import pyperclip
import pyautogui

try:
    documento = open('escribir_correos.txt', 'r') # Intentamos abrir el archivo 'escribir_correos.txt' en modo lectura.
    documento = documento.read().split('\n')
except FileNotFoundError: # Si se produce un error porque el archivo no existe, mostramos un mensaje de error y salimos del programa.
    print("El archivo 'escribir_correos.txt' no existe en el directorio actual.")
    exit()

for ema1l in documento:
    webbrowser.open_new_tab("https://haveibeenpwned.com/") # Abrir la página de comprobación de correos electrónicos en una pestaña nueva
    time.sleep(3) # Esperar 3 segundos para que la página se cargue completamente

    try:
        pyperclip.copy(ema1l) # Copiar la dirección de correo electrónico actual en el portapapeles
    except:
        os.system("sudo apt install xsel") # Si hay un error al copiar, instalar el programa xsel

    pyautogui.hotkey('ctrl', 'v', interval=0.15) # Simular pulsación de teclas para pegar la dirección de correo electrónico
    pyautogui.press("enter") # Simular pulsación de tecla para enviar la dirección de correo electrónico al sitio web
