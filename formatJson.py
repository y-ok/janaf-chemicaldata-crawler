'''
Created on 2017/03/27

@author: y-ok
'''
import json

import collections as cl


def format_json(chemicalElementsList, jsonfile_path):
    
    ys = []
    for i in range(len(chemicalElementsList)):
        data = cl.OrderedDict()
        
        data["element_name"] = chemicalElementsList[i].elementName
        data["element_url"] = chemicalElementsList[i].elementUrl
        ys.append(data)

    text = json.dumps(ys, indent=4)
    with open(jsonfile_path, 'w') as th:
        th.write(text)
