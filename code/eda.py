import numpy as np
import pandas as pd

class EDA:

    def __init__(self, df):
        self.df = df

    def dataInfo(self):
        print("Data Info")
        self.df.info()

        print("\nDescriptive Statistics")
        print(self.df.describe())

        print("\nFirst 5 Rows")
        print(self.df.head())

        print("\nMissing Values")
        print(self.df.isnull().sum())