def validTime(time):
    hh,mm = time[:2], time[3:]
    
    assert(len(hh) == 2)
    assert(len(mm) == 2)
    
    if int(hh)>=0 and int(hh)<=23 and int(mm)>=0 and int(mm)<= 59:
        return True
    return False