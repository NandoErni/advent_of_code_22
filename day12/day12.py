map_in = open('input.txt').read().split('\n')
row_length = len(map_in)
column_length = len(map_in[0])

score_map = [[0 for _ in range(column_length)] for _ in range(row_length)]
for r in range(row_length):
    for c in range(column_length):
        if map_in[r][c]== 'S':
            score_map[r][c] = 1
        elif map_in[r][c] == 'E':
            score_map[r][c] = 26
        else:
            score_map[r][c] = ord(map_in[r][c]) - ord('a') + 1

def search(starting_nodes):
    still_left = list()
    for row in range(row_length):
        for column in range(column_length):
            if map_in[row][column] == starting_nodes:
                still_left.append(((row,column), 0))

    seen = set()
    while still_left:
        (row,column),distance = still_left[0]
        still_left = still_left[1:]
        if (row,column) in seen:
            continue
        seen.add((row,column))
        if map_in[row][column]== 'E':
            return distance
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = row+dr
            cc = column+dc
            if 0<=rr<row_length and 0<=cc<column_length and score_map[rr][cc]<=1+score_map[row][column]:
                still_left.append(((rr,cc),distance+1))

print("Part one:", search('S'))
print("Part two:", search('a'))