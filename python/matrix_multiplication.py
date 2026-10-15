def matrix_multiplication(A, B):
    n = len(A)

    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Prueba inicial
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = matrix_multiplication(A, B)

for row in C:
    print(row)