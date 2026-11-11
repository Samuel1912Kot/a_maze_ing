import random
from a_maze_ing_func import (n_remover, s_remover, e_remover, w_remover, matrice_init, 
                             Cell, cell_factory, zone_filler, maze_verifying, parsing_info,
                             parsing_verif, perfect_verif)
from a_maze_ing_unperfect import unperfect_maker
from forty_two_logo import forty_two_logo


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
    if not matrice or not matrice[0]:
        return

    # Bord supérieur
    for cell in matrice[0]:
        if cell.forty_two:
            print("████", end="")
        else:
            print("o---" if cell.north else "o   ", end="")
    print("o")

    for ligne in matrice:
        # Partie supérieure des cellules
        for cell in ligne:
            if cell.forty_two:
                print("████", end="")
            else:
                print("|   " if cell.west else "    ", end="")

        if not ligne[-1].forty_two:
            print("|" if ligne[-1].est else " ", end="")
        else:
            print(" ", end="")
        print()

        # Partie inférieure des cellules
        for cell in ligne:
            if cell.forty_two:
                print("████", end="")
            else:
                print("o---" if cell.south else "o   ", end="")
        print("o")


def a_maze_ing():
    matrice = [[]]
    info = parsing_info("config.txt")
    
    if parsing_verif() is True:
        matrice = matrice_init(int(info["WIDTH"]), int(info["HEIGHT"]))
        while maze_verifying(matrice) != True:
            matrice = wall_finder(matrice)
        if perfect_verif() == True:
            matrice = forty_two_logo(matrice)
            return matrice
        else:
            matrice = forty_two_logo(matrice)
            matrice = unperfect_maker(matrice)
            return matrice

if __name__ == "__main__":
    maze_printer(a_maze_ing())
