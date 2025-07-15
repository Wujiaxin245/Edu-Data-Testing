# python/edu_tests.py
import pandas as pd

def check_education_data(df: pd.DataFrame):
    stats = {}

    # T01: 学号重复检测
    duplicate_ids = df[df.duplicated(subset="学号", keep=False)]
    stats["学号重复"] = duplicate_ids["学号"].nunique()

    # T02: 学习时长范围检测 (30 ~ 80 分钟)
    abnormal_duration = df[(df["学习时长"] < 30) | (df["学习时长"] > 80)]
    stats["学习时长异常"] = len(abnormal_duration)

    # T03: 凌晨学习检测（00:00 - 04:59）
    df["学习时间"] = pd.to_datetime(df["学习时间"], errors="coerce")
    df["hour"] = df["学习时间"].dt.hour
    night_study = df[(df["hour"] >= 0) & (df["hour"] < 5)]
    stats["凌晨学习"] = len(night_study)

    # T04: 完成状态缺失检测（空或“未完成”）
    incomplete = df["完成状态"].fillna("").apply(lambda x: str(x).strip() == "" or x == "未完成")
    stats["未完成"] = incomplete.sum()

    # T05: 状态逻辑冲突检测（正常 + 未完成/空）
    def has_conflict(row):
        status = str(row["学习状态"]).strip()
        finish = str(row["完成状态"]).strip()
        return status == "正常" and (finish == "" or finish == "未完成")

    logic_conflicts = df.apply(has_conflict, axis=1)
    stats["状态逻辑冲突"] = logic_conflicts.sum()

    # ✅ 添加对“正常”状态的统计
    stats["正常"] = (df["学习状态"] == "正常").sum()

    return df, stats
