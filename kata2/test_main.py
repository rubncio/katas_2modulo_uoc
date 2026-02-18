import pytest
from main import validarContraseña
from exceptions.contraseñaCortaException import ContraseñaCortaException

def test_contraseña_Invalida9c():
    assert validarContraseña("123456789")

def test_contraseña_Invalida8c():
    with pytest.raises(ContraseñaCortaException):
     validarContraseña("1234567")
