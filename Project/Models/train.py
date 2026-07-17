import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score


"""
Class functionality:
- Receive the cleaned DataFrame.
- Receive the target column.
- Detect whether the target is categorical or numeric.
- Preprocess the data.
- Split into train/test sets.
- Train a model.
- Evaluate it.

"""

class TrainModel:
    def __init__(self, datasetReceived, target_column):
       self.df = datasetReceived
       self.target_column = target_column

       self.X=None
       self.y=None

       self.X_train =None
       self.X_test =None
       self.y_train =None
       self.y_test =None

       self.model = None

    def select_model_type(self): #check: classification or regression
        self.X = self.df.drop(columns =[self.target_column])
        self.y = self.df[self.target_column]

        if(self.y.dtype == 'object'):
            print("\nClassification Problem")
            self.process_categorical_dataset()

        else:
            print("\nRegression Problem")
            self.process_regression_dataset()


    # for categorical:
    def process_categorical_dataset(self):
        self.encode_data()
        self.split_data()
        self.train_classification_data()
        self.evaluate_model()

    # for regression:
    def process_regression_dataset(self):
        pass


    def encode_data(self):
        print("\nEncoding Dataset...")
        self.feature_encoders = {}

        
        for column in self.X.columns:
            if(self.X[column].dtype == "object"):
                
                # encoding
                encoder = LabelEncoder()
                self.X[column] = encoder.fit_transform(self.X[column].astype(str))

                #=======================================================

                self.feature_encoders[column] = encoder

                # safe playing here as """ encoder = LabelEncoder() """ runs new for each loop, causing it to forget the rules 
                # defined for previous columns. 
                # And at the end, only the rules for """ y """ will be remembered. 

                # So use dictionary out side of the loop to store all rules.

                #=======================================================

        self.target_encoder = LabelEncoder()
        self.y = self.target_encoder.fit_transform(self.y)

    def split_data(self):
        print("\nSplitting Dataset...")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, 
            self.y,
            test_size =0.2,
            random_state =42
        )

    def train_classification_data(self):

        self.model = DecisionTreeClassifier(random_state=42)
        self.model.fit(self.X_train, self.y_train)
        print("\nModel Trained")
    

        # model_to_train = int(input("\nSelect a model to train:\n1)Decision Tree\n====== No other model availible yet ======"))

        # if(model_to_train == 1):
            # self.model = DecisionTreeClassifier(random_state=42)
            # self.model.fit(self.X_train, self.y_train)
            # print("\nModel Trained")
        # else:
        #     pass


    def evaluate_model(self):
        prediction = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, prediction)

        print(f"\nAccuracy: {accuracy:.2%}")