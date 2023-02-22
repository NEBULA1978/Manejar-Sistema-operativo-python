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


# Listar archivos disponibles
print("Archivos disponibles en la carpeta actual:")
for archivo in os.listdir():
    print(archivo)

# Pedir el nombre del archivo a copiar
archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")
archivo_copia = input("Ingrese el nombre que desea para la copia del archivo: ")

# SHUTIL (copiar y pegar archivos)
shutil.copy2(archivo_original, archivo_copia) 
print("Archivo copiado exitosamente.")

# Este código primero lista los archivos disponibles en la carpeta actual utilizando un bucle for y la función os.listdir(). Luego, solicita al usuario el nombre del archivo que desea copiar y el nombre que desea para la copia del archivo. Finalmente, copia el archivo y muestra un mensaje indicando que se ha copiado con éxito.