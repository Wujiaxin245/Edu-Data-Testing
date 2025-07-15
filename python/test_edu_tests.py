import pandas as pd
from edu_tests import check_education_data

def test_basic_stats():
    df = pd.DataFrame({
        '学号': ['001', '002', '003', '003', '004', '005', '006'],
        '学习时间': pd.to_datetime([
            '2025-01-01 01:00',
            '2025-01-01 10:00',
            '2025-01-01 04:00',
            '2025-01-01 14:00',
            '2025-01-01 16:00',
            '2025-01-01 17:00',
            '2025-01-01 18:00',
        ]),
        '学习时长': [25, 85, 60, 30, 60, 60, 60],
        '学习状态': ['正常', '正常', '正常', '', '正常', '正常', '正常'],
        '完成状态': ['未完成', '完成', '未完成', '', '未完成', '完成', '完成']
    })
    df_checked, stats = check_education_data(df)

    assert len(df_checked) == 7
    assert stats["学号重复"] == 1
    assert stats["学习时长异常"] == 2
    assert stats["凌晨学习"] == 2
    assert stats["未完成"] == 4
    assert stats["状态逻辑冲突"] == 3
    assert stats["正常"] == 2

def test_empty_completion_status():
    df = pd.DataFrame({
        '学号': ['100'],
        '学习时间': pd.to_datetime(['2025-01-01 09:00']),
        '学习时长': [60],
        '学习状态': ['正常'],
        '完成状态': ['']
    })
    _, stats = check_education_data(df)
    assert stats["未完成"] == 1

def test_logical_conflict():
    df = pd.DataFrame({
        '学号': ['101'],
        '学习时间': pd.to_datetime(['2025-01-01 11:00']),
        '学习时长': [60],
        '学习状态': ['正常'],
        '完成状态': ['未完成']
    })
    _, stats = check_education_data(df)
    assert stats["状态逻辑冲突"] == 1

def test_valid_study():
    df = pd.DataFrame({
        '学号': ['102'],
        '学习时间': pd.to_datetime(['2025-01-01 10:00']),
        '学习时长': [60],
        '学习状态': ['正常'],
        '完成状态': ['完成']
    })
    _, stats = check_education_data(df)
    assert stats["正常"] == 1

def test_edge_study_duration():
    df = pd.DataFrame({
        '学号': ['103', '104'],
        '学习时间': pd.to_datetime(['2025-01-01 12:00', '2025-01-01 13:00']),
        '学习时长': [30, 80],  # valid edge durations
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成']
    })
    _, stats = check_education_data(df)
    assert stats["学习时长异常"] == 0
    assert stats["正常"] == 2

def test_late_night_study_boundary():
    df = pd.DataFrame({
        '学号': ['105', '106'],
        '学习时间': pd.to_datetime(['2025-01-01 04:59', '2025-01-01 05:00']),
        '学习时长': [60, 60],
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成']
    })
    _, stats = check_education_data(df)
    assert stats["凌晨学习"] == 1
    assert stats["正常"] == 1
