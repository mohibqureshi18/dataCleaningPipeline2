import pandas as pd 
import numpy as np
from eda import EDA
from clean_data import CleanData
from exportToJson import Export

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
        df = pd.read_csv(dataset)


        try:
            option = int(input("\nwhat do you want to perform?\nPress 1 for EDA\nPress 2 for clean data"))
            if(option == 1):
                self.run_EDA(df)
            elif(option == 2): 
                self.Preprocessing(df)
            else:
                print("\nSelect correct option")
        except ValueError:
            print("Please enter a Number")
            return


    def run_EDA(self, dataset): 
        eda = EDA(dataset)
        while True:

            try:

                checkDataInfo = int(input("\n\nselect 1 option:\n1: Basic Information.\n2: Descriptive Stats.\n3: Missing Values.\n4: Duplicates and Unique Values.\n5: Full Report.\n7: Exit"))
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
                elif checkDataInfo == 6:
                    self.Preprocessing(df)
                
                elif(checkDataInfo == 7):
                    break

                else:
                    print("Invalid option.")
            
            except ValueError:
                print("Please enter a valid number (1-6).")


    
    def Preprocessing(self, dataset):         
        clean_dataSet = CleanData(dataset)
        
        cleaned_DF = clean_dataSet.Do_clean()
        while True:
            try:
                option_to_perforn_next_action = int(input("What do you want to do next: 1) Analyze data 2) export dataset in json 3) Exit"))
                if option_to_perforn_next_action == 1:
                    self.run_EDA(cleaned_DF)
                elif option_to_perforn_next_action == 2:
                    # expJson = Export(cleaned_DF)
                    # expJson.ExportToJson()
                    expJson = Export()
                    expJson.ExportToJson(cleaned_DF)
                elif option_to_perforn_next_action == 3:
                    print("Exiting...")
                    break
                else:
                    print("Please choose 1 or 2 or 3")

            except ValueError:
                print("Please enter a correct input...")
         
