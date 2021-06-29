def juego():
    nombre_1, nombre_2 = ingresar_nombres()


def ingresar_nombres():
    nombre_2 = "0"
    while nombre_2 == "0":
        nombre_1 = input("Ingrese el nombre del primer jugador (0 para retroceder)")
        if nombre_1 == "0":
            menu()
        nombre_2 = input("Ingrese el nombre del segundo jugador (0 para retroceder)")
        if nombre_2 != "0":
            return nombre_1, nombre_2


def configuracion():
    select = input("1. Configurar intentos\n2. Regresar\n3. Salir")


def highscores():
    pass


def menu():
    select = input("1. Jugar\n2.Configuración\n3.Highscores\n4.Salir\n")


    if select == "1":
        juego()
        pass
    elif select == "2":
        # configuracion()
        pass
    elif select == "3":
        # highscores()
        pass
    elif select == "4":
        # Salir del programa
        pass
menu()
