print("Part one:", min(filter(lambda x: x != 0, [(i+4) * (len(set(marker)) == len(marker)) for i, marker in enumerate([[z[i:i+4] for i in range(len(z)-4)] for z in [open("input.txt", "r").read()]][0])])))
print("Part two:", min(filter(lambda x: x != 0, [(i+14) * (len(set(marker)) == len(marker)) for i, marker in enumerate([[z[i:i+14] for i in range(len(z)-14)] for z in [open("input.txt", "r").read()]][0])])))