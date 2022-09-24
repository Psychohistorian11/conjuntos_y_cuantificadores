from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3


def conjunto1():
    print("       ========================================================")
    print(f"       \n     "
          f"    Resuelva el siguiente enunciado: (( ¬D ∩ ¬A) ꚛ ¬F)\n")

    B = {15, 100, 40}
    D = {45, 20, 60}
    F = {50, 100, 80, 20}
    U = {30, 50, 0, 15, 100, 40, 10, 80, 70, 45, 20, 60, 55}
    cantidad = 0

    resultado1 = ((U - D) & (U - B) ^ (U - F))

    print(f"         El resultado de: (( ¬D ∩ ¬A) ꚛ ¬F) es:  \n"
          f"         = {resultado1}\n")

    for numero in resultado1:
        cantidad += numero
    print(f"         La cantidad de mujeres que o ni son de estrato 1 ni\n"
          f"         de estrato de estrato 3 o no son mujeres que tienen\n"
          f"         1 hijo es de:  {cantidad}\n")
    print("       ========================================================")

    def lista_BDF():
        lista = [(B - (D | F)), ((B & D) - F), (D - (B | F)), (B & D & F), ((F & B) - D), ((F & D) - B), (F - (B | D))]
        for x in range(len(lista)):
            if lista[x] == set():
                lista[x] = "{vacio}"
        return lista

    list = lista_BDF()

    # Diagrama                                                                      #colores de conjuntos 100,010,001
    diagrama = venn3([2, 2, 1, 2, 1, 1, 1], set_labels=("B", "D", "F"), set_colors=('#3DBB3D', "#34A534", "#339533"))

    diagrama.get_label_by_id("100").set_text(list[0])
    diagrama.get_label_by_id("110").set_text(list[1])
    diagrama.get_label_by_id("010").set_text(list[2])
    diagrama.get_label_by_id("111").set_text(list[3])
    diagrama.get_label_by_id("101").set_text(list[4])
    diagrama.get_label_by_id("011").set_text(list[5])
    diagrama.get_label_by_id("001").set_text(list[6])

    # colores:
    diagrama.get_label_by_id("100").set_color("#1C8CD1")
    diagrama.get_label_by_id("010").set_color("#1C8CD1")
    diagrama.get_label_by_id("001").set_color("#1C8CD1")

    plt.title(U - (B | D | F))
    plt.show()


def conjunto2():
    print("      =========================================================")
    print(f"      \n    "
          f"      Resuelva el siguiente enunciado: (A U ¬E)\n")

    A = {30, 50, 0}
    E = {0, 40, 70, 60}
    U = {30, 50, 0, 15, 100, 40, 10, 80, 70, 45, 20, 60, 55}
    cantidad = 0
    resultado2 = (A | (U - E))
    print(f"          El resultado de: (A U ¬E) es de:\n"
          f"          = {resultado2}\n"
          )
    for numero in resultado2:
        cantidad += numero
    print(f"          La cantidad de mujeres que son de estrato 4 o no\n"
          f"          tienen 2 o más hijos es de: {cantidad}\n")
    print("      =========================================================")

    #Diagrama:
    diagrama = venn2((1, 1, 1), set_labels=("A", "E"), set_colors=('#3DBB3D', '#9D9595', "#3DBB3D"))
    diagrama.get_label_by_id("11").set_text(A & E)
    diagrama.get_label_by_id("10").set_text(A - E)
    diagrama.get_label_by_id("01").set_text(E - A)
    plt.title(U - (A | E))
    plt.show()
