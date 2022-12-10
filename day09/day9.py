import math

movements = [item for sublist in [[i] * int(j) for i, j in [row.split(" ") for row in open("input.txt", "r").read().split("\n")]] for item in sublist]
print(movements)

def do_rope_sim(n):
    rope = [[0, 0] for _ in range(n)]
    tail_positions = set()

    def is_tail_touching(next_knot, current_knot):
        return abs(next_knot[0] - current_knot[0]) <= 1 and abs(next_knot[1] - current_knot[1]) <= 1

    def do_head_move(m):
        if m == "D":
            rope[0][1] -= 1
        elif m == "U":
            rope[0][1] += 1
        elif m == "L":
            rope[0][0] -= 1
        elif m == "R":
            rope[0][0] += 1
        else:
            raise Exception("No! " + m)

    def do_tail_move(next_knot, current_knot):
        if is_tail_touching(next_knot, current_knot):
            return # nothing to do

        if next_knot[0] == current_knot[0]:
            current_knot[1] += math.copysign(1, next_knot[1] - current_knot[1])
            return

        if next_knot[1] == current_knot[1]:
            current_knot[0] += math.copysign(1, next_knot[0] - current_knot[0])
            return

        if abs(next_knot[0] - current_knot[0]) == 2 or abs(next_knot[1] - current_knot[1]) == 2:
            current_knot[0] += math.copysign(1, next_knot[0] - current_knot[0])
            current_knot[1] += math.copysign(1, next_knot[1] - current_knot[1])
            return
        raise Exception("This shouldn't be possible!")

    for move in movements:
        tail_positions.add((rope[-1][0], rope[-1][1]))
        do_head_move(move)
        for i in range(1, len(rope)):
            do_tail_move(rope[i-1], rope[i])

    tail_positions.add((rope[-1][0], rope[-1][1]))
    return len(tail_positions)

print("Part one:", do_rope_sim(2))
print("Part two:", do_rope_sim(10))
