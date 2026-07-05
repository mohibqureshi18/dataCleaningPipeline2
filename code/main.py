from loadData import LoadData
from cleanData import CleanData
from eda import EDA


import pandas as pd
import numpy as np


if __name__ == "__main__":
    FILE_PATH = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\messyCrimeDastaset\\crime_incidents_messy.csv"


    #load data
    loader = LoadData(FILE_PATH)
    df = loader.loadData()
    print(df.head(10))

    # Analyze before clean
    analyzer = EDA(df)
    analyzer.dataInfo()


    # cleaner
    cleaner = CleanData(df)
    cleaner.removeDuplicates(), cleaner.handleMissingValues(), cleaner.fixDataTypes(), cleaner.fixTypos(), cleaner.cleanReportedOnline(), cleaner.removeInvalidValues(), cleaner.standardizeText()
    cleaned_df = cleaner.getData()

    # Analyze
    analyzer = EDA(cleaned_df)
    analyzer.dataInfo()