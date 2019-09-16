def calkinWilfSequence(number):
    def fractions():
        from fractions import gcd
        a = b = 1
        while 1:
            yield [a, b]
            a, b = b, 2 * (a - a % b) + b - a                    
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
