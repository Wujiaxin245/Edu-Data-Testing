# Edu-Data-Testing

> 教育数据质量监控测试方案 - 基于 Excel/VBA 实现的数据验证与测试流程

## 📘 项目简介

本项目旨在通过模拟教育系统中的学生学习行为数据，设计并实现一套数据质量监控测试方案，覆盖异常学习时段、学习时长异常、数据缺失等典型数据问题。  
测试方案以探索性测试为核心，结合 VBA 自动化处理手段，构建 Excel 格式的数据质量监测工具，适用于实际教育信息化平台的数据验收和测试验证。

---

## 📂 项目结构

| 文件名               | 描述 |
|----------------------|------|
| `README.md`          | 项目说明文档（当前文件） |
| `LICENSE`            | 开源协议（MIT） |
| `.gitignore`         | Git 忽略配置 |
| `测试方案草案.md`     | 测试设计文档，包含场景设计与测试步骤说明 |
| `活动数据样本.xlsx`   | 模拟测试数据，包含学生学习行为信息 |
| `test.vba` | VBA 自动化脚本（用于异常检测、条件标记等） |

---

## 🧪 测试内容

### ✅ 测试目标

- 检查数据中是否存在学习时间异常（如凌晨学习）
- 检查学习时长是否超过合理区间
- 检查是否存在数据缺失、未完成记录
- 模拟边界条件、复合异常等特殊数据情况

### 🧪 已覆盖的测试场景示例

| 场景编号 | 描述 |
|----------|------|
| 1        | 凌晨 3 点学习数据记录的异常检测 |
| 2        | 学习时长字段为空值的处理 |
| 3        | 超时 + 未完成记录的复合异常分析 |
| 4        | 学号重复或数据格式错误检测 |

---

## 🧰 使用说明

1. 克隆或下载本项目：
   ```bash
   git clone https://github.com/Wujiaxin245/Edu-Data-Testing.git

![platform](https://img.shields.io/badge/platform-Excel--VBA-blue)
![status](https://img.shields.io/badge/status-maintained-brightgreen)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

edu-data-testing/
├── python/
│   ├── edu_tests.py
│   ├── test_edu_tests.py
│   └── requirements.txt
└── README.md

# python/edu_tests.py
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)

def has_duplicate_ids(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.duplicated(subset='学号', keep=False)]

def has_invalid_duration(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['学习时长(分钟)'] <= 0]

def has_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.isnull().any(axis=1)]

# python/test_edu_tests.py
import pandas as pd
from edu_tests import has_duplicate_ids, has_invalid_duration, has_missing_values

def test_duplicate_ids():
    df = pd.DataFrame({
        '学号': ['001', '002', '001'],
        '学习时长(分钟)': [60, 80, 70]
    })
    duplicates = has_duplicate_ids(df)
    assert len(duplicates) == 2

def test_invalid_duration():
    df = pd.DataFrame({
        '学号': ['001', '002', '003'],
        '学习时长(分钟)': [60, -10, 0]
    })
    invalids = has_invalid_duration(df)
    assert len(invalids) == 2

def test_missing_values():
    df = pd.DataFrame({
        '学号': ['001', None, '003'],
        '学习时长(分钟)': [60, 70, None]
    })
    missings = has_missing_values(df)
    assert len(missings) == 2

# python/requirements.txt
pandas
openpyxl
pytest

# README.md（附加到原 README 内容中）

## 🧪 Python 自动化测试模块（新增）

本项目新增 `python/` 目录，用于展示如何使用 Python 自动化进行数据校验测试。

### 📦 安装依赖
```bash
cd python
pip install -r requirements.txt
```

### 🚀 运行测试
```bash
pytest
```

### ✅ 包含测试逻辑
- 检查重复学号
- 检查学习时长为负或为零
- 检查空值

该模块用于展示从原始 Excel/VBA 测试迁移到自动化测试流程的能力，适合展示在软件测试类岗位的简历中。
