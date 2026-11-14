import random

def parsing_info(filename: str) -> dict:
    param = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line[0] == "#":
                continue
            key, value = line.split("=", 1)
            param[key.strip()] = value.strip()
    return param


def parsing_verif() -> bool:
    info = parsing_info("config.txt")
    keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
                 "OUTPUT_FILE", "PERFECT"]
    for key in keys:
        if key not in info:
            return False
    try:
        width = int(info["WIDTH"])
        height = int(info["HEIGHT"])
        if width < 8:
            print("Width is too low (min 8)")
            return False
        if height < 5:
            print("Height is too low (min 5)")
            return False
    except ValueError as e:
        print(f"{e}")
        return False

    if info["OUTPUT_FILE"].strip() == "":
        raise Exception("Output file parameter is missing")
    try:
        entry_x, entry_y = info["ENTRY"].split(",")
        exit_x, exit_y = info["EXIT"].split(",")
        entry_x, entry_y = int(entry_x), int(entry_y)
        exit_x, exit_y = int(exit_x), int(exit_y)

        if entry_x < 0 or entry_x >= width:
            return False
        if entry_y < 0 or entry_y >= height:
            return False

        if exit_x < 0 or exit_x >= width:
            return False
        if exit_y < 0 or exit_y >= height:
            return False
        if exit_y == entry_y and exit_x == entry_x:
            return False
    except Exception:
        print("The entry or exit point might be out of the maze, or juste wrong (check config.txt)") 
        return False
    return True
    

def perfect_verif() -> bool:
    info = parsing_info("config.txt")
    if info["PERFECT"].lower() == "true":
        return True
    else:
        return False


class Cell():
    def __init__(self):
        self.zone: int = 0
        self.north = True
        self.est = True
        self.south = True
        self.west = True
        self.forty_two = False
        self.path = False

def cell_factory(i: int) -> object:
    cell = Cell()
    cell.zone = i
    return cell


def matrice_init(length: int, height: int) -> list[list]:
    matrice: list[list] = []
    zone: int = 0
    for i in range(height):
        temp_list: list = []
        for e in range(length):
            temp_cell = cell_factory(zone)
            temp_list.append(temp_cell)
            zone += 1
        matrice.append(temp_list)
    return matrice

def zone_filler(matrice: list[list], n1: int, n2: int) -> list[list]:
    for ligne in matrice:
        for cell in ligne:
            if cell.zone == n1:
                cell.zone = n2
    return matrice


def maze_verifying(matrice: list[list]) -> list[list]:
    i = matrice[0][0].zone
    for ligne in matrice:
        for cell in ligne:
            if cell.forty_two:
                continue
            if cell.zone != i:
                return False
    return True


def n_remover(matrice: list[list], x: int, y: int) -> list[list]:
    matrice[y][x].north = False
    matrice[y-1][x].south = False
    return matrice


def s_remover(matrice: list[list], x: int, y: int) -> list[list]:
    matrice[y][x].south = False
    matrice[y+1][x].north = False
    return matrice


def e_remover(matrice: list[list], x: int, y: int) -> list[list]:
    matrice[y][x].est = False
    matrice[y][x+1].west = False
    return matrice


def w_remover(matrice: list[list], x: int, y: int) -> list[list]:
    matrice[y][x].west = False
    matrice[y][x-1].est = False
    return matrice

