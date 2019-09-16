def isBeautifulString(inputString):
    d = {}
    for e in inputString:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    previous = 0
    al = [chr(i) for i in range(97, 123)]
    r = max(set(inputString))
    for e in al:
        if e == r:
            break
        elif e in inputString:
            pass
        else:
            return False
            
        
    
    for key, v in sorted(d.items()):
        if previous and d[key] > previous:
            return False
        else:
            previous = d[key]
    return True