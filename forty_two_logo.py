import random


def forty_two_logo(matrice: list[list]) -> list[list]:
    y = len(matrice) // 2
    x = len(matrice[y]) // 2
    matrice[y - 2][x + 1].forty_two = True
    matrice[y - 2][x + 2].forty_two = True
    matrice[y - 2][x + 3].forty_two = True
    matrice[y - 2][x - 3].forty_two = True

    matrice[y - 1][x + 3].forty_two = True
    matrice[y - 1][x - 3].forty_two = True

    matrice[y][x - 1].forty_two = True
    matrice[y][x - 2].forty_two = True
    matrice[y][x - 3].forty_two = True
    matrice[y][x + 1].forty_two = True
    matrice[y][x + 2].forty_two = True
    matrice[y][x + 3].forty_two = True

    matrice[y + 1][x + 1].forty_two = True
    matrice[y + 1][x - 1].forty_two = True

    matrice[y + 2][x - 1].forty_two = True
    matrice[y + 2][x + 1].forty_two = True
    matrice[y + 2][x + 2].forty_two = True
    matrice[y + 2][x + 3].forty_two = True
    
    return matrice
