import pandas as pd
from edu_tests import check_education_data

def test_learning_duration_anomaly():
    df = pd.DataFrame({
        '学号': ['001', '002'],
        '学习时间': pd.to_datetime(['2023-01-01 12:00', '2023-01-01 13:00']),
        '学习时长': [10, 100],
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成']
    })
    _, stats = check_education_data(df)
    assert stats['学习时长异常'] == 2

def test_logic_conflict_between_status():
    df = pd.DataFrame({
        '学号': ['003'],
        '学习时间': [pd.Timestamp('2023-01-01 10:00')],
        '学习时长': [60],
        '学习状态': ['正常'],
        '完成状态': ['未完成']
    })
    df_checked, stats = check_education_data(df)
    assert '状态逻辑冲突' in df_checked['检测结果'].iloc[0]
    assert stats['状态逻辑冲突'] == 1

def test_unfinished_status():
    df = pd.DataFrame({
        '学号': ['004'],
        '学习时间': [pd.Timestamp('2023-01-01 10:00')],
        '学习时长': [60],
        '学习状态': ['中断'],
        '完成状态': ['未完成']
    })
    df_checked, stats = check_education_data(df)
    assert '未完成' in df_checked['检测结果'].iloc[0]
    assert stats['未完成'] == 1

def test_midnight_learning():
    df = pd.DataFrame({
        '学号': ['005'],
        '学习时间': [pd.Timestamp('2023-01-01 03:30')],
        '学习时长': [60],
        '学习状态': ['正常'],
        '完成状态': ['完成']
    })
    df_checked, stats = check_education_data(df)
    assert '凌晨学习' in df_checked['检测结果'].iloc[0]
    assert stats['凌晨学习'] == 1

def test_duplicate_student_id():
    df = pd.DataFrame({
        '学号': ['006', '006'],
        '学习时间': pd.to_datetime(['2023-01-01 10:00', '2023-01-01 11:00']),
        '学习时长': [60, 60],
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成']
    })
    df_checked, stats = check_education_data(df)
    assert '学号重复' in df_checked['检测结果'].iloc[1]
    assert stats['学号重复'] == 1
