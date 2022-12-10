rucksacks = [(row[0:len(row) // 2], row[len(row) // 2:]) for row in open("input.txt", "r").read().split("\n")]

score = 0
for first, second in rucksacks:
    common_element = (set(first) & set(second)).pop()
    if common_element.isupper():
        score += ord(common_element)-38
    else:
        score += ord(common_element)-96
print("Part one:", score)

rucksacks = open("input.txt", "r").read().split("\n")

score = 0
for i in range(int(len(rucksacks)/3)):
    common_element = (set(rucksacks[i*3]) & set(rucksacks[i*3+1]) & set(rucksacks[i*3+2])).pop()
    if common_element.isupper():
        score += ord(common_element)-38
    else:
        score += ord(common_element)-96
print("Part two:", score)