n = 7
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        matrix[i][j] = n - i - j

for row in matrix:
    print(" ".join(map(str, row)))
