def deleteDigit(n):
    
    a = []
    n = str(n)
    for i,j in enumerate(n):
        temp = n[:i]+n[i+1:]
        a.append(temp)
    a = map(int, a)
    return max(a)