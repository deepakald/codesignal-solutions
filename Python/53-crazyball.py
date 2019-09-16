from itertools import combinations

def crazyball(players, k):
    return sorted(list(combinations(sorted(players),k)))