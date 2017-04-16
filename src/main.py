'''
Created on 2017/03/27

@author: y-ok
'''
import os

from config import Configfile
from crawler import JanafCrawler
from formatJson import JsonUtil


if __name__ == '__main__':
    
    # 設定ファイル読み込み
    config = Configfile('./config.ini')
    params = config.read()
    jsonfile_path = os.getcwd() + params.jsonFileOutPutPath + params.jsonFileName

    # クローラによる情報取得   
    janafCrawler = JanafCrawler()
    chemicalElementsList = janafCrawler.getChemicalElementsInfo()

    # Jsonファイル作成
    jsonUtil = JsonUtil()
    jsonUtil.formatJson(chemicalElementsList, jsonfile_path)
