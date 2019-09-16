def findEmailDomain(address):
    index = address.rfind('@')
    return address[index+1:]