*This activity has been created as part of the 42 curriculum by student.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and visualizer built for the 42 curriculum. It reads a configuration file, generates either a perfect maze (a spanning tree with a single unique path between any two cells) or a Pac-Man-style playable maze (multiple loops, open corners/center, rare dead-ends, and no 3x3 open rooms), embeds a closed "42" pattern in the center, solves the shortest path via Breadth-First Search (BFS), exports the maze in hexadecimal format, and provides an interactive terminal display.

---

## Instructions

### Installation & Setup

Create a virtual environment and install build/lint tools:

~~~bash
python3 -m venv venv
source venv/bin/activate
make install
~~~

### Execution

Run the generator with the default configuration file:

~~~bash
python3 a_maze_ing.py config.txt
# or
make run
~~~

### Interactive Controls

Once running in the terminal, use the menu keys:

- `1`: Re-generate a new maze and update the output file.
- `2`: Toggle visibility of the shortest path (`*`).
- `3`: Cycle through wall colors.
- `4`: Cycle through "42" pattern colors.
- `q`: Quit the program.

### Building the Reusable Package (`mazegen`)

To build the `.whl` and `.tar.gz` archives at the root of the repository:

~~~bash
make build
~~~

This creates `mazegen-1.0.0-py3-none-any.whl` and `mazegen-1.0.0.tar.gz`.

### Linting & Tests

~~~bash
make lint
make lint-strict
pytest
~~~

---

## Configuration File Format

The configuration file uses one `KEY=VALUE` pair per line. Lines starting with `#` are ignored.

| Key | Required | Description | Example |
| :-: | :-: | :-: | :-: |
| `WIDTH` | Yes | Maze width in cells | `WIDTH=20` |
| `HEIGHT` | Yes | Maze height in cells | `HEIGHT=15` |
| `ENTRY` | Yes | Entry coordinates `x,y` | `ENTRY=0,0` |
| `EXIT` | Yes | Exit coordinates `x,y` | `EXIT=19,14` |
| `OUTPUT_FILE` | Yes | Destination file for hex export | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | No (default `False`) | `True` for single-path maze, `False` for multi-route Pac-Man board | `PERFECT=True` |
| `SEED` | No | Integer seed for reproducible generation | `SEED=42` |

---

## Maze Generation Algorithm

### Chosen Algorithm: Randomized Kruskal's Algorithm (with Union-Find)

1. **Grid Initialization:** Every cell starts with all 4 walls closed (North, East, South, West) and belongs to its own disjoint set (zone).
2. **42 Pattern Placement:** If the grid is at least `11x9`, the cells forming the `"42"` emblem in the center are marked as `forty_two=True` and excluded from wall removal.
3. **Spanning Tree Construction:** All valid internal edges between non-42 adjacent cells are shuffled using a seeded `random.Random` instance. Edges connecting two different disjoint sets are opened, merging their sets via path-compressed Union-Find.
4. **Pac-Man Mode (`PERFECT=False`):** Dead-ends (3 closed walls) as well as the 4 corners and center are opened by removing additional internal walls while strictly verifying that no `3x3` open area is created.
5. **Pathfinding:** Breadth-First Search (BFS) computes the shortest path from `ENTRY` to `EXIT`.

### Why This Algorithm?

- **Guaranteed Connectivity & No Loops:** Kruskal's algorithm naturally constructs a uniform spanning tree in O(E alpha(V)) time, guaranteeing a valid perfect maze without isolated regions even around the central `"42"` obstacle.
- **Deterministic Reproducibility:** Shuffling a fixed list of edges with `random.Random(seed)` makes maze generation 100% reproducible.
- **Clean Post-Processing for Imperfect Mode:** Starting from a spanning tree ensures full reachability before selectively removing dead-ends for the Pac-Man mode.

---

## Reusable Code (`mazegen`)

The core generation and solving logic is encapsulated in the standalone package `mazegen` (`mazegen/generator.py`), which can be installed via `pip install mazegen-1.0.0-py3-none-any.whl` and imported into future projects.

### Usage Example

~~~python
from mazegen import MazeGenerator

# 1. Instantiate with custom parameters (size, entry, exit, mode, seed)
generator = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit_pos=(19, 14),
    perfect=True,
    seed=42,
)

# 2. Generate the maze (returns a 2D list of Cell objects)
grid = generator.generate()

# 3. Access cell walls and attributes
top_left = grid[0][0]
print(top_left.north, top_left.east, top_left.south, top_left.west)
print("Hex encoding:", top_left.to_hex())

# 4. Access the shortest path (list of (x, y) coordinates or 'NESW' string)
coords = generator.solution_coords
directions = generator.get_solution_directions()
print("Shortest path:", directions)

# 5. Export to standard output file
generator.export_to_file("maze.txt")
~~~

---

## Project Management & Team

- **Team & Roles:** Solo project — architecture, algorithm design, CLI visualization, packaging, and testing.
- **Planning & Evolution:**
  1. Core grid representation and Kruskal generation.
  2. Hexadecimal export and BFS pathfinding.
  3. Refactoring into the standalone `MazeGenerator` class and adding Pac-Man mode (`PERFECT=False`), 3x3 room prevention, interactive CLI controls, and unit tests.
- **What Worked Well:** Separating `MazeGenerator` from CLI/I/O logic made unit testing and `.whl` packaging straightforward.
- **What Could Be Improved:** Adding an optional MiniLibX (MLX) graphical renderer alongside the terminal ASCII interface.
- **Tools Used:** Python 3, pytest, flake8, mypy, build/setuptools.

---

## Resources & AI Usage

### References

- *Mazes for Programmers* by Jamis Buck (Kruskal's algorithm and spanning trees).
- Wikipedia: [Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm) & [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure).

### Use of AI

AI assistance was used to audit the initial codebase against the project specification, identify edge cases (such as 3x3 open area prevention and small-grid "42" pattern handling), and structure the `pyproject.toml` packaging and `pytest` test suite.
