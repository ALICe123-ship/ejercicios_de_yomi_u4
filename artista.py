class Artista:

    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print("\nPresentación del artista")
        print("Nombre:", self.nombre)
        print("Género musical:", self.genero)
        print("Popularidad:", self.popularidad)

    def actuar(self):
        print("El artista realiza su presentación.")

    def despedirse(self):
        print(self.nombre, "agradece al público por asistir.")