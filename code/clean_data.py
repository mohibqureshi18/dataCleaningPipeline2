import pandas as pd
import numpy as np

class CleanData:
    def __init__(self, df):
        self.df = df
    
    def remove_duplicated(self):
        self.df.drop_duplicates(inplace=True)
        return self.df

    