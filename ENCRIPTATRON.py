import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import pygame 
import tkinter as tk 
import funciones as co
from tkinter import messagebox
from funciones import MusicPlayer

pygame.init()


# Rutas relativas
def resourcePath(relativePath):
   try:
      basePath = sys._MEIPASS
   except:
      basePath = os.path.abspath(".")
   return os.path.join(basePath,relativePath)

music_path = resourcePath('Bach-badinerie-piano-music.mp3')
icon_path = resourcePath('images (1).png')

valores = []
estilo = ('Courier New', 12, 'bold')
def almacenar():
   valores.append(nombre.get())
   nombre.pack_forget()
   CodificatorApp()
def regresarMainWindow():
   for widget in ventana.winfo_children():
      widget.destroy()
   CodificatorApp()
        
def Clean(x):
   x1 = x
   if '"' in x1:
       rutaN = x1.replace('"','')
   else:
      rutaN = x
   return rutaN
 
def cerrarPrograma():
   ventana.destroy()
   
def decodific4r():    
    for widget in ventana.winfo_children():
       if widget != nombre:
        widget.destroy()
    etiqueta5 = tk.Label(text='ingresa la ruta del archivo'.upper(),font=estilo, fg='green',bg='black')
    etiqueta5.pack(pady=10)
    ruta = tk.Entry(ventana,width=40,font=estilo, fg='green',bg='black',highlightcolor='red',highlightbackground='black',highlightthickness=3)
    ruta.pack(pady=10)
    BotonFiles = tk.Button(ventana,text='abrir explorador de archivos',font=estilo,fg='green',bg='black',command=lambda:co.Openfile(ruta))
    BotonFiles.pack(pady=10)
    
    botonTerminar = tk.Button(ventana,text='finalizar',font=estilo, fg='green',bg='black',borderwidth=5, relief='raise',command=lambda:cerrarPrograma())
    botonTerminar.place(relx=1.0,rely=1.0,x=-20,y=-20,anchor='se')
    
    botonMute = tk.Button(ventana,text='mute',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:reproduciendo.stop())
    botonMute.place(relx=1.0,rely=1.0,x=-190,y=-53)
    
    botonRegreso = tk.Button(ventana,text='volver',command=lambda:regresarMainWindow(),font=estilo, fg='green',bg='black',borderwidth=3, relief='raised')
    botonRegreso.place(relx=0.0,rely=1.0,anchor='sw',y=-20,x=10)
       
    boton6 = tk.Button(text='ingresar',command=lambda:modificacion(),font=estilo, fg='green',bg='black')
    boton6.pack(pady=10)
    def modificacion():
        if len(ruta.get()) >=1:  
          confirmacion = messagebox.askquestion('decision','¿deseas modificar el archivo?')
          if confirmacion == 'yes':
            messagebox.showinfo('AVISO','seleccionaste que deseas modificar los valores del archivo\npor tanto el archivo seleccionado sera sobreescrito con el resultado')
            procces2()
            
          else:
            messagebox.showinfo('AVISO','seleccionaste que no deseas que se modifique el archivo\npor tanto no se sobreescribira y solo se mostrara en pantalla')
            procces()
        else:
            messagebox.showerror('ERROR','porfavor ingresa la ruta del archivo')    
        
    
    def procces():
     try:
        Nruta = Clean(ruta.get())
        messagebox.showinfo('resultado',co.decodificador(Nruta))
        messagebox.showinfo('AVISO','se completo la accion satisfactoriamente')
           
     except Exception as i:
        messagebox.showerror('ERROR',f'algo salio mal error:{i}')
        
    def procces2():
     try:
        Nruta = Clean(ruta.get())
        messagebox.showinfo('resultado',co.decodificadorMod(Nruta))
        messagebox.showinfo('AVISO','se completo la accion satisfactoriamente')
           
     except Exception as i:
        messagebox.showerror('ERROR',f'algo salio mal error:{i}')
               

def codific4r():   
    for widget in ventana.winfo_children():
       if widget != nombre:
        widget.destroy()
    etiqueta3 = tk.Label(text='INGRESA LA RUTA DEL ARCHIVO:',font=estilo, fg='green',bg='black')
    etiqueta3.pack(pady=10)
    
    ruta = tk.Entry(ventana,width=40,highlightcolor='red',highlightbackground='black',highlightthickness=3,font=estilo, fg='green',bg='black')
    ruta.pack(pady=10)
    
    BotonFiles = tk.Button(ventana,text='abrir explorador de archivos',font=estilo,fg='green',bg='black',command=lambda:co.Openfile(ruta))
    BotonFiles.pack(pady=10)
    
    boton4 = tk.Button(text='Ingresar',font=estilo, fg='green',bg='black',command=lambda:procces())
    boton4.pack(pady=10)
    
    botonTerminar = tk.Button(ventana,text='finalizar',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:cerrarPrograma())
    botonTerminar.place(relx=1.0,rely=1.0,x=-20,y=-20,anchor='se')
    
    botonMute = tk.Button(ventana,text='mute',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:reproduciendo.stop())
    botonMute.place(relx=1.0,rely=1.0,x=-190,y=-53)
    
    botonRegreso = tk.Button(ventana,text='volver',command=lambda:regresarMainWindow(),font=estilo, fg='green',bg='black',borderwidth=3, relief='raised')
    botonRegreso.place(relx=0.0,rely=1.0,anchor='sw',y=-20,x=10)
    def procces():
     try:
        Nruta = Clean(ruta.get())
        co.codificador(Nruta)
        messagebox.showinfo('AVISO','se completo la accion satisfactoriamente')
     except Exception as i:
        messagebox.showerror('ERROR',f'algo salio mal error:{i}')
          
def CodificatorApp():
   for widget in ventana.winfo_children():
       if widget != nombre:
         widget.destroy()
   etiqueta2 = tk.Label(text=f'¿Que deseas hacer hoy {valores[-1]}?'.upper(), font=estilo, fg='green',bg='black')
   etiqueta2.pack(pady=10)
   
   botonTerminar = tk.Button(ventana,text='finalizar',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:cerrarPrograma())
   botonTerminar.place(relx=1.0,rely=1.0,x=-20,y=-20,anchor='se')
   
   botonMute = tk.Button(ventana,text='mute',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:reproduciendo.stop())
   botonMute.place(relx=1.0,rely=1.0,x=-190,y=-53)
    
   Codific4r = tk.Button(text='ENCRIPTAR',font=estilo, fg='green',bg='black',command=lambda: codific4r())
   Codific4r.pack(pady=10)
    
   Decodific4r = tk.Button(text='DESENCRIPTAR',font=estilo, fg='green',bg='black',command=lambda: decodific4r())
   Decodific4r.pack(pady=10)
   

ventana = tk.Tk()
ventana.geometry('500x500')
ventana.title('ENCRIPTATRON')
ventana.configure(background='black')

etiqueta = tk.Label(ventana,text='ingresa tu nombre:'.upper())
etiqueta.config(font=estilo, fg='green',bg='black')
etiqueta.pack(pady=10)

nombre = tk.Entry(ventana,highlightthickness=3,highlightbackground='black',highlightcolor='white',font=estilo, fg='green',bg='black')
nombre.pack(pady=10)

botonTerminar = tk.Button(ventana,text='finalizar',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:cerrarPrograma())
botonTerminar.place(relx=1.0,rely=1.0,x=-20,y=-20,anchor='se') #comando para poner un objeto en la esquina inferior de la pantalla
#relx y rely van de 0.0 a 1.0, donde 0.0 es el inicio y asi lo podemos ir variando, ademas con x.y podemos ajustarlo para que se desplace un poco


botonListo = tk.Button(ventana,text='Listo',font=estilo, fg='green',bg='black',command=lambda : almacenar() if len(nombre.get())>=1 else messagebox.showerror('ERROR','porfavor ingresa tu nombre en el campo en blanco'),bd=4,relief='raised')
botonListo.pack(pady=10)
icon = tk.PhotoImage(file=icon_path)
ventana.iconphoto(True, icon)

reproduciendo = co.MusicPlayer(music_path)

botonMute = tk.Button(ventana,text='mute',font=estilo, fg='green',bg='black',borderwidth=3, relief='raise',command=lambda:reproduciendo.stop())
botonMute.place(relx=1.0,rely=1.0,x=-190,y=-53)
ventana.mainloop()
  
