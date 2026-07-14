import pandas as pd
import numpy as np

class CleanData:

    def __init__(self, df):
        self.df = df
    
    def remove_duplicated(self):
        print("Removing Duplicates...\n")
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    def missing_values(self):
        print("Removing rows with missing values...\n")
        self.df = self.df.dropna()
        return self.df

    # final method that calls all
    def Do_clean(self):
        # call the function
        print("Cleaning the dataset...\n")
        self.remove_duplicated()
        self.missing_values()

        

        return self.df