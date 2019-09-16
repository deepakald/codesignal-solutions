def maliciousProgram(curDate, changes):
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12
            }
    inverse_map = dict(list(zip(list(range(1,13)),list(months.keys()))))
    import datetime
    day,month,year,t = curDate.split(' ')
    h,m,s = list(map(int, t.split(':')))
    day  = int(day)
    day  += changes[0]    
    mths  = months[month]
    mths +=changes[1]  
    if mths>12 or mths <1:
        mths = mths%12
    year = int(year)
    year += changes[2]
    h +=changes[3]
    m +=changes[4]
    s +=changes[5]    
    try:
        newdate = datetime.datetime(year,mths,day,h,m,s)
        day,h,m,s = list(map(str,list([day,h,m,s])))
        if int(day)<10: day = '0'+day
        if int(h)<10: h = '0'+h
        if int(m)<10: m = '0'+m 
        if int(s)<10: s = '0'+s
        return ' '.join([day,inverse_map[mths],str(year),h+':'+m+':'+s])
    except ValueError as e:
        return curDate        