import pandas as pd
from datetime import datetime
from edu_tests import check_education_data, save_with_stats, load_excel
import os

def test_check_education_data_logic():
    df = pd.DataFrame({
        '学号': ['001', '001', '002', '003', '004', '005', '006'],
        '学习时间': pd.to_datetime([
            '2025-01-01 01:00',
            '2025-01-01 10:00',
            '2025-01-01 04:00',
            '2025-01-01 14:00',
            '2025-01-01 15:00',
            '2025-01-01 16:00',
            '2025-01-01 17:00',
        ]),
        '学习时长': [25, 85, 60, 30, 60, 60, 60],
        '学习状态': ['正常', '正常', '正常', '', '正常', '正常', ''],
        '完成状态': ['未完成', '完成', '未完成', '', '未完成', '完成', '完成']
    })

    df_checked, stats = check_education_data(df)

    assert len(df_checked) == 7
    assert stats["学号重复"] == 1
    assert stats["学习时长异常"] == 2
    assert stats["凌晨学习"] == 2
    assert stats["未完成"] == 4
    assert stats["状态逻辑冲突"] == 2
    assert stats["正常"] >= 1
    assert '检测结果' in df_checked.columns

def test_save_with_stats(tmp_path):
    test_output = tmp_path / "output_test.xlsx"

    df = pd.DataFrame({
        '学号': ['001', '002'],
        '学习时间': [datetime(2025, 1, 1, 10, 0), datetime(2025, 1, 1, 15, 0)],
        '学习时长': [60, 60],
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成']
    })

    df_checked, stats = check_education_data(df)
    save_with_stats(df_checked, stats, test_output)

    assert test_output.exists()

    reloaded_df = load_excel(test_output)
    assert '学号' in reloaded_df.columns
    assert len(reloaded_df) == 2
