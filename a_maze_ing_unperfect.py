from a_maze_ing_func import n_remover, s_remover, e_remover, w_remover, Cell
import random


def cell_wall_count(cell: Cell) -> int:
    wall_count: int = 0
    if cell.north is True:
        wall_count += 1
    if cell.south is True:
        wall_count += 1
    if cell.est is True:
        wall_count += 1
    if cell.west is True:
        wall_count += 1
    return wall_count


def unperfect_maker(matrice: list[list]) -> list[list]:
    for line in range(len(matrice)):
        for c in range(len(matrice[line])):
            cell = matrice[line][c]
            if cell.forty_two is False and cell_wall_count(cell) == 3:
                possible_breaks = []
                if line > 0:
                    if cell.north and not matrice[line - 1][c].forty_two:
                        possible_breaks.append(0)
                if line < len(matrice) - 1:
                    if cell.south and not matrice[line + 1][c].forty_two:
                        possible_breaks.append(1)
                if c > 0:
                    if cell.west and not matrice[line][c - 1].forty_two:
                        possible_breaks.append(2)
                if c < len(matrice[line]) - 1:
                    if cell.est and not matrice[line][c + 1].forty_two:
                        possible_breaks.append(3)
                if possible_breaks:
                    random_break = random.choice(possible_breaks)
                    if random_break == 0:
                        matrice = n_remover(matrice, c, line)
                    elif random_break == 1:
                        matrice = s_remover(matrice, c, line)
                    elif random_break == 2:
                        matrice = w_remover(matrice, c, line)
                    elif random_break == 3:
                        matrice = e_remover(matrice, c, line)
    return matrice
