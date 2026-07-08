from loadData import LoadData
# from clean_data import CleanData
from eda import EDA

import pandas as pd
import numpy as np


if __name__ == "__main__":
    CrimeDastaset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\crime_incidents_messy.csv"
    FraudDataset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\creditcard.csv"

    def run_pipeline(dataframe):
        loader = LoadData(dataframe)
        df = loader.loadData()
        eda = EDA(df)

        checkDataInfo = int(input("select 1 option:\n1: Basic Information.\n2: Descriptive Stats.\n3: Missing Values.\n4: Duplicates and Unique Values.\n5: Full Report."))
        if checkDataInfo == 1:
            eda.dataInfo()

        elif checkDataInfo == 2:
            eda.summary_statistics()

        elif checkDataInfo == 3:
            eda.missing_values()

        elif checkDataInfo == 4:
            eda.duplicate_rows()
            eda.unique_values()

        elif checkDataInfo == 5:
            eda.full_report()

        else:
            print("Invalid option.")
            
        # print(df.head(4))
    

    try:
        print("loading file...")

        Selected_dataset = int(input("Select a dataset for research:\n1 for CrimeDastaset\n2 for FraudDataset\t"))

        if(Selected_dataset == 1):
            run_pipeline(CrimeDastaset)

        elif(Selected_dataset == 2):
            run_pipeline(FraudDataset)

        else:
            print("\nPlease select 1 or 2")
    except FileNotFoundError as e:
        print("file not found")