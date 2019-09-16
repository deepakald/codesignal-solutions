def lineEncoding(st):
    prev = st[0]
    count = 1
    out = []
    for i in st[1:]:
        if i == prev:
            
            count += 1    
        elif i != prev:
            if count > 1:
                out.append(''.join([str(count),prev]))
            else:
                out.append(''.join(prev))
            count = 1
        prev = i
    if count > 1:
        out.append(''.join([str(count),prev]))
    else:
        out.append(''.join(prev))
    return ''.join(out)