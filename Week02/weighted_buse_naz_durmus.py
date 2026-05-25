import random

def weighted_srs(data: list, n: int, weights: list, *, with_replacement: bool = False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    
    expanded = sum([[elem] * int(w * 1000) for elem, w in zip(data, weights)], [])
    return random.sample(expanded, k=n)
