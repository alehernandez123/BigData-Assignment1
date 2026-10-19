
import csv
import sys
from pathlib import Path

SIZES = [10, 50, 100, 250, 500]

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "results"


def load_matrix(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [[int(value) for value in row] for row in reader]


def compare_results(n):
    python_result = load_matrix(RESULTS_DIR / f"python_{n}.csv")
    java_result = load_matrix(RESULTS_DIR / f"java_{n}.csv")
    c_result = load_matrix(RESULTS_DIR / f"c_{n}.csv")

    if python_result == java_result == c_result:
        print(f"Matrix {n}x{n}: PASSED")
        return True

    print(f"Matrix {n}x{n}: FAILED")
    return False


def main():
    all_passed = True

    for n in SIZES:
        try:
            if not compare_results(n):
                all_passed = False
        except (OSError, ValueError) as error:
            print(f"Matrix {n}x{n}: ERROR - {error}")
            all_passed = False

    if all_passed:
        print("All matrix comparisons passed!")
    else:
        print("Some matrix comparisons failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()