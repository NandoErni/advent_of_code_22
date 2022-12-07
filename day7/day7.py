commands = open("input.txt", "r").read().split("\n")

MAX_SUM = 100_000
directories = dict()
directories["/"] = dict()
CWD = directories

cd_stack = list()

for line in commands:
    if line.startswith("$"):
        if line[2] == 'c':
            # cd command
            directory = line.split(" ")[-1]

            if directory == "..":
                CWD = cd_stack.pop()
                continue

            cd_stack.append(CWD)
            CWD = CWD[directory]
    else:
        size, name = line.split(" ")
        CWD[name] = dict() if size == "dir" else int(size)

part_one_result = 0


def calculate_size(dir, dict):
    global part_one_result
    successors = dict[dir]

    if isinstance(successors, int):
        return successors  # it's the size of a file

    current_size = sum([calculate_size(key, successors) for key in successors.keys()])

    if current_size <= MAX_SUM:
        part_one_result += current_size
    return current_size


free_space = 70000000 - calculate_size("/", directories)
needed_space = 30_000_000 - free_space

print("Part One:", part_one_result)

smallest_size = 70_000_000


def calculate_size_2(dir, dict):
    global smallest_size, needed_space
    successors = dict[dir]

    if isinstance(successors, int):
        return successors  # it's the size of a file

    current_size = sum([calculate_size_2(key, successors) for key in successors.keys()])

    if needed_space <= current_size < smallest_size:
        smallest_size = current_size
    return current_size


calculate_size_2("/", directories)
print("Part Two:", smallest_size)
