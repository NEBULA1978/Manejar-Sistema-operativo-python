import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Pedir al usuario si desea ver las carpetas en Home
ver_carpetas = input("¿Desea ver las carpetas disponibles en Home? (S/N): ")
if ver_carpetas.lower() == "s":
    home_dir = "/home/"
    carpetas = os.listdir(home_dir)
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(home_dir, carpeta)
        if os.path.isdir(ruta_carpeta):
            print(f"\nCarpeta: {carpeta}")
            archivos = os.listdir(ruta_carpeta)
            for archivo in archivos:
                print(f"  - {archivo}")
else:
    print("No se mostrarán las carpetas en Home.")

# Pedir al usuario la carpeta y archivo a copiar
carpeta = input("\nIngrese el nombre de la carpeta a copiar: ")
ruta_carpeta = os.path.join(home_dir, carpeta)

if not os.path.exists(ruta_carpeta):
    print(f"La carpeta '{carpeta}' no existe.")
else:
    archivos = os.listdir(ruta_carpeta)
    if len(archivos) == 0:
        print(f"La carpeta '{carpeta}' no contiene archivos.")
    else:
        print(f"\nArchivos disponibles en la carpeta '{carpeta}':")
        for archivo in archivos:
            print(f"  - {archivo}")

        archivo_original = input("Ingrese el nombre del archivo que desea copiar: ")

        # Pedir la cantidad de copias a realizar
        num_copias = input("Ingrese la cantidad de copias que desea hacer: ")

        # SHUTIL (copiar y pegar archivos)
        for i in range(int(num_copias)):
            shutil.copy2(os.path.join(ruta_carpeta, archivo_original), f"{archivo_original}_{i+1}.py") 
            print(f"Copia {i+1} de {num_copias} creada exitosamente.")

        print("Copias creadas exitosamente.")

# En este caso, el programa primero pregunta si el usuario desea ver las carpetas disponibles en Home. Si el usuario ingresa "S", se muestran todas las carpetas en Home y sus archivos.

# Luego, el programa solicita al usuario que ingrese el nombre de la carpeta que desea copiar. Si la carpeta no existe o no contiene archivos, se muestra un mensaje de error. Si la carpeta existe y contiene archivos, se muestran los archivos disponibles y se le solicita al usuario que ingrese el nombre del archivo que desea copiar y la cantidad de copias que desea realizar. Luego, se copian los archivos seleccionados.

