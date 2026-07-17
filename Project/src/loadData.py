import pandas as pd 
import numpy as np

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from Project.src.eda import EDA
from Project.src.clean_data import CleanData
from Project.src.exportToJson import Export
from Project.Models.train import TrainModel

class LoadData:


    def __init__(self):
        pass
        # try to make user Upload Dataset here
        # self.OpenFile()
        # self.CrimeDastaset = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\crime_incidents_messy.csv"
        # self.Mushrooms = r"C:\\Users\\mohib\\Desktop\\Mohib\\data-cleaning-pipeline\\Datasets\\mushrooms.csv"

        
    def OpenFileJson(self):
        print("Opening file Exploer.")
        fileName = askopenfilename(
            title="Select a Json file:",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        # df = pd.read_csv(fileName)
        return fileName


    def OpenFileCSV(self):
        print("Opening file Exploer.")
        fileName = askopenfilename(
            title="Select a dataset:",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        # df = pd.read_csv(fileName)
        return fileName

    def loadData(self):
        DataFile=self.OpenFileCSV()
        df = pd.read_csv(DataFile)

        self.selectOptionForDataset(df)

    # def loadData(self):

    #     Selected_dataset = int(input("\nSelect a dataset for research:"))

    #     if(Selected_dataset == 1):
    #         self.selectOptionForDataset(self.CrimeDastaset)

    #     elif(Selected_dataset == 2):
    #         self.selectOptionForDataset(self.Mushrooms)

    #     else:
    #         print("\nPlease select 1 or 2")


    

    def selectOptionForDataset(self,  df):
        print("\nloading file...")

        try:
            option = int(input("\nwhat do you want to perform?\nPress 1 for EDA\nPress 2 for clean data\t"))
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

                checkDataInfo = int(input("\n\nselect 1 option:\n1: Basic Information.\n2: Descriptive Stats.\n3: Missing Values." \
                "\n4: Duplicates and Unique Values.\n5: Full Report.\n6: Preprocessing\n7: Exit\t"))
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
                    self.Preprocessing(dataset)
                
                elif(checkDataInfo == 7):
                    break

                else:
                    print("Invalid option.")
            
            except ValueError:
                print("Please enter a valid number (1-7).")


    
    def Preprocessing(self, dataset):         
        clean_dataSet = CleanData(dataset)
        cleaned_DF = clean_dataSet.Do_clean()
        while True:
            try:
                option_to_perforn_next_action = int(input("What do you want to do next: \n1) Analyze data \n2) export dataset \n3) Train \n4) Exit\t"))
                if option_to_perforn_next_action == 1:
                    self.run_EDA(cleaned_DF)

                elif option_to_perforn_next_action == 2:
                    expJson = Export(cleaned_DF)

                    option_saveto = int(input("\nSave to 1) CSV\n2) json"))

                    if option_saveto == 1:
                        expJson.ExportToCSV()

                    elif option_saveto == 2:
                        expJson.ExportToJson()
                    else:
                        print("Please choose 1 or 2")
                
                elif option_to_perforn_next_action == 3: #train data here
                    # user input for Cleaned dataset
                    self.OpenFileJson()

                elif option_to_perforn_next_action == 4:
                    print("Exiting...")
                    break
                else:
                    print("Please choose 1 or 2 or 3")

            except ValueError:
                print("Please enter a correct input...")