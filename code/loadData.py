import pandas as pd 
import numpy as np
from eda import EDA


class LoadData:


    def __init__(self):
        self.CrimeDastaset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\crime_incidents_messy.csv"
        self.Mushrooms = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\Mushrooms.csv"

        

    def loadData(self):

        Selected_dataset = int(input("\nSelect a dataset for research:\n1 for CrimeDastaset\n2 for Mushrooms\t"))

        if(Selected_dataset == 1):
            self.selectOptionForDataset(self.CrimeDastaset)

        elif(Selected_dataset == 2):
            self.selectOptionForDataset(self.Mushrooms)

        else:
            print("\nPlease select 1 or 2")

    def selectOptionForDataset(self,  dataset):
        print("\nloading file...")

        option = int(input("\nwhat do you want to perform?\nPress 1 for EDA\nPress 2 for clean data"))
        if(option == 1):
            self.run_EDA(dataset)
        elif(option == 2): 
            self.Preprocessing(dataset)
        else:
            print("\nSelect correct option")


    def run_EDA(self, dataset):
        df = pd.read_csv(dataset)
        eda = EDA(df)
        while True:

            try:

                checkDataInfo = int(input("\n\nselect 1 option:\n1: Basic Information.\n2: Descriptive Stats.\n3: Missing Values.\n4: Duplicates and Unique Values.\n5: Full Report.\n6: Exit"))
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
                
                elif(checkDataInfo == 6):
                    break

                else:
                    print("Invalid option.")
            
            except ValueError:
                print("Please enter a valid number (1-6).")


    
    def Preprocessing(self, dataset):
         df = pd.read_csv(dataset)
         