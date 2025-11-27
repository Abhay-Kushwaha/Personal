def build_grid(rows, cols, max_day):
    grid = [[None for _ in range(cols)] for _ in range(rows)]
    day = 1
    for r in range(rows-1, -1, -1):
        for c in range(cols):
            if day <= max_day:
                grid[r][c] = day
                day += 1
            else:
                grid[r][c] = None
    return grid

# main
grid = build_grid(5, 7, 31)
headers = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("DEC' 25\n")
for h in headers:
    print(f"{h:<10}", end="")
print("\n")
for r in range(len(grid)):
    for c in range(len(grid[0])):
        val = grid[r][c]
        if val is None:
            print(f"{'':<10}", end="")
        else:
            print(f"{val:<10}", end="")
    print()