
import csv
import sys
import time
from pathlib import Path

SIZES = [10, 50, 100, 250, 500]
REPETITIONS = 5

PROJECT_DIR = Path(__file__).resolve().parent.parent
MATRIX_DIR = PROJECT_DIR / "experiments" / "matrix"
RESULTS_DIR = PROJECT_DIR / "results"

sys.path.insert(0, str(PROJECT_DIR / "python"))

from matrix_multiplication import load_matrix, matrix_multiplication


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    results = []

    for n in SIZES:
        A = load_matrix(MATRIX_DIR / f"A_{n}.csv")
        B = load_matrix(MATRIX_DIR / f"B_{n}.csv")

        print(f"\nBenchmarking {n}x{n} matrices")

        for repetition in range(1, REPETITIONS + 1):
            start_time = time.perf_counter()

            C = matrix_multiplication(A, B)

            execution_time = time.perf_counter() - start_time

            results.append([n, repetition, execution_time])

            print(
                f"Repetition {repetition}: "
                f"{execution_time:.6f} seconds"
            )

    output_file = RESULTS_DIR / "python_times.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["size", "repetition", "time_seconds"])
        writer.writerows(results)

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()
