from itertools import permutations,islice

def kthPermutation(numbers, k):
    return list(list(islice(list(permutations(numbers)), k-1, k))[0])