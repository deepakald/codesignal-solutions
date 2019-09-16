import xml.etree.ElementTree as ET
from collections import OrderedDict as odict

def xmlTags(xml):
    checks = [(ET.fromstring(xml), 0)] # ET.Element, depth
    finds = odict() # tag_name: [depth, set(attributes)]
    
    while checks:
        node, depth = checks.pop()
        if node.tag in finds:
            finds[node.tag][1] |= set(node.attrib.keys())
        else:
            finds[node.tag] = [depth, set(node.attrib.keys())]
        
        # Child nodes must be iterated in reverse for stack to work properly
        for child in reversed(node): 
            checks.append((child, depth+1))
    
    res = [2*v[0]*'-' + k + '(' + ", ".join(sorted(v[1])) + ')' for k, v in finds.items()]
    return res
                    