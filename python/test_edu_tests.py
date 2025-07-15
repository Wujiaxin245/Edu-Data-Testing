import pandas as pd
import pytest
from edu_tests import (
    load_excel,
    check_education_data,
    save_with_stats
)
import os

def test_check_education_data():
    df = pd.DataFrame({
        '学号': ['001', '001', '003'],
        '学习时间': pd.to_datetime(['2023-01-01 02:00', '2023-01-01 08:00', '2023-01-01 04:00']),
        '学习时长': [20, 60, 85],
        '学习状态': ['正常', '正常', '正常'],
        '完成状态': ['未完成', '完成', '未完成']
    })

    df_checked, stats = check_education_data(df)

    assert len(df_checked) == 3
    assert '检测结果' in df_checked.columns

    assert stats["总记录数"] == 3
    assert stats["学号重复"] == 1
    assert stats["学习时长异常"] == 2
    assert stats["凌晨学习"] == 2
    assert stats["未完成"] == 2
    assert stats["状态逻辑冲突"] == 2
    assert stats["正常"] == 0 

def test_save_with_stats(tmp_path):
    df = pd.DataFrame({
        '学号': ['001'],
        '学习时间': [pd.Timestamp('2023-01-01 02:00')],
        '学习时长': [25],
        '学习状态': ['正常'],
        '完成状态': ['未完成'],
        '检测结果': ['学习时长异常；凌晨学习；未完成；状态逻辑冲突']
    })

    stats = {
        "总记录数": 1,
        "正常": 0,
        "学号重复": 0,
        "学习时长异常": 1,
        "凌晨学习": 1,
        "未完成": 1,
        "状态逻辑冲突": 1
    }

    output_file = tmp_path / "output_test.xlsx"
    save_with_stats(df, stats, output_file)

    # 再读回来检查写入成功
    result_df = pd.read_excel(output_file, sheet_name="数据检测结果")
    report_df = pd.read_excel(output_file, sheet_name="统计报告")

    assert "检测结果" in result_df.columns
    assert "检测项" in report_df.columns
    assert len(report_df) == len(stats)

def test_load_excel(tmp_path):
    test_file = tmp_path / "test_input.xlsx"
    pd.DataFrame({'学号': ['001'], '学习时间': ['2023-01-01'], '学习时长': [60]}).to_excel(test_file, index=False)

    df = load_excel(test_file)
    assert not df.empty
    assert "学号" in df.columns
