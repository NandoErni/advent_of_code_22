print("Day 01 Part one:", max([sum(list(map(int, g.split("\n")))) for g in open("inputs/day01_input.txt", "r").read().split("\n\n")])) or print("Day 01 Part two:", sum(sorted([sum(list(map(int, g.split("\n")))) for g in open("inputs/day01_input.txt", "r").read().split("\n\n")])[-3:])) or print("Day 02 Part one:", sum([(ord(me) - 87) + (((((ord(me) - 88) - (ord(foe) - 65)) + 1) % 3) * 3) for foe, me in [r.split(" ") for r in open("inputs/day02_input.txt", "r").read().split("\n")]])) or print("Day 02 Part two:", sum([(((ord(foe) + ord(me) - 154) % 3) + 1) + ((ord(me) - 88) * 3) for foe, me in [r.split(" ") for r in open("inputs/day02_input.txt", "r").read().split("\n")]])) or print("Day 03 Part one:", sum([l - (29*((l-96)//abs(l-96)))-67 for l in [ord((set(row[0:len(row) // 2]) & set(row[len(row) // 2:])).pop()) for row in open("inputs/day03_input.txt", "r").read().split("\n")]])) or print("Day 03 Part two:", sum([l - (29*((l-96)//abs(l-96)))-67 for l in [ord((set(f) & set(s) & set(t)).pop()) for f, s, t in (zip(*(iter([row for row in open("inputs/day03_input.txt", "r").read().split("\n")]),) * 3))]])) or print("Day 04 Part one:", sum([int((f_p[0] <= s_p[0] and f_p[1] >= s_p[1]) or (s_p[0] <= f_p[0] and s_p[1] >= f_p[1])) for f_p, s_p in [[list(map(int, e.split("-"))) for e in pair.split(",")] for pair in open("inputs/day04_input.txt", "r").readlines()]])) or print("Day 04 Part two:", sum([int(f[1] >= s[0] and f[0] <= s[1]) for f, s in [[list(map(int, e.split("-"))) for e in pair.split(",")] for pair in open("inputs/day04_input.txt", "r").readlines()]])) or print("Day 05 Part one:", [(str([[z[c-1].append(z[b-1].pop()) for i in range(a)] for a, b, c in [(int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])) for i in open("inputs/day05_input.txt", "r").read().split('\n')[10:]]])[0:0], "".join([zz.pop() for zz in z])) for z in [[[single_char for single_char in "".join(stack).strip()] for stack in list(zip(*[([c for c in row.replace("    ", " ").replace("[", "").replace("] ", "").replace("]", "")]+[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])[:9] for row in open("inputs/day05_input.txt", "r").read().split('\n')[:8]][::-1]))]]][0][1:][0]) or print("Day 05 Part two:", [(str([[z[c-1].extend([z[b-1].pop() for i in range(a)][::-1])] for a, b, c in [(int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])) for i in open("inputs/day05_input.txt", "r").read().split('\n')[10:]]])[0:0], "".join([zz.pop() for zz in z])) for z in [[[single_char for single_char in "".join(stack).strip()] for stack in list(zip(*[([c for c in row.replace("    ", " ").replace("[", "").replace("] ", "").replace("]", "")]+[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])[:9] for row in open("inputs/day05_input.txt", "r").read().split('\n')[:8]][::-1]))]]][0][1]) or print("Day 06 Part one:", min(filter(lambda x: x != 0, [(i+4) * (len(set(marker)) == len(marker)) for i, marker in enumerate([[z[i:i+4] for i in range(len(z)-4)] for z in [open("inputs/day06_input.txt", "r").read()]][0])]))) or print("Day 06 Part two:", min(filter(lambda x: x != 0, [(i+14) * (len(set(marker)) == len(marker)) for i, marker in enumerate([[z[i:i+14] for i in range(len(z)-14)] for z in [open("inputs/day06_input.txt", "r").read()]][0])]))) or print("Day 07 Part one:", sum([num * (num <= 100_000) for num in [((lambda a: lambda aa, aaa, aaaa: a(a, aa, aaa, aaaa))(lambda rec, dir, dict, listi: (isinstance(dict[dir], int) and dict[dir]) or [(listi.append(current_size), current_size)[1] for current_size in [sum([rec(rec, key, dict[dir], listi) for key in dict[dir].keys()])]][0])("/", d, l), l)[1] for d, l in [([([(c[2] == 'c' and (((c.split(" ")[-1] == ".." and cd_stack.pop()) or cd_stack.append(cd_stack[-1][c.split(" ")[-1]])) or True)) or [(size == "dir" and (cd_stack[-1].update({name: dict()}) or True)) or cd_stack[-1].update({name: int(size)}) for size, name in [c.split(" ")]] for c in css], cd_stack[0])[1] for cd_stack, css in [([{"/": dict()}], [([cs.remove("$ ls") for _ in range(cs.count("$ ls"))], cs)[1] for cs in [open("inputs/day07_input.txt", "r").read().split("\n")]][0])]][0], list())]][0]])) or print("Day 07 Part two:", [min([int(n) for n in (" " + ", ".join([str(num * (num >= needed_space)) for num in num_list])).replace(" 0,", "").strip().split(", ")]) for needed_space, num_list in [(-40000000 + (lambda a: lambda aa, aaa, aaaa: a(a, aa, aaa, aaaa))(lambda rec, dir, dict, listi: (isinstance(dict[dir], int) and dict[dir]) or [(listi.append(current_size), current_size)[1] for current_size in [sum([rec(rec, key, dict[dir], listi) for key in dict[dir].keys()])]][0])("/", d, l), l) for d, l in [([([(c[2] == 'c' and (((c.split(" ")[-1] == ".." and cd_stack.pop()) or cd_stack.append(cd_stack[-1][c.split(" ")[-1]])) or True)) or [(size == "dir" and (cd_stack[-1].update({name: dict()}) or True)) or cd_stack[-1].update({name: int(size)}) for size, name in [c.split(" ")]] for c in css], cd_stack[0])[1] for cd_stack, css in [([{"/": dict()}], [([cs.remove("$ ls") for _ in range(cs.count("$ ls"))], cs)[1] for cs in [open("inputs/day07_input.txt", "r").read().split("\n")]][0])]][0], list())]]][0]) or print("Day 08 Part one:", [sum([all([val < tree_map[i][j] for val in tree_map[i][:j]]) or all([val < tree_map[i][j] for val in tree_map[i][j + 1:]]) or all([val < tree_map[i][j] for val in [row[j] for row in tree_map][:i]]) or all([val < tree_map[i][j] for val in [row[j] for row in tree_map][i + 1:]]) for i in range(1, len(tree_map)-1) for j in range(1, len(tree_map)-1)]) + 4 * len(tree_map) - 4 for tree_map in [[list(map(int, row)) for row in open("inputs/day08_input.txt", "r").read().split("\n")]]][0]) or print("Day 08 Part two:", max([[[([(tree >= tree_map[i][j]) and indices.append(idx) for idx, tree in enumerate(tree_map[i][j + 1:], start=1)], len(tree_map[i][j + 1:]) and ((len(indices) and indices[0]) or len(tree_map[i][j + 1:])))[1] for indices in [[]]][0] * [([(tree >= tree_map[i][j]) and indices.append(idx) for idx, tree in enumerate(tree_map[i][j-1::-1], start=1)], len(tree_map[i][j-1::-1]) and ((len(indices) and indices[0]) or len(tree_map[i][j-1::-1])))[1] for indices in [[]]][0] * [([(tree >= tree_map[i][j]) and indices.append(idx) for idx, tree in enumerate([row[j] for row in tree_map][i-1::-1], start=1)], len([row[j] for row in tree_map][i-1::-1]) and ((len(indices) and indices[0]) or len([row[j] for row in tree_map][i-1::-1])))[1] for indices in [[]]][0] * [([(tree >= tree_map[i][j]) and indices.append(idx) for idx, tree in enumerate([row[j] for row in tree_map][i + 1:], start=1)], len([row[j] for row in tree_map][i + 1:]) and ((len(indices) and indices[0]) or len([row[j] for row in tree_map][i + 1:])))[1] for indices in [[]]][0] for i in range(len(tree_map)) for j in range(len(tree_map))] for tree_map in [[list(map(int, row)) for row in open("inputs/day08_input.txt", "r").read().split("\n")]]][0])) or print("Day 09 Part one:", [([(tail_positions.add((rope[-1][0][-1], rope[-1][1][-1])), (move == "D" and (rope[0][1].append(rope[0][1][-1] - 1) or True)) or (move == "U" and (rope[0][1].append(rope[0][1][-1] + 1) or True)) or (move == "L" and (rope[0][0].append(rope[0][0][-1] - 1) or True)) or (move == "R" and (rope[0][0].append(rope[0][0][-1] + 1) or True)), [((abs(rope[i-1][0][-1] - rope[i][0][-1]) <= 1 and abs(rope[i-1][1][-1] - rope[i][1][-1]) <= 1) or (rope[i-1][0][-1] == rope[i][0][-1] and (rope[i][1].append(rope[i][1][-1] + sign(rope[i-1][1][-1] - rope[i][1][-1])) or True)) or (rope[i-1][1][-1] == rope[i][1][-1] and (rope[i][0].append(rope[i][0][-1] + sign(rope[i-1][0][-1] - rope[i][0][-1])) or True)) or ((abs(rope[i-1][0][-1] - rope[i][0][-1]) == 2 or abs(rope[i-1][1][-1] - rope[i][1][-1]) == 2) and ((rope[i][0].append(rope[i][0][-1] + sign(rope[i-1][0][-1] - rope[i][0][-1])), rope[i][1].append(rope[i][1][-1] + sign(rope[i-1][1][-1] - rope[i][1][-1]))) or True))) for i in range(1, len(rope))]) for move in [item for sublist in [[i] * int(j) for i, j in [row.split(" ") for row in open("inputs/day09_input.txt", "r").read().split("\n")]] for item in sublist]], tail_positions.add((rope[-1][0][-1], rope[-1][1][-1])), len(tail_positions))[2] for rope, sign, tail_positions in [([[[0], [0]] for _ in range(2)], lambda x: x / abs(x), set())]][0]) or print("Day 09 Part two:", [([(tail_positions.add((rope[-1][0][-1], rope[-1][1][-1])), (move == "D" and (rope[0][1].append(rope[0][1][-1] - 1) or True)) or (move == "U" and (rope[0][1].append(rope[0][1][-1] + 1) or True)) or (move == "L" and (rope[0][0].append(rope[0][0][-1] - 1) or True)) or (move == "R" and (rope[0][0].append(rope[0][0][-1] + 1) or True)), [((abs(rope[i-1][0][-1] - rope[i][0][-1]) <= 1 and abs(rope[i-1][1][-1] - rope[i][1][-1]) <= 1) or (rope[i-1][0][-1] == rope[i][0][-1] and (rope[i][1].append(rope[i][1][-1] + sign(rope[i-1][1][-1] - rope[i][1][-1])) or True)) or (rope[i-1][1][-1] == rope[i][1][-1] and (rope[i][0].append(rope[i][0][-1] + sign(rope[i-1][0][-1] - rope[i][0][-1])) or True)) or ((abs(rope[i-1][0][-1] - rope[i][0][-1]) == 2 or abs(rope[i-1][1][-1] - rope[i][1][-1]) == 2) and ((rope[i][0].append(rope[i][0][-1] + sign(rope[i-1][0][-1] - rope[i][0][-1])), rope[i][1].append(rope[i][1][-1] + sign(rope[i-1][1][-1] - rope[i][1][-1]))) or True))) for i in range(1, len(rope))]) for move in [item for sublist in [[i] * int(j) for i, j in [row.split(" ") for row in open("inputs/day09_input.txt", "r").read().split("\n")]] for item in sublist]], tail_positions.add((rope[-1][0][-1], rope[-1][1][-1])), len(tail_positions))[2] for rope, sign, tail_positions in [([[[0], [0]] for _ in range(10)], lambda x: x / abs(x), set())]][0]) or print("Day 10 Part one:", [([(instruction == "noop" and (X.append(X[-1]) or True)) or X.append(X[-1] + int(instruction)) for instruction in open("inputs/day10_input.txt", "r").read().replace("addx ", "noop\n").split("\n")], sum([i*X[i-1] for i in list(range(20, 221, 40))]))[1] for X in [[1]]][0]) or print("Day 10 Part two:", [([(instruction == "noop" and (X.append(X[-1]) or True)) or X.append(X[-1] + int(instruction)) for instruction in open("inputs/day10_input.txt", "r").read().replace("addx ", "noop\n").split("\n")], "".join([(i % 40 == 0) * "\n" + ("#" * ((i % 40)-1 <= x <= (i % 40)+1) + "." * (not ((i % 40)-1 <= x <= (i % 40)+1))) for i, x in enumerate(X[:-1], start=0)]))[1] for X in [[1]]][0]) or print("Day 11 Part one:", [([([nice_monkeys[nice_monkeys[i][3] * (worry_level % nice_monkeys[i][2] == 0) + nice_monkeys[i][4] * (worry_level % nice_monkeys[i][2] != 0)][0].insert(0, worry_level) for worry_level in [((((nice_monkeys[i][1][0] == "+") and (((nice_monkeys[i][1][1] == "old") and (nice_monkeys[i][0][-1]*2)) or nice_monkeys[i][0][-1] + int(nice_monkeys[i][1][1]))) or ((nice_monkeys[i][1][0] == "*") and (((nice_monkeys[i][1][1] == "old") and (nice_monkeys[i][0][-1]**2)) or nice_monkeys[i][0][-1] * int(nice_monkeys[i][1][1])))) //3)]], nice_monkeys[i][0].pop(), nice_monkeys[i][5].append("Yobama")) for _ in range(20) for i in range(len(nice_monkeys)) for _ in range(len(nice_monkeys[i][0]))], (sorted([len(inspections) for _, _, _, _, _, inspections in nice_monkeys])[-2] * sorted([len(inspections) for _, _, _, _, _, inspections in nice_monkeys])[-1]))[-1] for nice_monkeys in [[[list(map(int, (monkey[1][17:]).strip().split(", ")))[::-1], monkey[2][23:].split(), int(monkey[3].strip().split()[-1]), int(monkey[4].strip().split()[-1]), int(monkey[5].strip().split()[-1]), []] for monkey in [row.split("\n") for row in open("inputs/day11_input.txt", "r").read().split("\n\n")]]]][0]) or print("Day 11 Part two:", [([([nice_monkeys[nice_monkeys[i][3] * (worry_level % nice_monkeys[i][2] == 0) + nice_monkeys[i][4] * (worry_level % nice_monkeys[i][2] != 0)][0].insert(0, worry_level) for worry_level in [((((nice_monkeys[i][1][0] == "+") and (((nice_monkeys[i][1][1] == "old") and (nice_monkeys[i][0][-1]*2)) or nice_monkeys[i][0][-1] + int(nice_monkeys[i][1][1]))) or ((nice_monkeys[i][1][0] == "*") and (((nice_monkeys[i][1][1] == "old") and (nice_monkeys[i][0][-1]**2)) or nice_monkeys[i][0][-1] * int(nice_monkeys[i][1][1])))) % all_tests_multiplied[-1])]], nice_monkeys[i][0].pop(), nice_monkeys[i][5].append("Yobama")) for _ in range(10000) for i in range(len(nice_monkeys)) for _ in range(len(nice_monkeys[i][0]))], (sorted([len(inspections) for _, _, _, _, _, inspections in nice_monkeys])[-2] * sorted([len(inspections) for _, _, _, _, _, inspections in nice_monkeys])[-1]))[-1] for nice_monkeys, all_tests_multiplied in [([[list(map(int, (monkey[1][17:]).strip().split(", ")))[::-1], monkey[2][23:].split(), int(monkey[3].strip().split()[-1]), int(monkey[4].strip().split()[-1]), int(monkey[5].strip().split()[-1]), []] for monkey in [row.split("\n") for row in open("inputs/day11_input.txt", "r").read().split("\n\n")]], [([all_tests_multiplied.append(int(monkeyy[3].strip().split()[-1]) * all_tests_multiplied[-1]) for monkeyy in [row.split("\n") for row in open("inputs/day11_input.txt", "r").read().split("\n\n")]], all_tests_multiplied)[1] for all_tests_multiplied in [[1]]][0])]][0]) or print("Day 12 Part one:", [[([map_in[row][column] == 'S' and still_left.append(((row,column), 0)) for row in range(len(map_in)) for column in range(len(map_in[0]))], [still_left and [(rcd[0][0],rcd[0][1]) not in seen and (seen.add((rcd[0][0],rcd[0][1])), map_in[rcd[0][0]][rcd[0][1]] == 'E' and result.append(rcd[1]), [(0<=(rcd[0][0]+dr)<len(map_in) and 0<=(rcd[0][1]+dc)<len(map_in[0]) and score_map[(rcd[0][0]+dr)][(rcd[0][1]+dc)]<=1+score_map[rcd[0][0]][rcd[0][1]]) and still_left.insert(0, (((rcd[0][0]+dr),(rcd[0][1]+dc)),rcd[1]+1)) for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]]) for rcd in [still_left.pop()]] for _ in range((len(map_in) * len(map_in[0]) ** 2))], result[-1])[2] for score_map, still_left, seen, result in [([[(map_in[r][c] == 'S') + (map_in[r][c] == 'E') * 26 + (map_in[r][c] != 'S') * (map_in[r][c] != 'E') * (ord(map_in[r][c]) - ord('a') + 1) for c in range(len(map_in[0]))] for r in range(len(map_in))], list(), set(), list())]][0] for map_in in [open('inputs/day12_input.txt').read().split('\n')]][0]) or print("Day 12 Part two:", [[([map_in[row][column] == 'a' and still_left.append(((row,column), 0)) for row in range(len(map_in)) for column in range(len(map_in[0]))], [still_left and [(rcd[0][0],rcd[0][1]) not in seen and (seen.add((rcd[0][0],rcd[0][1])), map_in[rcd[0][0]][rcd[0][1]] == 'E' and result.append(rcd[1]), [(0<=(rcd[0][0]+dr)<len(map_in) and 0<=(rcd[0][1]+dc)<len(map_in[0]) and score_map[(rcd[0][0]+dr)][(rcd[0][1]+dc)]<=1+score_map[rcd[0][0]][rcd[0][1]]) and still_left.insert(0, (((rcd[0][0]+dr),(rcd[0][1]+dc)),rcd[1]+1)) for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]]) for rcd in [still_left.pop()]] for _ in range((len(map_in) * len(map_in[0]) ** 2))], result[-1])[2] for score_map, still_left, seen, result in [([[(map_in[r][c] == 'S') + (map_in[r][c] == 'E') * 26 + (map_in[r][c] != 'S') * (map_in[r][c] != 'E') * (ord(map_in[r][c]) - ord('a') + 1) for c in range(len(map_in[0]))] for r in range(len(map_in))], list(), set(), list())]][0] for map_in in [open('inputs/day12_input.txt').read().split('\n')]][0]) or print("Day 13 Part one:", sum([((lambda a:lambda v, v2:a(a,v, v2))(lambda s, p1, p2: [([(isinstance(p1[yob], int) and isinstance(p2[yob], int) and ((not return_value and p1[yob] < p2[yob]) and return_value.append(1), (not return_value and p1[yob] > p2[yob]) and return_value.append(-1)), isinstance(p1[yob], int) and isinstance(p2[yob], list) and (not return_value and s(s, [p1[yob]], p2[yob]) != 0) and return_value.append(s(s, [p1[yob]], p2[yob])), isinstance(p1[yob], list) and isinstance(p2[yob], int) and (not return_value and s(s, p1[yob], [p2[yob]]) != 0) and return_value.append(s(s, p1[yob], [p2[yob]])), isinstance(p1[yob], list) and isinstance(p2[yob], list) and (not return_value and s(s, p1[yob], p2[yob]) != 0) and return_value.append(s(s, p1[yob], p2[yob]))) for yob in range(min(len(p1), len(p2)))], ((return_value) and return_value[-1]) or (len(p1) < len(p2)) + -(len(p1) > len(p2)))[1] for return_value in [list()]][0])(p1, p2) == 1) * i for i, (p1, p2) in enumerate([tuple(map(eval, p.split("\n"))) for p in  open('inputs/day13_input.txt').read().split('\n\n')], start=1)])) or print("Day 13 Part two:", [([(value == [[2]] or value == [[6]]) and multi.append(multi[-1] * i) for i, value in enumerate([([((lambda a:lambda v, v2:a(a,v, v2))(lambda s, p1, p2: [([(isinstance(p1[yob], int) and isinstance(p2[yob], int) and ((not return_value and p1[yob] < p2[yob]) and return_value.append(1), (not return_value and p1[yob] > p2[yob]) and return_value.append(-1)), isinstance(p1[yob], int) and isinstance(p2[yob], list) and (not return_value and s(s, [p1[yob]], p2[yob]) != 0) and return_value.append(s(s, [p1[yob]], p2[yob])), isinstance(p1[yob], list) and isinstance(p2[yob], int) and (not return_value and s(s, p1[yob], [p2[yob]]) != 0) and return_value.append(s(s, p1[yob], [p2[yob]])), isinstance(p1[yob], list) and isinstance(p2[yob], list) and (not return_value and s(s, p1[yob], p2[yob]) != 0) and return_value.append(s(s, p1[yob], p2[yob]))) for yob in range(min(len(p1), len(p2)))], ((return_value) and return_value[-1]) or (len(p1) < len(p2)) + -(len(p1) > len(p2)))[1] for return_value in [list()]][0])(my_list[j], my_list[j + 1]) == -1) and my_list.insert(j, my_list.pop(j + 1)) for i in range(len(my_list)) for j in range(len(my_list) - i - 1)], my_list)[-1] for my_list in [[eval(p) for p in open('inputs/day13_input.txt').read().replace("\n\n", "\n").split('\n')] + [[[2]], [[6]]]]][0], start=1)], multi[-1])[-1] for multi in [[1]]][0]) or print("Day 14 Part one:", [[[([((rock[i][0] == rock[i + 1][0]) and [(cave[l].pop(rock[i][0]), cave[l].insert(rock[i][0], '#')) for l in max([list(range(rock[i][1], rock[i + 1][1] + 1)), list(range(rock[i + 1][1], rock[i][1] + 1))])], (rock[i][1] == rock[i + 1][1]) and [(cave[rock[i][1]].pop(l), cave[rock[i][1]].insert(l, '#')) for l in max([list(range(rock[i][0], rock[i + 1][0] + 1)), list(range(rock[i + 1][0], rock[i][0] + 1))])]) for rock in rocks for i in range(len(rock) - 1)], [([([(not early_return and cave[current_position[1]+1][current_position[0]] != '#') and (current_position.insert(1, current_position.pop(1) + 1), current_position[1] == abyss_starts_at and early_return.append(len(counter))) for _ in range(abyss_starts_at+3)], ((not early_return and cave[current_position[1] + 1][current_position[0] - 1] != '#') and ((current_position.insert(1, current_position.pop(1) + 1), current_position.insert(0, current_position.pop(0) - 1)) or True)) or (((not early_return and cave[current_position[1]+1][current_position[0]+1] != '#') and ((current_position.insert(1, current_position.pop(1) + 1), current_position.insert(0, current_position.pop(0) + 1)), True)) or (((not early_return) and ((cave[current_position[1]].pop(current_position[0]), cave[current_position[1]].insert(current_position[0], '#'), current_position.pop(0), current_position.insert(0, 500), current_position.pop(1), current_position.insert(1, 0), counter.append('Yobama')) or True))))) for _ in range((abyss_starts_at * 2000))], (early_return and early_return[-1]) or len(counter))[-1] for current_position, counter, early_return in [([500 , 0], list(), list())]][0])[-1] for cave in [[([((x == 0) and caver.append([]), ((y == 0 and x == 500) and caver[-1].append('+')) or caver[-1].append('.')) for y in range(abyss_starts_at+1) for x in range(2000)], caver)[-1] for caver in [[]]][0]]][0] for abyss_starts_at in [max([j[1] for i in rocks for j in i]) + 1]][0] for rocks in [[[(int(coords.split(",")[0]), int(coords.split(",")[1])) for coords in row.split(" -> ")] for row in open("inputs/day14_input.txt", "r").read().split("\n")]]][0]) or print("Day 14 Part two:", [[[([((rock[i][0] == rock[i + 1][0]) and [(cave[l].pop(rock[i][0]), cave[l].insert(rock[i][0], '#')) for l in max([list(range(rock[i][1], rock[i + 1][1] + 1)), list(range(rock[i + 1][1], rock[i][1] + 1))])], (rock[i][1] == rock[i + 1][1]) and [(cave[rock[i][1]].pop(l), cave[rock[i][1]].insert(l, '#')) for l in max([list(range(rock[i][0], rock[i + 1][0] + 1)), list(range(rock[i + 1][0], rock[i][0] + 1))])]) for rock in rocks for i in range(len(rock) - 1)], cave.insert(abyss_starts_at+1, ['#' for i in range(2000)]), [([(not early_return) and ([(cave[current_position[1]+1][current_position[0]] != '#') and current_position.insert(1, current_position.pop(1) + 1) for _ in range(abyss_starts_at+3)], ((cave[current_position[1] + 1][current_position[0] - 1] != '#') and ((current_position.insert(1, current_position.pop(1) + 1), current_position.insert(0, current_position.pop(0) - 1)) or True)) or (((cave[current_position[1]+1][current_position[0]+1] != '#') and ((current_position.insert(1, current_position.pop(1) + 1), current_position.insert(0, current_position.pop(0) + 1)) or True)) or ((cave[current_position[1]].pop(current_position[0]), cave[current_position[1]].insert(current_position[0], '#'), (current_position == [500 , 0]) and early_return.append(len(counter) + 1), current_position.pop(0), current_position.insert(0, 500), current_position.pop(1), current_position.insert(1, 0), counter.append(""))))) for _ in range((abyss_starts_at * 20000))], (early_return and early_return[-1]) or len(counter))[-1]for current_position, counter, early_return in [([500 , 0], [], [])]][0])[-1] for cave in [[([((x == 0) and caver.append([]), ((y == 0 and x == 500) and caver[-1].append('+')) or caver[-1].append('.')) for y in range(abyss_starts_at+1) for x in range(2000)], caver)[-1] for caver in [[]]][0]]][0] for abyss_starts_at in [max([j[1] for i in rocks for j in i]) + 1]][0] for rocks in [[[(int(coords.split(",")[0]), int(coords.split(",")[1])) for coords in row.split(" -> ")] for row in open("inputs/day14_input.txt", "r").read().split("\n")]]][0])