# flake8: noqa
ANSI_COLORS = [
    ("White", "\033[0m"),
    ("Cyan", "\033[96m"),
    ("Green", "\033[92m"),
    ("Yellow", "\033[93m"),
    ("Magenta", "\033[95m"),
    ("Blue", "\033[94m"),
]

LOGO_COLORS = [
    ("Red", "\033[91m"),
    ("Yellow", "\033[93m"),
    ("Magenta", "\033[95m"),
    ("Cyan", "\033[96m"),
]

RESET = "\033[0m"
PATH_COLOR = "\033[92m"
ENTRY_COLOR = "\033[96m"
EXIT_COLOR = "\033[91m"


def render_maze(
    grid: list[list],
    entry: tuple,
    exit_pos: tuple,
    show_path: bool,
    wall_color: str,
    logo_color: str,
) -> None:

    if not grid or not grid[0]:
        return

    height = len(grid)
    width = len(grid[0])

    top_line = []
    for x in range(width):
        top_line.append(
            f"{wall_color}+---" if grid[0][x].north
            else f"{wall_color}+   "
        )
    top_line.append(f"+{RESET}")
    print("".join(top_line))

    for y in range(height):
        mid_line = []
        bot_line = []

        for x in range(width):
            cell = grid[y][x]

            left_wall = f"{wall_color}|{RESET}" if cell.west else " "

            if cell.forty_two:
                content = f"{logo_color}███{RESET}"
            elif (x, y) == entry:
                content = f"{ENTRY_COLOR} E {RESET}"
            elif (x, y) == exit_pos:
                content = f"{EXIT_COLOR} S {RESET}"
            elif show_path and cell.path:
                content = f"{PATH_COLOR} * {RESET}"
            else:
                content = "   "

            mid_line.append(f"{left_wall}{content}")

            bot_line.append(
                f"{wall_color}+---" if cell.south
                else f"{wall_color}+   "
            )

        right_wall = (
            f"{wall_color}|{RESET}"
            if grid[y][width - 1].est else " "
        )

        mid_line.append(right_wall)
        bot_line.append(f"+{RESET}")

        print("".join(mid_line))
        print("".join(bot_line))


def interactive_loop(
    matrice: list[list],
    entry: tuple,
    exit_pos: tuple,
    output_file: str,
    perfect: bool,
    width: int,
    height: int,
    generator
) -> None:

    show_path = True
    wall_idx = 0
    logo_idx = 0
    generation_count = 0

    while True:
        print("\033[2J\033[H", end="")

        render_maze(
            grid=matrice,
            entry=entry,
            exit_pos=exit_pos,
            show_path=show_path,
            wall_color=ANSI_COLORS[wall_idx][1],
            logo_color=LOGO_COLORS[logo_idx][1],
        )

        print(
            f"\nMode: {'PERFECT' if perfect else 'PAC-MAN (IMPERFECT)'} | "
            f"Size: {width}x{height} | "
            f"Saved: {output_file}"
        )

        print("Controls:")
        print(" [1] Re-generate a new maze")
        print(f" [2] Show/Hide shortest path (currently: {'ON' if show_path else 'OFF'})")
        print(f" [3] Change wall color (currently: {ANSI_COLORS[wall_idx][0]})")
        print(f" [4] Change '42' logo color (currently: {LOGO_COLORS[logo_idx][0]})")
        print(" [q] Quit")

        try:
            choice = input("\nSelect an option: ").strip().lower()

        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if choice == "1":
            generation_count += 1
            matrice = generator()

        elif choice == "2":
            show_path = not show_path

        elif choice == "3":
            wall_idx = (wall_idx + 1) % len(ANSI_COLORS)

        elif choice == "4":
            logo_idx = (logo_idx + 1) % len(LOGO_COLORS)

        elif choice == "q":
            print("Goodbye!")
            break
