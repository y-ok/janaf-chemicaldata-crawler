'''
Created on 2017/03/27

@author: y-ok
'''

from collections import namedtuple

from bs4 import BeautifulSoup
import requests

base_url = "http://kinetics.nist.gov"

class JanafCrawler(object):
    
    def __init__(self):
        self.chemicalElementList = []
        self.elementList = []
        self.thermochemicalDataList = []


    def getChemicalElementsInfo(self):
        periodic_table_url = base_url + "/janaf/periodic_table.html"
        
        r = requests.get(periodic_table_url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        chemicalElementInfo = namedtuple('chemicalElementInfo', ('elementName', 'elementUrl', 'elementsList'))
        
        for td_tag in soup.findAll("td"):
            if td_tag.find("a") is None:
                continue
            elementName = td_tag.find("br").string
            elementUrl = base_url + td_tag.find("a").get("href")
            elementsList = self.getElementInfo(elementUrl)
            self.chemicalElementList.append(chemicalElementInfo(elementName, elementUrl, elementsList))
        return self.chemicalElementList


    def getElementInfo(self, elementUrl):
        
        r = requests.get(elementUrl)
        soup = BeautifulSoup(r.text, "html.parser")
        
        table = soup.findAll("table")[0]
        rows = table.findAll("tr")
        
        elementInfo = namedtuple('elementInfo', ('casNumber', 'formula', 'name', 'state', 'JANAFTableUrl', 'thermochemicalDataList'))
        for row in rows:            
            elementList = []
            index = 0
            for cell in row.findAll('td'):
                index = index + 1
                if cell.get("width") is None and index != 9:
                    if cell.find("a") is None:
                        # casNumber
                        if index == 1:
                            elementList.append(cell.get_text())
                        # formula
                        elif index == 3:
                            elementList.append(cell.get_text())
                        # name
                        elif index == 5:
                            elementList.append(cell.get_text())
                        # state
                        elif index == 7:
                            elementList.append(cell.get_text())
                elif index == 9:
                    JANAFTableUrl = base_url + "/janaf/" + cell.find("a").get("href")
                    elementList.append(JANAFTableUrl)
                
            if elementList != []:
                print("-----------------------")
                print(elementList[1], elementList[2], elementList[3])
                thermochemicalDataList = self.getThermochemicalDataList(elementList[4])
                self.elementList.append(elementInfo(elementList[0], elementList[1], elementList[2], elementList[3], elementList[4], thermochemicalDataList))
            
        return self.elementList

    def getThermochemicalDataList(self, JANAFTableUrl):
        
        r = requests.get(JANAFTableUrl)
        soup = BeautifulSoup(r.text, "html.parser")
        
        table = soup.findAll("table")[0]
        rows = table.findAll("tr")
        
        thermochemicalData = namedtuple('thermochemicalData', ('temperature', 'specificHeat', 'entropy', 'gibbs', 'enthalpy'))
        for row in rows:
            chemicalData = []
            index = 0
            for cell in row.findAll('td'):
                index = index + 1
                if cell.get("width") is None and cell.get("align") is None and cell.get("colspan") is None:
                    
                    if cell.get_text() == "+":
                        continue
                    
                    if index == 1:
                        # T/K
                        chemicalData.append(cell.get_text())
                    elif index == 3:
                        # Cp°
                        chemicalData.append(cell.get_text())
                    elif index == 5:
                        # S°
                        chemicalData.append(cell.get_text())
                    elif index == 7:
                        # -[G°-H°(Tr)]/T
                        chemicalData.append(cell.get_text())
                    elif index == 9:
                        # H-H°(Tr)
                        chemicalData.append(cell.get_text())
                    else:
                        continue
                else:
                    continue
                
            if chemicalData != []:
                print(chemicalData[0],chemicalData[1],chemicalData[2],chemicalData[3],chemicalData[4])
                self.thermochemicalDataList.append(thermochemicalData(
                    chemicalData[0],
                    chemicalData[1],
                    chemicalData[2],
                    chemicalData[3],
                    chemicalData[4]
                ))
    
        return self.thermochemicalDataList
            
    
