import re
def isMAC48Address(inputString):
    pattern = '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(pattern, inputString) != None:
        return True
    return False
