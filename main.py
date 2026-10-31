"""Show the shortest route through a grid using breadth-first search."""
from collections import deque

MAPS = {
    "1": ["S....", ".##..", "...#.", ".#...", "...#E"],
    "2": ["S.#..", "..#..", "..#..", "..#..", "..#.E"],
}

def find_path(grid):
    start = end = None
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if value == "S":
                start = (row, col)
            if value == "E":
                end = (row, col)
    if start is None or end is None:
        return []
    queue = deque([start])
    previous = {start: None}
    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return path[::-1]
        row, col = current
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row, next_col = row + dr, col + dc
            next_spot = (next_row, next_col)
            if (0 <= next_row < len(grid) and
                    0 <= next_col < len(grid[next_row]) and
                    grid[next_row][next_col] != "#" and next_spot not in previous):
                previous[next_spot] = current
                queue.append(next_spot)
    return []

def main():
    print("Pathfinding Visualizer: # = wall, * = shortest route")
    choice = input("Choose map 1 (route) or 2 (blocked): ").strip()
    grid = MAPS.get(choice)
    if grid is None:
        print("Choose 1 or 2.")
        return
    path = find_path(grid)
    picture = [list(row) for row in grid]
    for row, col in path[1:-1]:
        picture[row][col] = "*"
    print()
    for row in picture:
        print(" ".join(row))
    if path:
        print(f"Shortest route: {len(path) - 1} steps")
    else:
        print("No route exists on this map.")

if __name__ == "__main__":
    main()
