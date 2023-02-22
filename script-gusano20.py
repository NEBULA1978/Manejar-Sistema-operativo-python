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

# Con esta modificación, el programa primero verificará si la carpeta "Carpetita" ya existe. Si la carpeta no existe, se creará y se imprimirá un mensaje indicando que se ha creado exitosamente. Si la carpeta ya existe, se imprimirá un mensaje indicando que la carpeta ya existe y no se intentará crear de nuevo.