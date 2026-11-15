def parsing_info(file: str) -> dict:
    param = {}

    with open(file, "r") as config_file:
        for line in config_file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid config line: {line}")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if not key or not value:
                raise ValueError(f"Invalid config line: {line}")

            if key in param:
                raise ValueError(f"Duplicate key: {key}")

            param[key] = value

    return param


def parsing_verif() -> bool:
    try:
        info = parsing_info("config.txt")
    except (OSError, ValueError) as e:
        print(f"Config file error: {e}")
        return False
    keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
            "OUTPUT_FILE", "PERFECT"]

    for key in keys:
        if key not in info:
            print(f"Missing parameter: {key}")
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
    except ValueError:
        print("WIDTH and HEIGHT must be integers")
        return False

    if info["PERFECT"] not in ["True", "False"]:
        print("PERFECT must be True or False")
        return False
    if info["OUTPUT_FILE"].strip() == "":
        print("Output file parameter is missing")
        return False

    try:
        if len(info["ENTRY"].split(",")) != 2:
            return False
        if len(info["EXIT"].split(",")) != 2:
            return False
        entry_x, entry_y = info["ENTRY"].split(",")
        exit_x, exit_y = info["EXIT"].split(",")
        entry_x, entry_y = int(entry_x.strip()), int(entry_y.strip())
        exit_x, exit_y = int(exit_x.strip()), int(exit_y.strip())
        if entry_x < 0 or entry_x >= width:
            raise ValueError("Entry X coordinate is outside the maze limits")
        if entry_y < 0 or entry_y >= height:
            raise ValueError("Entry Y coordinate is outside the maze limits")
        if exit_x < 0 or exit_x >= width:
            raise ValueError("Exit X coordinate is outside the maze limits")
        if exit_y < 0 or exit_y >= height:
            raise ValueError("Exit Y coordinate is outside the maze limits")
        if (entry_x, entry_y) == (exit_x, exit_y):
            raise ValueError("Entry and exit coordinates cannot be the same")

    except ValueError as e:
        print(f"{e} \n(check config.txt)")
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


def maze_verifying(matrice: list[list]) -> bool:
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
