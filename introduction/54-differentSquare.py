def differentSquares(matrix):
    
    out = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            try:
                i = matrix[row][column]
                j = matrix[row + 1][column]
                k = matrix[row][column + 1]
                l = matrix[row + 1][column + 1]
                out.append([i,j,k,l])
            except IndexError:
                pass
    a = set(tuple(element) for element in out if element is not None)
    return len(a)