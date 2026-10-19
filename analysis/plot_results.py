
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = PROJECT_DIR / "analysis"
PLOTS_DIR = ANALYSIS_DIR / "plots"

PLOTS_DIR.mkdir(exist_ok=True)

LANGUAGES = ["python", "java", "c"]


def plot_execution_time():
    df = pd.read_csv(ANALYSIS_DIR / "time_statistics.csv")

    plt.figure(figsize=(9, 6))

    for language in LANGUAGES:
        data = df[df["language"] == language].sort_values("size")

        plt.plot(
            data["size"],
            data["median"],
            marker="o",
            label=language.capitalize()
        )

    plt.xlabel("Matrix size (N)")
    plt.ylabel("Median execution time (seconds)")
    plt.title("Matrix Multiplication Execution Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(PLOTS_DIR / "execution_time.png", dpi=300)
    plt.close()


def plot_execution_time_log():
    df = pd.read_csv(ANALYSIS_DIR / "time_statistics.csv")

    plt.figure(figsize=(9, 6))

    for language in LANGUAGES:
        data = df[df["language"] == language].sort_values("size")

        plt.plot(
            data["size"],
            data["median"],
            marker="o",
            label=language.capitalize()
        )

    plt.yscale("log")
    plt.xlabel("Matrix size (N)")
    plt.ylabel("Median execution time (seconds, log scale)")
    plt.title("Matrix Multiplication Execution Time (Log Scale)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(PLOTS_DIR / "execution_time_log.png", dpi=300)
    plt.close()


def plot_memory_usage():
    df = pd.read_csv(ANALYSIS_DIR / "memory_statistics.csv")

    plt.figure(figsize=(9, 6))

    for language in LANGUAGES:
        data = df[df["language"] == language].sort_values("size")

        plt.plot(
            data["size"],
            data["median"],
            marker="o",
            label=language.capitalize()
        )

    plt.xlabel("Matrix size (N)")
    plt.ylabel("Median peak observed RSS (MB)")
    plt.title("Matrix Multiplication Memory Usage")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(PLOTS_DIR / "memory_usage.png", dpi=300)
    plt.close()


def plot_time_variability():
    df = pd.read_csv(ANALYSIS_DIR / "time_statistics.csv")

    plt.figure(figsize=(9, 6))

    for language in LANGUAGES:
        data = df[df["language"] == language].sort_values("size")

        plt.plot(
            data["size"],
            data["iqr"],
            marker="o",
            label=language.capitalize()
        )

    plt.xlabel("Matrix size (N)")
    plt.ylabel("Execution time IQR (seconds)")
    plt.title("Execution Time Variability")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(PLOTS_DIR / "time_variability.png", dpi=300)
    plt.close()


def main():
    plot_execution_time()
    plot_execution_time_log()
    plot_memory_usage()
    plot_time_variability()

    print("All plots generated successfully!")


if __name__ == "__main__":
    main()
