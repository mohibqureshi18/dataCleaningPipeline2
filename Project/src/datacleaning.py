import pandas as pd
import pandas as pd
import numpy as np

class CleanAllData:
    def __init__(self, df):
        self.df = df

    # Check for remaining missing values
    def remove_empty(self):
        self.df = self.df.dropna()
        self.df.isnull().sum()
        self.text_columns = self.df.select_dtypes(include = "object").columns

        return self

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

    def remove_duplicates_rows(self):
    
        duplicate_rows = self.df.duplicated().sum()

        print("Number of duplicate rows:", duplicate_rows)

        self.df[self.df.duplicated().T]
        print("New Shape:", self.df.shape)

        # Remove exact duplicate rows
        self.df = self.df.drop_duplicates()

        print("New Shape:", self.df.shape)

        # Count duplicate incident IDs
        duplicate_ids = self.df["incident_id"].duplicated().sum()

        print("Duplicate Incident IDs:", duplicate_ids)

        self.df = self.df.drop_duplicates(subset="incident_id", keep="first")

        print("Duplicate Rows:", self.df.duplicated().sum())
        print("Duplicate Incident IDs:", self.df["incident_id"].duplicated().sum())

        return self

    
    def strip_spaces(self):
        # Remove leading and trailing spaces from all text columns
        for col in self.text_columns:
            self.df[col] = self.df[col].str.strip()

        self.df.head()
        return self


    def standardize_text(self):
        categorical_columns = [
            "crime_type",
            "district",
            "city",
            "state",
            "suspect_gender",
            "victim_gender",
            "suspect_race",
            "weapon_used",
            "severity",
            "case_status",
            "resolution"
        ]

        for col in categorical_columns:
            self.df[col] = self.df[col].str.title()

        for col in categorical_columns:
            print(f"\n{col}")
            print(self.df)

        for col in self.text_columns:
            self.df[col] = self.df[col].str.replace(r"\s+", " ", regex=True)

        gender_map = {
            "M": "Male",
            "Male": "Male",
            "MALE": "Male",
            "F": "Female",
            "Female": "Female",
            "FEMALE": "Female",
            "U": "Unknown",
            "Unknown": "Unknown"
        }

        reported_online_map = {
            "YES": True,
            "Yes": True,
            "yes": True,
            "Y": True,
            "y": True,
            "True": True,
            "TRUE": True,
            "true": True,
            "1": True,
            "NO": False,
            "No": False,
            "no": False,
            "N": False,
            "n": False,
            "False": False,
            "FALSE": False,
            "false": False,
            "0": False
        }

        severity_map = {
            "LOW": "Low",
            "Low": "Low",
            "low": "Low",
            "MEDIUM": "Medium",
            "Medium": "Medium",
            "medium": "Medium",
            "Med": "Medium",
            "HIGH": "High",
            "High": "High",
            "high": "High",
            "Crit": "Critical",
            "Critical": "Critical",
            "1": "Low",
            "2": "Medium",
            "3": "High",
            "4": "Critical"
        }


        crime_type_map = {
            "Homocide": "Homicide",
            "B&E": "Burglary",
            "Trespass": "Trespass",
            "Cyber Crime": "Cyber Crime",
            "Trespassing": "Trespass",
            "Homicide": "Homicide",
            "Hacking": "Cyber Crime",
            "Drug Offence": "Drug Offense",
            "Cybercrime": "Cyber Crime",
            "Burglary": "Burglary",
            "Vandalism": "Vandalism",
            "Sexual Assualt": "Sexual Assault",
            "Drug Offense": "Drug Offense",
            "Deception": "Fraud",
            "Domestc Violence": "Domestic Violence",
            "Armed Robbery": "Armed Robbery",
            "Dwi": "DUI",
            "Assault": "Assault",
            "Manslaughter": "Manslaughter",
            "Drugs": "Drug Offense",
            "Fraud": "Fraud",
            "Tresspassing": "Trespass",
            "Assault & Battery": "Assault & Battery",
            "Larceny": "Theft",
            "Theft/Larceny": "Theft",
            "Dv": "Domestic Violence",
            "Murder": "Homicide",
            "Narcotics": "Drug Offense",
            "Fire Setting": "Arson",
            "Theft": "Theft",
            "Sexual Assault": "Sexual Assault",
            "Dui": "DUI",
            "Abduction": "Kidnapping",
            "D.U.I.": "DUI",
            "Domestic Violence": "Domestic Violence",
            "Stealing": "Theft",
            "Kidnaping": "Kidnapping",
            "Fraudulent Activity": "Fraud",
            "Kidnapping": "Kidnapping",
            "Robbery": "Robbery",
            "Arson": "Arson",
            "Arsen": "Arson",
            "Duii": "DUI",
            "Property Damage": "Vandalism",
            "Roberry": "Robbery",
            "Asslt": "Assault",
            "Sex Assault": "Sexual Assault",
            "Drunk Driving": "DUI",
            "Vandlism": "Vandalism",
            "Robbry": "Robbery",
            "Burglry": "Burglary",
            "Dom. Violence": "Domestic Violence",
            "Graffiti": "Vandalism",
            "Online Fraud": "Fraud",
            "Scam": "Fraud",
            "Battery": "Battery",
            "Sa": "Sexual Assault",
            "Drug Offence": "Drug Offense",
            "Armed Robbery": "Armed Robbery"
        }


        self.df["suspect_gender"] = self.df["suspect_gender"].replace(gender_map)
        self.df["reported_online"] = self.df["reported_online"].replace(reported_online_map).astype(bool)
        self.df["victim_gender"] = self.df["victim_gender"].replace(gender_map)
        self.df["severity"] = self.df["severity"].replace(severity_map)
        self.df["crime_type"] = self.df["crime_type"].replace(crime_type_map)

        print(self.df["suspect_gender"].unique())
        print(self.df["victim_gender"].unique())
        print(self.df["reported_online"].unique())
        print(self.df["severity"].unique())
        print(self.df["crime_type"].unique())

        # self.df["crime_type"] = self.df["crime_type"].str.title()
        print(self.df)
        return self
    
        


    def correct_invalid_values(self):
        invalid_suspect_age = self.df[
            (self.df["suspect_age"] < 0) |
            (self.df["suspect_age"] > 120)
        ]

        invalid_victim_age = self.df[
            (self.df["victim_age"] < 0) |
            (self.df["victim_age"] > 120)
        ]

        print(invalid_suspect_age)
        print(invalid_victim_age)

        self.df = self.df[
            (self.df["suspect_age"].between(0, 120)) &
            (self.df["victim_age"].between(0, 120))
        ]

        invalid_coordinates = self.df[
            (~self.df["latitude"].between(-90, 90)) |
            (~self.df["longitude"].between(-180, 180))
        ]

        print(invalid_coordinates)

        self.df = self.df[
            self.df["latitude"].between(-90, 90) &
            self.df["longitude"].between(-180, 180)
        ]

        print(self.df["property_loss_usd"].dtype)

        self.df["property_loss_usd"].unique()[:20]

        self.df["property_loss_usd"] = (
            self.df["property_loss_usd"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )

        self.df["property_loss_usd"] = pd.to_numeric(
            self.df["property_loss_usd"],
            errors="coerce"
        )

        print(self.df["property_loss_usd"].dtype)

        print(self.df["property_loss_usd"].isnull().sum())

        self.df = self.df.dropna()

        print(self.df["property_loss_usd"].isnull().sum())

        self.df[self.df["property_loss_usd"] < 0]

        self.df = self.df[self.df["property_loss_usd"] >= 0]

        self.df[self.df["num_arrests"] < 0]

        self.df = self.df[self.df["num_arrests"] >= 0]
        
        self.df["victim_phone"] = (
            self.df["victim_phone"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
        )

        self.df = self.df[self.df["victim_phone"].str.len() == 10]

        self.df["victim_phone"].head()
    
        print(self.df["suspect_age"].between(0, 120).all())
        print(self.df["victim_age"].between(0, 120).all())

        print(self.df["latitude"].between(-90, 90).all())
        print(self.df["longitude"].between(-180, 180).all())

        print((self.df["property_loss_usd"] >= 0).all())
        print((self.df["num_arrests"] >= 0).all())

        return self


    def date_time_correct(self):

        self.df["incident_datetime"] = pd.to_datetime(
            self.df["incident_datetime"],
            errors="coerce"
        )
        self.df = self.df.dropna(subset=["incident_datetime"])
        (self.df["incident_datetime"].dtype)

        return self
    

    # self.df["reported_online"].unique()

    def type_conversion(self):

        print(self.df.dtypes)

        numeric_columns = [
            "suspect_age",
            "victim_age",
            "latitude",
            "longitude",
            "num_arrests",
            "property_loss_usd"
        ]

        for col in numeric_columns:
            self.df[col] = pd.to_numeric(self.df[col], errors="coerce")

        self.df["suspect_age"] = self.df["suspect_age"].astype(int)
        self.df["victim_age"] = self.df["victim_age"].astype(int)
        self.df["num_arrests"] = self.df["num_arrests"].astype(int)

        self.df.dropna(subset=["incident_datetime"], inplace=True)
        self.df.dropna(subset=["reported_online"], inplace=True)
        self.df.dropna(subset=["suspect_gender"], inplace=True)
        self.df.dropna(subset=["victim_gender"], inplace=True)
        self.df.dropna(subset=["severity"], inplace=True)
        self.df.dropna(subset=["crime_type"], inplace=True)

        self.df["reported_online"].value_counts()

        print(self.df.dtypes)

        return self

    def quality_check(self):
            
        print("Total Missing Values:", self.df.isnull().sum().sum())

        print("Duplicate Rows:", self.df.duplicated().sum())

        print("Suspect Age Valid:", self.df["suspect_age"].between(0, 120).all())
        print("Victim Age Valid:", self.df["victim_age"].between(0, 120).all())
        print("Latitude Valid:", self.df["latitude"].between(-90, 90).all())
        print("Longitude Valid:", self.df["longitude"].between(-180, 180).all())
        print("Property Loss Valid:", (self.df["property_loss_usd"] >= 0).all())
        print("Arrests Valid:", (self.df["num_arrests"] >= 0).all())

        self.df.info()

        return self

    def clean(self):
        print("\nCleaning Dataset...")

        self.remove_empty() .handle_outliers() .remove_duplicates_rows() .strip_spaces()
        self.standardize_text() .correct_invalid_values() .date_time_correct() .type_conversion()
        self.quality_check()
        print("\nCleaning Completed")
           
        return self.df
