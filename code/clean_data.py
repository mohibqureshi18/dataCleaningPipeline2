import pandas as pd
import numpy as np

class CleanData:
    def __init__(self, df):
        self.df = df
    
    def remove_duplicated(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    
    # def filter_rows(self, condition):
    #     self.df = self.df[condition]
    #     return self.df
    

    def missing_values(df):
        print(df.isnull().any(axis=1))