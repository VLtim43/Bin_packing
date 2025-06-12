import random
import time
import matplotlib.pyplot as plt
from algorithms import next_fit, first_fit, best_fit, first_fit_decreasing, best_fit_decreasing, brute_force_bin_packing

ALGORITHMS = {
    'Next Fit': next_fit,
    'First Fit': first_fit,
    'Best Fit': best_fit,
    'FFD': first_fit_decreasing,
    'BFD': best_fit_decreasing,
    'Brute Force': brute_force_bin_packing,
}


def benchmark_algorithms(sizes, trials=50):
    results = {name: {'n': [], 'time': [], 'bins': [], 'utilization': []}
               for name in ALGORITHMS}

    for n in sizes:
        for name, algo in ALGORITHMS.items():
            # Skip Brute Force for large n
            if name == 'Brute Force' and n > 10:
                continue

            total_time, total_bins, total_util = 0, 0, 0

            for _ in range(trials):
                items = [random.uniform(0.1, 1.0) for _ in range(n)]
                total_size = sum(items)

                start = time.perf_counter()
                bins = algo(items)
                end = time.perf_counter()

                bin_count = len(bins)
                used_space = total_size
                total_utilization = used_space / (bin_count * 1.0)

                total_time += end - start
                total_bins += bin_count
                total_util += total_utilization

            results[name]['n'].append(n)
            results[name]['time'].append(total_time / trials)
            results[name]['bins'].append(total_bins / trials)
            results[name]['utilization'].append(total_util / trials)

    return results


def plot_time_complexity(results):
    plt.figure(figsize=(10, 5))
    for name, data in results.items():
        plt.plot(data['n'], data['time'], label=name)
    plt.title("Time Complexity vs Number of Items")
    plt.xlabel("Number of items (n)")
    plt.ylabel("Average Execution Time (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_bin_usage(results):
    plt.figure(figsize=(10, 5))
    for name, data in results.items():
        plt.plot(data['n'], data['bins'], label=name)
    plt.title("Bin Usage")
    plt.xlabel("Number of items (n)")
    plt.ylabel("Average Number of Bins Used")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_space_utilization(results):
    plt.figure(figsize=(10, 5))
    for name, data in results.items():
        plt.plot(data['n'], data['utilization'], label=name)
    plt.title("Bin Space Utilization")
    plt.xlabel("Number of items (n)")
    plt.ylabel("Average Utilization (0 to 1)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_all_metrics(results):
    plot_time_complexity(results)
    plot_bin_usage(results)
    plot_space_utilization(results)


if __name__ == "__main__":
    sizes = list(range(1, 50, 1))
    results = benchmark_algorithms(sizes)
    plot_all_metrics(results)
