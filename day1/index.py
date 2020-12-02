with open("./data.txt", "r") as data_file:
    data = [int(row) for row in data_file.readlines()]

TARGET = 2020


def filter_data(data):
    data.sort()
    max = data[-1]
    min = data[0]
    filtered = []
    for value in data:
        value_diff = TARGET - value
        is_too_high = value_diff < min
        is_too_low = value_diff > max
        if (is_too_high or is_too_low):
            continue
        filtered.append(value)
    return filtered


def solve_first(data):
    result = -1
    filtered = filter_data(data)

    for i in filtered:
        diff = TARGET - i
        if diff in filtered:
            result = i * diff
            break
    return result


def solve_second(data):
    filtered = filter_data(data)
    result = -1
    for i in filtered:
        for j in filtered:
            if i == j:
                continue
            diff = TARGET - (i + j)
            if diff in filtered:
                result = i * j * diff
                break
    return result


print(solve_first(data))
print(solve_second(data))
