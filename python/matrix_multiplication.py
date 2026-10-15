
import csv
import sys
from pathlib import Path


def load_matrix(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [[int(value) for value in row] for row in reader]


def matrix_multiplication(A, B):
    n = len(A)

    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def main():
    if len(sys.argv) != 2:
        print("Usage: python matrix_multiplication.py <size>")
        sys.exit(1)

    n = int(sys.argv[1])

    project_dir = Path(__file__).resolve().parent.parent
    matrix_dir = project_dir / "experiments" / "matrix"

    A = load_matrix(matrix_dir / f"A_{n}.csv")
    B = load_matrix(matrix_dir / f"B_{n}.csv")

    C = matrix_multiplication(A, B)

    print(f"Matrix multiplication completed: {n}x{n}")
    print(f"Result verification value: {C[0][0]}")


if __name__ == "__main__":
    main()
