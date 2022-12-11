monkeys = [row.split("\n") for row in open("input.txt", "r").read().split("\n\n")]

nice_monkeys = list()

def get_divisible_lambda(num):
    return lambda x: x % num == 0

def get_lambda(operator, second):
    if operator == "+":
        return lambda x: x + (x if second == "old" else int(second))

    if operator == "*":
        return lambda x: x * (x if second == "old" else int(second))


for monkey in monkeys:
    monkey_id, items, operation, test, if_true, if_false = monkey
    items = list(map(int, (items[17:]).strip().split(", ")))[::-1]
    operator, second = operation[23:].split()
    operation = get_lambda(operator, second)
    test = get_divisible_lambda(int(test.strip().split()[-1]))
    if_true = int(if_true.strip().split()[-1])
    if_false = int(if_false.strip().split()[-1])

    nice_monkeys.append([items, operation, test, if_true, if_false, 0])

num_rounds = 20

for _ in range(num_rounds):
    for i in range(len(nice_monkeys)):

        while len(nice_monkeys[i][0]) > 0:
            current_item = nice_monkeys[i][0].pop()
            worry_level = nice_monkeys[i][1](current_item) // 3
            throw_to_monkey_id = nice_monkeys[i][3] if nice_monkeys[i][2](worry_level) else nice_monkeys[i][4]
            nice_monkeys[throw_to_monkey_id][0].insert(0, worry_level)
            nice_monkeys[i][5] += 1

inspection_list = [inspections for items, operation, test, if_true, if_false, inspections in nice_monkeys]
print("Part one:", sorted(inspection_list)[-2] * sorted(inspection_list)[-1])

nice_monkeys = list()

for monkey in monkeys:
    monkey_id, items, operation, test, if_true, if_false = monkey
    items = list(map(int, (items[17:]).strip().split(", ")))[::-1]
    operator, second = operation[23:].split()
    operation = get_lambda(operator, second)
    test = get_divisible_lambda(int(test.strip().split()[-1]))
    if_true = int(if_true.strip().split()[-1])
    if_false = int(if_false.strip().split()[-1])

    nice_monkeys.append([items, operation, test, if_true, if_false, 0])


num_rounds = 10000
all_tests_multiplied = 1
for monkey in monkeys:
    monkey_id, items, operation, test, if_true, if_false = monkey
    all_tests_multiplied *= int(test.strip().split()[-1])

for _ in range(num_rounds):
    for i in range(len(nice_monkeys)):

        while len(nice_monkeys[i][0]) > 0:
            current_item = nice_monkeys[i][0].pop()
            worry_level = nice_monkeys[i][1](current_item) % all_tests_multiplied
            throw_to_monkey_id = nice_monkeys[i][3] if nice_monkeys[i][2](worry_level) else nice_monkeys[i][4]
            nice_monkeys[throw_to_monkey_id][0].insert(0, worry_level)
            nice_monkeys[i][5] += 1

inspection_list = [inspections for items, operation, test, if_true, if_false, inspections in nice_monkeys]
print("Part two:", sorted(inspection_list)[-2] * sorted(inspection_list)[-1])
