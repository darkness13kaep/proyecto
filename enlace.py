# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:05:15 2022

@author: lab
"""

import webbrowser




boton=(int(input("ingrese la letra:  ")))
def entrada1(event):
    event.self=boton
if boton is True:
    
    webbrowser.open_new_tab("www.google.com\search?q=")   
try:
    
    webbrowser.get("chrome").open_new("www.google.com\search?q=",entrada1)
except webbrowser.Error:
    print( "ESPERE MIENTRAS SE ABRE......")
else:
    print("adios")