import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency



class EDA:

    def __init__(self, df):
        self.df = df
        self.numeric_features = self.df.select_dtypes(include = ['int64', 'float64']).columns
        # self.categorical_features = self.df.select_dtypes(include = ['object', 'category']).columns        
        self.categorical_features = self.df.select_dtypes(
            exclude = ['int64', 'float64']
        ).columns

    def dataInfo(self):
        print()
        print("BASIC INFORMATION:")
        self.df.info()
        print(f"\nShape of dataset:\t{self.df.shape}") 
        print(f"\nColumns of Dataset:\t{list(self.df.columns)}")
        print(f"\nDataTypes of Dataset:\t{self.df.dtypes}")

        print("\nFEATURES DETAILS:")
        print("\nNumeric:", self.numeric_features)
        print("\nCategorical:", self.categorical_features)


              
    def summary_statistics(self):
        print(f"\nsummary_statistics of Dataset:\n")
        print(self.df.describe(include="all"))

        missing_summary = pd.DataFrame({
                "Missing Values": self.df.isnull().sum(),
                "Percentage": (self.df.isnull().sum() / len(self.df)) * 100
            })

        missing_summary = missing_summary.sort_values(
            by="Missing Values",
            ascending=False
        )
        
        print(missing_summary)

    
    def missing_values(self):
        print(f"\nMissing values of each column:\n{self.df.isnull().sum()}\n")

    def duplicate_rows(self):
        print(f"\nDuplicate Rows:\t{self.df.duplicated().sum()}\n")

    def unique_values(self):
        print(f"\n{self.df.nunique()}\n")

    def detect_outliers(self):
        for col in self.numeric_features:

            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)

            IQR = Q3-Q1 

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers = self.df[
                (self.df[col] < lower) | (self.df[col] > upper)
            ]
            
            print(f"{col}")
            print(f"Lower Bound: {lower:.2f}")
            print(f"Upper Bound: {upper:.2f}")
            print(f"Outliers: {len(outliers)}")



    def  numeric_correlation(self):
        corr_matrix = self.df[self.numeric_features].corr()

        plt.figure(figsize=(10,6))

        sns.heatmap(
            corr_matrix, annot=True, cmap="coolwarm"
        )
        plt.show()


    def categorical_correlation(self, max_unique=20):
        print("\nCATEGORICAL CORRELATION")
        selected_features = [col for col in self.categorical_features if self.df[col].nunique(dropna=True) <= max_unique]
        
        results = []
        for i, feature1 in enumerate(selected_features):
            for feature2 in selected_features[i + 1:]:
                table = pd.crosstab(self.df[feature1], self.df[feature2])
                if table.shape[0] < 2 or table.shape[1] < 2:
                    continue
                chi2, p, dof, expected = chi2_contingency(table)
                results.append({"Feature1": feature1, "Feature2": feature2, "P-value": round(p, 6)})
                
        if not results:
            print("No valid categorical relationships found.")
            return None
            
        results_df = pd.DataFrame(results).sort_values("P-value").reset_index(drop=True)
        print(results_df)
        return results_df

    def value_counts(self):
        for col in self.categorical_features:

            print(f"\n{self.df[col].value_counts()}")


    def full_report(self):

        print("\nEXPLORATORY DATA ANALYSIS REPORT\n")
        self.dataInfo()

        self.summary_statistics()
        self.missing_values()
        self.duplicate_rows()
        self.unique_values()
        self.detect_outliers()
        self.numeric_correlation()
        self.categorical_correlation()