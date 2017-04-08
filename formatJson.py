'''
Created on 2017/03/27

@author: y-ok
'''
import json

import collections as cl


def formatJson(chemicalElementsList, jsonfile_path):
    
    ys = []
    for i in range(len(chemicalElementsList)):
        data = cl.OrderedDict()
        
        data["element_name"] = chemicalElementsList[i].elementName
        data["element_url"] = chemicalElementsList[i].elementUrl
        elementsList = chemicalElementsList[i].elementsList
        
        innerys = []
        for j in range(len(elementsList)):
            innerdata = cl.OrderedDict()
            
            innerdata["casNumber"] = elementsList[j].casNumber
            innerdata["formula"] = elementsList[j].formula
            innerdata["name"] = elementsList[j].name
            innerdata["state"] = elementsList[j].state
            innerdata["JANAFTableUrl"] = elementsList[j].JANAFTableUrl
            
            innerys.append(innerdata)
        
        data["elementsList"] = innerys
        
        ys.append(data)

    text = json.dumps(ys, indent=4)
    with open(jsonfile_path, 'w') as th:
        th.write(text)
