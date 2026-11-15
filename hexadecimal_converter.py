from a_maze_ing_func import parsing_info
# mypy: ignore-errors


def hexadecimal_converter(cell) -> str:
    value: int = 0

    if cell.forty_two:
        return "F"
    if cell.north:
        value |= 1 << 0
    if cell.est:
        value |= 1 << 1
    if cell.south:
        value |= 1 << 2
    if cell.west:
        value |= 1 << 3
    return format(value, "X")


def is_move_possible(matrice: list[list], x: int, y: int, dire: str) -> bool:
    if dire == "N":
        if y > 0:
            return (matrice[y][x].north is False
                    and matrice[y - 1][x].south is False
                    and matrice[y - 1][x].path is True)

    elif dire == "S":
        if y < len(matrice) - 1:
            return (matrice[y][x].south is False
                    and matrice[y + 1][x].north is False
                    and matrice[y + 1][x].path is True)

    elif dire == "E":
        if x < len(matrice[y]) - 1:
            return (matrice[y][x].est is False
                    and matrice[y][x + 1].west is False
                    and matrice[y][x + 1].path is True)

    elif dire == "W":
        if x > 0:
            return (matrice[y][x].west is False
                    and matrice[y][x - 1].est is False
                    and matrice[y][x - 1].path is True)

    return False


def path_converter(matrice: list[list], entry_c: tuple, exit_c: tuple) -> str:
    path: str = ""
    x, y = map(int, entry_c.split(","))
    fx, fy = map(int, exit_c.split(","))
    old_cord: tuple = (x, y)

    while (x, y) != (fx, fy):
        if matrice[y][x].path is not True:
            return "Error"
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
    if matrice[y][x].path is not True:
        return "Error"
    return path


def hexadecimal_file_creator(matrice: list[list], file_name: str) -> None:
    info = parsing_info("config.txt")
    path: str = path_converter(matrice, info["ENTRY"], info["EXIT"])
    new_line: str = ""
    with open(file_name, "w") as file:
        for y in range(len(matrice)):
            for x in range(len(matrice[y])):
                new_line += hexadecimal_converter(matrice[y][x])
            file.write(f"{new_line}\n")
            new_line = ""
        file.write("\n")
        file.write(info["ENTRY"].replace(" ", "") + "\n")
        file.write(info["EXIT"].replace(" ", "") + "\n")
        file.write(path + "\n")
