import pandas as pd
import pandas as pd
import numpy as np


class CleanData:

    def __init__(self, df):
        self.df = df

        self.gender_map = {
            "M": "Male",
            "Male": "Male",
            "MALE": "Male",
            "F": "Female",
            "Female": "Female",
            "FEMALE": "Female",
            "U": "Unknown",
            "Unknown": "Unknown"
        }

        self.reported_online_map = {
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
        self.case_status_map = {
            "closed": "Closed",
            "Closed": "Closed",
            "CLOSED": "Closed",
            "open": "Open",
            "Open": "Open",
            "OPEN": "Open",
            "Under Investigation": "Under Investigation",
            "under investigation": "Under Investigation",
            "Investgation": "Under Investigation",
            "Pending": "Pending",
            "Pendng": "Pending"
}

        self.severity_map = {
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

        self.crime_type_map = {
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

        self.categorical_columns = [
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

        self.numeric_columns = [
            "suspect_age",
            "victim_age",
            "latitude",
            "longitude",
            "num_arrests",
            "property_loss_usd"
        ]


    def explore_data(self):
        df = self.df
        print("SHAPE:")
        print(" ")
        print(df.shape)
        print("INFO:")
        print(" ")
        print(df.info())
        print("HEAD:")
        print(" ")
        print(df.head())
        print("DESCRIBE:")
        print(" ")
        print(df.describe(include="all"))
        print(" ")
        print("DATA_TYPES:")
        print(df.dtypes)

    def handle_missing_values(self):
        df = self.df

        missing_summary = pd.DataFrame({
            "Missing Values": df.isnull().sum(),
            "Percentage": (df.isnull().sum() / len(df)) * 100
        })

        missing_summary = missing_summary.sort_values(
            by="Missing Values",
            ascending=False
        )

        print(missing_summary)

        df = df.dropna()

        # Check for remaining missing values
        df.isnull().sum()

        self.df = df

    def remove_duplicates(self):
        df = self.df

        duplicate_rows = df.duplicated().sum()

        print("Number of duplicate rows:", duplicate_rows)

        df[df.duplicated().T]
        print("New Shape:", df.shape)

        # Remove exact duplicate rows
        df = df.drop_duplicates()

        print("New Shape:", df.shape)

        # Count duplicate incident IDs
        duplicate_ids = df["incident_id"].duplicated().sum()

        print("Duplicate Incident IDs:", duplicate_ids)

        df = df.drop_duplicates(subset="incident_id", keep="first")

        print("Duplicate Rows:", df.duplicated().sum())
        print("Duplicate Incident IDs:", df["incident_id"].duplicated().sum())

        self.df = df

    def clean_text_columns(self):
        df = self.df

        text_columns = df.select_dtypes(include="object").columns

        for col in text_columns:
            df[col] = df[col].str.strip()

        df.head()

        categorical_columns = self.categorical_columns

        for col in categorical_columns:
            df[col] = df[col].str.title()

        for col in categorical_columns:
            print(f"\n{col}")
            print(df[col].unique())

        for col in text_columns:
            df[col] = df[col].str.replace(r"\s+", " ", regex=True)

        self.df = df

    def map_categorical_values(self):
        df = self.df

        df["suspect_gender"] = df["suspect_gender"].replace(self.gender_map)
        df["reported_online"] = df["reported_online"].replace(self.reported_online_map).astype(bool)
        df["victim_gender"] = df["victim_gender"].replace(self.gender_map)
        df["severity"] = df["severity"].replace(self.severity_map)
        df["crime_type"] = df["crime_type"].replace(self.crime_type_map)
        df["case_status"] = df["case_status"].replace(self.case_status_map)

        print(df["suspect_gender"].unique())
        print(df["victim_gender"].unique())
        print(df["reported_online"].unique())
        print(df["severity"].unique())
        print(df["crime_type"].unique())

        df["case_status"] = df["case_status"].str.title()

        df["crime_type"] = df["crime_type"].str.title()
        print(df["crime_type"].unique())

        self.df = df

    def correct_invalid_ages(self):
        """# Step 5 – Correct Invalid Values"""
        df = self.df

        invalid_suspect_age = df[
            (df["suspect_age"] < 0) |
            (df["suspect_age"] > 120)
        ]

        invalid_victim_age = df[
            (df["victim_age"] < 0) |
            (df["victim_age"] > 120)
        ]

        print(invalid_suspect_age)
        print(invalid_victim_age)

        df = df[
            (df["suspect_age"].between(0, 120)) &
            (df["victim_age"].between(0, 120))
        ]

        self.df = df

    def correct_invalid_coordinates(self):
        df = self.df

        invalid_coordinates = df[
            (~df["latitude"].between(-90, 90)) |
            (~df["longitude"].between(-180, 180))
        ]

        print(invalid_coordinates)

        df = df[
            df["latitude"].between(-90, 90) &
            df["longitude"].between(-180, 180)
        ]

        self.df = df

    def clean_property_loss(self):
        df = self.df

        print(df["property_loss_usd"].dtype)

        df["property_loss_usd"].unique()[:20]

        df["property_loss_usd"] = (
            df["property_loss_usd"]
              .astype(str)
              .str.replace("$", "", regex=False)
              .str.replace(",", "", regex=False)
        )

        df["property_loss_usd"] = pd.to_numeric(
            df["property_loss_usd"],
            errors="coerce"
        )

        print(df["property_loss_usd"].dtype)

        print(df["property_loss_usd"].isnull().sum())

        df = df.dropna()

        print(df["property_loss_usd"].isnull().sum())

        df[df["property_loss_usd"] < 0]

        df = df[df["property_loss_usd"] >= 0]

        self.df = df

    def clean_num_arrests(self):
        df = self.df

        df[df["num_arrests"] < 0]

        df = df[df["num_arrests"] >= 0]

        self.df = df

    def clean_datetime(self):
        df = self.df

        df["incident_datetime"] = pd.to_datetime(
            df["incident_datetime"],
            errors="coerce"
        )

        df = df.dropna(subset=["incident_datetime"])

        (df["incident_datetime"].dtype)

        df["reported_online"].unique()

        self.df = df

    def clean_phone_numbers(self):
        df = self.df

        df["victim_phone"] = (
            df["victim_phone"]
              .astype(str)
              .str.replace(r"\D", "", regex=True)
        )

        df = df[df["victim_phone"].str.len() == 10]

        df["victim_phone"].head()

        print(df["suspect_age"].between(0, 120).all())
        print(df["victim_age"].between(0, 120).all())

        print(df["latitude"].between(-90, 90).all())
        print(df["longitude"].between(-180, 180).all())

        print((df["property_loss_usd"] >= 0).all())
        print((df["num_arrests"] >= 0).all())

        self.df = df

    def convert_data_types(self):
        """# Step 6: Data Type Conversion and Final Validation"""
        df = self.df

        print(df.dtypes)

        numeric_columns = self.numeric_columns

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df["suspect_age"] = df["suspect_age"].astype(int)
        df["victim_age"] = df["victim_age"].astype(int)
        df["num_arrests"] = df["num_arrests"].astype(int)

        df.dropna(subset=["incident_datetime"], inplace=True)
        df.dropna(subset=["reported_online"], inplace=True)
        df.dropna(subset=["suspect_gender"], inplace=True)
        df.dropna(subset=["victim_gender"], inplace=True)
        df.dropna(subset=["severity"], inplace=True)
        df.dropna(subset=["crime_type"], inplace=True)

        df["reported_online"].value_counts()

        print(df.dtypes)

        self.df = df

    def final_validation(self):
        df = self.df

        print("Total Missing Values:", df.isnull().sum().sum())

        print("Duplicate Rows:", df.duplicated().sum())

        print("Suspect Age Valid:", df["suspect_age"].between(0, 120).all())
        print("Victim Age Valid:", df["victim_age"].between(0, 120).all())
        print("Latitude Valid:", df["latitude"].between(-90, 90).all())
        print("Longitude Valid:", df["longitude"].between(-180, 180).all())
        print("Property Loss Valid:", (df["property_loss_usd"] >= 0).all())
        print("Arrests Valid:", (df["num_arrests"] >= 0).all())

        df.info()

        self.df = df


    def clean(self):
        self.explore_data()
        self.handle_missing_values()
        self.remove_duplicates()
        self.clean_text_columns()
        self.map_categorical_values()
        self.correct_invalid_ages()
        self.correct_invalid_coordinates()
        self.clean_property_loss()
        self.clean_num_arrests()
        self.clean_datetime()
        self.clean_phone_numbers()
        self.convert_data_types()
        self.final_validation()
        
        return self.df