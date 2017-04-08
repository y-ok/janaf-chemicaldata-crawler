'''
Created on 2017/03/27

@author: y-ok
'''

from collections import namedtuple

from bs4 import BeautifulSoup
import requests

base_url = "http://kinetics.nist.gov"

def getChemicalElementsInfo():
    periodic_table_url = base_url + "/janaf/periodic_table.html"
    
    r = requests.get(periodic_table_url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    chemicalElementList = []
    chemicalElementInfo = namedtuple('chemicalElementInfo', ('elementName', 'elementUrl'))
    
    for td_tag in soup.findAll("td"):
        if td_tag.find("a") is None:
            continue
        elementName = td_tag.find("br").string
        elementUrl  = base_url + td_tag.find("a").get("href")
        chemicalElementList.append(chemicalElementInfo(elementName, elementUrl))
    return chemicalElementList


def getElementInfo(chemicalElementList):
    
    ElementListAll = []
    for chemicalElement in chemicalElementList:
        
        elementUrl = chemicalElement.elementUrl
        r = requests.get(elementUrl)
        soup = BeautifulSoup(r.text, "html.parser")
    
        table = soup.findAll("table")[0]
        rows = table.findAll("tr")
    
        ElementList = []
        for row in rows:
            index = 0
            for cell in row.findAll('td'):
                index = index + 1
                if cell.get("width") is None and index != 9:
                    if cell.find("a") is None:
                        ElementList.append(cell.get_text())
                if index == 9:
                    ElementList.append(base_url + "/janaf/" + cell.find("a").get("href"))
                    
        for element in ElementList:
            print(element)
    
        print("---------------------------")
    
        ElementListAll.append(ElementList)

    
    for row_list in ElementListAll:
        print(row_list)
    
