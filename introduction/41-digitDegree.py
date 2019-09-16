def digitDegree(n):
    if n < 10: return 0
    else:
        c = 0
        while(n>=10):
            x = str(n)
            n = 0
            for y in x:
                n+=int(y)
            c += 1
    return c