from artista import Artista


class Banda(Artista):

    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print("La banda", self.nombre, "con", self.integrantes,
              "integrantes toca un poderoso solo de guitarra.")