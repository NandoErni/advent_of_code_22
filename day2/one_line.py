print("Part One:", sum([(ord(me) - 87) + (((((ord(me) - 88) - (ord(foe) - 65)) + 1) % 3) * 3) for foe, me in [r.split(" ") for r in open(
    "input.txt", "r").read().split("\n")]]))
print("Part Two:", sum([(((ord(foe) + ord(me) - 154) % 3) + 1) + ((ord(me) - 88) * 3) for foe, me in [r.split(" ") for r in open(
    "input.txt", "r").read().split("\n")]]))