#!/bin/bash

# Comprobamos si el paquete xsel está instalado
if ! command -v xsel &> /dev/null
then
    echo "El paquete xsel no está instalado. Instalando..."
    sudo apt install xsel
fi

# Leemos el archivo de correos electrónicos
if [ -f escribir_correos.txt ]
then
    while read -r email || [ -n "$email" ]
    do
        # Abrimos la página de comprobación de correos electrónicos en una pestaña nueva
        xdg-open "https://haveibeenpwned.com/"

        # Esperamos 3 segundos para que la página se cargue completamente
        sleep 3

        # Copiamos la dirección de correo electrónico actual en el portapapeles
        echo "$email" | xsel -i

        # Simulamos la pulsación de teclas para pegar la dirección de correo electrónico y enviarla al sitio web
        xdotool key ctrl+v
        xdotool key Return
    done < escribir_correos.txt
else
    echo "El archivo 'escribir_correos.txt' no existe en el directorio actual."
    exit 1
fi

# Este script funciona de manera similar al script original en Python. Primero, comprobamos si el paquete xsel está instalado y lo instalamos si no lo está. Luego, leemos el archivo escribir_correos.txt y para cada dirección de correo electrónico en el archivo, abrimos la página de comprobación de correos electrónicos en una pestaña nueva, copiamos la dirección de correo electrónico en el portapapeles, y simulamos la pulsación de teclas para pegar la dirección de correo electrónico y enviarla al sitio web.