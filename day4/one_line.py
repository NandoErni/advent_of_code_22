print("Part one:", sum([int((f_p[0] <= s_p[0] and f_p[1] >= s_p[1]) or (s_p[0] <= f_p[0] and s_p[1] >= f_p[1])) for f_p, s_p in [[list(map(int, e.split("-"))) for e in pair.split(",")] for pair in open(
    "input.txt", "r").readlines()]]))
print("Part two:", sum([int(f[1] >= s[0] and f[0] <= s[1]) for f, s in [[list(map(int, e.split("-"))) for e in pair.split(",")] for pair in open(
    "input.txt", "r").readlines()]]))