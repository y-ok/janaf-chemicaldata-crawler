'''
Created on 2017/03/27

@author: y-ok
'''
import json

import collections as cl

class JsonUtil(object):
    
    def __init__(self):
        self.ys = []

    def formatJson(self, chemicalElementsList, jsonfile_path):
        
        for i in range(len(chemicalElementsList)):
            data = cl.OrderedDict()
            
            data["element_name"] = chemicalElementsList[i].elementName
            data["element_url"] = chemicalElementsList[i].elementUrl
            elementsList = chemicalElementsList[i].elementsList
            
            innerys1 = []
            for j in range(len(elementsList)):
                innerdata1 = cl.OrderedDict()
                
                innerdata1["casNumber"] = elementsList[j].casNumber
                innerdata1["formula"] = elementsList[j].formula
                innerdata1["name"] = elementsList[j].name
                innerdata1["state"] = elementsList[j].state
                innerdata1["JANAFTableUrl"] = elementsList[j].JANAFTableUrl
                thermochemicalDataList = elementsList[j].thermochemicalDataList
                
                innerys2 = []
                for k in range(len(thermochemicalDataList)):
                    innerdata2 = cl.OrderedDict()
                    
                    innerdata2["temperature"] = thermochemicalDataList[k].temperature
                    innerdata2["specificHeat"] = thermochemicalDataList[k].specificHeat
                    innerdata2["entropy"] = thermochemicalDataList[k].entropy
                    innerdata2["gibbs"] = thermochemicalDataList[k].gibbs
                    innerdata2["enthalpy"] = thermochemicalDataList[k].enthalpy
                    
                    innerys2.append(innerdata2)
                    
                innerdata1["thermochemicalDataList"] = innerys2
                
                innerys1.append(innerdata1)
            
            data["elementsList"] = innerys1
            
            self.ys.append(data)
    
        text = json.dumps(self.ys, indent=4)
        with open(jsonfile_path, 'w') as th:
            th.write(text)
