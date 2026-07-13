import pandas as pd
import numpy as np
class Export:
    def __init__(self, Cleaned_Dataset):
        self.Cleaned_Dataset = Cleaned_Dataset    


    def ExportToJson(self):
        self.Cleaned_Dataset.to_json("cleaned_dataset.json", orient="records")
        print("\n\tdata Exported successfully")