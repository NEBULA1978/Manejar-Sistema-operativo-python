import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Pedir el nombre de la carpeta a crear
carpeta = input("Ingrese el nombre de la carpeta que desea crear: ")

# Verificar si la carpeta ya existe
if not os.path.exists(carpeta):
    # Crear la carpeta si no existe
    os.mkdir(carpeta)
    print("Carpeta creada exitosamente.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")

# Pedir el nombre del archivo a copiar
archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")
archivo_copia = input("Ingrese el nombre que desea para la copia del archivo: ")

# SHUTIL (copiar y pegar archivos)
shutil.copy2(archivo_original, archivo_copia) 
print("Archivo copiado exitosamente.")

# Este código primero solicita al usuario el nombre de la carpeta que desea crear. Luego, verifica si la carpeta ya existe y la crea si no existe. A continuación, solicita al usuario el nombre del archivo que desea copiar y el nombre que desea para la copia del archivo. Finalmente, copia el archivo y muestra un mensaje indicando que se ha copiado con éxito.

