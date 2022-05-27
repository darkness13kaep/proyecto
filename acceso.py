# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:32:30 2022

@author: USUARIO
"""

print("")
print("")
print("")
print("ESTE ES EL SISTEMA DE SEGURIDAD PARA EL USO DE LA APP:")
print("")
print("")
print("")



print(" solicite su clave de acceso luego de ingresar su usario")


personas_autorizadas = [ "Andres"]
nombre = input("Dígame su nombre: ")
if nombre not in personas_autorizadas:
    print("Se ha cerrado.....",exit())
else:print("")
from generador import*

lock = [CLAVE ] 
clave = input("Ingrese su clave temporal: ")        
print("")
if clave not in lock:
    print("Se ha cerrado.....",exit())
else:
    import calculadora
    p = calculadora.Punto()



