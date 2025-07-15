import pandas as pd

def check_education_data(df: pd.DataFrame):
    stats = {}

    # 转换学习时间为 datetime 和小时字段
    df["学习时间"] = pd.to_datetime(df["学习时间"])
    df["hour"] = df["学习时间"].dt.hour

    # 清洗字符串字段，防止因空格或大小写错误引发判断失误
    df["学习状态"] = df["学习状态"].astype(str).str.strip()
    df["完成状态"] = df["完成状态"].astype(str).str.strip()

    # T01: 学号重复检测
    stats["学号重复"] = df[df.duplicated(subset="学号", keep=False)]["学号"].nunique()

    # T02: 学习时长范围检测（不在30~80分钟内）
    stats["学习时长异常"] = df[(df["学习时长"] < 30) | (df["学习时长"] > 80)].shape[0]

    # T03: 凌晨学习检测（00:00 ~ 04:59）
    stats["凌晨学习"] = df[(df["hour"] >= 0) & (df["hour"] < 5)].shape[0]

    # T04: 完成状态缺失检测（空或“未完成”）
    stats["未完成"] = df["完成状态"].isin(["", "未完成"]).sum()

    # T05: 状态逻辑冲突检测（学习状态为“正常”，但完成状态为空或“未完成”）
    stats["状态逻辑冲突"] = df[(df["学习状态"] == "正常") & (df["完成状态"].isin(["", "未完成"]))].shape[0]

    # 补充：统计“正常”状态的数量
    stats["正常"] = (df["学习状态"] == "正常").sum()

    return df, stats
