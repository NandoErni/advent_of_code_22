import re

# Part 1:

input = open("input.txt", "r").read().split('\n')

str_stacks = input[:8]
num_of_stacks = int(max(input[8].split(" ")))

stacks = list()


def init_stacks():
    for i in range(num_of_stacks):
        stacks.append(list())

    for s in str_stacks[::-1]:
        for i in range(num_of_stacks):
            crate = s[i * 4:i * 4 + 3]
            if not crate.isspace() and crate != '':
                stacks[i].append(crate)

init_stacks()
instructions = [tuple(map(int, re.findall(r'\d+', i))) for i in input[10:]]
for num_crates, from_stack, to_stack in instructions:
    from_stack -= 1
    to_stack -= 1
    for i in range(num_crates):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)

for i in range(num_of_stacks):
    print(stacks[i].pop()[1], end='')

# Part 2:
init_stacks()
for num_crates, from_stack, to_stack in instructions:
    from_stack -= 1
    to_stack -= 1
    crates = []
    for i in range(num_crates):
        if not stacks[from_stack]:
            continue
        crates.append(stacks[from_stack].pop())
    for crate in crates[::-1]:
        stacks[to_stack].append(crate)

print()
for i in range(num_of_stacks):
    if not stacks[i]:
        print(' ', end='')
        continue
    print(stacks[i].pop()[1], end='')
