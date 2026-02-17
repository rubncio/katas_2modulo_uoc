from main import sumarLista

def testNumero1():
    assert sumarLista(1)==1

def testNumero0():
    assert sumarLista(0)==0

def testNumero123():
    assert sumarLista("1,2,3")==6