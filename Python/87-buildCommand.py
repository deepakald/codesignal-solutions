import numbers
import json
def buildCommand(jsonFile):
    from collections import OrderedDict as od
    def innerString(s):
        for k,v in s.items():
            if isinstance(v, str):
                s[k]= ""
            elif isinstance(v, numbers.Number):
                s[k] = 0
            elif isinstance(v, list):
                s[k]= []
            elif isinstance(v,dict):
                innerString(v)
        return s
    
    string = json.loads(jsonFile, object_pairs_hook=od)
    out = innerString(string)
    return json.dumps(out)