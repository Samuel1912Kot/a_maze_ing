import random
from a_maze_ing_func import (n_remover, s_remover, e_remover, w_remover, matrice_init, 
                             Cell, cell_factory, zone_filler, maze_verifying, parsing_info,
                             parsing_verif, perfect_verif)
from a_maze_ing_unperfect import unperfect_maker
from forty_two_logo import forty_two_logo
from a_maze_ing_path_finding import path_inscriptor, bfs


def wall_finder(matrice: list[list]) -> list[list]:
    numero_ligne = random.randint(0, len(matrice) - 1)
    numero_case = random.randint(0, len(matrice[numero_ligne]) - 1)
    i = matrice[numero_ligne][numero_case]
    if i.forty_two:
        return matrice
    direction = random.randint(0, 3)
    if direction == 0:
        if numero_ligne > 0:
            voisin = matrice[numero_ligne - 1][numero_case]
            if not voisin.forty_two and i.zone != voisin.zone:
                matrice = n_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, voisin.zone, i.zone)

    elif direction == 1:
        if numero_ligne < len(matrice) - 1:
            voisin = matrice[numero_ligne + 1][numero_case]
            if not voisin.forty_two and i.zone != voisin.zone:
                matrice = s_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, voisin.zone, i.zone)

    elif direction == 2:
        if numero_case > 0:
            voisin = matrice[numero_ligne][numero_case - 1]
            if not voisin.forty_two and i.zone != voisin.zone:
                matrice = w_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, voisin.zone, i.zone)

    elif direction == 3:
        if numero_case < len(matrice[numero_ligne]) - 1:
            voisin = matrice[numero_ligne][numero_case + 1]
            if not voisin.forty_two and i.zone != voisin.zone:
                matrice = e_remover(matrice, numero_case, numero_ligne)
                matrice = zone_filler(matrice, voisin.zone, i.zone)

    return matrice 


def maze_printer(matrice: list[list]) -> None:
    if not matrice or not matrice[0]:
        return

    # Bord supérieur
    for cell in matrice[0]:
        if cell.forty_two:
            print("█████", end="")
        else:
            print("o----" if cell.north else "o    ", end="")
    print("o")

    for ligne in matrice:
        # Partie supérieure des cellules
        for cell in ligne:
            if cell.forty_two:
                print("█████", end="")
            else:
                print(("|" if cell.west else " ") + "    ", end="")

        if not ligne[-1].forty_two:
            print("|" if ligne[-1].est else " ", end="")
        else:
            print(" ", end="")
        print()

        # Chemin BFS
        for cell in ligne:
            if cell.forty_two:
                print("█████", end="")
            elif cell.path:
                print("  *  ", end="")
            else:
                print("     ", end="")
        print()

        # Partie inférieure des cellules
        for cell in ligne:
            if cell.forty_two:
                print("█████", end="")
            else:
                print("o----" if cell.south else "o    ", end="")
        print("o")


def a_maze_ing():
    matrice = [[]]
    info = parsing_info("config.txt")
    entry_cord = tuple(map(int, info["ENTRY"].split(",")))
    exit_cord = tuple(map(int, info["EXIT"].split(",")))

    if parsing_verif() is True:
        matrice = matrice_init(int(info["WIDTH"]), int(info["HEIGHT"]))
        matrice = forty_two_logo(matrice)
        while maze_verifying(matrice) != True:
            matrice = wall_finder(matrice)
        if perfect_verif() == True:
            path = bfs(matrice, entry_cord, exit_cord)
            matrice = path_inscriptor(matrice, path)
            return matrice
        else:
            matrice = unperfect_maker(matrice)
            path = bfs(matrice, entry_cord, exit_cord)
            matrice = path_inscriptor(matrice, path)
            return matrice

if __name__ == "__main__":
    maze_printer(a_maze_ing())
