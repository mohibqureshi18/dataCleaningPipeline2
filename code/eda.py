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
              
    def summary_statistics(self):
        print(f"\nsummary_statistics of Dataset:\n{self.df.describe()}\n")
    
    def missing_values(self):
        print(f"\nMissing values of each column:\n{self.df.isnull().sum()}\n")

    def duplicate_rows(self):
        print(f"\nDuplicate Rows:\t{self.df.duplicated().sum()}\n")

    def unique_values(self):
        print(f"\n{self.df.nunique()}\n")

    def full_report(self):
        self.dataInfo()
        self.summary_statistics()
        self.missing_values()
        self.duplicate_rows()
        self.unique_values()

#================================================
# using matplot lib, i will use more EDA methods like Graphs, heatmaps, corelation heatmap...
#================================================
