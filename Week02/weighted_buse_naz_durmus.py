import random

def weighted_srs(data: list, n: int, weights: list, with_replacement: bool):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    secilenler = []
    
    while len(secilenler) < n:
        aday = random.choices(data, weights=weights, k=1)[0]
        if aday not in secilenler:
            secilenler.append(aday)
              return secilenler
