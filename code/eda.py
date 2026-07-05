import numpy as np
import pandas as pd

class EDA:
    
    def __init__(self, df):
        self.df = df

    def dataInfo(self):
        print(f"dataframe information: {self.df.info()}\n\n")
        print(f"dataframe describe: {self.df.describe().T}\n\n")
        print(f"dataframe Head: {self.df.head(5)}\n\n")
        print(f"Total null values: {self.df.isnull().sum()}\n\n")



