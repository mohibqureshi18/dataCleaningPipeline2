import pandas as pd
import numpy as np
class Export:
    def __init__(self, Cleaned_Dataset):
        self.Cleaned_Dataset = Cleaned_Dataset    

    def ExportToCSV(self):
        self.Cleaned_Dataset.to_csv(r"C:\\Users\\mohib\Desktop\\Mohib\\data-cleaning-pipeline\\Project\\processed\\cleaned_dataset.csv")
        print("\n\tdata Exported successfully")

    def ExportToJson(self):
        self.Cleaned_Dataset.to_json(r"C:\\Users\\mohib\Desktop\\Mohib\\data-cleaning-pipeline\\Project\\Exported_Dataset_json\\cleaned_dataset.json", orient="records", indent=4)
        print("\n\tdata Exported successfully")