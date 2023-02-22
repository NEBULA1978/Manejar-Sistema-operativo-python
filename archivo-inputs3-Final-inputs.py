import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Pedir el nombre de la carpeta a crear
carpeta = ""
while not carpeta:
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
archivo_original = ""
while not archivo_original:
    archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")

# Pedir la cantidad de copias a realizar
num_copias = ""
while not num_copias:
    num_copias = input("Ingrese la cantidad de copias que desea hacer: ")

# SHUTIL (copiar y pegar archivos)
for i in range(int(num_copias)):
    shutil.copy2(archivo_original, f"{archivo_original}_{i+1}.py") 
    print(f"Copia {i+1} de {num_copias} creada exitosamente.")

print("Copias creadas exitosamente.")
