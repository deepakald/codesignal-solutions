from collections import Counter

def electionsWinners(votes, k):    
    
    if all(votes[0] == ix for ix in votes[1:]):
        if k == 0:  
            return 0
        else:
            return len(votes)
    
    m = max(votes)
    my_dict = dict(Counter(votes))
        
   
    if k == 0:
        if my_dict[m] > 1:
            return 0
        else:
            return my_dict[m]

    wins = 0
    for ix in votes:
        if ix!= m and ix + k > m:
            wins += 1
    wins += my_dict[m]
    return wins