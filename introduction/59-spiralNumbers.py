def spiralNumbers(n):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    curdir = 0
    curpos = (0,0)
    res = [[0 for ix in range(n)] for j in range(n)]

    for i in range(1,n*n+1):
        res[curpos[0]][curpos[1]] = i
        nextpos = curpos[0]+dirs[curdir][0], curpos[1]+dirs[curdir][1]
        if not (0 <= nextpos[0] < n and 
                0 <= nextpos[1] < n and
                res[nextpos[0]][nextpos[1]] == 0):
            curdir = (curdir + 1)%4
            nextpos = curpos[0]+dirs[curdir][0], curpos[1]+dirs[curdir][1]
        curpos = nextpos
    return res