import pandas as pd

def check_education_data(df: pd.DataFrame):
    stats = {}

    # T01: 学号重复检测
    duplicate_ids = df[df.duplicated(subset="学号", keep=False)]
    stats["学号重复"] = duplicate_ids["学号"].nunique()

    # T02: 学习时长异常检测
    df["学习时长"] = pd.to_numeric(df["学习时长"], errors="coerce")
    stats["学习时长异常"] = int(((df["学习时长"] < 30) | (df["学习时长"] > 80)).sum())

    # T03: 凌晨学习检测
    df["学习时间"] = pd.to_datetime(df["学习时间"], errors="coerce")
    stats["凌晨学习"] = int(df["学习时间"].dt.hour.between(0, 4, inclusive="both").sum())

    # T04: 未完成检测
    df["完成状态"] = df["完成状态"].fillna("").astype(str).str.strip()
    stats["未完成"] = int(df["完成状态"].isin(["", "未完成"]).sum())

    # T05: 状态逻辑冲突
    df["学习状态"] = df["学习状态"].fillna("").astype(str).str.strip()
    conflict = (df["学习状态"] == "正常") & df["完成状态"].isin(["", "未完成"])
    stats["状态逻辑冲突"] = int(conflict.sum())

    return df, stats
