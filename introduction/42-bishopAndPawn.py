def bishopAndPawn(bishop, pawn):
    
    if bishop[0] == pawn[0]: return False
    
    else:
        if abs(ord(bishop[0]) - ord(pawn[0])) ==  abs(int(bishop[1]) - int(pawn[1])):
            return True
    return False
        