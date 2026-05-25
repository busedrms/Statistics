import random

def weighted_srs(data: list, n: int, weights: list, with_replacement: bool):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)

    expanded = sum([[elem] * int(w) for elem, w in zip(data, weights)], [])
    return random.sample(expanded, k=n)