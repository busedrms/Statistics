mport random

def weighted_srs(data: list, n: int, weights: list, *, with_replacement: bool = False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(sum([[e] * int(w * 100) for e, w in zip(data, weights)], []), k=n)
