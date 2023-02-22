import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Pedir el nombre de la carpeta a crear
carpeta = input("Ingrese el nombre de la carpeta que desea crear (presione Enter para omitir): ")

# Verificar si se ingresó un nombre de carpeta
if carpeta != "":
    # Verificar si la carpeta ya existe
    if not os.path.exists(carpeta):
        # Crear la carpeta si no existe
        os.mkdir(carpeta)
        print("Carpeta creada exitosamente.")
    else:
        print(f"La carpeta '{carpeta}' ya existe.")
else:
    print("Se ha omitido la creación de la carpeta.")

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

# En este código, primero se verifica si se ingresó un nombre de carpeta antes de verificar si la carpeta ya existe o crearla si no existe. Si la entrada del usuario está vacía, se omite la creación de la carpeta y se muestra un mensaje correspondiente.