import pandas as pd
import numpy as np


# Class functionality :
#     Remove Duplicates Rows 
#     Remove Empty rows or cols
#     empty strings with NaN 
#     Strip spaces
#     Standardize text
#     Convert numeric strings
#     Missing values
#     Reset index


class CleanData:
    def __init__(self, df):
        self.df = df
        
    def remove_duplicates_rows(self):
        self.df = self.df.drop_duplicates()
        print(f"\nDuplicate Rows: {self.df.duplicated().sum()}")
        return self

    def remove_duplicates_cols(self):
        self.df = self.df.loc[:, ~self.df.columns.duplicated()]
        print(f"\nDuplicate Cols: {self.df.duplicated().sum()}")
        return self

    def remove_empty(self):
        self.df = self.df.dropna(how="all")
        # self.df = self.df.dropna(axis = 1, how="all")
        return self
    
    def replace_empty_strings(self):
        self.df.replace(
            r'^\s*$',
            np.nan,
            regex = True,
            inplace=True
        )
        return self
    
    def stip_spaces(self):
        stripSpaces = self.df.select_dtypes(
            include = ["object", "string"]
        ).columns
        for col in stripSpaces:
            self.df[col] = self.df[col].str.strip()
        
        return self
    

    def standardize_text(self, case = "lower"):
        case_of_text = self.df.select_dtypes(
            include=["object", "string"]
        ).columns

        for col in case_of_text:
            if case == "lower":
                self.df[col] = self.df[col].str.lower()
            
            elif case == "upper":
                self.df[col] = self.df[col].str.upper()
        
        return self
    
    def numeric_convert(self):
        for col in self.df.columns:
            self.df[col] = pd.to_numeric(
                self.df[col], errors="ignore"
            )

        return self

    
    def handle_missing_values(self):
        self.df.dropna(inplace = True)
        return self

    # def handle_missing_values(self, strategy="median"):
    #     numeric = self.df.select_dtypes(
    #         include = np.number
    #     ).columns

    #     categorical = self.df.select_dtypes(
    #         exclude = np.number
    #     ).columns

    #     if strategy == "drop":
            
    #         self.df = self.df.dropna()


    #     elif strategy == "mean":
    #         self.df[numeric] =self.df[numeric].fillna(
    #             self.df[numeric].mean()
    #         )
    #         for col in categorical:
    #             mode = self.df[col].mode()
                
    #             if not mode.empty:
    #                 self.df[col] = self.df[col].fillna(mode.iloc[0])



    #     elif strategy == "median":
            
    #         self.df[numeric] = self.df[numeric].fillna(
    #             self.df[numeric].median()
    #         )
            
    #         for col in categorical:
    #             mode = self.df[col].mode()

    #             if not mode.empty:
    #                 self.df[col] = self.df[col].fillna(mode.iloc[0])



    #     elif strategy == "mode":
            
    #         for col in self.df.columns:
    #             mode = self.df[col].mode()

    #             if not mode.empty:
    #                 self.df[col] = self.df[col].fillna(mode.iloc[0])


    #     else:
    #         print(f"\nstrategy must be 'drop', 'mean', 'median', 'mode'")

    #     return self
    
    
    def handle_outliers(self):
        print("\nHandling outliers")
        
        removed_in_pass = -1
        pass_count = 1
        
        while removed_in_pass != 0:
            before_total = len(self.df)
            print(f"\n--- Outlier Pass {pass_count} ---")
            
            for col in self.df.select_dtypes(include="number").columns:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1

                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR

                before_col = len(self.df)
                self.df = self.df[
                    (self.df[col] >= lower) & (self.df[col] <= upper)
                ]
                removed = before_col - len(self.df)
                if removed > 0:
                    print(f"{col}: Removed {removed} outlier(s)")

            removed_in_pass = before_total - len(self.df)
            pass_count += 1
            
        print("\nAll outliers successfully handled across passes.")
        return self
    
    def index_reset(self):
        self.df = self.df.reset_index(drop =True)
        return self
    

# Final cleaning pipeline


    def clean(self):
        print("\nCleaning Dataset...")

        self.remove_duplicates_rows() .remove_duplicates_cols() .remove_empty() .replace_empty_strings() .handle_outliers()
        self.stip_spaces() .standardize_text(case="lower") .numeric_convert() .handle_missing_values() .index_reset()

        print("\nCleaning Completed")
        
        return self.df