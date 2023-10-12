class Empleado:
    def __init__(self, nombre ,rut, fecha_nacimiento ,usuario ,contraseña):
        self.nombre = nombre
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contraseña = contraseña

    def inicio_secion(self):
        if self.usuario == "matias" and self.contraseña == "1234":
            print("Se inicio secion correctamente")
        else:
            print("esta mal el usuario o contraseña")
