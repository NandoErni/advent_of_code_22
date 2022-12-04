# Part one:
pairs = [pair.split(",") for pair in open("input.txt", "r").read().split("\n")]


def contains(container, inside):
    return int(container[0]) <= int(inside[0]) and int(container[1]) >= int(inside[1])


count = 0

for first, second in pairs:
    f_s = first.split("-")
    s_s = second.split("-")
    if contains(f_s, s_s) or contains(s_s, f_s):
        count += 1

print("Part one:", count)


# Part two:
def no_overlaps(first, second):
    return int(first[1]) < int(second[0]) or int(first[0]) > int(second[1])


count = 0

for first, second in pairs:
    f_s = first.split("-")
    s_s = second.split("-")
    if not no_overlaps(f_s, s_s):
        count += 1

print("Part two:", count)
