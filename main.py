'''
Created on 2017/03/27

@author: y-ok
'''
from crawler import getChemicalElementsInfo, getElementInfo
from formatJson import format_json
import os

if __name__ == '__main__':
        
    jsonfile_name = "chemical_element_info.json"
    jsonfile_path = os.getcwd() + "/output/json/" + jsonfile_name
    
    chemicalElementsList = getChemicalElementsInfo()
    
    getElementInfo(chemicalElementsList)
    
    format_json(chemicalElementsList, jsonfile_path)
    