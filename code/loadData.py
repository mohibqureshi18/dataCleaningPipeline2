import pandas as pd 
import numpy as np

class LoadData:
    def __init__(self,  filePath):
        self.filePath = filePath
        

    def loadData(self):
        self.df = pd.read_csv(self.filePath)
        return self.df