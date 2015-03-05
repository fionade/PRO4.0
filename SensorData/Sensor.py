'''
Created on 22.01.2015

@author: fiona
'''

class Sensor(object):
    '''
    parent class for all sensor objects
    '''


    def __init__(self, name, sensorType, firmata):
        '''
        Constructor
        '''

        
        self.__name = name
        self.__type = sensorType
        
        self.__rawValue = -1
        self.__value = -1
        
        self.__firmata = firmata
        
        self.__thread = None
        self.__running = False

        # TODO: timestamp?
    
        
    def getValue(self):
        raise NotImplementedError("Method not implemented.")

    def getName(self):
        return self.__name

    def read(self):
        return self.__value
    
    def initCommunication(self):
        raise NotImplementedError("Not implemented")
    
    def firmata(self):
        return self.__firmata