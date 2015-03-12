'''
Created on 12.03.2015

@author: fiona
'''

class i2cSensor(object):
    '''
    Parent class for i2c sensors used with the pyMata library
    '''


    def __init__(self, board, params):
        '''
        Constructor
        '''
        self.__board = board
        
    def getBoard(self):
        return self.__board