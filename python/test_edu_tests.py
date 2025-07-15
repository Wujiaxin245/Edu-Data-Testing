import pandas as pd
import pytest
from edu_tests import check_education_data

def test_all_logic_points():
    df = pd.DataFrame({
        "学号": ["A", "B", "A", "C", "D", "E", "F"],
        "学习时长": [25, 85, 60, 30, 60, 81, 29],
        "学习时间": [
            "2025-01-01 01:00",  # 清晨 ✓
            "2025-01-01 10:00",
            "2025-01-01 03:00",  # 清晨 ✓
            "2025-01-01 05:00",
            "2025-01-01 04:59",  # 清晨 ✓
            "2025-01-01 07:00",
            "2025-01-01 23:00",
        ],
        "学习状态": ["正常", "正常", "正常", "", "正常", "正常", "正常"],
        "完成状态": ["未完成", "完成", "未完成", "", "未完成", "完成", "完成"],
    })

    _, stats = check_education_data(df)

    assert stats["学号重复"] == 1             # A 重复
    assert stats["学习时长异常"] == 4        # 25,85,81,29
    assert stats["凌晨学习"] == 3            # 01:00,03:00,04:59
    assert stats["未完成"] == 4
    assert stats["状态逻辑冲突"] == 3        # 学号 A、C、D
    # 可选：对“正常”不测试

def test_empty_df():
    df = pd.DataFrame(columns=["学号","学习时长","学习时间","学习状态","完成状态"])
    _, stats = check_education_data(df)
    assert all(v == 0 for v in stats.values())

@pytest.mark.parametrize("time_str, expected", [
    ("2025-01-01 04:59", 1),
    ("2025-01-01 05:00", 0),
    ("", 0),
    (pd.NaT, 0),
])
def test_night_boundary(time_str, expected):
    df = pd.DataFrame({
        "学号": ["X"],
        "学习时长": [60],
        "学习时间": [time_str],
        "学习状态": ["正常"],
        "完成状态": ["完成"],
    })
    _, stats = check_education_data(df)
    assert stats["凌晨学习"] == expected
