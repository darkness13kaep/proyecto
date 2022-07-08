# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:47:06 2022

@author: lab
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
def saludar():
    print("¡Hola, mundo!")
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = ttk.Button(text="¡Hola, mundo!", command=saludar)
def aceptar(event):
    import viaje.py
   
boton.bind("<Button-1>",aceptar)
boton.place(x=50, y=50)

image=Image.open("viaje.png")
photo=ImageTk.PhotoImage(image)

boton.pack()

root.mainloop()
