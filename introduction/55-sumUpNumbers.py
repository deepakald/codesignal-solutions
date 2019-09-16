import re
def sumUpNumbers(s):
    out = re.sub('[a-zA-Z!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+',' ',s)
    val = 0

    for ix in sorted(out.split(' ')):
        if ix != '':
            val+= int(ix)
    return val