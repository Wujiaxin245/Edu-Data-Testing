import pandas as pd
import pytest
from edu_tests import check_education_data

def test_input_excel_file():
    # 加载 Excel 文件
    file_path = "input.xlsx"
    df = pd.read_excel(file_path)

    # 执行数据质量检查函数
    _, stats = check_education_data(df)

    # 输出结果（可用于调试）
    print("\n=== 教育数据质量检查统计 ===")
    for key, value in stats.items():
        print(f"{key}: {value}")

    # 示例断言（根据你的实际数据修改这些值）
    assert isinstance(stats, dict)
    assert all(key in stats for key in [
        "学号重复", "学习时长异常", "凌晨学习", "未完成", "状态逻辑冲突", "正常"
    ])
