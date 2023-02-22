import os
import shutil


# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Crear carpetas
os.mkdir("Carpetita")

# Listar archivos lista 
lista = os.listdir()

# SHUTIL (copiar y pegar archivos)

shutil.copy2("archivo.py", "archivo_copia.py") 

