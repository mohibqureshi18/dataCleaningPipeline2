import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from catboost import CatBoostClassifier

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
    def __init__(self, datasetReceived, target_column, columns_to_drop=None, model_type="random_forest"):
       self.df = datasetReceived
       self.target_column = target_column
       self.model_type = model_type

       self.columns_to_drop = columns_to_drop if columns_to_drop else []

       self.X=None
       self.y=None

       self.X_train =None
       self.X_test =None
       self.y_train =None
       self.y_test =None

       self.model = None

       self.scaler = StandardScaler()
       self.feature_encoders = {}
       self.target_encoder = None


    def select_model_type(self): # check: classification or regression

        # 1. Check if target column exists
        if self.target_column not in self.df.columns:
            raise ValueError(f"Target column '{self.target_column}' not found in dataset columns: {list(self.df.columns)}")

        # 2. Assign X and y FIRST before performing any checks on y
        self.columns_to_drop = list(set([self.target_column] + self.columns_to_drop))
        existing_drops = [col for col in self.columns_to_drop if col in self.df.columns]
        
        self.X = self.df.drop(columns=existing_drops)
        self.y = self.df[self.target_column]

        # 3. Clean target string anomalies for categorical text safely now that y exists
        if self.y.dtype == 'object' or str(self.y.dtype) == 'string':
            self.y = self.y.astype(str).str.lower().str.strip()

        # 4. Handle NaNs in target safely
        valid_idx = self.y.notna()
        self.X = self.X[valid_idx]
        self.y = self.y[valid_idx]

        self.X = self.X.dropna(axis=1, how='all')

        # 5. Impute missing values in feature matrix
        num_cols = self.X.select_dtypes(include=[np.number]).columns
        if len(num_cols) > 0:
            self.X[num_cols] = self.X[num_cols].fillna(self.X[num_cols].median())
        self.X = self.X.fillna("missing_category")

        # 6. Check: Classification vs Regression
        if self.y.dtype == 'object' or str(self.y.dtype) == 'string' or self.y.nunique() < 30:
            print("\nClassification Problem")
            self.process_categorical_dataset()
        else:
            print("\nRegression Problem")
            self.process_regression_dataset()


    # for categorical:
    def process_categorical_dataset(self):
        self.encode_data()
        self.split_data()
        self.scale_data()
        self.train_classification_data()
        self.evaluate_model()




    # for regression:
    def process_regression_dataset(self):
        self.encode_data()
        self.split_data()
        self.scale_data()
        self.train_regression_data()
        self.evaluate_regression_model()

    def train_regression_data(self):
        print("Training Linear Regression Model...")
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def evaluate_regression_model(self):
        prediction = self.model.predict(self.X_test)
        mae = mean_absolute_error(self.y_test, prediction)
        mse = mean_squared_error(self.y_test, prediction)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, prediction)

        print(f"\nEVALUATION RESULT")
        print(f"MAE : {mae:.4f}")
        print(f"MSE : {mse:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"R²  : {r2:.4f}\n")

    def encode_data(self):
        print("\nEncoding Dataset...")
            
        for column in self.X.columns:
            if(self.X[column].dtype == "object") or (self.X[column].dtype == "string"):
                
                # encoding
                encoder = LabelEncoder()
                self.X[column] = encoder.fit_transform(self.X[column].astype(str).str.lower().str.strip())

                self.feature_encoders[column] = encoder

        if self.y.dtype == 'object' or not np.issubdtype(self.y.dtype, np.number):
            self.target_encoder = LabelEncoder()
            self.y = self.target_encoder.fit_transform(self.y.astype(str))
        else:
            self.y = self.y.values

    def split_data(self):
        print("\nSplitting Dataset...")
        unique_classes, counts = np.unique(self.y, return_counts=True)
        stratify_target = self.y if (len(unique_classes) > 1 and np.min(counts) >= 2 and len(unique_classes) < 50) else None

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, 
            self.y,
            test_size=0.2,
            random_state=42,
            stratify=stratify_target
        )
    
    def scale_data(self):
        print("Scaling Feature Matrix...")
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)


    def train_classification_data(self):
        if(self.model_type == "decision_tree"):
            self.model = DecisionTreeClassifier(random_state=42)

        elif(self.model_type == "gradient_boosting"):
            self.model = GradientBoostingClassifier(
                n_estimators=100,
                learning_rate=0.1,
                random_state=42
            )

        elif(self.model_type == "random_forest"):
            self.model = RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )

        elif(self.model_type == "catboost"):
            self.model = CatBoostClassifier(
                n_estimators=300,
                learning_rate=0.1,
                depth=6,
                verbose=0,
                random_state=42
            )
        else:
            raise ValueError("Unsported Model Type")
        
        self.model.fit(self.X_train, self.y_train)
        print(f"\n{self.model_type} Model Trained")



    def evaluate_model(self):
        prediction = self.model.predict(self.X_test)

        accuracy = accuracy_score(self.y_test, prediction)
        print(f"\nAccuracy: {accuracy:.2%}")