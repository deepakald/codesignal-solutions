def fileNaming(names):
    filenames = {}
    for name in names:
#         print(name)
        if name in filenames:
#             print('inside first if', name)
            newname = ''.join([name,'(',str(filenames[name]),')'])
#             print('newname',newname)
            while (newname in filenames):
#                 print('inside second if',newname)
                newname = ''.join([name,'(',str(filenames[name]+1),')'])
                filenames[name] += 1
#                 print('newname',newname)
            filenames[newname] = 1
        else:
            filenames[name] = 1
#         print(name,' == ',filenames)
    out = []
    _ = [out.append(ix) for ix in filenames.keys()]
    return out