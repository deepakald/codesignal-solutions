class Prizes(object):
    def __init__(self,purchases,n,d):
        self.purchases = purchases
        self.n = n
        self.d = d
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i < len(self.purchases):
            self.i += 1
            if self.i%self.n == 0 and self.purchases[self.i-1]%self.d == 0:
                return self.i
        raise StopIteration
    
            
            
    


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
