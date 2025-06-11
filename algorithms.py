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
