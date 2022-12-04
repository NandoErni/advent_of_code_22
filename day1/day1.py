# First challenge:
calories = [list(map(int, g.split("\n"))) for g in open("input.txt", "r").read().split("\n\n")]
calories_sum = [sum(c) for c in calories]
print(max(calories_sum))

# or this in one line
print(max([sum(list(map(int, g.split("\n")))) for g in open("input.txt", "r").read().split("\n\n")]))


# Second challenge:
calories = [list(map(int, g.split("\n"))) for g in open("input.txt", "r").read().split("\n\n")]
calories_sum = [sum(c) for c in calories]

first = max(calories_sum)
calories_sum.remove(first)
second = max(calories_sum)
calories_sum.remove(second)
third = max(calories_sum)

print("Top 3:", first + second + third)


print(sum(sorted([sum(list(map(int, g.split("\n")))) for g in open("input.txt", "r").read().split("\n\n")], reverse=True)[:3]))