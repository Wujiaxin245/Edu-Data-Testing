# Edu-Data-Testing 📈 教育数据质量监控测试方案

> 基于 Excel/VBA 与 Python 自动化实现的数据验证与测试流程

![platform](https://img.shields.io/badge/platform-Excel--VBA%20%2B%20Python-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)
![license](https://img.shields.io/badge/license-MIT-lightgrey)
![Python CI](https://github.com/Wujiaxin245/Edu-Data-Testing/actions/workflows/python-tests.yml/badge.svg)
![codecov](https://codecov.io/gh/Wujiaxin245/Edu-Data-Testing/branch/main/graph/badge.svg)

---

## 📘 项目简介

本项目模拟教育系统中的学生学习行为数据，设计并实现一套完整的数据质量监控测试方案，覆盖异常时间段、学习时长、空值、重复学号等典型问题。

项目最初通过 Excel + VBA 实现数据校验逻辑，并在后续阶段转移至 Python 自动化测试框架（pytest），实现持续集成、覆盖率分析与 HTML 测试报告产出，提升测试效率与工程化能力。

---

## 📂 项目结构

| 文件/目录                | 描述 |
|--------------------------|------|
| `活动数据样本.xlsx`       | 模拟教育行为数据 |
| `test.vba`               | VBA 自动化脚本（异常检测） |
| `测试方案草案.md`         | 原始测试设计文档 |
| `python/`                | Python 自动化测试模块 |
| `.github/workflows/`     | GitHub Actions CI 流程配置 |
| `README.md`              | 当前项目说明 |

---

## 🧪 测试内容

| 场景编号 | 描述 |
|----------|------|
| 1        | 凌晨 3 点学习数据记录的异常检测 |
| 2        | 学习时长字段为 0 或负数 |
| 3        | 缺失值处理（空值、NaN） |
| 4        | 学号重复或格式异常 |
| 5        | 边界场景：空表、全部异常、全部合规 |

---

## 🛠️ 使用说明【Excel VBA】

1. 打开 `活动数据样本.xlsx`
2. 启用实现异常检测的宏 (macro)
3. 在 VBA 编辑器中运行 `test.vba` 脚本

---

## 💪 Python 自动化测试模块

为实现工程化自动测试流程，项目新增了 `python/` 目录，使用 `pytest` 实现测试用例定义与校验逻辑。

### 📦 安装依赖
```bash
cd python
pip install -r requirements.txt
```

### ▶️ 运行测试
```bash
pytest
```

### 📊 生成 HTML + coverage 报告
```bash
pytest --cov=edu_tests --cov-report=html --html=report.html
```

生成文件：
- `report.html`：测试结果报告
- `htmlcov/index.html`：覆盖率分析

---

## ♻️ GitHub Actions & Codecov 持续集成

项目集成 GitHub Actions 实现 CI 流程，自动运行 pytest 并上传 HTML 报告 + coverage.xml 到 [Codecov.io](https://app.codecov.io/gh/Wujiaxin245/Edu-Data-Testing)

### 每次 push/pull request 会:
- 自动解析是否通过 pytest
- 生成 report.html 和 coverage.html 报告
- 在主页显示 Codecov 测试覆盖率

---

## ✨ 项目优势

- 支持 Excel 手工校验 + Python 自动测试的混合模式
- 从传统手工转向自动化，展示工程化转型能力
- 覆盖典型数据问题检测 + 边界测试
- 集成 Codecov 实现可视化覆盖率反馈
- 可复用于其他结构化数据校验测试场景

---

## 👨‍💻 作者信息

- GitHub：[@Wujiaxin245](https://github.com/Wujiaxin245)
- 项目地址：[Edu-Data-Testing](https://github.com/Wujiaxin245/Edu-Data-Testing)
- License：MIT
