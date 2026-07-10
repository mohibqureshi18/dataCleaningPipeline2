from loadData import LoadData
from clean_data import CleanData
from eda import EDA

import pandas as pd
import numpy as np


if __name__ == "__main__":

    # 7/10/2026
    # attempt to only call from main instead to write code logc

    loader = LoadData()
    loader.loadData()