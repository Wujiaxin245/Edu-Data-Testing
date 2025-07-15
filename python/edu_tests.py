import pandas as pd

def check_education_data(df: pd.DataFrame):
    stats = {}

    # T01: 学号重复检测（相同学号出现2次及以上）
    if "学号" in df.columns:
        duplicate_ids = df[df.duplicated(subset="学号", keep=False)]
        stats["学号重复"] = duplicate_ids["学号"].nunique()
    else:
        stats["学号重复"] = 0

    # T02: 学习时长范围检测（应为 30~80 分钟）
    if "学习时长" in df.columns:
        df["学习时长"] = pd.to_numeric(df["学习时长"], errors="coerce")
        abnormal_duration = df[(df["学习时长"] < 30) | (df["学习时长"] > 80)]
        stats["学习时长异常"] = len(abnormal_duration)
    else:
        stats["学习时长异常"] = 0

    # T03: 凌晨学习检测（00:00 - 04:59）
    if "学习时间" in df.columns:
        df["学习时间"] = pd.to_datetime(df["学习时间"], errors="coerce")
        night_study = df[df["学习时间"].dt.hour.between(0, 4)]
        stats["凌晨学习"] = len(night_study)
    else:
        stats["凌晨学习"] = 0

    # T04: 完成状态缺失检测（空或“未完成”）
    if "完成状态" in df.columns:
        df["完成状态"] = df["完成状态"].fillna("").astype(str).str.strip()
        incomplete = df["完成状态"].apply(lambda x: x == "" or x == "未完成")
        stats["未完成"] = incomplete.sum()
    else:
        stats["未完成"] = 0

    # T05: 状态逻辑冲突检测（状态为“正常”但完成状态为“未完成”或空）
    if "学习状态" in df.columns and "完成状态" in df.columns:
        df["学习状态"] = df["学习状态"].fillna("").astype(str).str.strip()
        logic_conflicts = df.apply(
            lambda row: row["学习状态"] == "正常" and (row["完成状态"] == "" or row["完成状态"] == "未完成"),
            axis=1
        )
        stats["状态逻辑冲突"] = logic_conflicts.sum()
    else:
        stats["状态逻辑冲突"] = 0

    return df, stats
