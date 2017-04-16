'''
Created on 2017/04/15

@author: y-ok
'''
import configparser


class Configfile(object):
    '''
    classdocs
    '''
    
    class Params:
        def __init__(self):
            self.jsonFileOutPutPath = ""
            self.jsonFileName = ""

    def __init__(self, configfile):
        '''
        Constructor
        '''
        self.configfile = configfile
    
    def read(self):
        config = configparser.ConfigParser()
        config.read(self.configfile)
        
        section = 'default'
        params = self.Params()
        params.jsonFileOutPutPath = config.get(section, 'jsonFileOutPutPath')
        params.jsonFileName = config.get(section, 'jsonFileName')
        
        return params
    
        
        
