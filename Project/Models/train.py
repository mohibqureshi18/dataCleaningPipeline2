import numpy as np
import pandas as pd

# training inports here

class TrainModel:
    def __init__(self, datasetReceived, target_column):
        self.df = datasetReceived
        self.target_column = target_column

        


    def select_model_type(self): #check: classification or regression
        pass


    # for regression:
    def process_regression_dataset(self):
        pass


    # for categorical:
    def process_categorical_dataset(self):
        pass

    def train_model(self):
        self.X = self.df.drop(columns=[self.target_column])
        self.Y = self.df[self.target_column]
