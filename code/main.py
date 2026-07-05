from loadData import LoadData
from cleanData import CleanData
from eda import EDA


import pandas as pd
import numpy as np


if __name__ == "__main__":
    FILE_PATH = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\messyCrimeDastaset\\crime_incidents_messy.csv"

    try:
        #load data
        loader = LoadData(FILE_PATH)
        df = loader.loadData()
        print(df.head(10))

        # Analyze
        analyzer = EDA()
        analyzer.dataInfo()

    except FileNotFoundError as e:
        print("File not found")