'''
Created on 22.01.2015

@author: fiona
'''

class Sensor(object):
    '''
    parent class for all sensor objects
    '''


    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
        self.__name = name
        self.__type = sensorType
        
        self.__rawValue = -1
        self.__value = -1
        
        # TODO: timestamp?
    
        
    def getCurrentData(self):
        raise NotImplementedError("Method not implemented.")