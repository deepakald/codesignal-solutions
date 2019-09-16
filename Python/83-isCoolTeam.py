class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self): 
        f = [i[0].lower() for i in self.names]
        l = [i[-1].lower() for i in self.names]
        for i in f :
            try:
                l.remove(i)
            except:
                pass
        if len(l) > 1:
            return False    
        df = dict()
        dl = dict()
        nodes = []
        c = 0
        for i in self.names:
            if i[0].lower() in df:
                df[i[0].lower()] += [c]
            else:
                df.update( { i[0].lower() : [c] } )
            if i[-1].lower() in dl:
                dl[i[-1].lower()] += [c]
            else:
                dl.update( { i[-1].lower() : [c] } )
            nodes.append( [i[0].lower(), i[-1].lower()] )
            c += 1
        g = 0
        f = 1
        for i in nodes:
                if i[1] in df:
                    if (i[0] not in dl ) or ( len(df[i[0]]) > len(dl[i[0]]) ):
                        f = 0
                        break
                g += 1
        if f : g = 0 
        v = [0]*len(nodes)
        q = df[nodes[g][0]]
        while q != []:
            print(v)
            n = q.pop(0)
            v[n] = 1
            try :
                l = df[nodes[n][1]][:]
                for i in l:
                    if v[i] == 0 :
                        q.append( df[ nodes[n][1] ].pop(0)  )
            except : pass
        
        for i in v:
            if i == 0 : return False
        return True
                
            

def isCoolTeam(team):
    return bool(Team(team))
