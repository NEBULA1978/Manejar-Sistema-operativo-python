import os
import shutil

# Obtener la ubicacion de trabajo actual
print(os.getcwd())

# Nombre de la carpeta a crear
carpeta = "Carpetita"

# Verificar si la carpeta ya existe
if not os.path.exists(carpeta):
    # Crear la carpeta si no existe
    os.mkdir(carpeta)
    print("Carpeta creada exitosamente.")
else:
    print(f"La carpeta '{carpeta}' ya existe.")

# Listar archivos lista 
lista = os.listdir()

# SHUTIL (copiar y pegar archivos)
shutil.copy2("archivo.py", "archivo_copia.py") 

# GUSANO EN PYTHON COLAPSA EL PC

contador = 0

while contador == 10:
    shutil.copy2("archivo.py", f"script-gusano(contador).py")
    contador+=1

# Atimatizar eliminacion de archivo que cumplan un patron

for archivo in os.listdir():
    if archivo.startswith("script-gusano") == True:
        os.remove(archivo)

# Ejecutar comandos del sistema desde pythons
# Crear un archivo
os.system("touch pruebayeaa")
# Levantar un servidor con python con el puerto 5000
os.system("python3 -m http.server 5000")

