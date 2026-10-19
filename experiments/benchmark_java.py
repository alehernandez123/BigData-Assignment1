
import csv
import subprocess
from pathlib import Path

SIZES = [10, 50, 100, 250, 500]

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "results"


def run_java(n):
    result = subprocess.run(
        ["java", "-cp", "java", "MatrixMultiplication", str(n)],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        check=True
    )

    measurements = []

    for line in result.stdout.splitlines():
        if line.startswith("RESULT,"):
            _, size, repetition, execution_time = line.split(",")

            measurements.append([
                int(size),
                int(repetition),
                float(execution_time)
            ])

    if len(measurements) != 5:
        raise RuntimeError(
            f"Expected 5 measurements for size {n}, "
            f"but found {len(measurements)}"
        )

    return measurements


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    results = []

    for n in SIZES:
        print(f"\nBenchmarking {n}x{n} matrices")

        measurements = run_java(n)

        for size, repetition, execution_time in measurements:
            results.append([size, repetition, execution_time])

            print(
                f"Repetition {repetition}: "
                f"{execution_time:.6f} seconds"
            )

    output_file = RESULTS_DIR / "java_times.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["size", "repetition", "time_seconds"])
        writer.writerows(results)

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()
