min_x = 0
max_x = 1600
rocks = [[(int(coords.split(",")[0])-min_x, int(coords.split(",")[1])) for coords in row.split(" -> ")] for row in open("input.txt", "r").read().split("\n")]

max_depth = max([j[1] for i in rocks for j in i])

abyss_starts_at = max_depth + 1

cave = []

SAND_SOURCE = (500 - min_x, 0)
def reset_cave():
    global cave
    cave = []
    for y in range(abyss_starts_at+1):
        cave.append([])
        for x in range(max_x-min_x):
            cave[-1].append('.')

    cave[SAND_SOURCE[1]][SAND_SOURCE[0]] = '+'

    for rock in rocks:
        for i in range(len(rock) - 1):
            from_c = rock[i]
            to_c = rock[i + 1]

            if from_c[0] == to_c[0]:
                for l in max([list(range(from_c[1], to_c[1] + 1)), list(range(to_c[1], from_c[1] + 1))]):
                    cave[l][from_c[0]] = '#'

            if from_c[1] == to_c[1]:
                for l in max([list(range(from_c[0], to_c[0] + 1)), list(range(to_c[0], from_c[0] + 1))]):
                    cave[from_c[1]][l] = '#'
reset_cave()

def print_cave():
    print("\n".join(["".join(row) for row in cave]))





BLOCKING_OBJECTS = ['#', 'o']

def let_sand_fall():
    current_position = list(SAND_SOURCE)
    counter = 0
    while True:
        while cave[current_position[1]+1][current_position[0]] not in BLOCKING_OBJECTS:
            current_position[1] += 1
            if current_position[1] == abyss_starts_at:
                return counter
        if cave[current_position[1] + 1][current_position[0] - 1] not in BLOCKING_OBJECTS:
            current_position[1] += 1
            current_position[0] -= 1
            continue
        if cave[current_position[1]+1][current_position[0]+1] not in BLOCKING_OBJECTS:
            current_position[1] += 1
            current_position[0] += 1
            continue
        # can't go further!
        cave[current_position[1]][current_position[0]] = 'o'
        current_position = list(SAND_SOURCE)
        #print_cave()
        counter += 1
    return counter




print("Part one:", let_sand_fall())
reset_cave()
cave.insert(abyss_starts_at+1, ['#' for i in range(max_x-min_x)])
def let_sand_fall2():
    current_position = list(SAND_SOURCE)
    counter = 0
    while True:
        while cave[current_position[1]+1][current_position[0]] not in BLOCKING_OBJECTS:
            current_position[1] += 1
        if cave[current_position[1] + 1][current_position[0] - 1] not in BLOCKING_OBJECTS:
            current_position[1] += 1
            current_position[0] -= 1
            continue
        if cave[current_position[1]+1][current_position[0]+1] not in BLOCKING_OBJECTS:
            current_position[1] += 1
            current_position[0] += 1
            continue
        # can't go further!
        cave[current_position[1]][current_position[0]] = 'o'
        if current_position == list(SAND_SOURCE):
            return counter + 1
        current_position = list(SAND_SOURCE)
        counter += 1
    return counter


print("Part two:", let_sand_fall2())
