"""hacer test y funcion string calculator 
1º tiene que recibir string "1, 2, 3"->6|""->0


"""

def sumarLista(string:str):
    listaNumeros:list[]=string.split(",")
    suma=0
    for numero in listaNumeros:
        suma+=int(numero)
    return suma
if __name__=="__main__":
    pass