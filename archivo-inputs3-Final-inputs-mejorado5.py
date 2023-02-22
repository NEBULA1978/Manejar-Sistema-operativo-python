import os
import shutil

# Obtener la lista de directorios principales del sistema
directorios = ['/home', '/']

print("¿Desea explorar una carpeta?")
opcion = input("s/n: ")

if opcion == "s":
    print("Lista de carpetas disponibles:")
    
    for i, d in enumerate(directorios):
        print(i+1, d)

    while True:
        try:
            directorio_seleccionado = input("Seleccione la carpeta que desea explorar (o presione Enter para omitir este paso): ")
            if not directorio_seleccionado:
                break
            directorio_seleccionado = directorios[int(directorio_seleccionado)-1]
            break
        except (ValueError, IndexError):
            print("Por favor, ingrese una opción válida.")

    if directorio_seleccionado:
        while True:
            # Listar archivos y carpetas disponibles
            print("Archivos y carpetas disponibles en la carpeta '{}'".format(directorio_seleccionado))
            contenido = os.listdir(directorio_seleccionado)
            for elemento in contenido:
                print(elemento)
            opcion = input("Seleccione un elemento para explorar o presione Enter para volver atrás: ")
            if not opcion:
                break
            ruta_seleccionada = os.path.join(directorio_seleccionado, opcion)
            if os.path.isdir(ruta_seleccionada):
                directorio_seleccionado = ruta_seleccionada
            elif os.path.isfile(ruta_seleccionada):
                opcion = input("¿Desea leer el archivo o copiarlo? (l/c): ")
                if opcion == "l":
                    with open(ruta_seleccionada, "r") as f:
                        print(f.read())
                elif opcion == "c":
                    archivo_copiar = ruta_seleccionada
                    while True:
                        try:
                            num_copias = input("Ingrese la cantidad de copias que desea hacer: ")
                            for i in range(int(num_copias)):
                                shutil.copy(archivo_copiar, os.getcwd())
                            break
                        except ValueError:
                            print("Por favor, ingrese una cantidad válida de copias.")
                else:
                    print("Opción inválida.")
            else:
                print("La opción seleccionada no es un archivo ni una carpeta.")

archivo_seleccionado = input("Ingrese el nombre del archivo que desea copiar (o presione Enter para omitir este paso): ")

if archivo_seleccionado:
    while True:
        try:
            num_copias = input("Ingrese la cantidad de copias que desea hacer: ")
            for i in range(int(num_copias)):
                shutil.copy(os.path.join(directorio_seleccionado, archivo_seleccionado), os.getcwd())
            break
        except ValueError:
            print("Por favor, ingrese una cantidad válida de copias.")
else:
    print("Ha decidido omitir el paso de copiar archivos.")
