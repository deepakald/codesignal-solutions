def groupDating(male, female):
    return  [[],[]] if male == female else list(zip(*filter(lambda x: x[0] != x[1], zip(male, female))))