
some_builds = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

trans_matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(len(some_builds)):
    for j in range(len(some_builds[0])):
        trans_matrix[j][i] = some_builds[i][j]

a = sum(trans_matrix[0]), sum(trans_matrix[1]), sum(trans_matrix[2]), sum(trans_matrix[3])

print((a.index(max(a)) + 1), ',', max(a))