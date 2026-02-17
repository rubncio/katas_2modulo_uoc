"""hacer test y funcion string calculator 
1º tiene que recibir string "1, 2, 3"->6|""->0


"""

import re


def sumarstring(string:str):
    listaNumeros=re.split(r'[,\n]', string)
    
    print(listaNumeros)
    suma=0
    
    for numero in listaNumeros:
        if numero.strip():
            suma+=int(numero)
    return suma

if __name__=="__main__":
    print(sumarstring(input()))