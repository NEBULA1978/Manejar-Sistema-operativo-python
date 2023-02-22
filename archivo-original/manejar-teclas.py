import pyautogui

# Pulsar intro
pyautogui.press("enter")

# Copiar y pegar
pyautogui.hotkey('ctrl','v')

# Mover el cursor del mouse a las coordenadas (x=100, y=100) en 2 segundos
pyautogui.moveTo(100, 100, duration=2)

# Hacer clic con el botón izquierdo del mouse en las coordenadas (x=100, y=100)
pyautogui.click(100, 100, button='left')

# Escribir "Hola, mundo!" en el teclado
pyautogui.write('Hola, mundo!')

# Esperar 1 segundo
pyautogui.sleep(1)

# Presionar y mantener la tecla 'shift'
pyautogui.keyDown('shift')

# Escribir 'hola' con mayúsculas
pyautogui.write('hola', interval=0.25)

# Soltar la tecla 'shift'
pyautogui.keyUp('shift')

# Capturar una captura de pantalla y guardarla como 'captura.png'
pyautogui.screenshot('captura.png')

# Mover el cursor del mouse a las coordenadas (x=200, y=200) en 1 segundo y hacer clic derecho
pyautogui.moveTo(200, 200, duration=1)
pyautogui.click(button='right')

# Escribir una secuencia de teclas: 'ctrl' + 'alt' + 'supr'
pyautogui.hotkey('ctrl', 'alt', 'delete')

# Desplazarse hacia abajo en una página web
pyautogui.scroll(-100)

# Mover el cursor del mouse a un color específico en la pantalla y hacer clic
pyautogui.click(pyautogui.locateCenterOnScreen('imagen.png'))

# Cambiar la velocidad de movimiento del cursor
pyautogui.PAUSE = 1

# Obtener la posición actual del cursor del mouse
x, y = pyautogui.position()
print(f"La posición actual del cursor es: x={x}, y={y}")




