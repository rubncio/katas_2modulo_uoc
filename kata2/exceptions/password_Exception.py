class ContrasenaCortaException(Exception):
    def __init__(self):
        super().__init__("La contraseña es demsiado corta, minimo 8 caracteres.")

class ContrasenaSinNumeroException(Exception):
    def __init__(self):
        super().__init__("La contraseña debe contener al menos un numero.")

    