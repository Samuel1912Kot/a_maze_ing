from a_maze_ing_func import n_remover, s_remover, e_remover, w_remover
import random

def cell_wall_count(cell: object) -> int:
    wall_count: int = 0
    if cell.north == True:
        wall_count += 1
    if cell.south == True:
        wall_count += 1
    if cell.est == True:
        wall_count += 1
    if cell.west == True:
        wall_count += 1
    return wall_count


def unperfect_maker(matrice: list[list]) -> list[list]:
    for ligne in range(len(matrice)):
        for c in range(len(matrice[ligne])):

            if cell_wall_count(matrice[ligne][c]) == 3:
                while True:
                    random_break = random.randint(0, 3)
                    if random_break == 0:
                        if ligne > 0 and matrice[ligne][c].north:
                            matrice = n_remover(matrice, c, ligne)
                            break

                    elif random_break == 1:
                        if ligne < len(matrice) - 1 and matrice[ligne][c].south:
                            matrice = s_remover(matrice, c, ligne)
                            break

                    elif random_break == 2:
                        if c > 0 and matrice[ligne][c].west:
                            matrice = w_remover(matrice, c, ligne)
                            break

                    elif random_break == 3:
                        if c < len(matrice[ligne]) - 1 and matrice[ligne][c].est:
                            matrice = e_remover(matrice, c, ligne)
                            break
    return matrice
