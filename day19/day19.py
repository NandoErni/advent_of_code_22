from collections import deque
from copy import deepcopy

blueprints_raw = open("input.txt", "r").read().split('\n')

blueprints = list()

for row in blueprints_raw:
    ore_rob, clay_rob, obsi_rob, geode_rob, _ = row.split('.')
    ore_rob = int(ore_rob.split(' ')[-2])
    clay_rob = int(clay_rob.split(' ')[-2])
    obsi_rob = obsi_rob.split(' ')
    obsi_rob = tuple(map(int, (obsi_rob[-5], obsi_rob[-2])))
    geode_rob = geode_rob.split(' ')
    geode_rob = tuple(map(int, (geode_rob[-5], geode_rob[-2])))

    blueprints.append((ore_rob, clay_rob, obsi_rob, geode_rob))



def pick_geode(time, blueprint):
    best_score = 0
    max_core = max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0])

    seen = dict()
    q = deque([([(1,0), (0, 0), (0, 0), (0, 0)], time, [0, 0, 0, 0])])
    while q:
        robots, time_left, inventory = q.popleft()
        if time_left <= 0:
            continue
        key = (tuple(robots), time_left, tuple(inventory))
        if key in seen:
            continue
        seen[key] = True

        for i in range(4):
            inventory[i] += robots[i][0] - robots[i][1]
            robots[i] = (robots[i][0], 0)

        if best_score > inventory[3]:
            continue

        best_score = max(best_score, inventory[3])

        if inventory[0] >= blueprint[3][0] and inventory[2] >= blueprint[3][1]:
            new_inventory = deepcopy(inventory)
            new_robots = deepcopy(robots)
            new_inventory[0] -= blueprint[3][0]
            new_inventory[2] -= blueprint[3][1]
            new_robots[3] = (new_robots[3][0]+1, 1)
            q.append((new_robots, time_left - 1, new_inventory))
        if inventory[0] >= blueprint[2][0] and inventory[1] >= blueprint[2][1] > robots[2][0]:
            new_inventory = deepcopy(inventory)
            new_robots = deepcopy(robots)
            new_inventory[0] -= blueprint[2][0]
            new_inventory[1] -= blueprint[2][1]
            new_robots[2] = (new_robots[2][0]+1, 1)
            q.append((new_robots, time_left - 1, new_inventory))
        if inventory[0] >= blueprint[1] and robots[1][0] < blueprint[2][1]:
            new_inventory = deepcopy(inventory)
            new_robots = deepcopy(robots)
            new_inventory[0] -= blueprint[1]
            new_robots[1] = (new_robots[1][0]+1, 1)
            q.append((new_robots, time_left - 1, new_inventory))
        if inventory[0] >= blueprint[0] and robots[0][0] < max_core:
            new_inventory = deepcopy(inventory)
            new_robots = deepcopy(robots)
            new_inventory[0] -= blueprint[0]
            new_robots[0] = (new_robots[0][0]+1, 1)
            q.append((new_robots, time_left - 1, new_inventory))

        q.append((robots, time_left - 1, inventory))

    return best_score
result2 = 1
result = 0
for i in range(len(blueprints)):
    score = pick_geode(24, blueprints[i])

    if i < 3:
        score2 = pick_geode(32, blueprints[i])
        result2 *= score2
    result += (i+1) * score
print("Part one:", result)
print("Part two:", result2)