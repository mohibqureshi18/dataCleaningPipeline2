import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
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
    def __init__(self, datasetReceived, target_column, columns_to_drop=None):
       self.df = datasetReceived
       self.target_column = target_column

       self.columns_to_drop = columns_to_drop if columns_to_drop else []

       self.X=None
       self.y=None

       self.X_train =None
       self.X_test =None
       self.y_train =None
       self.y_test =None

       self.model = None

    def select_model_type(self): # check: classification or regression

        # columns_to_drop = [
        #     self.target_column, 'incident_id', 'address', 'latitude', 'longitude', 
        #     'incident_datetime', 'officer_id', 'officer_first_name', 'officer_last_name', 
        #     'badge_number', 'suspect_id', 'suspect_first_name', 'suspect_last_name', 
        #     'victim_id', 'victim_first_name', 'victim_last_name', 'victim_phone', 'notes'
        # ]
        self.columns_to_drop = [self.target_column] + self.columns_to_drop
        
        existing_drops = [col for col in self.columns_to_drop if col in self.df.columns]
        
        self.X = self.df.drop(columns=existing_drops)
        self.y = self.df[self.target_column]

        if self.y.dtype == 'object':
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
        self.split_data()
        self.train_regression_data()
        self.evaluate_regression_model()





    def train_regression_data(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        print("\nModel trained")

    def evaluate_regression_model(self):
        prediction = self.model.predict(self.X_test)

        mae = mean_absolute_error(self.y_test, prediction)
        mse = mean_squared_error(self.y_test, prediction)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, prediction)

        print(f"\nMAE : {mae:.4f}")
        print(f"MSE : {mse:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"R²  : {r2:.4f}")



    def encode_data(self):
        print("\nEncoding Dataset...")
        self.feature_encoders = {}

        
        for column in self.X.columns:
            if(self.X[column].dtype == "object"):
                
                # encoding
                encoder = LabelEncoder()
                self.X[column] = encoder.fit_transform(self.X[column].astype(str))

                self.feature_encoders[column] = encoder

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

    def evaluate_model(self):
        prediction = self.model.predict(self.X_test)

        accuracy = accuracy_score(self.y_test, prediction)
        print(f"\nAccuracy: {accuracy:.2%}")