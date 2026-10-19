
import csv
import subprocess
import time
from pathlib import Path

import psutil

SIZES = [10, 50, 100, 250, 500]
REPETITIONS = 5

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "results"

COMMANDS = {
    "python": ["python", "python/matrix_multiplication.py"],
    "java": ["java", "-cp", "java", "MatrixMultiplication"],
    "c": [str(PROJECT_DIR / "c" / "matrix_multiplication.exe")]
}


def measure_memory(command):
    process = subprocess.Popen(
        command,
        cwd=PROJECT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE
    )

    ps_process = psutil.Process(process.pid)
    peak_memory = 0

    while process.poll() is None:
        try:
            memory = ps_process.memory_info().rss
            peak_memory = max(peak_memory, memory)
        except psutil.NoSuchProcess:
            break

        time.sleep(0.001)

    # Capture one final sample if the process still exists
    try:
        memory = ps_process.memory_info().rss
        peak_memory = max(peak_memory, memory)
    except psutil.NoSuchProcess:
        pass

    _, stderr = process.communicate()

    if process.returncode != 0:
        raise RuntimeError(
            f"Process failed: {stderr.decode(errors='replace')}"
        )

    return peak_memory / (1024 * 1024)


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    results = []

    for language, command in COMMANDS.items():
        print(f"\nBenchmarking {language} memory")

        for n in SIZES:
            for repetition in range(1, REPETITIONS + 1):
                full_command = command + [str(n)]

                memory_mb = measure_memory(full_command)

                results.append([
                    language,
                    n,
                    repetition,
                    memory_mb
                ])

                print(
                    f"{n}x{n} - Repetition {repetition}: "
                    f"{memory_mb:.2f} MB"
                )

    output_file = RESULTS_DIR / "memory_results.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "language",
            "size",
            "repetition",
            "peak_memory_mb"
        ])
        writer.writerows(results)

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()