import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Nombre de la carpeta a crear
carpeta = "Carpetita"

# Verificar si la carpeta ya existe
if not os.path.exists(carpeta):
    # Crear la carpeta si no existe
    os.mkdir(carpeta)
    print("Carpeta creada exitosamente.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")

# Listar archivos lista 
lista = os.listdir()

# SHUTIL (copiar y pegar archivos)
shutil.copy2("archivo.py", "archivo_copia.py") 
