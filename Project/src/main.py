import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

#============================================================================================== 

            # This above code is usefull when run the main file using play button in vs code
            # othervise in run in terminal using "python -m Project.src.main"

#==============================================================================================


from Project.src.loadData import LoadData
import pandas as pd
import numpy as np


if __name__ == "__main__":


    loader = LoadData()
    loader.loadData()