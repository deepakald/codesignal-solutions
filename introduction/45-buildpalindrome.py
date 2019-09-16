def checkpalindrome(st):
    if st == st[::-1]:
        return True
    return False
        # for ix in range(len(st)//2): 
        #     if st[ix] == st[len(st) - ix + 1 ]:
        #         continue
        #     else:  
        #         return False                
        # return True 
    
def buildPalindrome(st):
    
    if st == st[::-1]:
        return st
    
    indices = []
    for ix in range(len(st)-1,-1,-1):
        temp  = st[ix:]
        if temp == temp[::-1]:            
            indices.append(ix)
    return "".join([st,st[:min(indices)][::-1]])