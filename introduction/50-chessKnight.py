def chessKnight(cell):
    moves = 0
    row,col = cell[0],int(cell[1])
    
    if col+2 <=8:
        if ord(row)+1 <= 104:
            moves +=1
        if ord(row)-1 >= 97:
            moves +=1 
    if col+1 <= 8:
        if ord(row)+2 <= 104:
            moves+=1
        if ord(row)-2 >=97:
            moves+=1
    if col -2 >=1:
        if ord(row)+1 <= 104:
            moves +=1
        if ord(row)-1 >= 97:
            moves +=1
    if col -1 >=1:
        if ord(row)+2 <= 104:
            moves+=1
        if ord(row)-2 >=97:
            moves+=1
    return moves
    
        
       
    