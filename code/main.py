from loadData import LoadData
# from cleanData import CleanData
from clean_data import CleanData
# from eda import EDA

import os # for exporting data in json format.


import pandas as pd
import numpy as np


if __name__ == "__main__":
    CrimeDastaset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\messyCrimeDastaset\\crime_incidents_messy.csv"
    FraudDataset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\FraudDataset\\creditcard.csv"

    try:
        print("loading file...")

        Selected_dataset = int(input("Select a dataset for research:\n1 for CrimeDastaset\n2 for FraudDataset\t"))

        if(Selected_dataset == 1):
            loader = LoadData(CrimeDastaset)
            df = loader.loadData()
            print(df.head(4))
        elif(Selected_dataset == 2):
            loader = LoadData(FraudDataset)
            df = loader.loadData()
            print(df.head(4))
        else:
            print("\nPlease select 1 or 2")
    
    except FileNotFoundError as e:
        print("file not found")