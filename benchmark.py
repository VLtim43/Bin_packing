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


def plot_all_metrics(results):
    fig, axs = plt.subplots(3, 1, figsize=(10, 14))

    for name, data in results.items():
        axs[0].plot(
            data['n'],
            data['time'],
            label=name,
        )
    axs[0].set_title("Time Complexity vs Number of Items")
    axs[0].set_xlabel("Number of items (n)")
    axs[0].set_ylabel("Average Execution Time (s)")
    axs[0].legend()
    axs[0].grid(True)

    for name, data in results.items():
        axs[1].plot(
            data['n'],
            data['bins'],
            label=name,
        )
    axs[1].set_title("Bin Usage")
    axs[1].set_xlabel("Number of items (n)")
    axs[1].set_ylabel("Average Number of Bins Used")
    axs[1].legend()
    axs[1].grid(True)

    for name, data in results.items():
        axs[2].plot(
            data['n'],
            data['utilization'],
            label=name,
        )
    axs[2].set_title("Bin Space Utilization")
    axs[2].set_xlabel("Number of items (n)")
    axs[2].set_ylabel("Average Utilization (0 to 1)")
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sizes = list(range(1, 50, 1))
    results = benchmark_algorithms(sizes)
    plot_all_metrics(results)
