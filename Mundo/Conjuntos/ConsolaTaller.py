from Mundo.Conjuntos.ConjuntosTaller import conjunto1, conjunto2


def mostrar_menu_de_inicio():
    print("""
    \n       ========================================================
       |DESARROLLO DE PUNTOS A Y B DE "MOMENTO EVALUATIVO #3" |
       ========================================================
       |                                                      |
       |     MENU DE OPCIONES:                                |
       |                                                      |
       ========================================================
       |                                                      |
       |      1: OBSERVAR PUNTO A                             |
       |      2: OBSERVAR PUNTO B                             |
       |                                                      |
       ========================================================                                  
    """)


def opciones():
    opciones_de_puntos = {
        "1": conjunto1,
        "2": conjunto2
    }
    return opciones_de_puntos


opciones1 = opciones()


def ejecutar():
    while True:
        mostrar_menu_de_inicio()
        opcion = input("""
            SELECCIONE UNA OPCIÓN: """)

        funcion = opciones1.get(opcion)
        if funcion is not None:
            funcion()
