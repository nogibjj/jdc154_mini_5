"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests
import os
import pandas as pd


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/nfl-wide-receivers/advanced-historical.csv",
    file_path="data/nfl-wide-receivers.csv",
    directory="data",
):
    if not os.path.exists(directory):
        os.makedirs(directory)
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    df = pd.read_csv(file_path)
    df_subset = df.head(121)
    df_subset.to_csv(file_path, index=False)
    return file_path
