from loadData import LoadData
from cleanData import CleanData
from eda import EDA

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\mohib\Desktop\Mohib\data-cleaning-pipeline\Datasets\messyCrimeDastaset\crime_incidents_messy.csv"

    try:
        #load data
        loader = LoadData(FILE_PATH)
        raw_df = loader.loadData()
        


    except FileNotFoundError as e:
        print("File not found")