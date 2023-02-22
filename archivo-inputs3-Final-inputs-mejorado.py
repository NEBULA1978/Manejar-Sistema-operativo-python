import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Pedir al usuario si desea crear una carpeta
crear_carpeta = input("¿Desea crear una carpeta? (S/N): ")
if crear_carpeta.lower() == "s":
    # Pedir el nombre de la carpeta a crear
    carpeta = input("Ingrese el nombre de la carpeta que desea crear: ")

    # Verificar si la carpeta ya existe
    if not os.path.exists(carpeta):
        # Crear la carpeta si no existe
        os.mkdir(carpeta)
        print("Carpeta creada exitosamente.")
    else:
        print(f"La carpeta '{carpeta}' ya existe.")
else:
    carpeta = None
    print("No se creará una carpeta.")

# Listar archivos disponibles
print("Archivos disponibles en la carpeta actual:")
for archivo in os.listdir():
    print(archivo)

# Pedir al usuario si desea copiar un archivo
copiar_archivo = input("¿Desea copiar un archivo? (S/N): ")
if copiar_archivo.lower() == "s":
    # Pedir el nombre del archivo a copiar
    archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")

    # Pedir la cantidad de copias a realizar
    num_copias = input("Ingrese la cantidad de copias que desea hacer: ")

    # SHUTIL (copiar y pegar archivos)
    for i in range(int(num_copias)):
        shutil.copy2(archivo_original, f"{archivo_original}_{i+1}.py") 
        print(f"Copia {i+1} de {num_copias} creada exitosamente.")

    print("Copias creadas exitosamente.")
else:
    print("No se copiará ningún archivo.")

# En este caso, el programa primero pregunta si el usuario desea crear una carpeta. Si el usuario ingresa "S", se le solicita que ingrese el nombre de la carpeta y se crea la carpeta si no existe. Si el usuario ingresa "N", no se crea una carpeta.

# Luego, el programa pregunta si el usuario desea copiar un archivo. Si el usuario ingresa "S", se le solicita que ingrese el nombre del archivo y la cantidad de copias que desea realizar, y se copian los archivos. Si el usuario ingresa "N", no se copia ningún archivo.