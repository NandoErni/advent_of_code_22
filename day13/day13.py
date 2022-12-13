packets_in = open('input.txt').read().split('\n\n')

packets = [(eval(p.split("\n")[0]), eval(p.split("\n")[1])) for p in packets_in]

def is_in_order(left, right):
    for i in range(min(len(left), len(right))):
        value_left = left[i]
        value_right = right[i]

        if isinstance(value_left, int) and isinstance(value_right, int):
            if value_left < value_right:
                return 1
            if value_left > value_right:
                return -1
        elif isinstance(value_left, int) and isinstance(value_right, list):
            value_left = [value_left]
        elif isinstance(value_left, list) and isinstance(value_right, int):
            value_right = [value_right]
        if isinstance(value_left, list) and isinstance(value_right, list):
            comparison = is_in_order(value_left, value_right)
            if comparison != 0:
                return comparison

    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    return 0


the_sum = 0
for i, (p1, p2) in enumerate(packets, start=1):
    order = is_in_order(p1, p2)
    if order == 1:
        the_sum += i

print("Part one:", the_sum)

packets = [eval(p) for p in open('input.txt').read().replace("\n\n", "\n").split('\n')]
packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(is_in_order), reverse=True)

the_multiplication = 1
for i, value in enumerate(packets, start=1):
    if value == [[2]] or value == [[6]]:
        the_multiplication *= i

print("Part two:", the_multiplication)
