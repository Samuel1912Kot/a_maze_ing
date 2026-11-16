import sys


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

            if not key or (not value and key != "SEED"):
                raise ValueError(f"Invalid config line: {line}")

            if key in param:
                raise ValueError(f"Duplicate key: {key}")

            param[key] = value

    return param


def parsing_verif() -> bool:
    try:
        info = parsing_info(sys.argv[1])

    except (OSError, ValueError) as e:
        print(f"{e} \n(check {sys.argv[1]})")
        return False

    keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
            "OUTPUT_FILE", "PERFECT"]

    for key in keys:
        if key not in info:
            print(f"Missing parameter: {key}")
            return False
    if "SEED" in info and info["SEED"] != "":
        try:
            int(info["SEED"])

        except ValueError:
            print("SEED must be an integer")
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
        entry_values = info["ENTRY"].split(",")
        exit_values = info["EXIT"].split(",")

        if any(value.strip() == "" for value in entry_values):
            print("ENTRY must contain exactly two coordinates (x, y)")
            return False
        if any(value.strip() == "" for value in exit_values):
            print("EXIT must contain exactly two coordinates (x, y)")
            return False

        entry_x, entry_y = entry_values
        exit_x, exit_y = exit_values
        try:
            entry_x, entry_y = int(entry_x.strip()), int(entry_y.strip())
            exit_x, exit_y = int(exit_x.strip()), int(exit_y.strip())
        except ValueError:
            raise ValueError("ENTRY and EXIT coordinates must be integers")

    except ValueError as e:
        print(f"{e} \n(check {sys.argv[1]})")
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
