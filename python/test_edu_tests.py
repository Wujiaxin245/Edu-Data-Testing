import pandas as pd
from edu_tests import has_duplicate_ids, has_invalid_duration, has_missing_values

def test_duplicate_ids():
    df = pd.DataFrame({
        '学号': ['001', '002', '001'],
        '学习时长(分钟)': [60, 80, 70]
    })
    duplicates = has_duplicate_ids(df)
    assert len(duplicates) == 2

def test_invalid_duration():
    df = pd.DataFrame({
        '学号': ['001', '002', '003'],
        '学习时长(分钟)': [60, -10, 0]
    })
    invalids = has_invalid_duration(df)
    assert len(invalids) == 2

def test_missing_values():
    df = pd.DataFrame({
        '学号': ['001', None, '003'],
        '学习时长(分钟)': [60, 70, None]
    })
    missings = has_missing_values(df)
    assert len(missings) == 2
