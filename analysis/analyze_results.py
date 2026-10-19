
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "results"
ANALYSIS_DIR = PROJECT_DIR / "analysis"


def calculate_statistics(df, value_column):
    statistics = (
        df.groupby(["language", "size"])[value_column]
        .agg(
            count="count",
            mean="mean",
            median="median",
            minimum="min",
            maximum="max",
            std="std"
        )
        .reset_index()
    )

    quartiles = (
        df.groupby(["language", "size"])[value_column]
        .quantile([0.25, 0.75])
        .unstack()
        .reset_index()
    )

    quartiles.columns = [
        "language",
        "size",
        "q1",
        "q3"
    ]

    statistics = statistics.merge(
        quartiles,
        on=["language", "size"]
    )

    statistics["iqr"] = (
        statistics["q3"] - statistics["q1"]
    )

    return statistics


def analyze_time():
    print("\n=== EXECUTION TIME ANALYSIS ===")

    data = []

    for language in ["python", "java", "c"]:
        filename = RESULTS_DIR / f"{language}_times.csv"

        df = pd.read_csv(filename)
        df["language"] = language

        data.append(df)

    time_data = pd.concat(data, ignore_index=True)

    time_statistics = calculate_statistics(
        time_data,
        "time_seconds"
    )

    print(time_statistics.to_string(index=False))

    output_file = ANALYSIS_DIR / "time_statistics.csv"

    time_statistics.to_csv(output_file, index=False)

    print(f"\nTime statistics saved to {output_file}")


def analyze_memory():
    print("\n=== MEMORY USAGE ANALYSIS ===")

    filename = RESULTS_DIR / "memory_results.csv"

    memory_data = pd.read_csv(filename)

    memory_statistics = calculate_statistics(
        memory_data,
        "peak_memory_mb"
    )

    print(memory_statistics.to_string(index=False))

    output_file = ANALYSIS_DIR / "memory_statistics.csv"

    memory_statistics.to_csv(output_file, index=False)

    print(f"\nMemory statistics saved to {output_file}")


def main():
    ANALYSIS_DIR.mkdir(exist_ok=True)

    analyze_time()
    analyze_memory()

    print("\nStatistical analysis completed!")


if __name__ == "__main__":
    main()
