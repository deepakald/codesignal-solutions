def primesSum(a, b):
    return   sum([n for n in range(a, b+1) if n > 1 and all([n % b for b in range(2, int(math.sqrt(n))+ 1)])])
