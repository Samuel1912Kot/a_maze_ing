import random
from a_maze_ing_func import (n_remover, s_remover, e_remover, w_remover, matrice_init, 
                             Cell, cell_factory, zone_filler, maze_verifying, parsing_info,
                             parsing_verif, perfect_verif)
from a_maze_ing_unperfect import unperfect_maker


def wall_finder(matrice: list[list]) -> list[list]:
    numero_ligne = random.randint(0, len(matrice) - 1)
    numero_case = random.randint(0, len(matrice[numero_ligne]) - 1)
    i = matrice[numero_ligne][numero_case]
    direction = random.randint(0, 3)

    if direction == 0:  # Nord
        if numero_ligne > 0:
            if i.zone != matrice[numero_ligne - 1][numero_case].zone:
                matrice = n_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, matrice[numero_ligne - 1][numero_case].zone, i.zone)
    
    elif direction == 1:  # Sud
        if numero_ligne < len(matrice) - 1:
            if i.zone != matrice[numero_ligne + 1][numero_case].zone:
                matrice = s_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, matrice[numero_ligne + 1][numero_case].zone, i.zone)

    elif direction == 2:  # West
        if numero_case > 0:
            if i.zone != matrice[numero_ligne][numero_case - 1].zone:
                matrice = w_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, matrice[numero_ligne][numero_case - 1].zone, i.zone)

    elif direction == 3:  # Est
        if numero_case < len(matrice[numero_ligne]) - 1:
            if i.zone != matrice[numero_ligne][numero_case + 1].zone:
                matrice = e_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, matrice[numero_ligne][numero_case + 1].zone, i.zone)

    return matrice
    

def maze_printer(matrice: list[list]) -> None:
    # Afficher le haut du labyrinthe
    for cell in matrice[0]:
        print("o---", end="")
    print("o")

    for y, ligne in enumerate(matrice):
        # Afficher les cellules et leurs murs ouest/est
        for cell in ligne:
            print("|" if cell.west else " ", end="")
            print("   ", end="")
        print("|" if ligne[-1].est else " ")

        # Afficher les murs sud de chaque cellule
        for cell in ligne:
            print("o---" if cell.south else "o   ", end="")
        print("o")


def a_maze_ing(length: int, height: int):
    matrice = [[]]
    matrice = matrice_init(length, height)
    while maze_verifying(matrice) != True:
        matrice = wall_finder(matrice)
    if perfect_verif() is True:
        return matrice
    else:
        matrice = unperfect_maker(matrice)
        return matrice

if __name__ == "__main__":
    maze_printer(a_maze_ing(30, 30))
