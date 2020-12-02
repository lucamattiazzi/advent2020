with open("./data.txt", "r") as data_file:
    data = [row for row in data_file.readlines()]


def parse_row_first(row):
    [range, letter, string] = row.split(' ')
    [min, max] = range.split('-')
    letter = letter[0]
    count = string.count(letter)
    return int(max) >= count >= int(min)


def parse_row_second(row):
    [range, letter, string] = row.split(' ')
    [min, max] = range.split('-')
    letter = letter[0]
    first = string[int(min) - 1] == letter
    second = string[int(max) - 1] == letter
    return first != second


def solve_first(data):
    parsed = [row for row in data if parse_row_first(row)]
    print(len(parsed))


def solve_second(data):
    parsed = [row for row in data if parse_row_second(row)]
    print(len(parsed))


solve_first(data)
solve_second(data)
