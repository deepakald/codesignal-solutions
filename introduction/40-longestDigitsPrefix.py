def longestDigitsPrefix(inputString):
    if ord(inputString[0]) <48 and ord(inputString[0]) >57:
        return ""
    else:
        i = 0
        while i < len(inputString) and ord(inputString[i])>=47 and ord(inputString[i]) <=58 :
            i+=1
    return inputString[:i]