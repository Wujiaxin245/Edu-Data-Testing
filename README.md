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
   git clone https://github.com/你的用户名/Edu-Data-Testing.git

![platform](https://img.shields.io/badge/platform-Excel--VBA-blue)
![status](https://img.shields.io/badge/status-maintained-brightgreen)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

