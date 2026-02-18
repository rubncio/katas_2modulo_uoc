import pytest
from main import validarContrasena
from exceptions.password_Exception import ContrasenaCortaException, ContrasenaSinNumeroException

def test_contrasena_Valida():
    assert validarContrasena("123456789")

def test_contrasena_Invalida7c():
    with pytest.raises(ContrasenaCortaException):
     validarContrasena("1234567")

def test_contrasena_InvalidaNoNumeros():
    with pytest.raises(ContrasenaSinNumeroException):
     validarContrasena("aaaaaaaa")

