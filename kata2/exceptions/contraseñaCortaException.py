class ContraseñaCortaException(Exception):
    def __init__(self):
        super().__init__("La contraseña es demsiado corta, minimo 8 caracteres.")