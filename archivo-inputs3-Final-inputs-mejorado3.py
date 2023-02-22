import os
import shutil

# Pedir al usuario si desea ver las carpetas disponibles
ver_carpetas = input("¿Desea ver las carpetas disponibles? (S/N): ")
if ver_carpetas.lower() == "s":
    print("Carpetas disponibles en la raíz ('/'):")
    for dirpath, dirnames, filenames in os.walk('/'):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
    print("Carpetas disponibles en el directorio de inicio del usuario:")
    for dirpath, dirnames, filenames in os.walk(os.path.expanduser('~')):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
else:
    print("No se mostrarán las carpetas disponibles.")

# Pedir al usuario la ruta de la carpeta que desea explorar
carpeta = input("Ingrese la ruta de la carpeta que desea explorar (o presione Enter para omitir este paso): ")
if carpeta and not os.path.exists(carpeta):
    print(f"La carpeta '{carpeta}' no existe.")
else:
    print(f"Archivos disponibles en la carpeta '{carpeta}':")
    for archivo in os.listdir(carpeta):
        print(f"  - {archivo}")

# Pedir al usuario el nombre del archivo a copiar
archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")

# Pedir al usuario la cantidad de copias a realizar
num_copias = input("Ingrese la cantidad de copias que desea hacer: ")

# SHUTIL (copiar y pegar archivos)
for i in range(int(num_copias)):
    shutil.copy2(archivo_original, f"{archivo_original}_{i+1}.py") 
    print(f"Copia {i+1} de {num_copias} creada exitosamente.")

print("Copias creadas exitosamente.")

# En este caso, el código muestra las carpetas disponibles tanto en la raíz como en el directorio de inicio del usuario actual. Después de mostrar las carpetas disponibles, se le pide al usuario que ingrese la ruta de la carpeta que desea explorar (o presione Enter para omitir este paso). Si el usuario ingresa una ruta de carpeta, se muestran los archivos disponibles en la carpeta, de lo contrario, se omitirá esta parte del proceso y se continuará con la pregunta del archivo a copiar.s
