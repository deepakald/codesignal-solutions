def sudoku(c):
    if any([len(set(ix))==1 for ix in c]):
        return False
    out1 = set([sum(ix) for ix in c]) == {45}
    transpose = list(map(list, zip(*c)))
    out2 = set([sum(ix) for ix in transpose]) == {45}

    val = {}.fromkeys(['b'+str(i) for i in range(9)])
    k= 0 
    for ix in range(9):
        if ix%3 == 0 and ix!=0:
            k += 3
        for col in range(0,9,3):
            if  val['b'+str(k+col//3)]!= None:
                val['b'+str(k+col//3)] += sum(c[ix][col:col+3])
            else:
                val['b'+str(k+col//3)] = sum(c[ix][col:col+3])
    out3 = all([ix[1] == 45 for ix in val.items()])
    return all([out1,out2,out3])