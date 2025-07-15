import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import sys
import os

def load_excel(file_path):
    return pd.read_excel(file_path)

def save_with_stats(df, stats, output_path):
    # 写入主数据表（创建文件）
    df.to_excel(output_path, index=False, sheet_name="数据检测结果")

    stats_df = pd.DataFrame({
        '检测项': list(stats.keys()),
        '数量': list(stats.values())
    })

    with pd.ExcelWriter(output_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        stats_df.to_excel(writer, sheet_name="统计报告", index=False)

def check_education_data(df):
    results = []
    seen_ids = set()
    
    stats = {
        "总记录数": len(df),
        "正常": 0,
        "学号重复": 0,
        "学习时长异常": 0,
        "凌晨学习": 0,
        "未完成": 0,
        "状态逻辑冲突": 0
    }

    for idx, row in df.iterrows():
        result = []

        学号 = str(row.get('学号')).strip()
        学习时间 = row.get('学习时间')
        学习时长 = row.get('学习时长')
        学习状态 = str(row.get('学习状态')).strip() if not pd.isna(row.get('学习状态')) else ''
        完成状态 = str(row.get('完成状态')).strip() if not pd.isna(row.get('完成状态')) else ''

        if 学号 in seen_ids:
            result.append("学号重复")
            stats["学号重复"] += 1
        elif 学号:
            seen_ids.add(学号)

        if pd.notna(学习时长) and (学习时长 < 30 or 学习时长 > 80):
            result.append("学习时长异常")
            stats["学习时长异常"] += 1

        if isinstance(学习时间, pd.Timestamp):
            if 0 <= 学习时间.hour < 5:
                result.append("凌晨学习")
                stats["凌晨学习"] += 1

        if 完成状态 == "" or 完成状态 == "未完成":
            result.append("未完成")
            stats["未完成"] += 1

        if 学习状态 == "正常" and 完成状态 == "未完成":
            result.append("状态逻辑冲突")
            stats["状态逻辑冲突"] += 1

        if not result:
            result.append("正常")
            stats["正常"] += 1

        results.append("；".join(result))

    df['检测结果'] = results
    return df, stats

def print_report(stats):
    print("\n📊 数据质量检测报告")
    print("-" * 30)
    for k, v in stats.items():
        print(f"{k:<14}: {v}")
    print("-" * 30)

if __name__ == "__main__":
    input_file = "input.xlsx"
    output_file = "output_检测结果.xlsx"

    try:
        df = load_excel(input_file)
        df_checked, stats = check_education_data(df)
        save_with_stats(df_checked, stats, output_file)
        print(f"\n✅ 检测完成，结果已保存到: {output_file}")
        print_report(stats)
    except Exception as e:
        print(f"❌ 出错: {e}")
        sys.exit(1)
