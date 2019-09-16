def messageFromBinaryCode(s):
    out = []
    for ix in range(0,len(s),8):
        st  = s[ix:ix+8][::-1]
        val = 0
        for ix in range(8):
            val += 2**ix * int(st[ix])
        out.append(chr(val))
    return ''.join([i for i in out])