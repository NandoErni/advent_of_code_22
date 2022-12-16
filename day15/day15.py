sensors_and_beacons = [[list(map(int, numbers.split(','))) for numbers in row.split(':')] for row in open('input.txt', 'r').read().replace('Sensor at x=', ''). replace(' y=', ''). replace(' closest beacon is at x=','').split('\n')]

def get_manhatten(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ROW = 2000000

no_bacon = set()
for (sensor, beacon) in sensors_and_beacons:
    distance = get_manhatten(sensor, beacon)
    if abs(ROW - sensor[1]) > distance: continue
    y = ROW
    for x in range(sensor[0]-distance, sensor[0]+distance):
        current_coordinate = (x, y)
        if get_manhatten(sensor, current_coordinate) <= distance:
            no_bacon.add((x,y))

for (sensor, beacon) in sensors_and_beacons:
    if tuple(sensor) in no_bacon:
        no_bacon.remove(tuple(sensor))
    if tuple(beacon) in no_bacon:
        no_bacon.remove(tuple(beacon))

print("Part one:", len(no_bacon))
# 5716881


def is_not_seen_by_sensor(coords):
    for pair in sensors_and_beacons:
        sensor, beacon = pair
        distance = get_manhatten(sensor, beacon)
        distance_to_point = get_manhatten(sensor, coords)
        if distance >= distance_to_point:
            return False
    return True


no_bacon = set()
for pair in sensors_and_beacons:
    if no_bacon:
        break
    sensor, beacon = pair
    distance = get_manhatten(sensor, beacon)

    # check the edge of the sensors view
    for x_all in range(distance + 2):
        y_all = (distance + 1) - x_all
        for side in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            x = sensor[0]+(x_all * side[0])
            y = sensor[1]+(y_all * side[1])
            current_coordinate = (x, y)
            if not (0<=x<=4000000 and 0<=y<=4000000):
                continue
            if is_not_seen_by_sensor(current_coordinate) and not no_bacon:
                no_bacon.add(x*4000000 + y)


print("Part two:", no_bacon.pop())

