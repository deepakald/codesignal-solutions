from itertools import product, combinations

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([x  for x in list(createNumber(ix) for ix in list(product(digits, repeat=k))) if int(x)%d==0])