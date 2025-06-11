
def brute_force_bin_packing(items, capacity=1.0):
    if len(items) > 10:
        raise ValueError("Brute-force only allowed for 10 items or fewer")

    min_bins = [len(items)]

    def backtrack(remaining, bins):
        if not remaining:
            min_bins[0] = min(min_bins[0], len(bins))
            return
        if len(bins) >= min_bins[0]:
            return
        item = remaining[0]
        rest = remaining[1:]

        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                backtrack(rest, bins)
                bins[i] -= item

        bins.append(item)
        backtrack(rest, bins)
        bins.pop()

    backtrack(items, [])
    return [0] * min_bins[0]


def next_fit(items, capacity=1.0):
    bins = [0]
    for item in items:
        if bins[-1] + item <= capacity:
            bins[-1] += item
        else:
            bins.append(item)
    return bins


def first_fit(items, capacity=1.0):
    bins = []
    for item in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break
        if not placed:
            bins.append(item)
    return bins


def best_fit(items, capacity=1.0):
    bins = []
    for item in items:
        best_idx = -1
        min_space_left = float('inf')
        for i, fill in enumerate(bins):
            space_left = capacity - fill
            if item <= space_left and space_left < min_space_left:
                best_idx = i
                min_space_left = space_left
        if best_idx >= 0:
            bins[best_idx] += item
        else:
            bins.append(item)
    return bins


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    return best_fit(sorted(items, reverse=True), capacity)


def is_valid_bin(bin_items, capacity):
    return sum(bin_items) <= capacity
