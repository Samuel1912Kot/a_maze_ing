from a_maze_ing_func import parsing_info


def is_move_possible(matrice: list[list], x: int, y: int, direction: str) -> bool:
    if direction == "N":
        if y != 0:
            if matrice[y][x].north is False and matrice[y - 1][x].south is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "S":
        if y != len(matrice) - 1:
            if matrice[y][x].south is False and matrice[y + 1][x].north is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "E":
        if x != len(matrice[y]) - 1:
            if matrice[y][x].est is False and matrice[y][x + 1].west is False:
                return True
            else:
                return False
        else:
            return False
    elif direction == "W":
        if x != 0:
            if matrice[y][x].west is False and matrice[y][x - 1].est is False:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def bfs(matrice: list[list], entry_cord: tuple, exit_cord: tuple) -> list[list]:
    queue = [entry_cord]
    visited = [entry_cord]
    previous = {}
    directions = ["N", "S", "E", "W"]
    while queue:
        x, y = queue.pop(0)
        if (x, y) == exit_cord:
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

    if exit_cord not in visited:
        return None
    path = []
    current = exit_cord

    while current != entry_cord:
        path.append(current)
        current = previous[current]
    path.append(entry_cord)
    path.reverse()
    return path


def path_inscriptor(matrice: list[list], path: list[tuple]) -> list[list]:
    for coord in path:
        x, y = coord
        matrice[y][x].path = True
    return matrice











