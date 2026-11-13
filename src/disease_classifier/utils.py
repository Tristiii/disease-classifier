from pathlib import Path
import pandas as pd

def get_root() -> Path:
    return Path(__file__).parent.parent.parent

def get_data() -> Path:
    return get_root() / 'data' / 'disease-and-symptoms-dataset.csv'

def dataframe() -> pd.DataFrame:
    return pd.read_csv(get_data())

def get_model() -> Path:
    return get_root() / 'model' / 'model.pkl'