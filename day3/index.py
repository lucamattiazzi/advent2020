with open("./data.txt", "r") as data_file:
    data = [row for row in data_file.read().splitlines()]


def solve_first(data):
    rows_count = len(data[0])
    cols_count = len(data)
    x = 0
    y = 0
    trees = 0
    while y < cols_count:
        matrix_point = data[y][x]
        if matrix_point == "#":
            trees += 1
        x += 3
        x %= rows_count
        y += 1
    return trees


def solve_second(data):
    movements = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),

    ]
    rows_count = len(data[0])
    cols_count = len(data)
    trees = 1
    for movement in movements:
        x = 0
        y = 0
        movement_trees = 0
        while y < cols_count:
            matrix_point = data[y][x]
            if matrix_point == "#":
                movement_trees += 1
            x += movement[0]
            x %= rows_count
            y += movement[1]
        trees *= movement_trees
    return trees


print(solve_first(data))
print(solve_second(data))
