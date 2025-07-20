import os
import pandas as pd
import pytest
from edu_tests import check_education_data

def test_input_excel_and_export_results():
    # 1. 读取 input.xlsx（确保文件存在）
    input_path = "input.xlsx"
    assert os.path.exists(input_path), f"找不到文件: {input_path}"
    df = pd.read_excel(input_path)

    # 2. 执行检测函数
    checked_df, stats = check_education_data(df)

    # 3. 输出结果为新的 Excel 文件
    output_dir = "python"
    output_file = os.path.join(output_dir, "output_检测结果.xlsx")
    os.makedirs(output_dir, exist_ok=True)

    # 将原始数据 + 检测统计一起写入 Excel（两个 sheet）
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        checked_df.to_excel(writer, index=False, sheet_name="原始数据（含处理）")
        pd.DataFrame([stats]).to_excel(writer, index=False, sheet_name="检测统计")

    # 4. 基础断言
    assert isinstance(stats, dict)
    assert all(key in stats for key in [
        "学号重复", "学习时长异常", "凌晨学习", "未完成", "状态逻辑冲突", "正常"
    ])
    assert os.path.exists(output_file), "检测结果文件未成功生成"

    print("\n✅ 检测完成，已导出到:", output_file)
