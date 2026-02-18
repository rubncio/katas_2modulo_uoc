"""hacer PasswordValidator
1º tdd primero test y codigo y excepciones
validar si contraseña minimo 8 caracteres
devolver si es true si esta bien
2º debe contener al menos un numero.
"""
import re
from exceptions.password_Exception import ContrasenaCortaException, ContrasenaSinNumeroException


def validarContrasena(cadena:str):
    
    if(len(cadena)<8):
        raise ContrasenaCortaException()
    if(not re.search(r"\d", cadena)):
        raise ContrasenaSinNumeroException()
    return True


if __name__=="__main__":
    contraseña=input("Introduzca contraseña: ")
    if validarContrasena(contraseña):
        print("contraseña correcta.")