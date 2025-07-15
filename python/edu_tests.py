import pandas as pd
from datetime import datetime
from main import check_education_data, save_with_stats, load_excel  # 替换 main 为你的实际模块名
import os

def test_check_education_data_all_cases():
    df = pd.DataFrame({
        '学号': ['001', '001', '002', '003', '004', '005', '006'],
        '学习时间': pd.to_datetime([
            '2025-01-01 01:00',  # 凌晨
            '2025-01-01 10:00',
            '2025-01-01 04:00',  # 凌晨
            '2025-01-01 14:00',
            '2025-01-01 15:00',
            '2025-01-01 16:00',
            '2025-01-01 17:00',
        ]),
        '学习时长': [25, 85, 60, 30, 60, 60, 60],  # 异常、正常
        '学习状态': ['正常', '正常', '正常', '', '正常', '正常', ''],  # 空状态、正常状态
        '完成状态': ['未完成', '完成', '未完成', '', '未完成', '完成', '完成']  # 空、完成、未完成
    })

    df_checked, stats = check_education_data(df)

    assert len(df_checked) == 7
    assert '检测结果' in df_checked.columns

    assert stats["总记录数"] == 7
    assert stats["学号重复"] == 1          # 第二个 '001'
    assert stats["学习时长异常"] == 2     # 时长为 25 和 85
    assert stats["凌晨学习"] == 2         # index 0 和 2
    assert stats["未完成"] == 3           # 包含空值和 '未完成'
    assert stats["状态逻辑冲突"] == 2     # '正常' + '未完成'
    assert stats["正常"] >= 1             # 至少一个正常样本

def test_save_and_load_excel(tmp_path):
    test_file = tmp_path / "test_output.xlsx"

    df = pd.DataFrame({
        '学号': ['001', '002'],
        '学习时间': [datetime(2025, 1, 1, 10, 0), datetime(2025, 1, 1, 15, 0)],
        '学习时长': [60, 65],
        '学习状态': ['正常', '正常'],
        '完成状态': ['完成', '完成'],
    })

    df_checked, stats = check_education_data(df)
    save_with_stats(df_checked, stats, test_file)

    # 检查文件是否存在
    assert test_file.exists()

    # 重新加载并验证
    loaded = load_excel(test_file)
    assert '学号' in loaded.columns
    assert len(loaded) == 2
