print("Part one:", sum([int(l - (29*((l-96)/abs(l-96)))-67) for l in [ord((set(row[0:len(row) // 2]) & set(row[len(row) // 2:])).pop()) for row in open("input.txt", "r").read().split("\n")]]))
print("Part two:", sum([int(l - (29*((l-96)/abs(l-96)))-67) for l in [ord((set(f) & set(s) & set(t)).pop()) for f, s, t in (zip(*(iter([row for row in open("input.txt", "r").read().split("\n")]),) * 3))]]))