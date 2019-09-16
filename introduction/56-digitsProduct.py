def digitsProduct(product):
    if product ==1 : return product        
    
    
    if product < 10:
        if product in [2,3,5,7]:
            return product
        return product+10
        
    arr = []
    n = 9
    while n > 1:
        if product % n == 0:
            # print('product:',product)
            product = product / n 
            arr.append(n)
            n = 10
        # print(n)
        n -= 1
    if product >1: return -1
    arr = sorted(arr)
    
    return int("".join( [str(i) for i in arr]))