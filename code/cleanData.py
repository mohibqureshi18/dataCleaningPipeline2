import numpy as np
import pandas as pd

class CleanData:
    
    def __init__(self, df):
        self.df = df
    
    def removeDuplicates(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    def handleMissingValues(self):
        self.df['num_arrests'] = self.df['num_arrests'].fillna(0)
        self.df['victim_gender'] = self.df['victim_gender'].fillna('unknown')
        return self.df
    