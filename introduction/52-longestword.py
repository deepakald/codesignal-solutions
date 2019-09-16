import re
def longestWord(t):
    my_dict = {}
    for ix in re.split('[^a-zA-Z]', t):
        my_dict[ix.strip(string.punctuation)] = len(ix.strip(string.punctuation))
    return max(my_dict, key = lambda k: my_dict[k])
    