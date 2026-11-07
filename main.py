from cantante import Cantante
from dj import DJ
from banda import Banda
from festival import iniciar_festival


def main():

    lista_artistas = []

    cantidad = int(input("¿Cuántos artistas se presentarán? "))

    for i in range(cantidad):

        print("\nArtista", i + 1)

        print("1. Cantante")
        print("2. DJ")
        print("3. Banda")

        tipo = input("Seleccione el tipo de artista: ")

        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1-100): "))

        if tipo == "1":

            cancion = input("Canción más popular: ")

            artista = Cantante(
                nombre,
                genero,
                popularidad,
                cancion
            )

        elif tipo == "2":

            estilo = input("Estilo musical del DJ: ")

            artista = DJ(
                nombre,
                genero,
                popularidad,
                estilo
            )

        elif tipo == "3":

            integrantes = int(input("Número de integrantes: "))

            artista = Banda(
                nombre,
                genero,
                popularidad,
                integrantes
            )

        else:
            print("Tipo de artista no válido.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()