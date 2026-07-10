import numpy as np
import pandas as pd

class EDA:

    def __init__(self, df):
        self.df = df

    def dataInfo(self):
        print()
        print("BASIC INFORMATION:")
        self.df.info()
        print(f"\nShape of dataset:\t{self.df.shape}") 
        print(f"\nColumns of Dataset:\t{self.df.columns}")
        print(f"\nDataTypes of Dataset:\t{self.df.dtypes}")
        # print(f"\nDataTypes of Dataset:\t{self.df.dtypes}")
              
    def summary_statistics(self):
        print(f"\nsummary_statistics of Dataset:\t{self.df.describe()}")
    
    def missing_values(self):
        print(f"\nMissing values of each column:\t{self.df.isnull().sum()}")

    def duplicate_rows(self):
        print(f"\nDuplicate Rows:\t{self.df.duplicated().sum()}")

    def unique_values(self):
        print(self.df.nunique())

    def full_report(self):
        self.dataInfo()
        self.summary_statistics()
        self.missing_values()
        self.duplicate_rows()
        self.unique_values()

#================================================
# using matplot lib, i will use more EDA methods like Graphs, heatmaps, corelation heatmap...
#================================================
