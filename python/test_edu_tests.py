import pandas as pd
from edu_tests import check_education_data

def test_check_education_data():
    # 构造一个包含各种问题的 DataFrame
    df = pd.DataFrame({
        '学号': ['001', '002', '001', '004'],
        '学习时间': pd.to_datetime(['2024-07-01 01:00', '2024-07-01 09:00', '2024-07-01 02:00', '2024-07-01 10:00']),
        '学习时长': [25, 90, 60, 70],
        '学习状态': ['正常', '异常', '正常', '正常'],
        '完成状态': ['未完成', '', '完成', '未完成']
    })

    checked_df, stats = check_education_data(df)

    # 检查检测结果列是否存在
    assert '检测结果' in checked_df.columns

    # 检查具体的统计项数量是否正确
    assert stats['总记录数'] == 4
    assert stats['学号重复'] == 1
    assert stats['凌晨学习'] == 2
    assert stats['学习时长异常'] == 2
    assert stats['未完成'] == 3
    assert stats['状态逻辑冲突'] == 2
    assert stats['正常'] == 0  # 都有问题

    print("✅ 所有测试通过")

if __name__ == "__main__":
    test_check_education_data()
