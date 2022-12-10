instructions = [row.replace("addx", "noop").split(" ") if row.startswith("addx") else [row] for row in open("input.txt", "r").read().split("\n")]
instructions = [item for sublist in instructions for item in sublist]


X = [1]

for i in instructions:
    if i != "noop":
        X.append(X[-1] + int(i))
    else:
        X.append(X[-1])

indices = list(range(20, 221, 40))

sums = list()
for i in indices:
    sums.append(i*X[i-1])

print("Part one:", sum(sums))

crt = ""
for i, x in enumerate(X, start=0):
    index = i % 40
    if index-1 <= x <= index+1:
        crt += "#"
    else:
        crt += "."

for i in list(range(40, len(X), 40)):
    print(crt[i-40:i])