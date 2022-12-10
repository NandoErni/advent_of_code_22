# part one
rounds = [r.split(" ") for r in open("input.txt", "r").read().split("\n")]
shape_score = {
    'A': 1,
    'B': 2,
    'C': 3
}
winning_shape = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}
conversion = {
    'Y': 'B',
    'X': 'A',
    'Z': 'C'
}

score = 0
for opponent, me in rounds:
    me_c = conversion[me]
    score += shape_score[me_c]
    if opponent == me_c:
        score += 3
    elif winning_shape[opponent] == me_c:
        score += 6
print(score)

# part two
winning_shape = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}
losing_shape = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}
shape_score = {
    'A': 1,
    'B': 2,
    'C': 3
}

score = 0
for opponent, me in rounds:
    if me == 'Y':
        score += 3
        score += shape_score[opponent]
    elif me == 'X':
        score += shape_score[losing_shape[opponent]]
    elif me == 'Z':
        score += 6
        score += shape_score[winning_shape[opponent]]
print(score)
