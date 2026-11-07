def iniciar_festival(lista_artistas):

    print("\nFESTIVAL DE MUSICA")
    print("------------------------------")

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()

        print("------------------------------")
        print("Fin de la actuación")
        print("------------------------------")