import pandas as pd
from edu_tests import check_education_data

def test_basic_stats():
    df = pd.DataFrame({
        '学号': ['10001', '10002', '10003', '10003', '10004', '10005', '10006'],
        '学习时间': pd.to_datetime([
            '2025-01-01 01:00',  # 凌晨
            '2025-01-01 10:00',  # 白天
            '2025-01-01 03:00',  # 凌晨
            '2025-01-01 14:00',
            '2025-01-01 16:00',
            '2025-01-01 17:00',
            '2025-01-01 18:00'
        ]),
        '学习时长': [25, 85, 60, 30, 60, 60, 60],
        '学习状态': ['正常', '正常', '正常', '', '正常', '正常', '正常'],
        '完成状态': ['未完成', '完成', '未完成', '', '未完成', '完成', '完成']
    })

    df_checked, stats = check_education_data(df)

    assert len(df_checked) == 7
    assert stats["学号重复"] == 1            # "10003" 重复
    assert stats["学习时长异常"] == 2       # 25, 85
    assert stats["凌晨学习"] == 2           # 01:00 和 03:00
    assert stats["未完成"] == 4             # 包括空字符串
    assert stats["状态逻辑冲突"] == 3       # 第1行、第3行、第5行
    assert stats["正常"] == 6               # 共6行"正常"
