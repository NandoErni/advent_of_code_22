from collections import deque

cubes_dict = {tuple(map(int, row.split(','))): True for row in open("input.txt", "r").read().split('\n')}
cubes = list(cubes_dict.keys())

def get_faces(cubes):
    result = 0
    for i in range(len(cubes)):
        for j in range(len(cubes)):
            distance = abs(cubes[i][0] - cubes[j][0]) + abs(cubes[i][1] - cubes[j][1]) + abs(cubes[i][2] - cubes[j][2])
            if distance == 1:
                result += 1

    return (len(cubes)*6) - result
print("Part one:", get_faces(cubes))


from itertools import product

max_coord = max([max(x, y ,z) for x, y, z in cubes])
potential_air_pockets = set(product(range(0, max_coord + 1), repeat=3)) - set(cubes)

def is_on_edge(x, y, z):
    return x <= 0 or y <= 0 or z <= 0 or x >= max_coord or y >= max_coord or z >= max_coord

def is_surrounded(ap, old_c_dict) -> bool:
    if is_on_edge(*ap):
        return False
    c_dict = old_c_dict.copy()
    el_q = deque([ap])
    seen = set()
    while el_q:
        current = el_q.popleft()
        if current in seen:
            continue
        seen.add(current)
        if is_on_edge(*current):
            return False
        for s in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            is_this_lava = tuple([sum(value) for value in zip(current, s)])

            if is_this_lava not in c_dict:
                el_q.append(is_this_lava)
    return True

actual_air_pockets = [ap for ap in potential_air_pockets if is_surrounded(ap, cubes_dict)]


print("Part two:", get_faces(cubes)-(get_faces(actual_air_pockets)))