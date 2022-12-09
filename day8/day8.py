tree_map = [list(map(int, row)) for row in open("input.txt", "r").read().split("\n")]

dim = len(tree_map)

def all_smaller(num, l):
    for i in l:
        if i >= num:
            return False
    return True

num_of_trees_visible = 0
for i in range(dim):
    for j in range(dim):
        if i == 0 or i == dim-1 or j == 0 or j == dim-1:
            continue

        current_tree_height = tree_map[i][j]
        h_nums = tree_map[i]
        v_nums = [row[j] for row in tree_map]


        if all_smaller(current_tree_height, h_nums[:j]) or all_smaller(current_tree_height, h_nums[j + 1:]) or all_smaller(current_tree_height, v_nums[:i]) or all_smaller(current_tree_height, v_nums[i + 1:]):
            num_of_trees_visible += 1


num_of_trees_visible += 2 * dim + 2 * (dim - 2)

print("Part one:", num_of_trees_visible)

def calc_scenic(height, trees):
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            return score

    return score

highest_scenic_score = 0
for i in range(dim):
    for j in range(dim):
        current_tree_height = tree_map[i][j]
        h_nums = tree_map[i]
        v_nums = [row[j] for row in tree_map]

        right = h_nums[j + 1:]
        left = h_nums[j-1::-1]
        down = v_nums[i + 1:]
        up = v_nums[i-1::-1]

        current_score = calc_scenic(current_tree_height, right) * calc_scenic(current_tree_height, left) * calc_scenic(current_tree_height, up) * calc_scenic(current_tree_height, down)

        print(current_score)
        if current_score > highest_scenic_score:
            highest_scenic_score = current_score

print("Part two:", highest_scenic_score)