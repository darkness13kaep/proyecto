# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:38:25 2022

@author: USUARIO
"""

import random 

from tkinter import *
from tkinter.ttk import *
  
def low(): 
    entry.delete(0, END) 
  
    
    length = var1.get() 
  
    BAJA = "01234"
    MEDIA = "ABCDE01234"
    ALTA = "abcDABCD01234"
    password = "" 
  
    
    if var.get() == 1: 
        for i in range(0, length): 
            password = password + random.choice(BAJA) 
        return password 
  
    
    elif var.get() == 0: 
        for i in range(0, length): 
            password = password + random.choice(MEDIA) 
        return password 
  
    
    elif var.get() == 3: 
        for i in range(0, length): 
            password = password + random.choice(ALTA) 
        return password 
    else: 
        print("ELIGE EL TIPO DE CLAVE") 
  
  
def GENERAR(): 
    password1 = low() 
    entry.insert(10, password1) 
  
  
def COPIAR(): 
    random_password = entry.get() 
    pyperclip.copy(random_password) 
  
  
  
root = Tk() 
var = IntVar() 
var1 = IntVar() 
  
root.title("GENERADOR CLAVE TEMPORAL") 
  
Random_password = Label(root, text="CLAVE") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
  
c_label = Label(root, text="TAMAÑO DE CLAVE") 
c_label.grid(row=1) 
  
copy_button = Button(root, text="COPIAR", command=COPIAR) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="GENERAR", command=GENERAR) 
generate_button.grid(row=0, column=3) 
  
radio_low = Radiobutton(root, text="BAJO", variable=var, value=1) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="MEDIO", variable=var, value=0) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="ALTO", variable=var, value=3) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1) 
  
combo['values'] = (5,6,7,8) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1) 

  
root.mainloop() 