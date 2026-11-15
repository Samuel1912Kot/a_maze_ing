def is_move_possible(mat: list[list], x: int, y: int, direction: str) -> bool:
    if direction == "N":
        if y != 0:
            if mat[y][x].north is False and mat[y - 1][x].south is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "S":
        if y != len(mat) - 1:
            if mat[y][x].south is False and mat[y + 1][x].north is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "E":
        if x != len(mat[y]) - 1:
            if mat[y][x].est is False and mat[y][x + 1].west is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "W":
        if x != 0:
            if mat[y][x].west is False and mat[y][x - 1].est is False:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def bfs(matrice: list[list], entry_cor: tuple, exit_cor: tuple):
    queue = [entry_cor]
    visited = [entry_cor]
    previous = {}
    directions = ["N", "S", "E", "W"]
    while queue:
        x, y = queue.pop(0)
        if (x, y) == exit_cor:
            break

        for direction in directions:
            if is_move_possible(matrice, x, y, direction):
                if direction == "N":
                    nx, ny = x, y - 1
                elif direction == "S":
                    nx, ny = x, y + 1
                elif direction == "E":
                    nx, ny = x + 1, y
                elif direction == "W":
                    nx, ny = x - 1, y
                voisin = (nx, ny)
                if voisin not in visited:
                    visited.append(voisin)
                    previous[voisin] = (x, y)
                    queue.append(voisin)

    if exit_cor not in visited:
        return 
    path = []
    current = exit_cor

    while current != entry_cor:
        path.append(current)
        current = previous[current]
    path.append(entry_cor)
    path.reverse()
    return path


def path_inscriptor(matrice: list[list], path: list[tuple]) -> list[list]:
    if path is None:
        raise ValueError("Impossible de trouver un chemin entre ENTRY et EXIT")
    for coord in path:
        x, y = coord
        matrice[y][x].path = True
    return matrice
