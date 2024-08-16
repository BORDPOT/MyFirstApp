import tkinter as tk
from tkinter import filedialog
import pygame 
class MusicPlayer:
    def __init__(self,ruta):
        pygame.mixer.init()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(loops=-1)
    def stop(self):
        pygame.mixer.music.stop()
        
def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "Error: El archivo no se encuentra en la ruta especificada."
    except IOError:
        return "Error: No se puede leer el archivo."
    except Exception as e:
        return f"Error inesperado: {e}"

def codificador(ruta):
    code = [] #almacena las letras en formato ascci 
    lectura = leer_archivo(ruta)
    for i in lectura:
        code.append(ord(i))
    with open(ruta,'w') as archivo:
        archivo.write(str(code))
    

def decodificador(ruta):
     #aca se almacenan los datos convertidos a ascci
    Lectura = leer_archivo(ruta)
    Lectura = Lectura.strip('[]')
    Lectura = Lectura.split(',') #convertimos los datos de el archivo en una lista
    #procesos
    word = [int(i) for i in Lectura]
    x = [chr (i) for i in word]
    #utilizamos join() para generar un texto legible
    return ''.join(x)

def Openfile(entry):
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        entry.delete(0, tk.END)
        entry.insert(0, archivo)
        
def decodificadorMod(ruta):
    Lectura = leer_archivo(ruta)
    Lectura = Lectura.strip('[]')
    Lectura = Lectura.split(',')
    num = [int(i) for i in Lectura]
    y = [chr(i) for i in num]
    united = ''.join(y)
    with open(ruta,'w') as archivo:
        archivo.write(united)
    return united
                  
#utilizamos .join() para generar un texto legible 'unir el texto'
    



    
    

    
        