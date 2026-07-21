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
       

        
    def OpenFileJson(self):
        print("Opening file Exploer.")
        fileName = askopenfilename(
            title="Select a Json file:",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        return fileName


    def OpenFileCSV(self):
        print("Opening file Exploer.")
        fileName = askopenfilename(
            title="Select a dataset:",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
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
            option = int(input("\nWhat do you want to perform?\n1) EDA\n2) Clean Data\nEnter choice: "))
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

            print("""
==================== EDA MENU ====================

1. Basic Information
2. Descriptive Statistics
3. Missing Values
4. Duplicates & Unique Values
5. Full Report
6. Preprocessing
7. Numeric Correlation
8. Categorical Correlation
9. Detect Outliers
10. Exit EDA

==================================================
""")

            try:
                choice = int(input("Select an option: "))

                if choice == 1:
                    eda.dataInfo()

                elif choice == 2:
                    eda.summary_statistics()

                elif choice == 3:
                    eda.missing_values()

                elif choice == 4:
                    eda.duplicate_rows()
                    eda.unique_values()

                elif choice == 5:
                    eda.full_report()

                elif choice == 6:
                    self.Preprocessing(dataset)

                elif choice == 7:
                    print("\nNumeric Correlation\n")
                    eda.numeric_correlation()

                elif choice == 8:
                    eda.categorical_correlation()
                elif choice == 9:
                    eda.detect_outliers()

                elif choice == 10:
                    print("Exiting EDA...")
                    break

                else:
                    print("Please select a number between 1 and 9.")

            except ValueError:
                print("Invalid input. Please enter a number.")


    
    def Preprocessing(self, dataset):         
        clean_dataSet = CleanData(dataset)
        cleaned_DF = clean_dataSet.clean()
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
                
                elif option_to_perforn_next_action == 3: # train data here
                    json_file_path = self.OpenFileJson()
                    json_DF = pd.read_json(json_file_path)
    
                    target_column = input("\nEnter the name of the target column: ").strip()
                    drop_columns = [
                        "incident_id", "address", "latitude", "longitude", "incident_datetime", "officer_id", 
                        "officer_first_name", "officer_last_name", "badge_number", "suspect_id", "suspect_first_name", 
                        "suspect_last_name", "victim_id", "victim_first_name", "victim_last_name", "victim_phone", "notes"
                    ]

                    model_type_selected_classification = input("\nEnter the name of Classificaltion Model:\n1) decision_tree\n2) gradient_boosting\n3) random_forest\n4) catboost").strip()
                    
                    train_data = TrainModel(json_DF, target_column, columns_to_drop = drop_columns, model_type=model_type_selected_classification)
                    train_data.select_model_type()

                elif option_to_perforn_next_action == 4:
                    print("Exiting...")
                    break
                else:
                    print("Please choose 1 or 2 or 3")

            except ValueError:
                print("Please enter a correct input...")