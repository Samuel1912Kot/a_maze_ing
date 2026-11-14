def hexadecimal_converter(object: cell) -> hex:
    value: int = 0
   
    if cell.forty_two:
        return "X"
    if cell.nord:
        value |= 1 << 0
    if cell.est:
        value |= 1 << 1
    if cell.south:
        value |= 1 << 2
    if cell.west:
        value |= 1 << 3
    if cell.path:
        value |= 1 << 4

    return value


def is_move_possible(matrice: list[list], x: int, y: int, direction: str) -> bool:
    if direction == "N":
        if y > 0:
            return (matrice[y][x].north is False
                    and matrice[y - 1][x].south is False
                    and matrice[y - 1][x].path is True)

    elif direction == "S":
        if y < len(matrice) - 1:
            return (matrice[y][x].south is False
                    and matrice[y + 1][x].north is False
                    and matrice[y + 1][x].path is True)

    elif direction == "E":
        if x < len(matrice[y]) - 1:
            return (matrice[y][x].est is False
                    and matrice[y][x + 1].west is False
                    and matrice[y][x + 1].path is True)

    elif direction == "W":
        if x > 0:
            return (matrice[y][x].west is False
                    and matrice[y][x - 1].est is False
                    and matrice[y][x - 1].path is True)

    return False


def path_converter(matrice: list[list], entry_cord: tuple, exit_cord: tuple) -> str:
    path: str = ""
    x, y = map(int, entry_cord)
    fx, fy = map(int, exit_cord)
    cell: object
    old_cord: tuple = (x, y)

    if matrice[y][x].path != True:
        return "Error"
    while (x, y) != (fx, fy):
        cell = matrice[y][x]
        if is_move_possible(matrice, x, y, "N") and (x, y - 1) != old_cord:
            old_cord = (x, y)
            y -= 1
            path += "N"
        elif is_move_possible(matrice, x, y, "E") and (x + 1, y) != old_cord:
            old_cord = (x, y)
            x += 1
            path += "E"
        elif is_move_possible(matrice, x, y, "S") and (x, y + 1) != old_cord:
            old_cord = (x, y)
            y += 1
            path += "S"
        elif is_move_possible(matrice, x, y, "W") and (x - 1, y) != old_cord:
            old_cord = (x, y)
            x -= 1
            path += "W"
    return path
    
