### Stockholm

Pequeño ransomware que cifra los archivos de una determinada carpeta local. Se genera una clave de encriptado que se usará para dicho fin.

[ -help ]		Se muestran los comandos disponibles para el programa
[ -silent ]		Silencia el proceso de encriptación de los archivos.
[ -version ]	Muestra la versión del programa.
[ -reverse ]	Descifra los archivos usándolo junto con la clave de descifrado [ ./ramon -reverse + [key] ]

Instalar: 
>python3

>pip3 install cryptography

>pip install --upgrade pip setuptools
