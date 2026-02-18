"""hacer 
1º tdd primero test y codigo y excepciones
validar si contraseña minimo 8 caracteres
devolver si es true si esta bien

"""
from exceptions.contraseñaCortaException import ContraseñaCortaException
def validarContraseña(cadena:str):
    if(len(cadena)<8):
        raise ContraseñaCortaException()
    return True
if __name__=="__main__":
    contraseña=input("Introduzca contraseña: ")
    if validarContraseña(contraseña):
        print("contraseña correcta.")