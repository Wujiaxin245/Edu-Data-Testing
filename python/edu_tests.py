import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)

def has_duplicate_ids(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.duplicated(subset='学号', keep=False)]

def has_invalid_duration(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['学习时长(分钟)'] <= 0]

def has_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.isnull().any(axis=1)]
