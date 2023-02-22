import os
import shutil

# Obtener las carpetas importantes del sistema
home = os.path.expanduser("~")
carpetas_importantes = ["/", home]

# Mostrar las carpetas importantes
print("Carpetas importantes:")
for carpeta in carpetas_importantes:
    print(carpeta)

# Pedir la ruta de la carpeta a explorar
ruta_carpeta = input("Ingrese la ruta de la carpeta que desea explorar (o presione Enter para omitir este paso): ")
if ruta_carpeta:
    # Verificar si la carpeta existe
    if not os.path.exists(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' no existe.")
    else:
        # Listar archivos disponibles
        print(f"Archivos disponibles en la carpeta '{ruta_carpeta}':")
        for archivo in os.listdir(ruta_carpeta):
            print(archivo)

# Pedir el nombre del archivo a copiar
archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")

# Pedir la cantidad de copias a realizar
num_copias = input("Ingrese la cantidad de copias que desea hacer: ")
if num_copias == "":
    print("No se ingresó ningún valor para la cantidad de copias.")
else:
    for i in range(int(num_copias)):
        shutil.copy2(archivo_original, f"{archivo_original}_{i+1}.py") 
        print(f"Copia {i+1} de {num_copias} creada exitosamente.")

print("salimos exitosamente.")


# En este caso, el código muestra solo las carpetas principales tanto en la raíz como en el directorio de inicio del usuario actual. Después de mostrar las carpetas disponibles, se le pide al usuario que ingrese la ruta de la carpeta que desea explorar (o presione Enter para omitir este paso). Si el usuario ingresa una ruta de carpeta, se muestran los archivos disponibles en la carpeta, de lo contrario, se omitirá esta parte del proceso y se continuará con la pregunta del archivo a copiar.