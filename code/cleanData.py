import pandas as pd
import numpy as np


class CleanData:

    def __init__(self, df):
        self.df = df.copy()

    # Remove duplicate rows
    def removeDuplicates(self):
        self.df.drop_duplicates(inplace=True)
        return self.df

    # Handle missing values
    def handleMissingValues(self):

        # Numeric columns
        numeric_cols = [
            "latitude", "longitude", "badge_number",
            "suspect_age", "victim_age",
            "num_arrests", "property_loss_usd"
        ]

        self.df["property_loss_usd"] = pd.to_numeric(
            self.df["property_loss_usd"],
            errors="coerce"
        )

        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col].fillna(self.df[col].median(), inplace=True)

        # Categorical columns
        categorical_cols = [
            "suspect_gender",
            "victim_gender",
            "suspect_race",
            "weapon_used",
            "severity",
            "case_status",
            "resolution",
            "reported_online"
        ]

        for col in categorical_cols:
            if col in self.df.columns:
                self.df[col].fillna("Unknown", inplace=True)

        return self.df

    # Convert columns to correct data types
    def fixDataTypes(self):

        self.df["incident_datetime"] = pd.to_datetime(
            self.df["incident_datetime"],
            errors="coerce"
        )

        self.df["property_loss_usd"] = pd.to_numeric(
            self.df["property_loss_usd"],
            errors="coerce"
        )

        return self.df

    # Correct spelling mistakes
    def fixTypos(self):

        crime_mapping = {
            "asslt": "Assault",
            "Homocide": "Homicide",
            "Domestc Violence": "Domestic Violence",
            "B&E": "Breaking & Entering",
            "burglary": "Burglary",
            "robbery": "Robbery",
            "manslaughter": "Manslaughter"
        }

        self.df["crime_type"] = self.df["crime_type"].replace(crime_mapping)

        district_mapping = {
            "Sou": "South",
            "Cen": "Central",
            "southeast": "Southeast",
            "Southwest ": "Southwest",
            "East ": "East",
            "North ": "North"
        }

        self.df["district"] = self.df["district"].replace(district_mapping)

        return self.df

    # Standardize text formatting
    def standardizeText(self):

        text_columns = [
            "crime_type",
            "district",
            "city",
            "resolution",
            "case_status",
            "severity"
        ]

        for col in text_columns:
            if col in self.df.columns:
                self.df[col] = (
                    self.df[col]
                    .astype(str)
                    .str.strip()
                    .str.title()
                )

        return self.df

    # Fix boolean column
    def cleanReportedOnline(self):

        mapping = {
            "YES": True,
            "Yes": True,
            "yes": True,
            "TRUE": True,
            "True": True,
            True: True,

            "NO": False,
            "No": False,
            "no": False,
            "FALSE": False,
            "False": False,
            False: False
        }

        self.df["reported_online"] = self.df["reported_online"].map(mapping)

        return self.df

    # Remove invalid values
    def removeInvalidValues(self):

        # Invalid ages
        self.df.loc[
            (self.df["suspect_age"] < 0) |
            (self.df["suspect_age"] > 100),
            "suspect_age"
        ] = np.nan

        self.df.loc[
            (self.df["victim_age"] < 0) |
            (self.df["victim_age"] > 100),
            "victim_age"
        ] = np.nan

        # Invalid latitude
        self.df.loc[
            (self.df["latitude"] < -90) |
            (self.df["latitude"] > 90),
            "latitude"
        ] = np.nan

        # Invalid longitude
        self.df.loc[
            (self.df["longitude"] < -180) |
            (self.df["longitude"] > 180),
            "longitude"
        ] = np.nan

        # Invalid arrests
        self.df.loc[
            self.df["num_arrests"] < 0,
            "num_arrests"
        ] = 0

        return self.df

    # Return cleaned dataframe
    def getData(self):
        return self.df