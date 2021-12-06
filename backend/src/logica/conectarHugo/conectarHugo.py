#El módulo OS nos da funcionalidades específicas del sistema operativo, como:
# crear una carpeta, listar contenidos de una carpeta, 
# conocer acerca de un proceso, finalizar un proceso,etc
import os 

#El módulo SH nos permite hacer operaciones de alto nivel en archivos y 
# colecciones de archivos. Ej: copiar, mover, eliminar...
import shutil

# Para saber el contenido del directorio del que vamos a copiar
contenido = "Este es el contenido que hay en la carpeta: \n" +  str(os.listdir(f'{os.getcwd()}/archivosMarkdown/'))
print(contenido)
print(os.getcwd())

def conectarHugo():
    
#Establecemos la ruta de origen y destino en variables para manejar mejor el código
    rutaOrigen = f'{os.getcwd()}/archivosMarkdown/'
    rutaDestino =f'{os.getcwd()}/frontend/webProyecto/content/'

#Creamos una lista de los archivos que con contiene la carpeta origen 
# en forma de variable
    archivos = os.listdir(rutaOrigen)

    for archivo in archivos:
        #SHUTIL.COPY copia lo que está en primer lugar, ya sea un archivo específico 
        #o ruta en el lugar que indicamos después de la ",". 
        # Y OS.PATH.JOIN combina uno o más nombres de ruta en una única ruta.
        shutil.copy(os.path.join(rutaOrigen, archivo), rutaDestino)
    
    return conectarHugo


