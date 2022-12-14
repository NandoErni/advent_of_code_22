packets = [(eval(p.split("\n")[0]), eval(p.split("\n")[1])) for p in  open('input.txt').read().split('\n\n')]

def compare(left, right):
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            if left[i] > right[i]:
                return -1
        elif isinstance(left[i], int) and isinstance(right[i], list):
            comparison = compare([left[i]], right[i])
            if comparison != 0:
                return comparison
        elif isinstance(left[i], list) and isinstance(right[i], int):
            comparison = compare(left[i], [right[i]])
            if comparison != 0:
                return comparison
        elif isinstance(left[i], list) and isinstance(right[i], list):
            comparison = compare(left[i], right[i])
            if comparison != 0:
                return comparison

    return (len(left) < len(right)) + -(len(left) > len(right))


the_sum = sum([(compare(p1, p2) == 1) * i for i, (p1, p2) in enumerate(packets, start=1)])
print("Part one:", the_sum)

from functools import cmp_to_key
packets = sorted([eval(p) for p in open('input.txt').read().replace("\n\n", "\n").split('\n')] + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)

the_multiplication = 1
for i, value in enumerate(packets, start=1):
    if value == [[2]] or value == [[6]]:
        the_multiplication *= i

print("Part two:", the_multiplication)
